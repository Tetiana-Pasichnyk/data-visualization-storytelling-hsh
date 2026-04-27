# OpenShift-compatible Dockerfile for Job Scraper Webapp
# Based on Python 3.11 slim image with non-root user support

FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    FLASK_APP=webapp/backend.py \
    FLASK_ENV=production \
    PORT=5000

# Create app directory and data directory
WORKDIR /app

# Create necessary directories with proper permissions for OpenShift
# OpenShift runs containers with arbitrary user IDs, so we need group permissions
RUN mkdir -p /app/webapp/data && \
    mkdir -p /app/webapp/static && \
    chmod -R g+rwX /app && \
    chmod -R g+rwX /tmp

# Copy requirements file first for better layer caching
COPY webapp/requirements.txt /app/webapp/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r /app/webapp/requirements.txt

# Copy application files
COPY webapp/ /app/webapp/

# Set proper permissions for all files
# OpenShift uses arbitrary UIDs but always uses GID 0 (root group)
RUN chgrp -R 0 /app && \
    chmod -R g=u /app && \
    chmod -R g+rwX /app/webapp/data

# Create a non-root user (OpenShift will override the UID but keep the GID)
# Using UID 1001 as it's a common practice for OpenShift
RUN useradd -u 1001 -r -g 0 -d /app -s /sbin/nologin \
    -c "Default application user" appuser

# Switch to non-root user
USER 1001

# Expose port 5000
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:5000/api/health', timeout=5)" || exit 1

# Set working directory to webapp
WORKDIR /app/webapp

# Run the Flask application
# Use gunicorn for production (add to requirements if needed) or Flask's built-in server
CMD ["python", "backend.py"]