/**
 * JavaScript Job Scraper with Advanced Features
 * Includes Heatmap and Company Analysis
 */

// Configuration
const API_BASE_URL = 'http://localhost:5000/api';

// Job categories state
let jobCategories = [
    "Business Intelligence",
    "Full-Stack",
    "Data Scientist",
    "Data Analyst",
    "System Administrator",
    "DevOps Engineer",
    "Backend Developer",
    "Frontend Developer",
    "Machine Learning Engineer",
    "Cloud Architect"
];

// Job types
const jobTypes = {
    "Arbeit": 1,
    "Ausbildung": 34,
    "Selbstständigkeit": 4
};

// Chart instances
let charts = {};
let currentData = [];
let locationsData = [];
let companiesData = {};
let map = null;

// Initialize app
document.addEventListener('DOMContentLoaded', function() {
    // Load categories from localStorage
    const savedCategories = localStorage.getItem('jobCategories');
    if (savedCategories) {
        jobCategories = JSON.parse(savedCategories);
    }
    
    renderCategories();
    
    // Try to load data from backend
    loadData();
    
    // Initialize category filter for heatmap
    updateCategoryFilter();
});

/**
 * Switch between tabs
 */
function switchTab(tabName) {
    // Hide all tabs
    document.querySelectorAll('.tab-content').forEach(tab => {
        tab.classList.remove('active');
    });
    
    // Remove active class from all tab buttons
    document.querySelectorAll('.tab').forEach(btn => {
        btn.classList.remove('active');
    });
    
    // Show selected tab
    document.getElementById(`tab-${tabName}`).classList.add('active');
    
    // Add active class to clicked button
    event.target.classList.add('active');
    
    // Load data for specific tabs
    if (tabName === 'heatmap' && locationsData.length === 0) {
        loadHeatmapData();
    } else if (tabName === 'heatmap' && map) {
        map.invalidateSize();
    }
    
    if (tabName === 'companies' && Object.keys(companiesData).length === 0) {
        loadCompaniesData();
    }
}

/**
 * Render categories list
 */
function renderCategories() {
    const container = document.getElementById('categoriesList');
    container.innerHTML = '';
    
    jobCategories.forEach((category, index) => {
        const tag = document.createElement('div');
        tag.className = 'category-tag';
        tag.innerHTML = `
            <span>${category}</span>
            <button onclick="removeCategory(${index})" title="Entfernen">×</button>
        `;
        container.appendChild(tag);
    });
}

/**
 * Add new category
 */
function addCategory() {
    const input = document.getElementById('newCategory');
    const category = input.value.trim();
    
    if (!category) {
        showStatus('Bitte geben Sie ein Berufsfeld ein', 'error');
        return;
    }
    
    if (jobCategories.includes(category)) {
        showStatus('Dieses Berufsfeld existiert bereits', 'error');
        return;
    }
    
    jobCategories.push(category);
    input.value = '';
    renderCategories();
    updateCategoryFilter();
    showStatus(`"${category}" wurde hinzugefügt`, 'success');
    
    // Save to localStorage
    localStorage.setItem('jobCategories', JSON.stringify(jobCategories));
}

/**
 * Remove category
 */
function removeCategory(index) {
    const category = jobCategories[index];
    jobCategories.splice(index, 1);
    renderCategories();
    updateCategoryFilter();
    showStatus(`"${category}" wurde entfernt`, 'info');
    
    // Save to localStorage
    localStorage.setItem('jobCategories', JSON.stringify(jobCategories));
}

/**
 * Show status message
 */
function showStatus(message, type = 'info') {
    const container = document.getElementById('statusMessage');
    container.innerHTML = `<div class="status-message status-${type}">${message}</div>`;
    
    setTimeout(() => {
        container.innerHTML = '';
    }, 5000);
}

/**
 * Scrape now - uses backend API
 */
async function scrapeNow() {
    showStatus('Scraping wird gestartet... Dies kann einige Minuten dauern.', 'info');
    
    try {
        const response = await fetch(`${API_BASE_URL}/scrape`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                categories: jobCategories
            })
        });
        
        if (!response.ok) {
            throw new Error('Scraping fehlgeschlagen');
        }
        
        const data = await response.json();
        showStatus(`Scraping abgeschlossen! ${data.count} Einträge gespeichert`, 'success');
        
        // Reload data from backend
        setTimeout(() => loadData(), 1000);
        
    } catch (error) {
        console.error('Scraping error:', error);
        showStatus('Fehler beim Scraping. Stellen Sie sicher, dass der Backend-Server läuft (python backend.py)', 'error');
    }
}

/**
 * Scrape detailed data for heatmap and companies
 */
async function scrapeDetailed() {
    showStatus('Detailliertes Scraping wird gestartet... Dies kann 5-10 Minuten dauern.', 'info');
    
    try {
        const response = await fetch(`${API_BASE_URL}/scrape-detailed`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                categories: jobCategories,
                max_per_category: 50
            })
        });
        
        if (!response.ok) {
            throw new Error('Detailliertes Scraping fehlgeschlagen');
        }
        
        const data = await response.json();
        showStatus(`Detailliertes Scraping abgeschlossen! ${data.stats.jobs} Jobs, ${data.stats.locations} Standorte, ${data.stats.companies} Unternehmen`, 'success');
        
        // Reload advanced data
        setTimeout(() => {
            loadHeatmapData();
            loadCompaniesData();
        }, 1000);
        
    } catch (error) {
        console.error('Detailed scraping error:', error);
        showStatus('Fehler beim detaillierten Scraping. Stellen Sie sicher, dass der Backend-Server läuft.', 'error');
    }
}

/**
 * Load data from backend
 */
async function loadData() {
    const chartsContainer = document.getElementById('charts');
    chartsContainer.innerHTML = '<div class="loading"><div class="spinner"></div><p>Daten werden geladen...</p></div>';
    
    try {
        const response = await fetch(`${API_BASE_URL}/data`);
        
        if (!response.ok) {
            throw new Error('Daten konnten nicht geladen werden');
        }
        
        const data = await response.json();
        currentData = data;
        
        if (!data || data.length === 0) {
            chartsContainer.innerHTML = '<div class="loading"><p>Keine Daten vorhanden. Bitte führen Sie ein Scraping durch.</p></div>';
            return;
        }
        
        // Update stats
        updateStats(data);
        
        // Render charts
        renderCharts(data);
        
        showStatus('Daten erfolgreich geladen', 'success');
        
    } catch (error) {
        console.error('Load data error:', error);
        chartsContainer.innerHTML = '<div class="loading"><p>Fehler beim Laden der Daten. Stellen Sie sicher, dass der Backend-Server läuft.</p></div>';
        showStatus('Fehler beim Laden der Daten', 'error');
    }
}

/**
 * Clear all data
 */
function clearData() {
    if (confirm('Möchten Sie wirklich alle Daten löschen?')) {
        currentData = [];
        document.getElementById('charts').innerHTML = '<div class="loading"><p>Keine Daten vorhanden.</p></div>';
        document.getElementById('stats').innerHTML = '';
        showStatus('Alle Daten wurden gelöscht', 'info');
    }
}

/**
 * Update statistics
 */
function updateStats(data) {
    const statsContainer = document.getElementById('stats');
    
    if (!data || data.length === 0) {
        statsContainer.innerHTML = '';
        return;
    }
    
    // Calculate stats
    const uniqueCategories = [...new Set(data.map(d => d.category))].length;
    const uniqueJobTypes = [...new Set(data.map(d => d.job_type))].length;
    
    // Get latest data
    const latestDate = data.reduce((max, d) => d.date > max ? d.date : max, data[0].date);
    const latestData = data.filter(d => d.date === latestDate);
    const totalJobs = latestData.reduce((sum, d) => sum + d.count, 0);
    
    statsContainer.innerHTML = `
        <div class="stat-card">
            <h3>${uniqueCategories}</h3>
            <p>Berufsfelder</p>
        </div>
        <div class="stat-card">
            <h3>${uniqueJobTypes}</h3>
            <p>Angebotsarten</p>
        </div>
        <div class="stat-card">
            <h3>${totalJobs.toLocaleString()}</h3>
            <p>Aktuelle Stellenangebote</p>
        </div>
        <div class="stat-card">
            <h3>${data.length}</h3>
            <p>Datenpunkte</p>
        </div>
    `;
}

/**
 * Render all charts
 */
function renderCharts(data) {
    const chartsContainer = document.getElementById('charts');
    
    if (!data || data.length === 0) {
        chartsContainer.innerHTML = '<div class="loading"><p>Keine Daten vorhanden. Bitte führen Sie ein Scraping durch.</p></div>';
        return;
    }
    
    chartsContainer.innerHTML = '';
    
    // Destroy existing charts
    Object.values(charts).forEach(chart => {
        if (chart && typeof chart.destroy === 'function') {
            chart.destroy();
        }
    });
    charts = {};
    
    // Create charts for each job type
    Object.keys(jobTypes).forEach(jobType => {
        const chartContainer = document.createElement('div');
        chartContainer.className = 'chart-container';
        chartContainer.innerHTML = `
            <h2>📊 ${jobType}</h2>
            <div class="chart-wrapper">
                <canvas id="chart-${jobType.replace(/\s+/g, '-')}"></canvas>
            </div>
        `;
        chartsContainer.appendChild(chartContainer);
        
        // Create chart
        createBarChart(data, jobType);
    });
    
    // Add time series chart
    createTimeSeriesChart(data);
}

/**
 * Create bar chart for job type
 */
function createBarChart(data, jobType) {
    const canvasId = `chart-${jobType.replace(/\s+/g, '-')}`;
    const ctx = document.getElementById(canvasId);
    
    // Filter and aggregate data
    const filteredData = data.filter(d => d.job_type === jobType);
    const aggregated = {};
    
    filteredData.forEach(d => {
        if (!aggregated[d.category]) {
            aggregated[d.category] = [];
        }
        aggregated[d.category].push(d.count);
    });
    
    // Calculate averages
    const categories = Object.keys(aggregated);
    const averages = categories.map(cat => {
        const counts = aggregated[cat];
        return counts.reduce((sum, c) => sum + c, 0) / counts.length;
    });
    
    // Sort by average
    const sorted = categories.map((cat, i) => ({ category: cat, average: averages[i] }))
        .sort((a, b) => b.average - a.average);
    
    const labels = sorted.map(s => s.category);
    const values = sorted.map(s => s.average);
    
    // Create gradient
    const gradient = ctx.getContext('2d').createLinearGradient(0, 0, 0, 400);
    gradient.addColorStop(0, 'rgba(102, 126, 234, 0.8)');
    gradient.addColorStop(1, 'rgba(118, 75, 162, 0.8)');
    
    // Create chart
    charts[jobType] = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Durchschnittliche Anzahl',
                data: values,
                backgroundColor: gradient,
                borderColor: 'rgba(102, 126, 234, 1)',
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return `Durchschnitt: ${Math.round(context.parsed.y)} Stellen`;
                        }
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        callback: function(value) {
                            return Math.round(value);
                        }
                    }
                },
                x: {
                    ticks: {
                        maxRotation: 45,
                        minRotation: 45
                    }
                }
            }
        }
    });
}

/**
 * Create time series chart
 */
function createTimeSeriesChart(data) {
    const uniqueCategories = [...new Set(data.map(d => d.category))];
    
    const chartContainer = document.createElement('div');
    chartContainer.className = 'chart-container';
    chartContainer.innerHTML = `
        <h2>📈 Zeitverlauf</h2>
        <div style="margin-bottom: 15px;">
            <label for="categorySelect">Berufsfeld auswählen:</label>
            <select id="categorySelect" onchange="updateTimeSeriesChart()" style="margin-left: 10px; padding: 8px;">
                ${uniqueCategories.map(cat => 
                    `<option value="${cat}">${cat}</option>`
                ).join('')}
            </select>
        </div>
        <div class="chart-wrapper">
            <canvas id="chart-timeseries"></canvas>
        </div>
    `;
    document.getElementById('charts').appendChild(chartContainer);
    
    updateTimeSeriesChart();
}

/**
 * Update time series chart
 */
function updateTimeSeriesChart() {
    const select = document.getElementById('categorySelect');
    if (!select) return;
    
    const category = select.value;
    const ctx = document.getElementById('chart-timeseries');
    
    // Destroy existing chart
    if (charts['timeseries']) {
        charts['timeseries'].destroy();
    }
    
    const filteredData = currentData.filter(d => d.category === category);
    
    // Group by date and job type
    const grouped = {};
    filteredData.forEach(d => {
        if (!grouped[d.job_type]) {
            grouped[d.job_type] = {};
        }
        grouped[d.job_type][d.date] = d.count;
    });
    
    // Get all unique dates
    const dates = [...new Set(filteredData.map(d => d.date))].sort();
    
    // Create datasets
    const colors = [
        { border: 'rgba(102, 126, 234, 1)', bg: 'rgba(102, 126, 234, 0.1)' },
        { border: 'rgba(118, 75, 162, 1)', bg: 'rgba(118, 75, 162, 0.1)' },
        { border: 'rgba(237, 100, 166, 1)', bg: 'rgba(237, 100, 166, 0.1)' }
    ];
    
    const datasets = Object.keys(grouped).map((jobType, index) => {
        return {
            label: jobType,
            data: dates.map(date => grouped[jobType][date] || 0),
            borderColor: colors[index % colors.length].border,
            backgroundColor: colors[index % colors.length].bg,
            tension: 0.4,
            fill: true
        };
    });
    
    // Create chart
    charts['timeseries'] = new Chart(ctx, {
        type: 'line',
        data: {
            labels: dates,
            datasets: datasets
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'top'
                },
                tooltip: {
                    mode: 'index',
                    intersect: false
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        callback: function(value) {
                            return Math.round(value);
                        }
                    }
                }
            }
        }
    });
}

/**
 * Export data as CSV
 */
function exportData() {
    if (!currentData || currentData.length === 0) {
        showStatus('Keine Daten zum Exportieren vorhanden', 'error');
        return;
    }
    
    // Convert to CSV
    const headers = Object.keys(currentData[0]);
    const csv = [
        headers.join(','),
        ...currentData.map(row => headers.map(header => row[header]).join(','))
    ].join('\n');
    
    // Download
    const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `job_data_${new Date().toISOString().split('T')[0]}.csv`;
    a.click();
    window.URL.revokeObjectURL(url);
    
    showStatus('Daten erfolgreich exportiert', 'success');
}

// ============================================
// HEATMAP FUNCTIONALITY
// ============================================

/**
 * Load heatmap data
 */
async function loadHeatmapData() {
    showStatus('Lade Standortdaten...', 'info');
    
    try {
        const response = await fetch(`${API_BASE_URL}/locations`);
        
        if (!response.ok) {
            throw new Error('Standortdaten konnten nicht geladen werden');
        }
        
        locationsData = await response.json();
        
        if (locationsData.length === 0) {
            showStatus('Keine Standortdaten vorhanden. Bitte führen Sie ein detailliertes Scraping durch.', 'info');
            return;
        }
        
        initializeMap();
        updateHeatmap();
        showStatus(`${locationsData.length} Standorte geladen`, 'success');
        
    } catch (error) {
        console.error('Load locations error:', error);
        showStatus('Fehler beim Laden der Standortdaten', 'error');
    }
}

/**
 * Initialize Leaflet map
 */
function initializeMap() {
    if (map) {
        map.remove();
    }
    
    // Create map centered on Germany
    map = L.map('map').setView([51.1657, 10.4515], 6);
    
    // Add OpenStreetMap tiles
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors',
        maxZoom: 18
    }).addTo(map);
}

/**
 * Update heatmap with filters
 */
function updateHeatmap() {
    if (!map) {
        initializeMap();
    }
    
    // Clear existing markers
    map.eachLayer(layer => {
        if (layer instanceof L.CircleMarker) {
            map.removeLayer(layer);
        }
    });
    
    // Get filter values
    const jobTypeFilter = document.getElementById('heatmapJobType').value;
    const categoryFilter = document.getElementById('heatmapCategory').value;
    
    // Filter locations
    let filteredLocations = locationsData;
    
    if (jobTypeFilter) {
        filteredLocations = filteredLocations.filter(loc => loc.job_type === jobTypeFilter);
    }
    
    if (categoryFilter) {
        filteredLocations = filteredLocations.filter(loc => loc.category === categoryFilter);
    }
    
    // Add markers
    filteredLocations.forEach(location => {
        if (location.lat && location.lon) {
            const marker = L.circleMarker([location.lat, location.lon], {
                radius: 6,
                fillColor: '#667eea',
                color: '#fff',
                weight: 1,
                opacity: 1,
                fillOpacity: 0.7
            }).addTo(map);
            
            marker.bindPopup(`
                <strong>${location.company || 'Unbekannt'}</strong><br>
                ${location.city}, ${location.plz}<br>
                <em>${location.category}</em><br>
                <small>${location.job_type}</small>
            `);
        }
    });
    
    // Update stats
    const uniqueCities = [...new Set(filteredLocations.map(l => l.city))].length;
    const uniqueCompanies = [...new Set(filteredLocations.map(l => l.company).filter(c => c))].length;
    
    document.getElementById('heatmapStats').innerHTML = `
        📍 ${filteredLocations.length} Standorte | 
        🏙️ ${uniqueCities} Städte | 
        🏢 ${uniqueCompanies} Unternehmen
    `;
}

/**
 * Update category filter options
 */
function updateCategoryFilter() {
    const select = document.getElementById('heatmapCategory');
    if (!select) return;
    
    const currentValue = select.value;
    select.innerHTML = '<option value="">Alle Berufsfelder</option>';
    
    jobCategories.forEach(category => {
        const option = document.createElement('option');
        option.value = category;
        option.textContent = category;
        if (category === currentValue) {
            option.selected = true;
        }
        select.appendChild(option);
    });
}

// ============================================
// COMPANIES FUNCTIONALITY
// ============================================

/**
 * Load companies data
 */
async function loadCompaniesData() {
    showStatus('Lade Unternehmensdaten...', 'info');
    
    try {
        const response = await fetch(`${API_BASE_URL}/companies`);
        
        if (!response.ok) {
            throw new Error('Unternehmensdaten konnten nicht geladen werden');
        }
        
        companiesData = await response.json();
        
        if (Object.keys(companiesData).length === 0) {
            showStatus('Keine Unternehmensdaten vorhanden. Bitte führen Sie ein detailliertes Scraping durch.', 'info');
            return;
        }
        
        updateCompaniesView();
        showStatus('Unternehmensdaten geladen', 'success');
        
    } catch (error) {
        console.error('Load companies error:', error);
        showStatus('Fehler beim Laden der Unternehmensdaten', 'error');
    }
}

/**
 * Update companies view
 */
function updateCompaniesView() {
    const jobType = document.getElementById('companyJobType').value;
    const limit = parseInt(document.getElementById('companyLimit').value);
    
    if (!companiesData[jobType]) {
        document.getElementById('companiesList').innerHTML = '<p>Keine Daten für diese Angebotsart</p>';
        return;
    }
    
    const companies = companiesData[jobType].slice(0, limit);
    
    // Render companies list
    const listContainer = document.getElementById('companiesList');
    listContainer.innerHTML = '';
    
    companies.forEach(company => {
        const item = document.createElement('div');
        item.className = 'company-item';
        item.innerHTML = `
            <div>
                <strong>${company.name}</strong>
                <span style="color: #6c757d; margin-left: 10px;">${company.count} Stellen</span>
            </div>
            <input type="checkbox" ${company.visible ? 'checked' : ''} 
                   onchange="toggleCompanyVisibility('${jobType}', '${company.name.replace(/'/g, "\\'")}', this.checked)">
        `;
        listContainer.appendChild(item);
    });
    
    // Update chart
    renderCompaniesChart(companies.filter(c => c.visible));
    
    // Update stats
    const totalJobs = companies.reduce((sum, c) => sum + c.count, 0);
    const visibleCompanies = companies.filter(c => c.visible).length;
    
    document.getElementById('companiesStats').innerHTML = `
        🏢 ${companies.length} Unternehmen | 
        📊 ${totalJobs} Stellenangebote | 
        👁️ ${visibleCompanies} sichtbar
    `;
}

/**
 * Render companies chart
 */
function renderCompaniesChart(companies) {
    const ctx = document.getElementById('companiesChart');
    
    // Destroy existing chart
    if (charts['companies']) {
        charts['companies'].destroy();
    }
    
    const labels = companies.map(c => c.name);
    const values = companies.map(c => c.count);
    
    // Create gradient
    const gradient = ctx.getContext('2d').createLinearGradient(0, 0, 0, 400);
    gradient.addColorStop(0, 'rgba(102, 126, 234, 0.8)');
    gradient.addColorStop(1, 'rgba(118, 75, 162, 0.8)');
    
    charts['companies'] = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Anzahl Stellenangebote',
                data: values,
                backgroundColor: gradient,
                borderColor: 'rgba(102, 126, 234, 1)',
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            indexAxis: 'y',
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return `${context.parsed.x} Stellen`;
                        }
                    }
                }
            },
            scales: {
                x: {
                    beginAtZero: true,
                    ticks: {
                        callback: function(value) {
                            return Math.round(value);
                        }
                    }
                }
            }
        }
    });
}

/**
 * Toggle company visibility
 */
async function toggleCompanyVisibility(jobType, companyName, visible) {
    try {
        const response = await fetch(`${API_BASE_URL}/companies/visibility`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                job_type: jobType,
                company_name: companyName,
                visible: visible
            })
        });
        
        if (!response.ok) {
            throw new Error('Fehler beim Aktualisieren der Sichtbarkeit');
        }
        
        const data = await response.json();
        companiesData = data.companies;
        updateCompaniesView();
        
    } catch (error) {
        console.error('Toggle visibility error:', error);
        showStatus('Fehler beim Aktualisieren der Sichtbarkeit', 'error');
    }
}

/**
 * Export companies data
 */
function exportCompanies() {
    const jobType = document.getElementById('companyJobType').value;
    
    if (!companiesData[jobType]) {
        showStatus('Keine Daten zum Exportieren', 'error');
        return;
    }
    
    const companies = companiesData[jobType];
    
    // Convert to CSV
    const csv = [
        'Unternehmen,Anzahl,Sichtbar',
        ...companies.map(c => `"${c.name}",${c.count},${c.visible}`)
    ].join('\n');
    
    // Download
    const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `companies_${jobType}_${new Date().toISOString().split('T')[0]}.csv`;
    a.click();
    window.URL.revokeObjectURL(url);
    
    showStatus('Unternehmensdaten erfolgreich exportiert', 'success');
}

// Made with Bob
