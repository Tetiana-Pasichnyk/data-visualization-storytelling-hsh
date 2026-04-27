# OpenShift Deployment Guide for Job Scraper Webapp

This guide provides instructions for deploying the Job Scraper webapp to OpenShift.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Detailed Deployment Steps](#detailed-deployment-steps)
- [Configuration](#configuration)
- [Persistent Storage](#persistent-storage)
- [Monitoring and Health Checks](#monitoring-and-health-checks)
- [Troubleshooting](#troubleshooting)
- [Scaling](#scaling)

## Prerequisites

- OpenShift CLI (`oc`) installed and configured
- Access to an OpenShift cluster
- Docker or Podman installed (for local testing)
- Git repository access (if deploying from source)

## Quick Start

### Option 1: Deploy from Local Build

```bash
# 1. Login to OpenShift
oc login <your-openshift-cluster-url>

# 2. Create a new project
oc new-project job-scraper

# 3. Build and push the image
docker build -t job-scraper:latest -f Dockerfile .
docker tag job-scraper:latest <your-registry>/job-scraper:latest
docker push <your-registry>/job-scraper:latest

# 4. Deploy the application
oc new-app <your-registry>/job-scraper:latest --name=job-scraper-webapp

# 5. Expose the service
oc expose svc/job-scraper-webapp

# 6. Get the route URL
oc get route job-scraper-webapp
```

### Option 2: Deploy from Git Repository

```bash
# 1. Login to OpenShift
oc login <your-openshift-cluster-url>

# 2. Create a new project
oc new-project job-scraper

# 3. Create a new app from Git
oc new-app https://github.com/<your-repo>/job-scraper.git \
  --context-dir=job_scraper \
  --name=job-scraper-webapp

# 4. Expose the service
oc expose svc/job-scraper-webapp

# 5. Get the route URL
oc get route job-scraper-webapp
```

## Detailed Deployment Steps

### 1. Create OpenShift Project

```bash
oc new-project job-scraper --display-name="Job Scraper Application"
```

### 2. Create Persistent Volume Claim (PVC)

The application needs persistent storage for data files. Create a PVC:

```bash
cat <<EOF | oc apply -f -
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: job-scraper-data
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 5Gi
EOF
```

### 3. Create Deployment Configuration

```bash
cat <<EOF | oc apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: job-scraper-webapp
  labels:
    app: job-scraper-webapp
spec:
  replicas: 1
  selector:
    matchLabels:
      app: job-scraper-webapp
  template:
    metadata:
      labels:
        app: job-scraper-webapp
    spec:
      containers:
      - name: webapp
        image: <your-registry>/job-scraper:latest
        ports:
        - containerPort: 5000
          protocol: TCP
        env:
        - name: FLASK_ENV
          value: "production"
        - name: PORT
          value: "5000"
        volumeMounts:
        - name: data
          mountPath: /app/webapp/data
        resources:
          limits:
            memory: "512Mi"
            cpu: "500m"
          requests:
            memory: "256Mi"
            cpu: "250m"
        livenessProbe:
          httpGet:
            path: /api/health
            port: 5000
          initialDelaySeconds: 30
          periodSeconds: 10
          timeoutSeconds: 5
          failureThreshold: 3
        readinessProbe:
          httpGet:
            path: /api/health
            port: 5000
          initialDelaySeconds: 10
          periodSeconds: 5
          timeoutSeconds: 3
          failureThreshold: 3
      volumes:
      - name: data
        persistentVolumeClaim:
          claimName: job-scraper-data
EOF
```

### 4. Create Service

```bash
cat <<EOF | oc apply -f -
apiVersion: v1
kind: Service
metadata:
  name: job-scraper-webapp
  labels:
    app: job-scraper-webapp
spec:
  ports:
  - port: 5000
    targetPort: 5000
    protocol: TCP
    name: http
  selector:
    app: job-scraper-webapp
  type: ClusterIP
EOF
```

### 5. Create Route

```bash
cat <<EOF | oc apply -f -
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: job-scraper-webapp
  labels:
    app: job-scraper-webapp
spec:
  to:
    kind: Service
    name: job-scraper-webapp
  port:
    targetPort: http
  tls:
    termination: edge
    insecureEdgeTerminationPolicy: Redirect
EOF
```

## Configuration

### Environment Variables

The application supports the following environment variables:

| Variable | Default | Description |
|----------|---------|-------------|
| `FLASK_ENV` | `production` | Flask environment (production/development) |
| `PORT` | `5000` | Port the application listens on |
| `FLASK_APP` | `webapp/backend.py` | Flask application entry point |

### Setting Environment Variables

```bash
# Set environment variable in deployment
oc set env deployment/job-scraper-webapp FLASK_ENV=production

# Or use ConfigMap
oc create configmap job-scraper-config \
  --from-literal=FLASK_ENV=production

# Reference ConfigMap in deployment
oc set env deployment/job-scraper-webapp --from=configmap/job-scraper-config
```

## Persistent Storage

### Data Directory Structure

The application stores data in `/app/webapp/data/`:
- `job_data.json` - Simple job counts
- `job_details.json` - Detailed job information
- `job_history.csv` - Historical data
- `companies_data.json` - Company information
- `locations_data.json` - Location data

### Backup Data

```bash
# Create a backup pod
oc run backup --image=busybox --restart=Never --rm -it \
  --overrides='
{
  "spec": {
    "containers": [{
      "name": "backup",
      "image": "busybox",
      "command": ["tar", "czf", "/backup/data-backup.tar.gz", "/data"],
      "volumeMounts": [{
        "name": "data",
        "mountPath": "/data"
      }, {
        "name": "backup",
        "mountPath": "/backup"
      }]
    }],
    "volumes": [{
      "name": "data",
      "persistentVolumeClaim": {
        "claimName": "job-scraper-data"
      }
    }, {
      "name": "backup",
      "emptyDir": {}
    }]
  }
}'

# Copy backup from pod
oc cp backup:/backup/data-backup.tar.gz ./data-backup.tar.gz
```

### Restore Data

```bash
# Copy backup to pod
oc cp ./data-backup.tar.gz <pod-name>:/tmp/data-backup.tar.gz

# Extract in pod
oc exec <pod-name> -- tar xzf /tmp/data-backup.tar.gz -C /app/webapp/data/
```

## Monitoring and Health Checks

### Health Check Endpoint

The application provides a health check endpoint at `/api/health`:

```bash
# Check health
curl https://<your-route>/api/health
```

Expected response:
```json
{
  "status": "healthy",
  "timestamp": "2024-01-01T12:00:00"
}
```

### View Logs

```bash
# View application logs
oc logs -f deployment/job-scraper-webapp

# View logs from specific pod
oc logs -f <pod-name>

# View logs from previous container (if crashed)
oc logs --previous <pod-name>
```

### Monitoring Metrics

```bash
# Get pod metrics
oc adm top pod -l app=job-scraper-webapp

# Get node metrics
oc adm top node
```

## Troubleshooting

### Common Issues

#### 1. Permission Denied Errors

**Problem**: Container fails with permission errors on `/app/webapp/data/`

**Solution**: Ensure the PVC has proper permissions. OpenShift uses arbitrary UIDs:

```bash
# Check pod security context
oc get pod <pod-name> -o yaml | grep -A 10 securityContext

# The Dockerfile already handles this with group permissions
# Verify the data directory has group write permissions
oc exec <pod-name> -- ls -la /app/webapp/data/
```

#### 2. Image Pull Errors

**Problem**: `ImagePullBackOff` or `ErrImagePull`

**Solution**: Check image registry credentials:

```bash
# Create image pull secret
oc create secret docker-registry regcred \
  --docker-server=<your-registry> \
  --docker-username=<username> \
  --docker-password=<password> \
  --docker-email=<email>

# Link secret to service account
oc secrets link default regcred --for=pull
```

#### 3. Pod Crashes or CrashLoopBackOff

**Problem**: Pod keeps restarting

**Solution**: Check logs and events:

```bash
# Check pod events
oc describe pod <pod-name>

# Check logs
oc logs <pod-name>

# Check previous logs if pod restarted
oc logs --previous <pod-name>
```

#### 4. Application Not Accessible

**Problem**: Cannot access application via route

**Solution**: Verify service and route:

```bash
# Check service endpoints
oc get endpoints job-scraper-webapp

# Check route
oc get route job-scraper-webapp

# Test service internally
oc run test --image=curlimages/curl --rm -it --restart=Never -- \
  curl http://job-scraper-webapp:5000/api/health
```

### Debug Mode

To enable debug mode temporarily:

```bash
# Set debug environment variable
oc set env deployment/job-scraper-webapp FLASK_ENV=development

# Watch logs
oc logs -f deployment/job-scraper-webapp
```

**Warning**: Do not use debug mode in production!

## Scaling

### Manual Scaling

```bash
# Scale to 3 replicas
oc scale deployment/job-scraper-webapp --replicas=3

# Verify scaling
oc get pods -l app=job-scraper-webapp
```

### Horizontal Pod Autoscaler (HPA)

```bash
# Create HPA based on CPU usage
oc autoscale deployment/job-scraper-webapp \
  --min=1 --max=5 --cpu-percent=80

# Check HPA status
oc get hpa job-scraper-webapp
```

**Note**: For HPA to work, ensure metrics-server is installed in your cluster.

## Security Considerations

### Non-Root User

The Dockerfile runs the application as a non-root user (UID 1001). OpenShift will assign an arbitrary UID but maintain the root group (GID 0), which is the standard OpenShift security model.

### Security Context Constraints (SCC)

The application is compatible with the `restricted` SCC, which is the default in OpenShift:

```bash
# Verify SCC
oc get pod <pod-name> -o yaml | grep scc
```

### Network Policies

To restrict network access:

```bash
cat <<EOF | oc apply -f -
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: job-scraper-netpol
spec:
  podSelector:
    matchLabels:
      app: job-scraper-webapp
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector: {}
    ports:
    - protocol: TCP
      port: 5000
EOF
```

## Cleanup

To remove the application:

```bash
# Delete all resources
oc delete all -l app=job-scraper-webapp

# Delete PVC (warning: this deletes data!)
oc delete pvc job-scraper-data

# Delete project
oc delete project job-scraper
```

## Additional Resources

- [OpenShift Documentation](https://docs.openshift.com/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)

## Support

For issues or questions:
1. Check the [Troubleshooting](#troubleshooting) section
2. Review application logs: `oc logs -f deployment/job-scraper-webapp`
3. Check OpenShift events: `oc get events --sort-by='.lastTimestamp'`

---

**Last Updated**: 2024
**Version**: 1.0