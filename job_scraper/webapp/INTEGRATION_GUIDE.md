# Integration Guide: Modulare Filter in app.js

## Schnellstart

### 1. Füge `filters.js` in `index.html` ein

```html
<!-- Vor app.js einfügen -->
<script src="filters.js"></script>
<script src="app.js"></script>
```

### 2. Entferne duplizierte Filter-Funktionen aus `app.js`

**Zu entfernen:**
- `let excludeKeywords = [...]`
- `let includeKeywords = []`
- `function shouldExcludeJob()`
- `function shouldIncludeJob()`
- `function filterJobsByKeywords()`
- `function renderExcludeKeywords()`
- `function renderIncludeKeywords()`
- `function addExcludeKeyword()`
- `function removeExcludeKeyword()`
- `function addIncludeKeyword()`
- `function removeIncludeKeyword()`
- `function addSuggestedIncludeKeyword()`

**Grund:** Diese Funktionen sind jetzt in `filters.js` und werden automatisch geladen.

### 3. Aktualisiere Diagramme-Tab

**Ersetze die `loadData()` Funktion:**

```javascript
async function loadData() {
    try {
        // Verwende neuen /api/jobs/filtered Endpoint
        const response = await fetch('/api/jobs/filtered', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(getFilterPayload())  // Von filters.js
        });
        
        const result = await response.json();
        
        if (result.error) {
            console.error('Error loading data:', result.error);
            return;
        }
        
        // Verwende gefilterte aggregierte Daten
        jobData = result.aggregated;
        
        // Zeige Filter-Info
        if (result.filters_applied.include || result.filters_applied.exclude) {
            console.log(`Filters applied: ${result.total_jobs} → ${result.filtered_jobs} jobs`);
        }
        
        updateCharts();
    } catch (error) {
        console.error('Error loading data:', error);
    }
}
```

**Füge Event Listener hinzu:**

```javascript
// Am Ende von app.js
window.addEventListener('filtersChanged', () => {
    loadData();  // Lädt Daten neu wenn Filter sich ändern
});
```

### 4. Aktualisiere Heatmap-Tab

**Ändere `toggleCityJobs()` Funktion:**

```javascript
async function toggleCityJobs(city, count) {
    const jobList = document.getElementById(`jobs-${city}`);
    
    if (jobList.style.display === 'block') {
        jobList.style.display = 'none';
        return;
    }
    
    // Lade Jobs mit Filtern
    const selectedJobType = document.getElementById('jobTypeFilter').value;
    const selectedCategory = document.getElementById('categoryFilter').value;
    
    const response = await fetch('/api/jobs/by-city', {
        method: 'POST',  // Geändert von GET zu POST
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            city: city,
            job_type: selectedJobType,
            category: selectedCategory,
            ...getFilterPayload()  // Filter automatisch inkludiert
        })
    });
    
    const jobs = await response.json();
    
    // Rest bleibt gleich...
    displayJobs(jobs, jobList);
}
```

**Füge Event Listener hinzu:**

```javascript
window.addEventListener('filtersChanged', () => {
    updateHeatmap();  // Aktualisiert Karte wenn Filter sich ändern
});
```

### 5. Aktualisiere Companies-Tab

**Ändere `toggleCompanyJobs()` Funktion:**

```javascript
async function toggleCompanyJobs(company, count) {
    const jobList = document.getElementById(`company-jobs-${company.replace(/\s+/g, '-')}`);
    
    if (jobList.style.display === 'block') {
        jobList.style.display = 'none';
        return;
    }
    
    // Lade Jobs mit Filtern
    const response = await fetch('/api/jobs/by-company', {
        method: 'POST',  // Geändert von GET zu POST
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            company: company,
            ...getFilterPayload()  // Filter automatisch inkludiert
        })
    });
    
    const jobs = await response.json();
    
    // Rest bleibt gleich...
    displayCompanyJobs(jobs, jobList);
}
```

**Füge Event Listener hinzu:**

```javascript
window.addEventListener('filtersChanged', () => {
    loadCompanies();  // Aktualisiert Unternehmen wenn Filter sich ändern
});
```

### 6. CSS für Include-Keywords

**Füge in `index.html` <style> Sektion ein:**

```css
/* Include-Keywords Styling (blau statt gelb) */
.keyword-tag.include-keyword {
    background-color: #e3f2fd;
    border: 1px solid #2196f3;
    color: #1565c0;
}

.keyword-tag.include-keyword.whole-word {
    background-color: #bbdefb;
    border: 2px solid #1976d2;
}

.keyword-tag.include-keyword .keyword-remove {
    color: #1565c0;
}

.keyword-tag.include-keyword .keyword-remove:hover {
    background-color: #1976d2;
    color: white;
}
```

## Vollständiges Beispiel: Diagramme-Tab Integration

```javascript
// ========================================
// DIAGRAMME TAB
// ========================================

let jobData = [];

async function loadData() {
    try {
        const response = await fetch('/api/jobs/filtered', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(getFilterPayload())
        });
        
        const result = await response.json();
        jobData = result.aggregated;
        
        updateCharts();
        
        // Optional: Zeige Filter-Status
        if (hasActiveFilters()) {
            showFilterStatus(result.total_jobs, result.filtered_jobs);
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

function updateCharts() {
    // Bestehender Chart-Code bleibt unverändert
    updateCategoryChart();
    updateJobTypeChart();
}

// Event Listener für Filter-Änderungen
window.addEventListener('filtersChanged', () => {
    loadData();
});

// Initial load
document.addEventListener('DOMContentLoaded', () => {
    loadData();
});
```

## Testing

### 1. Backend testen

```bash
cd job_scraper/webapp
python backend.py
```

### 2. Filter testen

1. Öffne `http://localhost:5000`
2. Gehe zu Einstellungen
3. Füge Include-Keyword hinzu: "Junior"
4. Wechsle zu Diagramme → Zahlen sollten sich ändern
5. Wechsle zu Heatmap → Karte sollte aktualisiert sein
6. Wechsle zu Unternehmen → Liste sollte gefiltert sein

### 3. Konsole prüfen

```javascript
// In Browser-Konsole
console.log(getFilterPayload());
// Sollte zeigen: { includeKeywords: [...], excludeKeywords: [...] }

console.log(hasActiveFilters());
// Sollte true sein wenn Filter aktiv
```

## Troubleshooting

### Problem: Filter werden nicht angewendet

**Lösung:**
1. Hard-Reload: `Ctrl+Shift+R` (Windows) oder `Cmd+Shift+R` (Mac)
2. Prüfe Browser-Konsole auf Fehler
3. Prüfe ob `filters.js` geladen wurde: `console.log(typeof getFilterPayload)`

### Problem: Diagramme zeigen alte Zahlen

**Lösung:**
1. Klicke "🔄 Vollständig aktualisieren" in Einstellungen
2. Warte bis Scraping fertig ist
3. Filter werden nur auf detaillierte Daten angewendet

### Problem: API-Fehler 405 Method Not Allowed

**Lösung:**
- Endpoints wurden von GET zu POST geändert
- Prüfe ob alle `fetch()` Calls `method: 'POST'` verwenden

## Vorteile der neuen Architektur

✅ **Keine Code-Duplikation**: Filter-Logik nur einmal implementiert  
✅ **Automatische Synchronisation**: Alle Tabs nutzen dieselben Filter  
✅ **Einfache Wartung**: Änderungen nur an einem Ort nötig  
✅ **Bessere Performance**: Server-seitige Filterung  
✅ **Erweiterbar**: Neue Filter-Typen einfach hinzufügbar  

## Nächste Schritte

1. ✅ Backend-Änderungen sind fertig
2. ✅ `filters.js` Modul ist erstellt
3. ⏳ `app.js` muss aktualisiert werden (siehe oben)
4. ⏳ `index.html` muss `filters.js` einbinden
5. ⏳ CSS für Include-Keywords hinzufügen

**Geschätzte Zeit für Integration: 15-30 Minuten**