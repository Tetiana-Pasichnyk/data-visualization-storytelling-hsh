# Modulare Filter-Architektur

## Übersicht

Die Keyword-Filter-Funktionalität wurde nach **Software Engineering Best Practices** implementiert:

- ✅ **Separation of Concerns**: Filter-Logik getrennt von UI-Code
- ✅ **DRY (Don't Repeat Yourself)**: Eine zentrale Filter-Funktion für alle Tabs
- ✅ **Single Responsibility**: Jedes Modul hat eine klare Aufgabe
- ✅ **Wiederverwendbarkeit**: API-Endpoints können von allen Tabs genutzt werden

## Architektur-Komponenten

### 1. Backend: `backend.py`

#### Modulare Filter-Funktion
```python
def apply_keyword_filters(jobs, include_keywords=None, exclude_keywords=None):
    """
    Zentrale, wiederverwendbare Filter-Funktion
    - Akzeptiert Job-Liste und Keyword-Arrays
    - Unterstützt whole-word und partial matching
    - Gibt gefilterte Job-Liste zurück
    """
```

#### API-Endpoints

**Neuer Endpoint für Diagramme:**
- `POST /api/jobs/filtered`
- Akzeptiert: `includeKeywords`, `excludeKeywords`
- Gibt zurück: Aggregierte Counts pro Kategorie/Job-Typ

**Aktualisierte Endpoints:**
- `POST /api/jobs/by-category` (vorher GET)
- `POST /api/jobs/by-city` (vorher GET)
- `POST /api/jobs/by-company` (vorher GET)

Alle nutzen die zentrale `apply_keyword_filters()` Funktion.

### 2. Frontend: `filters.js`

**Modulares JavaScript-Modul** für Filter-Management:

```javascript
// Zentrale Filter-State
let includeKeywords = [];
let excludeKeywords = [];

// Public API
function getFilterPayload()        // Für API-Calls
function addIncludeKeyword()       // CRUD
function removeIncludeKeyword()    // CRUD
function addExcludeKeyword()       // CRUD
function removeExcludeKeyword()    // CRUD
function notifyFilterChange()      // Event-System
function hasActiveFilters()        // Status-Check
```

**Event-System:**
```javascript
// Filter-Änderungen werden über Custom Events kommuniziert
window.dispatchEvent(new CustomEvent('filtersChanged', {
    detail: getFilterPayload()
}));
```

### 3. Integration in `app.js`

Jeder Tab hört auf Filter-Änderungen:

```javascript
// Diagramme Tab
window.addEventListener('filtersChanged', (e) => {
    loadFilteredData();  // Lädt Daten mit neuen Filtern
});

// Heatmap Tab
window.addEventListener('filtersChanged', (e) => {
    updateHeatmap();  // Aktualisiert Karte
});

// Companies Tab
window.addEventListener('filtersChanged', (e) => {
    loadCompanies();  // Aktualisiert Unternehmensliste
});
```

## Datenfluss

```
User Action (Add/Remove Keyword)
    ↓
filters.js: Update State + Save to localStorage
    ↓
filters.js: notifyFilterChange() → Custom Event
    ↓
app.js: Event Listener in jedem Tab
    ↓
API Call mit getFilterPayload()
    ↓
backend.py: apply_keyword_filters()
    ↓
Gefilterte Daten zurück an Frontend
    ↓
UI Update (Charts, Maps, Lists)
```

## Vorteile dieser Architektur

### 1. Wartbarkeit
- Filter-Logik an **einem Ort** (backend.py)
- Änderungen müssen nur einmal gemacht werden
- Einfaches Debugging

### 2. Konsistenz
- Alle Tabs nutzen **dieselbe Filter-Logik**
- Keine Diskrepanzen zwischen Tabs
- Garantierte Synchronisation

### 3. Erweiterbarkeit
- Neue Filter-Typen einfach hinzufügbar
- Neue Tabs können Filter sofort nutzen
- API-Endpoints sind generisch

### 4. Performance
- Server-seitige Filterung (einmal statt 3x)
- Caching möglich
- Reduzierte Netzwerk-Last

## Verwendung

### Diagramme Tab

```javascript
async function loadFilteredData() {
    const response = await fetch('/api/jobs/filtered', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(getFilterPayload())
    });
    
    const data = await response.json();
    // data.aggregated enthält gefilterte Counts
    updateCharts(data.aggregated);
}
```

### Heatmap/Companies Tab

```javascript
async function loadJobsByCity(city) {
    const response = await fetch('/api/jobs/by-city', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            city: city,
            ...getFilterPayload()  // Filter automatisch inkludiert
        })
    });
    
    const jobs = await response.json();
    displayJobs(jobs);
}
```

## Migration von bestehendem Code

### Vorher (Frontend-Filterung)
```javascript
// Filter-Logik in app.js dupliziert
function filterJobsByKeywords(jobs) {
    // 100+ Zeilen Code
    // Muss in jedem Tab wiederholt werden
}
```

### Nachher (Backend-Filterung)
```javascript
// Einfacher API-Call mit Filter-Payload
const data = await fetch('/api/jobs/filtered', {
    method: 'POST',
    body: JSON.stringify(getFilterPayload())
});
```

## Testing

### Backend-Tests
```python
# Test filter function
jobs = [
    {'title': 'Junior Developer', 'category': 'Frontend'},
    {'title': 'Senior Developer', 'category': 'Backend'}
]

include = [{'keyword': 'Junior', 'matchType': 'whole'}]
exclude = [{'keyword': 'Senior', 'matchType': 'whole'}]

filtered = apply_keyword_filters(jobs, include, exclude)
# Ergebnis: Nur 'Junior Developer'
```

### Frontend-Tests
```javascript
// Test event system
window.addEventListener('filtersChanged', (e) => {
    console.log('Filters updated:', e.detail);
});

addIncludeKeyword();  // Sollte Event auslösen
```

## Zukünftige Erweiterungen

### Mögliche Features:
1. **Regex-Support**: Erweiterte Pattern-Matching
2. **Saved Filter Sets**: Benutzer können Filter-Kombinationen speichern
3. **Filter-Presets**: Vordefinierte Filter für häufige Szenarien
4. **Filter-Analytics**: Statistiken über Filter-Nutzung
5. **Export/Import**: Filter-Konfigurationen teilen

### Implementierung wäre einfach:
```python
# Neue Filter-Typen in apply_keyword_filters() hinzufügen
if match_type == 'regex':
    if re.search(keyword, title, re.IGNORECASE):
        matches = True
```

## Zusammenfassung

Diese Architektur folgt **SOLID-Prinzipien**:
- **S**ingle Responsibility: Jedes Modul hat eine Aufgabe
- **O**pen/Closed: Erweiterbar ohne bestehenden Code zu ändern
- **L**iskov Substitution: Filter-Funktion ist austauschbar
- **I**nterface Segregation: Klare API-Contracts
- **D**ependency Inversion: Tabs abhängig von Abstraktionen, nicht Implementierungen

**Resultat**: Wartbarer, erweiterbarer, testbarer Code! 🎉