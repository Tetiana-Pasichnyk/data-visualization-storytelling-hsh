# 📊 Datenquellen-Erklärung

## Problem: Unterschiedliche Zahlen in verschiedenen Tabs

Sie sehen unterschiedliche Stellenzahlen in:
- **Diagramme Tab**: Z.B. 5000 Stellen
- **Heatmap Tab**: Z.B. 479 Stellen
- **Unternehmen Tab**: Z.B. 468 Stellen

**Das ist NORMAL und kein Bug!** Hier ist warum:

---

## 🔍 Zwei verschiedene Scraping-Arten

### 1. **Einfaches Scraping** ("Jetzt scrapen")
- **Datei**: `job_data.json`
- **Verwendet von**: Diagramme Tab
- **Was wird gespeichert**: Nur Zählungen
- **Schnell**: ~30 Sekunden
- **Beispiel**:
  ```json
  {
    "category": "Business Intelligence",
    "job_type": "Arbeit",
    "count": 150,
    "date": "2026-04-25"
  }
  ```

### 2. **Detailliertes Scraping** ("Detailliert Scrapen")
- **Dateien**: `job_details.json`, `locations_data.json`, `companies_data.json`
- **Verwendet von**: Heatmap Tab, Unternehmen Tab, Clickable Job-Listen
- **Was wird gespeichert**: Vollständige Job-Details
- **Langsam**: ~5-15 Minuten
- **Beispiel**:
  ```json
  {
    "title": "Data Analyst (m/w/d)",
    "company": "SAP SE",
    "category": "Business Intelligence",
    "job_type": "Arbeit",
    "location": {
      "city": "München",
      "lat": 48.1351,
      "lon": 11.5820
    },
    "url": "https://..."
  }
  ```

---

## 📈 Warum unterschiedliche Zahlen?

### Szenario 1: Nur einfaches Scraping gemacht
```
Diagramme:  5000 Stellen ✅ (aus job_data.json)
Heatmap:    0 Stellen    ❌ (job_details.json existiert nicht)
Unternehmen: 0 Stellen   ❌ (companies_data.json existiert nicht)
```

### Szenario 2: Beide Scraping-Arten gemacht, aber zu unterschiedlichen Zeiten
```
Diagramme:  5000 Stellen ✅ (gescraped heute 14:00)
Heatmap:    479 Stellen  ✅ (gescraped gestern 10:00)
Unternehmen: 468 Stellen ✅ (gescraped gestern 10:00)
```

### Szenario 3: Detailliertes Scraping mit Limit
```
Diagramme:  5000 Stellen ✅ (alle Jobs)
Heatmap:    500 Stellen  ✅ (max 50 pro Kategorie = 10 Kategorien × 50)
Unternehmen: 500 Stellen ✅ (gleiche Daten)
```

---

## ✅ Lösung: Synchronisierte Daten

### Option A: Nur detailliertes Scraping verwenden
1. **Detailliert Scrapen** klicken
2. Warten bis fertig
3. **Alle Tabs zeigen gleiche Daten**

**Vorteil**: Konsistente Daten überall
**Nachteil**: Dauert länger (5-15 Min)

### Option B: Beide Scraping-Arten gleichzeitig
1. **Jetzt scrapen** klicken (für Diagramme)
2. **Detailliert Scrapen** klicken (für Heatmap/Unternehmen)
3. Beide zur gleichen Zeit ausführen

**Vorteil**: Schnelle Übersicht + Details
**Nachteil**: Zahlen können leicht abweichen

---

## 🎯 Empfehlung

### Für Produktiv-Nutzung:
```bash
# Einmal täglich detailliert scrapen
python3 backend.py &
# Dann in Webapp: "Detailliert Scrapen" klicken
```

### Für schnelle Checks:
```bash
# Nur einfaches Scraping
# In Webapp: "Jetzt scrapen" klicken
```

---

## 📊 Datenfluss-Diagramm

```
┌─────────────────────┐
│  "Jetzt scrapen"    │
│  (Einfach)          │
└──────────┬──────────┘
           │
           ▼
    job_data.json
           │
           ▼
    ┌──────────┐
    │ Diagramme│
    └──────────┘


┌─────────────────────┐
│ "Detailliert        │
│  Scrapen"           │
└──────────┬──────────┘
           │
           ├──► job_details.json ──► Heatmap (Statistiken)
           │                     └──► Clickable Job-Listen
           │
           ├──► locations_data.json ──► Heatmap (Karte)
           │
           └──► companies_data.json ──► Unternehmen Tab
```

---

## 🔧 Technische Details

### Einfaches Scraping
- **API-Call**: `/stellenangebote?was={category}&angebotsart={type}`
- **Response**: Nur `{"anzahlGesamt": 150}`
- **Speichert**: Nur die Zahl

### Detailliertes Scraping
- **API-Call**: `/stellenangebote?was={category}&angebotsart={type}&page=1`
- **Response**: Vollständige Job-Objekte mit allen Details
- **Speichert**: Titel, Firma, Standort, URL, etc.
- **Limit**: Standard 50 pro Kategorie (konfigurierbar)

---

## ❓ FAQ

**Q: Warum nicht immer detailliert scrapen?**
A: Dauert viel länger und belastet die API mehr.

**Q: Kann ich das Limit erhöhen?**
A: Ja, in der Sidebar bei "Detailliert Scrapen" → max_per_category ändern.

**Q: Warum sind Heatmap-Zahlen kleiner als Diagramme?**
A: Heatmap zeigt nur Jobs MIT Standort. Siehe Statistiken für Details.

**Q: Wie oft sollte ich scrapen?**
A: Einmal täglich reicht. Stellenangebote ändern sich nicht stündlich.

---

## 🚀 Best Practice

```python
# Empfohlener Workflow:

# 1. Morgens: Detailliertes Scraping
#    → Alle Daten aktuell und konsistent

# 2. Tagsüber: Nur Diagramme anschauen
#    → Schneller Überblick

# 3. Bei Bedarf: Einzelne Kategorien detailliert nachscrapen
#    → Gezielte Updates
```

---

## 📝 Zusammenfassung

| Tab | Datenquelle | Scraping-Art | Aktualisierung |
|-----|-------------|--------------|----------------|
| Diagramme | job_data.json | Einfach | "Jetzt scrapen" |
| Heatmap | job_details.json + locations_data.json | Detailliert | "Detailliert Scrapen" |
| Unternehmen | companies_data.json | Detailliert | "Detailliert Scrapen" |
| Job-Listen (onClick) | job_details.json | Detailliert | "Detailliert Scrapen" |

**Merke**: Unterschiedliche Zahlen = Unterschiedliche Datenquellen = Normal! ✅