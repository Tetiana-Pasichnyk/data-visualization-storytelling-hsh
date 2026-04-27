/**
 * Job Scraper v3.0 - Choropleth + City View + Enhanced Filters
 */

const API_BASE_URL = 'http://localhost:5000/api';

let jobCategories = ["Business Intelligence","Full-Stack","Data Scientist","Data Analyst","System Administrator","DevOps Engineer","Backend Developer","Frontend Developer","Machine Learning Engineer","Cloud Architect"];
const jobTypes = {"Arbeit": 1,"Ausbildung/Duales Studium": 34,"Selbstständigkeit": 4};
const praktikumKeywords = ['praktikum', 'praktikant', 'intern', 'internship'];

// Exclude keywords with default values
let excludeKeywords = [
    { keyword: 'Senior', matchType: 'whole' },
    { keyword: 'manager', matchType: 'partial' },
    { keyword: 'Manager', matchType: 'whole' }
];

// Include keywords (must have at least one of these)
let includeKeywords = [];

let charts = {}, currentData = [], locationsData = [], companiesData = {};
let map = null, geojsonLayer = null, cityMarkersLayer = null;
let bundeslandData = {}, cityData = {}, currentMapView = 'bundesland';

const bundeslandMapping = {'Baden-Württemberg':'Baden-Württemberg','Bayern':'Bayern','Berlin':'Berlin','Brandenburg':'Brandenburg','Bremen':'Bremen','Hamburg':'Hamburg','Hessen':'Hessen','Mecklenburg-Vorpommern':'Mecklenburg-Vorpommern','Niedersachsen':'Niedersachsen','Nordrhein-Westfalen':'Nordrhein-Westfalen','Rheinland-Pfalz':'Rheinland-Pfalz','Saarland':'Saarland','Sachsen':'Sachsen','Sachsen-Anhalt':'Sachsen-Anhalt','Schleswig-Holstein':'Schleswig-Holstein','Thüringen':'Thüringen'};

const germanyGeoJSON = {"type":"FeatureCollection","features":[{"type":"Feature","properties":{"name":"Baden-Württemberg"},"geometry":{"type":"Polygon","coordinates":[[[9.0,47.5],[10.5,47.5],[10.5,49.8],[9.0,49.8],[9.0,47.5]]]}},{"type":"Feature","properties":{"name":"Bayern"},"geometry":{"type":"Polygon","coordinates":[[[10.0,47.3],[13.8,47.3],[13.8,50.5],[10.0,50.5],[10.0,47.3]]]}},{"type":"Feature","properties":{"name":"Berlin"},"geometry":{"type":"Polygon","coordinates":[[[13.1,52.3],[13.8,52.3],[13.8,52.7],[13.1,52.7],[13.1,52.3]]]}},{"type":"Feature","properties":{"name":"Brandenburg"},"geometry":{"type":"Polygon","coordinates":[[[11.3,51.4],[14.8,51.4],[14.8,53.6],[11.3,53.6],[11.3,51.4]]]}},{"type":"Feature","properties":{"name":"Bremen"},"geometry":{"type":"Polygon","coordinates":[[[8.5,53.0],[8.9,53.0],[8.9,53.6],[8.5,53.6],[8.5,53.0]]]}},{"type":"Feature","properties":{"name":"Hamburg"},"geometry":{"type":"Polygon","coordinates":[[[9.7,53.4],[10.3,53.4],[10.3,53.8],[9.7,53.8],[9.7,53.4]]]}},{"type":"Feature","properties":{"name":"Hessen"},"geometry":{"type":"Polygon","coordinates":[[[8.2,49.4],[10.2,49.4],[10.2,51.7],[8.2,51.7],[8.2,49.4]]]}},{"type":"Feature","properties":{"name":"Mecklenburg-Vorpommern"},"geometry":{"type":"Polygon","coordinates":[[[10.6,53.1],[14.4,53.1],[14.4,54.7],[10.6,54.7],[10.6,53.1]]]}},{"type":"Feature","properties":{"name":"Niedersachsen"},"geometry":{"type":"Polygon","coordinates":[[[6.7,51.3],[11.6,51.3],[11.6,53.9],[6.7,53.9],[6.7,51.3]]]}},{"type":"Feature","properties":{"name":"Nordrhein-Westfalen"},"geometry":{"type":"Polygon","coordinates":[[[6.0,50.3],[9.5,50.3],[9.5,52.5],[6.0,52.5],[6.0,50.3]]]}},{"type":"Feature","properties":{"name":"Rheinland-Pfalz"},"geometry":{"type":"Polygon","coordinates":[[[6.1,48.9],[8.5,48.9],[8.5,50.9],[6.1,50.9],[6.1,48.9]]]}},{"type":"Feature","properties":{"name":"Saarland"},"geometry":{"type":"Polygon","coordinates":[[[6.4,49.1],[7.4,49.1],[7.4,49.6],[6.4,49.6],[6.4,49.1]]]}},{"type":"Feature","properties":{"name":"Sachsen"},"geometry":{"type":"Polygon","coordinates":[[[11.9,50.2],[15.0,50.2],[15.0,51.7],[11.9,51.7],[11.9,50.2]]]}},{"type":"Feature","properties":{"name":"Sachsen-Anhalt"},"geometry":{"type":"Polygon","coordinates":[[[10.6,50.9],[13.2,50.9],[13.2,53.0],[10.6,53.0],[10.6,50.9]]]}},{"type":"Feature","properties":{"name":"Schleswig-Holstein"},"geometry":{"type":"Polygon","coordinates":[[[8.4,53.4],[11.3,53.4],[11.3,55.1],[8.4,55.1],[8.4,53.4]]]}},{"type":"Feature","properties":{"name":"Thüringen"},"geometry":{"type":"Polygon","coordinates":[[[9.9,50.2],[12.7,50.2],[12.7,51.6],[9.9,51.6],[9.9,50.2]]]}}]};

document.addEventListener('DOMContentLoaded', function() {
    const saved = localStorage.getItem('jobCategories');
    if (saved) jobCategories = JSON.parse(saved);
    
    const savedExclude = localStorage.getItem('excludeKeywords');
    if (savedExclude) excludeKeywords = JSON.parse(savedExclude);
    
    const savedInclude = localStorage.getItem('includeKeywords');
    if (savedInclude) includeKeywords = JSON.parse(savedInclude);
    
    renderCategories();
    renderExcludeKeywords();
    renderIncludeKeywords();
    loadData();
    updateCategoryFilter();
    checkDataStatus();  // Check data consistency on load
});

async function checkDataStatus() {
    try {
        const r = await fetch(`${API_BASE_URL}/data-status`);
        if (!r.ok) return;
        
        const status = await r.json();
        updateDataStatusDisplay(status);
        
        // Show warning if data is inconsistent
        if (!status.consistency.is_consistent) {
            showDataInconsistencyWarning(status);
        }
    } catch (e) {
        console.error('Error checking data status:', e);
    }
}

function updateDataStatusDisplay(status) {
    const container = document.getElementById('dataStatusContainer');
    if (!container) return;
    
    const simple = status.simple_scraping;
    const detailed = status.detailed_scraping;
    const consistency = status.consistency;
    
    const statusClass = consistency.is_consistent ? 'status-ok' : 'status-warning';
    
    container.innerHTML = `
        <div class="data-status-widget">
            <h4>📊 Daten-Status</h4>
            <div class="status-row">
                <span class="status-label">Diagramme:</span>
                <span class="status-value">${simple.total_jobs.toLocaleString()} Jobs</span>
                <span class="status-date">${simple.last_updated}</span>
            </div>
            <div class="status-row">
                <span class="status-label">Heatmap/Unternehmen:</span>
                <span class="status-value">${detailed.total_jobs.toLocaleString()} Jobs</span>
                <span class="status-date">${detailed.last_updated}</span>
            </div>
            <div class="status-sync ${statusClass}">
                ${consistency.is_consistent ? '✅' : '⚠️'} ${consistency.message}
            </div>
        </div>
    `;
}

function showDataInconsistencyWarning(status) {
    const diff = status.consistency.difference;
    const message = `
        <div class="warning-banner">
            <strong>⚠️ Dateninkonsistenz erkannt!</strong><br>
            Diagramme: ${status.simple_scraping.total_jobs} Jobs<br>
            Heatmap/Unternehmen: ${status.detailed_scraping.total_jobs} Jobs<br>
            Differenz: ${diff} Jobs<br><br>
            <strong>Empfehlung:</strong> Klicken Sie auf "🔄 Vollständig aktualisieren" um alle Daten zu synchronisieren.
        </div>
    `;
    
    const banner = document.createElement('div');
    banner.innerHTML = message;
    banner.style.cssText = 'position: fixed; top: 80px; left: 50%; transform: translateX(-50%); z-index: 9999; max-width: 500px;';
    document.body.appendChild(banner);
    
    // Auto-hide after 10 seconds
    setTimeout(() => banner.remove(), 10000);
}

function switchTab(tabName) {
    document.querySelectorAll('.tab-content').forEach(t => t.classList.remove('active'));
    document.querySelectorAll('.tab').forEach(b => b.classList.remove('active'));
    document.getElementById(`tab-${tabName}`).classList.add('active');
    event.target.classList.add('active');
    if (tabName === 'heatmap') {
        if (locationsData.length === 0) loadHeatmapData();
        else if (map) setTimeout(() => map.invalidateSize(), 100);
    }
    if (tabName === 'companies' && Object.keys(companiesData).length === 0) loadCompaniesData();
}

function switchMapView(view) {
    currentMapView = view;
    document.getElementById('btnBundeslandView').classList.toggle('active', view === 'bundesland');
    document.getElementById('btnCityView').classList.toggle('active', view === 'city');
    updateHeatmap();
}

function renderCategories() {
    const c = document.getElementById('categoriesList');
    c.innerHTML = '';
    jobCategories.forEach((cat, i) => {
        const tag = document.createElement('div');
        tag.className = 'category-tag';
        tag.innerHTML = `<span>${cat}</span><button onclick="removeCategory(${i})">×</button>`;
        c.appendChild(tag);
    });
}

function addCategory() {
    const input = document.getElementById('newCategory');
    const cat = input.value.trim();
    if (!cat) return showStatus('Bitte geben Sie ein Berufsfeld ein', 'error');
    if (jobCategories.includes(cat)) return showStatus('Existiert bereits', 'error');
    jobCategories.push(cat);
    input.value = '';
    renderCategories();
    updateCategoryFilter();
    showStatus(`"${cat}" hinzugefügt`, 'success');
    localStorage.setItem('jobCategories', JSON.stringify(jobCategories));
}

function removeCategory(i) {
    const cat = jobCategories[i];
    jobCategories.splice(i, 1);
    renderCategories();
    updateCategoryFilter();
    showStatus(`"${cat}" entfernt`, 'info');
    localStorage.setItem('jobCategories', JSON.stringify(jobCategories));
}

function showStatus(msg, type = 'info') {
    const c = document.getElementById('sidebarStatus');
    c.innerHTML = `<div class="status-message status-${type}">${msg}</div>`;
    setTimeout(() => c.innerHTML = '', 5000);
}

async function scrapeNow() {
    showStatus('Scraping startet...', 'info');
    try {
        const r = await fetch(`${API_BASE_URL}/scrape`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({categories: jobCategories})
        });
        if (!r.ok) throw new Error('Fehler');
        const d = await r.json();
        showStatus(`Fertig! ${d.count} Einträge`, 'success');
        setTimeout(() => loadData(), 1000);
    } catch (e) {
        showStatus('Fehler beim Scraping', 'error');
    }
}

async function scrapeDetailed() {
    showStatus('Detailliertes Scraping startet (10-20 Min)...', 'info');
    try {
        const r = await fetch(`${API_BASE_URL}/scrape-detailed`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({categories: jobCategories, max_per_category: 500})  // Erhöht von 50 auf 500
        });
        if (!r.ok) throw new Error('Fehler');
        const d = await r.json();
        showStatus(`Fertig! ${d.stats.jobs} Jobs, ${d.stats.locations} Standorte`, 'success');
        
        // Reload all data and check status
        setTimeout(() => {
            loadData();  // Reload Diagramme (now synchronized)
            loadHeatmapData();
            loadCompaniesData();
            checkDataStatus();  // Update status display
        }, 1000);
    } catch (e) {
        showStatus('Fehler beim detaillierten Scraping', 'error');
    }
}

async function loadData() {
    const c = document.getElementById('charts');
    c.innerHTML = '<div class="loading"><div class="spinner"></div><p>Laden...</p></div>';
    try {
        const r = await fetch(`${API_BASE_URL}/data`);
        if (!r.ok) throw new Error('Fehler');
        currentData = await r.json();
        if (!currentData || currentData.length === 0) {
            c.innerHTML = '<div class="loading"><p>Keine Daten. Bitte scrapen.</p></div>';
            return;
        }
        updateStats(currentData);
        renderCharts(currentData);
        showStatus('Daten geladen', 'success');
    } catch (e) {
        c.innerHTML = '<div class="loading"><p>Fehler beim Laden</p></div>';
        showStatus('Fehler', 'error');
    }
}

function clearData() {
    if (confirm('Wirklich löschen?')) {
        currentData = [];
        document.getElementById('charts').innerHTML = '<div class="loading"><p>Keine Daten</p></div>';
        document.getElementById('stats').innerHTML = '';
        showStatus('Gelöscht', 'info');
    }
}

function updateStats(data) {
    const s = document.getElementById('stats');
    if (!data || data.length === 0) {s.innerHTML = ''; return;}
    const cats = [...new Set(data.map(d => d.category))].length;
    const types = [...new Set(data.map(d => d.job_type))].length;
    const latest = data.reduce((m, d) => d.date > m ? d.date : m, data[0].date);
    const latestData = data.filter(d => d.date === latest);
    const total = latestData.reduce((sum, d) => sum + d.count, 0);
    s.innerHTML = `<div class="stat-card"><h3>${cats}</h3><p>Berufsfelder</p></div><div class="stat-card"><h3>${types}</h3><p>Angebotsarten</p></div><div class="stat-card"><h3>${total.toLocaleString()}</h3><p>Stellenangebote</p></div><div class="stat-card"><h3>${data.length}</h3><p>Datenpunkte</p></div>`;
}

function renderCharts(data) {
    const c = document.getElementById('charts');
    if (!data || data.length === 0) {c.innerHTML = '<div class="loading"><p>Keine Daten</p></div>'; return;}
    c.innerHTML = '';
    Object.values(charts).forEach(ch => {if (ch && ch.destroy) ch.destroy();});
    charts = {};
    
    // Render charts for each job type
    Object.keys(jobTypes).forEach(jt => {
        const div = document.createElement('div');
        div.className = 'chart-container';
        div.innerHTML = `<h2>📊 ${jt}</h2><div class="chart-wrapper"><canvas id="chart-${jt.replace(/\s+/g, '-')}"></canvas></div><div id="chart-jobs-${jt.replace(/\s+/g, '-')}" class="collapse-content"></div>`;
        c.appendChild(div);
        createBarChart(data, jt);
    });
    
    // Add Praktikum chart separately (uses data from Ausbildung/Duales Studium with keyword filtering)
    const praktikumDiv = document.createElement('div');
    praktikumDiv.className = 'chart-container';
    praktikumDiv.innerHTML = `<h2>📊 Praktikum</h2><div class="chart-wrapper"><canvas id="chart-Praktikum"></canvas></div><div id="chart-jobs-Praktikum" class="collapse-content"></div>`;
    c.appendChild(praktikumDiv);
    createBarChart(data, 'Praktikum');
    
    createTimeSeriesChart(data);
}

function createBarChart(data, jobType) {
    const id = `chart-${jobType.replace(/\s+/g, '-')}`;
    const ctx = document.getElementById(id);
    
    // Filter data based on job type
    let filtered;
    if (jobType === 'Praktikum') {
        // Praktikum: filter from Ausbildung/Duales Studium data (will be separated during detailed scraping)
        filtered = data.filter(d => d.job_type === 'Praktikum');
    } else {
        filtered = data.filter(d => d.job_type === jobType);
    }
    
    const agg = {};
    filtered.forEach(d => {
        if (!agg[d.category]) agg[d.category] = [];
        agg[d.category].push(d.count);
    });
    const cats = Object.keys(agg);
    const avgs = cats.map(c => agg[c].reduce((s, v) => s + v, 0) / agg[c].length);
    const sorted = cats.map((c, i) => ({category: c, average: avgs[i]})).sort((a, b) => b.average - a.average);
    const labels = sorted.map(s => s.category);
    const values = sorted.map(s => s.average);
    const grad = ctx.getContext('2d').createLinearGradient(0, 0, 0, 400);
    grad.addColorStop(0, 'rgba(102, 126, 234, 0.8)');
    grad.addColorStop(1, 'rgba(118, 75, 162, 0.8)');
    charts[jobType] = new Chart(ctx, {
        type: 'bar',
        data: {labels: labels, datasets: [{label: 'Durchschnitt', data: values, backgroundColor: grad, borderColor: 'rgba(102, 126, 234, 1)', borderWidth: 2}]},
        options: {
            responsive: true,
            maintainAspectRatio: false,
            onClick: (event, elements) => {
                if (elements.length > 0) {
                    const index = elements[0].index;
                    const category = labels[index];
                    const containerId = `chart-jobs-${jobType.replace(/\s+/g, '-')}`;
                    toggleChartJobs(event, category, jobType, containerId);
                }
            },
            plugins: {
                legend: {display: false},
                tooltip: {callbacks: {label: c => `Durchschnitt: ${Math.round(c.parsed.y)} Stellen (Klicken für Details)`}}
            },
            scales: {
                y: {beginAtZero: true, ticks: {callback: v => Math.round(v)}},
                x: {ticks: {maxRotation: 45, minRotation: 45}}
            }
        }
    });
}

function createTimeSeriesChart(data) {
    const cats = [...new Set(data.map(d => d.category))];
    const div = document.createElement('div');
    div.className = 'chart-container';
    div.innerHTML = `<h2>📈 Zeitverlauf</h2><div style="margin-bottom:15px;"><label>Berufsfeld:</label><select id="categorySelect" onchange="updateTimeSeriesChart()" style="margin-left:10px;padding:8px;">${cats.map(c => `<option value="${c}">${c}</option>`).join('')}</select></div><div class="chart-wrapper"><canvas id="chart-timeseries"></canvas></div>`;
    document.getElementById('charts').appendChild(div);
    updateTimeSeriesChart();
}

function updateTimeSeriesChart() {
    const sel = document.getElementById('categorySelect');
    if (!sel) return;
    const cat = sel.value;
    const ctx = document.getElementById('chart-timeseries');
    if (charts['timeseries']) charts['timeseries'].destroy();
    const filtered = currentData.filter(d => d.category === cat);
    const grouped = {};
    filtered.forEach(d => {
        if (!grouped[d.job_type]) grouped[d.job_type] = {};
        grouped[d.job_type][d.date] = d.count;
    });
    const dates = [...new Set(filtered.map(d => d.date))].sort();
    const colors = [{border: 'rgba(102, 126, 234, 1)', bg: 'rgba(102, 126, 234, 0.1)'},{border: 'rgba(118, 75, 162, 1)', bg: 'rgba(118, 75, 162, 0.1)'},{border: 'rgba(237, 100, 166, 1)', bg: 'rgba(237, 100, 166, 0.1)'}];
    const datasets = Object.keys(grouped).map((jt, i) => ({label: jt, data: dates.map(d => grouped[jt][d] || 0), borderColor: colors[i % colors.length].border, backgroundColor: colors[i % colors.length].bg, tension: 0.4, fill: true}));
    charts['timeseries'] = new Chart(ctx, {
        type: 'line',
        data: {labels: dates, datasets: datasets},
        options: {responsive: true, maintainAspectRatio: false, plugins: {legend: {position: 'top'}, tooltip: {mode: 'index', intersect: false}}, scales: {y: {beginAtZero: true, ticks: {callback: v => Math.round(v)}}}}
    });
}

function exportData() {
    if (!currentData || currentData.length === 0) return showStatus('Keine Daten', 'error');
    const h = Object.keys(currentData[0]);
    const csv = [h.join(','), ...currentData.map(r => h.map(k => r[k]).join(','))].join('\n');
    const blob = new Blob([csv], {type: 'text/csv;charset=utf-8;'});
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `job_data_${new Date().toISOString().split('T')[0]}.csv`;
    a.click();
    window.URL.revokeObjectURL(url);
    showStatus('Exportiert', 'success');
}

async function loadHeatmapData() {
    showStatus('Lade Standortdaten...', 'info');
    try {
        const r = await fetch(`${API_BASE_URL}/locations`);
        if (!r.ok) throw new Error('Fehler');
        const data = await r.json();
        
        // Handle new API response format with statistics
        if (data.locations) {
            locationsData = data.locations;
            const stats = data.statistics;
            
            // Display statistics
            if (stats) {
                const statsHtml = `
                    <div class="location-stats">
                        <h3>📊 Standort-Statistiken</h3>
                        <div class="stats-grid">
                            <div class="stat-item">
                                <strong>${stats.total_jobs.toLocaleString()}</strong>
                                <span>Gesamt Jobs</span>
                            </div>
                            <div class="stat-item success">
                                <strong>${stats.jobs_with_location.toLocaleString()}</strong>
                                <span>Mit Standort (${stats.location_coverage_percent}%)</span>
                            </div>
                            <div class="stat-item warning">
                                <strong>${stats.jobs_without_location.toLocaleString()}</strong>
                                <span>Ohne Standort</span>
                            </div>
                        </div>
                        ${stats.jobs_without_location > 0 ? `
                            <details class="missing-locations">
                                <summary>⚠️ Alle ${stats.jobs_without_location} Jobs ohne Standort anzeigen</summary>
                                <div class="missing-list">
                                    ${stats.missing_location_details.map(job => `
                                        <div class="missing-job">
                                            <strong>${job.title}</strong><br>
                                            <small>${job.company} | ${job.category} | ${job.job_type}</small><br>
                                            <em>Standort: ${job.location_text}</em>
                                        </div>
                                    `).join('')}
                                </div>
                            </details>
                        ` : ''}
                    </div>
                `;
                
                // Insert stats before map
                const mapContainer = document.getElementById('map');
                let statsContainer = document.getElementById('location-stats-container');
                if (!statsContainer) {
                    statsContainer = document.createElement('div');
                    statsContainer.id = 'location-stats-container';
                    mapContainer.parentNode.insertBefore(statsContainer, mapContainer);
                }
                statsContainer.innerHTML = statsHtml;
            }
        } else {
            // Fallback for old API format
            locationsData = data;
        }
        
        if (locationsData.length === 0) return showStatus('Keine Standortdaten. Bitte detailliert scrapen.', 'info');
        aggregateByBundesland();
        aggregateByCity();
        initializeMap();
        updateHeatmap();
        showStatus(`${locationsData.length} Standorte geladen`, 'success');
    } catch (e) {
        showStatus('Fehler beim Laden', 'error');
        console.error(e);
    }
}

function aggregateByBundesland() {
    bundeslandData = {};
    locationsData.forEach(loc => {
        const bl = bundeslandMapping[loc.region] || loc.region || 'Unbekannt';
        if (!bundeslandData[bl]) bundeslandData[bl] = {count: 0, cities: {}, categories: {}, jobTypes: {}};
        bundeslandData[bl].count++;
        const city = loc.city || 'Unbekannt';
        bundeslandData[bl].cities[city] = (bundeslandData[bl].cities[city] || 0) + 1;
        const cat = loc.category || 'Unbekannt';
        bundeslandData[bl].categories[cat] = (bundeslandData[bl].categories[cat] || 0) + 1;
        const jt = loc.job_type || 'Unbekannt';
        bundeslandData[bl].jobTypes[jt] = (bundeslandData[bl].jobTypes[jt] || 0) + 1;
    });
}

function aggregateByCity() {
    cityData = {};
    locationsData.forEach(loc => {
        const city = loc.city || 'Unbekannt';
        if (!loc.lat || !loc.lon) return;
        if (!cityData[city]) cityData[city] = {count: 0, lat: loc.lat, lon: loc.lon, categories: {}, jobTypes: {}, bundesland: loc.region || 'Unbekannt'};
        cityData[city].count++;
        const cat = loc.category || 'Unbekannt';
        cityData[city].categories[cat] = (cityData[city].categories[cat] || 0) + 1;
        const jt = loc.job_type || 'Unbekannt';
        cityData[city].jobTypes[jt] = (cityData[city].jobTypes[jt] || 0) + 1;
    });
}

function initializeMap() {
    if (map) map.remove();
    map = L.map('map').setView([51.1657, 10.4515], 6);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {attribution: '© OpenStreetMap', maxZoom: 18}).addTo(map);
}

function getColor(c) {
    // Subtilere Farbskala mit weniger starken Unterschieden
    return c > 200 ? '#7e57c2' :
           c > 100 ? '#9575cd' :
           c > 50 ? '#b39ddb' :
           c > 20 ? '#c5cae9' :
           c > 10 ? '#d1c4e9' :
           c > 5 ? '#e8eaf6' :
           '#f3e5f5';
}

function updateHeatmap() {
    if (!map) initializeMap();
    if (geojsonLayer) {map.removeLayer(geojsonLayer); geojsonLayer = null;}
    if (cityMarkersLayer) {map.removeLayer(cityMarkersLayer); cityMarkersLayer = null;}
    const jtf = document.getElementById('heatmapJobType').value;
    const catf = document.getElementById('heatmapCategory').value;
    let filtered = locationsData;
    
    // Apply keyword filters first
    filtered = filterJobsByKeywords(filtered);
    
    if (jtf) filtered = filtered.filter(l => l.job_type === jtf);
    if (catf) filtered = filtered.filter(l => l.category === catf);
    const temp = locationsData;
    locationsData = filtered;
    aggregateByBundesland();
    aggregateByCity();
    if (currentMapView === 'bundesland') renderBundeslandView();
    else renderCityView();
    locationsData = temp;
    updateHeatmapStats(filtered);
}

function renderBundeslandView() {
    geojsonLayer = L.geoJSON(germanyGeoJSON, {
        style: f => {
            const bl = f.properties.name;
            const d = bundeslandData[bl];
            const c = d ? d.count : 0;
            return {fillColor: getColor(c), weight: 2, opacity: 1, color: 'white', dashArray: '3', fillOpacity: 0.7};
        },
        onEachFeature: (f, l) => {
            l.on({
                mouseover: e => {e.target.setStyle({weight: 5, color: '#667eea', dashArray: '', fillOpacity: 0.9}); e.target.bringToFront();},
                mouseout: e => geojsonLayer.resetStyle(e.target),
                click: showBundeslandDetails
            });
            const bl = f.properties.name;
            const d = bundeslandData[bl];
            const c = d ? d.count : 0;
            l.bindTooltip(`<strong>${bl}</strong><br>${c} Stellenangebote`, {permanent: false, direction: 'center'});
        }
    }).addTo(map);
    addLegend();
}

function renderCityView() {
    cityMarkersLayer = L.layerGroup();
    Object.entries(cityData).forEach(([city, d]) => {
        if (!d.lat || !d.lon) return;
        const r = Math.sqrt(d.count) * 3;
        const c = getColor(d.count);
        const m = L.circleMarker([d.lat, d.lon], {radius: r, fillColor: c, color: 'white', weight: 2, opacity: 1, fillOpacity: 0.7});
        m.bindTooltip(`<strong>${city}</strong><br>${d.count} Stellenangebote`, {permanent: false});
        m.on('click', () => showCityDetails(city, d));
        m.addTo(cityMarkersLayer);
    });
    cityMarkersLayer.addTo(map);
    addLegend();
}

function showBundeslandDetails(e) {
    const bl = e.target.feature.properties.name;
    const d = bundeslandData[bl];
    if (!d) return showModal(bl, '<p>Keine Daten</p>');
    const cities = Object.entries(d.cities).sort((a, b) => b[1] - a[1]).slice(0, 20);
    let html = `<div style="margin-bottom:20px;"><h3 style="color:#667eea;margin-bottom:10px;">📊 Übersicht</h3><p><strong>Gesamt:</strong> ${d.count}</p><p><strong>Städte:</strong> ${Object.keys(d.cities).length}</p></div><div style="margin-bottom:20px;"><h3 style="color:#667eea;margin-bottom:10px;">🏙️ Top Städte</h3><ul class="city-list">`;
    cities.forEach(([c, cnt], idx) => {
        html += `<li class="city-item">
            <div>
                <span class="city-name">${c}</span>
                <span class="job-count-clickable" onclick="toggleCityJobs(event, '${c.replace(/'/g, "\\'")}', '${bl}', 'city-${idx}')">${cnt} Stellen ▼</span>
            </div>
            <div id="city-${idx}" class="collapse-content"></div>
        </li>`;
    });
    html += `</ul></div><div style="margin-bottom:20px;"><h3 style="color:#667eea;margin-bottom:10px;">💼 Nach Angebotsart</h3><ul class="city-list">`;
    Object.entries(d.jobTypes).forEach(([t, cnt]) => html += `<li class="city-item"><span class="city-name">${t}</span><span class="city-count">${cnt} Stellen</span></li>`);
    html += `</ul></div>`;
    if (Object.keys(d.categories).length > 0) {
        html += `<div><h3 style="color:#667eea;margin-bottom:10px;">👨‍💻 Nach Berufsfeld</h3><ul class="city-list">`;
        Object.entries(d.categories).sort((a, b) => b[1] - a[1]).slice(0, 10).forEach(([cat, cnt]) => html += `<li class="city-item"><span class="city-name">${cat}</span><span class="city-count">${cnt} Stellen</span></li>`);
        html += `</ul></div>`;
    }
    showModal(bl, html);
}

function showCityDetails(city, d) {
    let html = `<div style="margin-bottom:20px;"><h3 style="color:#667eea;margin-bottom:10px;">📊 Übersicht</h3><p><strong>Gesamt:</strong> ${d.count}</p><p><strong>Bundesland:</strong> ${d.bundesland}</p></div><div style="margin-bottom:20px;"><h3 style="color:#667eea;margin-bottom:10px;">💼 Nach Angebotsart</h3><ul class="city-list">`;
    Object.entries(d.jobTypes).forEach(([t, cnt], idx) => {
        html += `<li class="city-item">
            <div>
                <span class="city-name">${t}</span>
                <span class="job-count-clickable" onclick="toggleCityJobs(event, '${city.replace(/'/g, "\\'")}', '', 'jobtype-${idx}', '${t}')">${cnt} Stellen ▼</span>
            </div>
            <div id="jobtype-${idx}" class="collapse-content"></div>
        </li>`;
    });
    html += `</ul></div><div><h3 style="color:#667eea;margin-bottom:10px;">👨‍💻 Nach Berufsfeld</h3><ul class="city-list">`;
    Object.entries(d.categories).sort((a, b) => b[1] - a[1]).forEach(([cat, cnt], idx) => {
        html += `<li class="city-item">
            <div>
                <span class="city-name">${cat}</span>
                <span class="job-count-clickable" onclick="toggleCityJobs(event, '${city.replace(/'/g, "\\'")}', '', 'category-${idx}', '', '${cat.replace(/'/g, "\\'")}')">${cnt} Stellen ▼</span>
            </div>
            <div id="category-${idx}" class="collapse-content"></div>
        </li>`;
    });
    html += `</ul></div>`;
    showModal(city, html);
}

function updateHeatmapStats(filtered) {
    const total = filtered.length;
    const withLocation = filtered.filter(l => l.city && l.city !== 'Unbekannt').length;
    const withoutLocation = total - withLocation;
    const percentage = total > 0 ? ((withLocation / total) * 100).toFixed(1) : 0;
    
    // Calculate market share (assuming total German IT job market is ~50,000)
    const estimatedMarketSize = 50000;
    const marketShare = ((total / estimatedMarketSize) * 100).toFixed(2);
    
    document.getElementById('heatmapStats').innerHTML = `
        <div style="cursor: pointer; padding: 15px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 8px; color: white; box-shadow: 0 4px 6px rgba(0,0,0,0.1);" onclick="showGermanyStats()">
            <div style="font-size: 1.1em; font-weight: bold; margin-bottom: 8px;">🇩🇪 Deutschland Statistik</div>
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; font-size: 0.9em;">
                <div>
                    <div style="opacity: 0.9;">Gesamt Jobs</div>
                    <div style="font-size: 1.3em; font-weight: bold;">${total.toLocaleString()}</div>
                    <div style="font-size: 0.8em; opacity: 0.8;">~${marketShare}% Marktanteil</div>
                </div>
                <div>
                    <div style="opacity: 0.9;">Mit Standort</div>
                    <div style="font-size: 1.3em; font-weight: bold;">${withLocation.toLocaleString()}</div>
                    <div style="font-size: 0.8em; opacity: 0.8;">${percentage}%</div>
                </div>
                <div>
                    <div style="opacity: 0.9;">Ohne Standort</div>
                    <div style="font-size: 1.3em; font-weight: bold;">${withoutLocation.toLocaleString()}</div>
                    <div style="font-size: 0.8em; opacity: 0.8;">${(100 - percentage).toFixed(1)}%</div>
                </div>
            </div>
            <div style="margin-top: 10px; font-size: 0.85em; opacity: 0.9; text-align: center;">💡 Klicken für Details</div>
        </div>
    `;
}

function showGermanyStats() {
    const total = locationsData.length;
    const withLocation = locationsData.filter(l => l.city && l.city !== 'Unbekannt').length;
    const withoutLocation = total - withLocation;
    const percentage = total > 0 ? ((withLocation / total) * 100).toFixed(1) : 0;
    
    // Calculate market share
    const estimatedMarketSize = 50000;
    const marketShare = ((total / estimatedMarketSize) * 100).toFixed(2);
    
    // Get top cities
    const cityCount = {};
    locationsData.forEach(l => {
        if (l.city && l.city !== 'Unbekannt') {
            cityCount[l.city] = (cityCount[l.city] || 0) + 1;
        }
    });
    const topCities = Object.entries(cityCount).sort((a, b) => b[1] - a[1]).slice(0, 10);
    
    // Get top categories
    const catCount = {};
    locationsData.forEach(l => {
        if (l.category) {
            catCount[l.category] = (catCount[l.category] || 0) + 1;
        }
    });
    const topCategories = Object.entries(catCount).sort((a, b) => b[1] - a[1]).slice(0, 10);
    
    // Get job types
    const jobTypeCount = {};
    locationsData.forEach(l => {
        if (l.job_type) {
            jobTypeCount[l.job_type] = (jobTypeCount[l.job_type] || 0) + 1;
        }
    });
    
    let html = `
        <div style="margin-bottom:20px;">
            <h3 style="color:#667eea;margin-bottom:15px;">📊 Gesamtübersicht</h3>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 15px;">
                <div style="background: #f8f9fa; padding: 15px; border-radius: 8px;">
                    <div style="font-size: 0.9em; color: #6c757d; margin-bottom: 5px;">Gesamt Stellenangebote</div>
                    <div style="font-size: 2em; font-weight: bold; color: #667eea;">${total.toLocaleString()}</div>
                    <div style="font-size: 0.85em; color: #6c757d; margin-top: 5px;">~${marketShare}% des geschätzten Marktes (${estimatedMarketSize.toLocaleString()} Jobs)</div>
                </div>
                <div style="background: #f8f9fa; padding: 15px; border-radius: 8px;">
                    <div style="font-size: 0.9em; color: #6c757d; margin-bottom: 5px;">Standort-Abdeckung</div>
                    <div style="font-size: 2em; font-weight: bold; color: #28a745;">${percentage}%</div>
                    <div style="font-size: 0.85em; color: #6c757d; margin-top: 5px;">${withLocation.toLocaleString()} mit Standort, ${withoutLocation.toLocaleString()} ohne</div>
                </div>
            </div>
        </div>
        
        <div style="margin-bottom:20px;">
            <h3 style="color:#667eea;margin-bottom:10px;">💼 Nach Angebotsart</h3>
            <ul class="city-list">
    `;
    
    Object.entries(jobTypeCount).sort((a, b) => b[1] - a[1]).forEach(([type, count]) => {
        const pct = ((count / total) * 100).toFixed(1);
        html += `<li class="city-item">
            <span class="city-name">${type}</span>
            <span class="city-count">${count.toLocaleString()} (${pct}%)</span>
        </li>`;
    });
    
    html += `</ul></div><div style="margin-bottom:20px;">
        <h3 style="color:#667eea;margin-bottom:10px;">🏙️ Top 10 Städte</h3>
        <ul class="city-list">`;
    
    topCities.forEach(([city, count]) => {
        const pct = ((count / withLocation) * 100).toFixed(1);
        html += `<li class="city-item">
            <span class="city-name">${city}</span>
            <span class="city-count">${count.toLocaleString()} (${pct}%)</span>
        </li>`;
    });
    
    html += `</ul></div><div>
        <h3 style="color:#667eea;margin-bottom:10px;">👨‍💻 Top 10 Berufsfelder</h3>
        <ul class="city-list">`;
    
    topCategories.forEach(([cat, count]) => {
        const pct = ((count / total) * 100).toFixed(1);
        html += `<li class="city-item">
            <span class="city-name">${cat}</span>
            <span class="city-count">${count.toLocaleString()} (${pct}%)</span>
        </li>`;
    });
    
    html += `</ul></div>`;
    
    showModal('🇩🇪 Deutschland Statistik', html);
}

function showModal(title, content) {
    document.getElementById('modalTitle').textContent = title;
    document.getElementById('modalBody').innerHTML = content;
    document.getElementById('bundeslandModal').style.display = 'block';
}

function closeModal() {
    document.getElementById('bundeslandModal').style.display = 'none';
}

window.onclick = e => {
    const m = document.getElementById('bundeslandModal');
    if (e.target == m) m.style.display = 'none';
}

function addLegend() {
    const leg = L.control({position: 'bottomright'});
    leg.onAdd = () => {
        const div = L.DomUtil.create('div', 'info legend');
        const grades = [0, 5, 10, 20, 50, 100, 200];
        div.innerHTML = '<h4 style="margin:0 0 5px 0;">Stellenangebote</h4>';
        for (let i = 0; i < grades.length; i++) {
            div.innerHTML += '<i style="background:' + getColor(grades[i] + 1) + '; width:18px; height:18px; float:left; margin-right:8px; opacity:0.8;"></i> ' + grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+');
        }
        div.style.background = 'white';
        div.style.padding = '10px';
        div.style.borderRadius = '5px';
        div.style.boxShadow = '0 0 15px rgba(0,0,0,0.2)';
        return div;
    };
    leg.addTo(map);
}

function updateCategoryFilter() {
    const sel = document.getElementById('heatmapCategory');
    if (!sel) return;
    const cur = sel.value;
    sel.innerHTML = '<option value="">Alle Berufsfelder</option>';
    jobCategories.forEach(c => {
        const opt = document.createElement('option');
        opt.value = c;
        opt.textContent = c;
        if (c === cur) opt.selected = true;
        sel.appendChild(opt);
    });
}

async function loadCompaniesData() {
    showStatus('Lade Unternehmensdaten...', 'info');
    try {
        // Check if filters are active
        const hasFilters = includeKeywords.length > 0 || excludeKeywords.length > 0;
        
        let r;
        if (hasFilters) {
            // Use POST with filters
            r = await fetch(`${API_BASE_URL}/companies`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    includeKeywords: includeKeywords,
                    excludeKeywords: excludeKeywords
                })
            });
        } else {
            // Use GET without filters (faster, uses cached data)
            r = await fetch(`${API_BASE_URL}/companies`);
        }
        
        if (!r.ok) throw new Error('Fehler');
        companiesData = await r.json();
        if (Object.keys(companiesData).length === 0) return showStatus('Keine Unternehmensdaten. Bitte detailliert scrapen.', 'info');
        updateCompaniesView();
        showStatus('Unternehmensdaten geladen', 'success');
    } catch (e) {
        showStatus('Fehler', 'error');
    }
}

function updateCompaniesView() {
    const jt = document.getElementById('companyJobType').value;
    const lim = parseInt(document.getElementById('companyLimit').value);
    if (!companiesData[jt]) {document.getElementById('companiesList').innerHTML = '<p>Keine Daten</p>'; return;}
    const comps = companiesData[jt].slice(0, lim);
    const list = document.getElementById('companiesList');
    list.innerHTML = '';
    comps.forEach((c, idx) => {
        const item = document.createElement('div');
        item.className = 'company-item';
        item.style.display = 'block';
        item.innerHTML = `
            <div style="display:flex;justify-content:space-between;align-items:center;">
                <div>
                    <strong>${c.name}</strong>
                    <span class="job-count-clickable" onclick="toggleCompanyJobs(event, '${c.name.replace(/'/g, "\\'")}', '${jt}', 'company-${idx}')" style="margin-left:10px;">${c.count} Stellen ▼</span>
                </div>
                <input type="checkbox" ${c.visible ? 'checked' : ''} onchange="toggleCompanyVisibility('${jt}', '${c.name.replace(/'/g, "\\'")}', this.checked)">
            </div>
            <div id="company-${idx}" class="collapse-content"></div>
        `;
        list.appendChild(item);
    });
    renderCompaniesChart(comps.filter(c => c.visible));
    const total = comps.reduce((s, c) => s + c.count, 0);
    const vis = comps.filter(c => c.visible).length;
    document.getElementById('companiesStats').innerHTML = `🏢 ${comps.length} Unternehmen | 📊 ${total} Stellenangebote | 👁️ ${vis} sichtbar`;
}

function renderCompaniesChart(comps) {
    const ctx = document.getElementById('companiesChart');
    if (charts['companies']) charts['companies'].destroy();
    const labels = comps.map(c => c.name);
    const values = comps.map(c => c.count);
    const grad = ctx.getContext('2d').createLinearGradient(0, 0, 0, 400);
    grad.addColorStop(0, 'rgba(102, 126, 234, 0.8)');
    grad.addColorStop(1, 'rgba(118, 75, 162, 0.8)');
    charts['companies'] = new Chart(ctx, {
        type: 'bar',
        data: {labels: labels, datasets: [{label: 'Anzahl', data: values, backgroundColor: grad, borderColor: 'rgba(102, 126, 234, 1)', borderWidth: 2}]},
        options: {responsive: true, maintainAspectRatio: false, indexAxis: 'y', plugins: {legend: {display: false}, tooltip: {callbacks: {label: c => `${c.parsed.x} Stellen`}}}, scales: {x: {beginAtZero: true, ticks: {callback: v => Math.round(v)}}}}
    });
}

async function toggleCompanyVisibility(jt, name, vis) {
    try {
        const r = await fetch(`${API_BASE_URL}/companies/visibility`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({job_type: jt, company_name: name, visible: vis})
        });
        if (!r.ok) throw new Error('Fehler');
        const d = await r.json();
        companiesData = d.companies;
        updateCompaniesView();
    } catch (e) {
        showStatus('Fehler beim Aktualisieren', 'error');
    }
}

function exportCompanies() {
    const jt = document.getElementById('companyJobType').value;
    if (!companiesData[jt]) return showStatus('Keine Daten', 'error');
    const comps = companiesData[jt];
    const csv = ['Unternehmen,Anzahl,Sichtbar', ...comps.map(c => `"${c.name}",${c.count},${c.visible}`)].join('\n');
    const blob = new Blob([csv], {type: 'text/csv;charset=utf-8;'});
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `companies_${jt}_${new Date().toISOString().split('T')[0]}.csv`;
    a.click();
    window.URL.revokeObjectURL(url);
    showStatus('Exportiert', 'success');
}


async function toggleCityJobs(event, city, bundesland = '', containerId, jobType = '', category = '') {
    event.stopPropagation();
    const container = document.getElementById(containerId);
    const clickedSpan = event.target;
    
    if (container.classList.contains('show')) {
        container.classList.remove('show');
        container.innerHTML = '';
        clickedSpan.innerHTML = clickedSpan.innerHTML.replace('▲', '▼');
        return;
    }
    
    clickedSpan.innerHTML = clickedSpan.innerHTML.replace('▼', '▲');
    container.innerHTML = '<div style="padding:10px;text-align:center;"><div class="spinner" style="width:20px;height:20px;"></div></div>';
    
    try {
        let url = `${API_BASE_URL}/jobs/by-city?city=${encodeURIComponent(city)}`;
        if (jobType) url += `&job_type=${encodeURIComponent(jobType)}`;
        if (category) url += `&category=${encodeURIComponent(category)}`;
        
        const r = await fetch(url);
        if (!r.ok) throw new Error('Fehler');
        let jobs = await r.json();
        
        // Apply keyword filters
        jobs = filterJobsByKeywords(jobs);
        
        if (jobs.length === 0) {
            container.innerHTML = '<p style="padding:10px;color:#6c757d;">Keine detaillierten Job-Daten verfügbar.</p>';
            container.classList.add('show');
            return;
        }
        
        let html = '<div class="jobs-list">';
        jobs.forEach(job => {
            html += `<div class="job-item">`;
            html += `<a href="${job.url}" target="_blank" rel="noopener noreferrer" class="job-link">📄 ${job.title}</a>`;
            html += `<div class="job-meta">`;
            html += `🏢 ${job.company || 'Unbekannt'}`;
            if (job.city) html += ` | 📍 ${job.city}`;
            html += ` | 💼 ${job.job_type}`;
            if (job.category) html += ` | 👨‍💻 ${job.category}`;
            html += `</div></div>`;
        });
        html += `</div>`;
        
        container.innerHTML = html;
        container.classList.add('show');
    } catch (e) {
        container.innerHTML = '<p style="padding:10px;color:#dc3545;">Fehler beim Laden der Job-Details</p>';
        container.classList.add('show');
    }
}

async function toggleCompanyJobs(event, company, jobType, containerId) {
    event.stopPropagation();
    const container = document.getElementById(containerId);
    const clickedSpan = event.target;
    
    if (container.classList.contains('show')) {
        container.classList.remove('show');
        container.innerHTML = '';
        clickedSpan.innerHTML = clickedSpan.innerHTML.replace('▲', '▼');
        return;
    }
    
    clickedSpan.innerHTML = clickedSpan.innerHTML.replace('▼', '▲');
    container.innerHTML = '<div style="padding:10px;text-align:center;"><div class="spinner" style="width:20px;height:20px;"></div></div>';
    
    try {
        let url = `${API_BASE_URL}/jobs/by-company?company=${encodeURIComponent(company)}`;
        if (jobType) url += `&job_type=${encodeURIComponent(jobType)}`;
        
        const r = await fetch(url);
        if (!r.ok) throw new Error('Fehler');
        let jobs = await r.json();
        
        // Apply keyword filters
        jobs = filterJobsByKeywords(jobs);
        
        if (jobs.length === 0) {
            container.innerHTML = '<p style="padding:10px;color:#6c757d;">Keine detaillierten Job-Daten verfügbar.</p>';
            container.classList.add('show');
            return;
        }
        
        let html = '<div class="jobs-list">';
        jobs.forEach(job => {
            html += `<div class="job-item">`;
            html += `<a href="${job.url}" target="_blank" rel="noopener noreferrer" class="job-link">📄 ${job.title}</a>`;
            html += `<div class="job-meta">`;
            if (job.city) html += `📍 ${job.city} | `;
            html += `💼 ${job.job_type}`;
            if (job.category) html += ` | 👨‍💻 ${job.category}`;
            html += `</div></div>`;
        });
        html += `</div>`;
        
        container.innerHTML = html;
        container.classList.add('show');
    } catch (e) {
        container.innerHTML = '<p style="padding:10px;color:#dc3545;">Fehler beim Laden der Job-Details</p>';
        container.classList.add('show');
    }
}


async function toggleChartJobs(event, category, jobType, containerId) {
    const container = document.getElementById(containerId);
    
    if (container.classList.contains('show')) {
        container.classList.remove('show');
        container.innerHTML = '';
        return;
    }
    
    container.innerHTML = '<div style="padding:10px;text-align:center;"><div class="spinner" style="width:20px;height:20px;"></div><p>Lade Jobs für ' + category + '...</p></div>';
    
    try {
        let url = `${API_BASE_URL}/jobs/by-category?category=${encodeURIComponent(category)}&job_type=${encodeURIComponent(jobType)}`;
        
        const r = await fetch(url);
        if (!r.ok) throw new Error('Fehler');
        const jobs = await r.json();
        
        if (jobs.length === 0) {
            container.innerHTML = '<p style="padding:10px;color:#6c757d;">Keine detaillierten Job-Daten verfügbar. Bitte führen Sie ein detailliertes Scraping durch.</p>';
            container.classList.add('show');
            return;
        }
        
        let html = `<div style="padding:15px;background:#f8f9fa;border-radius:8px;margin-top:15px;">`;
        html += `<h3 style="color:#667eea;margin-bottom:15px;">📄 ${jobs.length} Stellenangebote: ${category} - ${jobType}</h3>`;
        html += '<div class="jobs-list">';
        
        jobs.forEach(job => {
            html += `<div class="job-item">`;
            html += `<a href="${job.url}" target="_blank" rel="noopener noreferrer" class="job-link">📄 ${job.title}</a>`;
            html += `<div class="job-meta">`;
            html += `🏢 ${job.company || 'Unbekannt'}`;
            if (job.city) html += ` | 📍 ${job.city}`;
            html += `</div></div>`;
        });
        
        html += `</div></div>`;
        
        container.innerHTML = html;
        container.classList.add('show');
    } catch (e) {
        container.innerHTML = '<p style="padding:10px;color:#dc3545;">Fehler beim Laden der Job-Details. Möglicherweise wurden noch keine detaillierten Daten gescraped.</p>';
        container.classList.add('show');
    }
}


// ============================================
// EXCLUDE KEYWORDS MANAGEMENT
// ============================================

function renderExcludeKeywords() {
    const list = document.getElementById('excludeKeywordsList');
    if (!list) return;
    
    if (excludeKeywords.length === 0) {
        list.innerHTML = '<p style="color:#6c757d;font-size:0.85em;padding:10px;text-align:center;">Keine Ausschluss-Keywords definiert</p>';
        return;
    }
    
    list.innerHTML = excludeKeywords.map((item, index) => `
        <div class="keyword-tag ${item.matchType === 'whole' ? 'whole-word' : ''}">
            <span>${item.keyword}</span>
            <span class="match-type">(${item.matchType === 'whole' ? 'Ganzes Wort' : 'Teil'})</span>
            <button onclick="removeExcludeKeyword(${index})" title="Entfernen">×</button>
        </div>
    `).join('');
}

function addExcludeKeyword() {
    const input = document.getElementById('newExcludeKeyword');
    const matchType = document.getElementById('keywordMatchType').value;
    const keyword = input.value.trim();
    
    if (!keyword) {
        alert('Bitte geben Sie ein Keyword ein');
        return;
    }
    
    // Check if already exists
    const exists = excludeKeywords.some(item => 
        item.keyword.toLowerCase() === keyword.toLowerCase() && 
        item.matchType === matchType
    );
    
    if (exists) {
        alert('Dieses Keyword existiert bereits');
        return;
    }
    
    excludeKeywords.push({ keyword, matchType });
    localStorage.setItem('excludeKeywords', JSON.stringify(excludeKeywords));
    
    input.value = '';
    renderExcludeKeywords();
    
    // Re-apply filters to all views
    applyKeywordFilters();
}

function removeExcludeKeyword(index) {
    excludeKeywords.splice(index, 1);
    localStorage.setItem('excludeKeywords', JSON.stringify(excludeKeywords));
    renderExcludeKeywords();
    
    // Re-apply filters to all views
    applyKeywordFilters();
}

function shouldExcludeJob(jobTitle) {
    if (!jobTitle) return false;
    
    for (const item of excludeKeywords) {
        if (item.matchType === 'whole') {
            // Whole word matching - use word boundaries
            const regex = new RegExp(`\\b${item.keyword}\\b`, 'i');
            if (regex.test(jobTitle)) {
                return true;
            }
        } else {
            // Partial matching - case insensitive
            if (jobTitle.toLowerCase().includes(item.keyword.toLowerCase())) {
                return true;
            }
        }
    }
    
    return false;
}

function applyKeywordFilters() {
    // Reload all views with filters applied
    if (currentData.length > 0) {
        loadData();
    }
    if (locationsData.length > 0) {
        updateHeatmap();
    }
    if (Object.keys(companiesData).length > 0) {
        loadCompaniesData();  // Reload companies data with filters
    }
}

function filterJobsByKeywords(jobs) {
    return jobs.filter(job => {
        // First check include filter (if any)
        if (!shouldIncludeJob(job.title)) return false;
        
        // Then check exclude filter
        if (shouldExcludeJob(job.title)) return false;
        
        return true;
    });
}


function shouldIncludeJob(jobTitle) {
    if (!jobTitle) return false;
    if (includeKeywords.length === 0) return true; // No include filter = include all
    
    // Must match at least ONE include keyword
    for (const item of includeKeywords) {
        if (item.matchType === 'whole') {
            const regex = new RegExp(`\\b${item.keyword}\\b`, 'i');
            if (regex.test(jobTitle)) {
                return true;
            }
        } else {
            if (jobTitle.toLowerCase().includes(item.keyword.toLowerCase())) {
                return true;
            }
        }
    }
    
    return false;
}

// ============================================
// INCLUDE KEYWORDS MANAGEMENT
// ============================================

function renderIncludeKeywords() {
    const list = document.getElementById('includeKeywordsList');
    if (!list) return;
    
    if (includeKeywords.length === 0) {
        list.innerHTML = '<p style="color:#6c757d;font-size:0.85em;padding:10px;text-align:center;">Keine Include-Keywords (alle Jobs werden angezeigt)</p>';
        return;
    }
    
    list.innerHTML = includeKeywords.map((item, index) => `
        <div class="keyword-tag" style="background:#d1ecf1;border-color:#17a2b8;color:#0c5460;">
            <span>${item.keyword}</span>
            <span class="match-type">(${item.matchType === 'whole' ? 'Ganzes Wort' : 'Teil'})</span>
            <button onclick="removeIncludeKeyword(${index})" title="Entfernen">×</button>
        </div>
    `).join('');
}

function addIncludeKeyword() {
    const input = document.getElementById('newIncludeKeyword');
    const matchType = document.getElementById('includeKeywordMatchType').value;
    const keyword = input.value.trim();
    
    if (!keyword) {
        alert('Bitte geben Sie ein Keyword ein');
        return;
    }
    
    const exists = includeKeywords.some(item => 
        item.keyword.toLowerCase() === keyword.toLowerCase() && 
        item.matchType === matchType
    );
    
    if (exists) {
        alert('Dieses Keyword existiert bereits');
        return;
    }
    
    includeKeywords.push({ keyword, matchType });
    localStorage.setItem('includeKeywords', JSON.stringify(includeKeywords));
    
    input.value = '';
    renderIncludeKeywords();
    applyKeywordFilters();
}

function removeIncludeKeyword(index) {
    includeKeywords.splice(index, 1);
    localStorage.setItem('includeKeywords', JSON.stringify(includeKeywords));
    renderIncludeKeywords();
    applyKeywordFilters();
}

function addSuggestedIncludeKeyword(keyword) {
    const matchType = 'whole'; // Default for suggestions
    
    const exists = includeKeywords.some(item => 
        item.keyword.toLowerCase() === keyword.toLowerCase()
    );
    
    if (exists) {
        alert('Dieses Keyword existiert bereits');
        return;
    }
    
    includeKeywords.push({ keyword, matchType });
    localStorage.setItem('includeKeywords', JSON.stringify(includeKeywords));
    renderIncludeKeywords();
    applyKeywordFilters();
}
