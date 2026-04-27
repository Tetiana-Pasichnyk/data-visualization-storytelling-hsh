# Arbeitsagentur Job Scraper

Ein Tool zum täglichen Überwachen von IT-Stellenangeboten auf der Arbeitsagentur-Website mit zwei verschiedenen Implementierungen.

## 📁 Projekt-Struktur

```
job_scraper/
├── backend/              # Python Backend (Streamlit + Scheduler)
│   ├── config.py
│   ├── scraper.py
│   ├── streamlit_app.py
│   ├── scheduler.py
│   ├── backend_api.py
│   ├── requirements.txt
│   └── run_streamlit.sh/bat
│
├── webapp/               # Pure JavaScript Webapp (NO Backend!)
│   ├── index.html
│   ├── app.js
│   ├── backend.py       # Optional Python backend
│   ├── requirements.txt
│   └── README.md
│
├── README.md            # This file
└── QUICKSTART.md        # Quick start guide
```

## 🚀 Zwei Versionen

### Version 1: Streamlit App (Python)

**Vollständige Python-Lösung mit Backend**

- ✅ Streamlit Web-Interface
- ✅ Matplotlib & Plotly Express Visualisierungen
- ✅ Automatisches tägliches Scraping
- ✅ Datenbank-Speicherung (JSON + CSV)
- ✅ Scheduler für automatische Updates

**Start:**
```bash
cd backend
pip install -r requirements.txt
streamlit run streamlit_app.py
```

### Version 2: Pure JavaScript Webapp

**100% Client-Side - Kein Backend erforderlich!**

- ✅ Läuft komplett im Browser
- ✅ Ruft Arbeitsagentur API direkt auf
- ✅ Speichert Daten in localStorage
- ✅ Chart.js Visualisierungen
- ✅ Keine Installation nötig

**Start:**
```bash
cd webapp
# Einfach index.html im Browser öffnen!
# Oder mit lokalem Server:
python -m http.server 8000
```

## 🎯 Features

### Gemeinsame Features

- ✅ Offizielle Arbeitsagentur Jobsuche API
- ✅ Modulare Berufsfelder (einfach erweiterbar)
- ✅ 3 Angebotsarten (Arbeit, Ausbildung, Selbstständigkeit)
- ✅ Interaktive Visualisierungen
- ✅ Zeitverlauf-Diagramme
- ✅ CSV-Export

### Streamlit-Spezifisch

- ✅ Automatisches tägliches Scraping
- ✅ Persistente Datenspeicherung
- ✅ Matplotlib & Plotly Charts
- ✅ Backend-API verfügbar

### Webapp-Spezifisch

- ✅ Keine Installation erforderlich
- ✅ Läuft komplett im Browser
- ✅ Funktioniert offline (nach erstem Scrape)
- ✅ Privat (Daten bleiben im Browser)

## 📊 Standard-Berufsfelder

- Business Intelligence
- Full-Stack
- Data Scientist
- Data Analyst
- System Administrator
- DevOps Engineer
- Backend Developer
- Frontend Developer
- Machine Learning Engineer
- Cloud Architect

## 🔧 Welche Version soll ich nutzen?

### Nutze **Streamlit** wenn du:
- ✅ Automatisches tägliches Scraping möchtest
- ✅ Historische Daten langfristig speichern willst
- ✅ Python bevorzugst
- ✅ Matplotlib/Plotly Visualisierungen möchtest
- ✅ Einen Server/Computer hast, der dauerhaft läuft

### Nutze **Webapp** wenn du:
- ✅ Keine Installation möchtest
- ✅ Schnell starten willst
- ✅ Keinen Server betreiben möchtest
- ✅ Daten im Browser speichern willst
- ✅ Maximale Privatsphäre möchtest

## 📖 Dokumentation

- **QUICKSTART.md** - Schnellstart-Anleitung
- **backend/README.md** - Streamlit-Dokumentation (coming soon)
- **webapp/README.md** - Webapp-Dokumentation

## 🔑 API-Details

Beide Versionen nutzen die offizielle Arbeitsagentur Jobsuche API:

- **Base URL:** `https://rest.arbeitsagentur.de/jobboerse/jobsuche-service`
- **API Key:** `jobboerse-jobsuche` (öffentlicher Schlüssel)
- **Endpoint:** `/pc/v4/app/jobs`

## 🛠️ Installation

### Streamlit Version

```bash
cd backend
pip install -r requirements.txt
streamlit run streamlit_app.py
```

### Webapp Version

```bash
cd webapp
# Keine Installation nötig!
# Einfach index.html öffnen
```

## 📝 Konfiguration

### Berufsfelder anpassen

**Streamlit:** Bearbeite `backend/config.py`
```python
JOB_CATEGORIES = [
    "Business Intelligence",
    "Dein Berufsfeld"
]
```

**Webapp:** Bearbeite `webapp/app.js` oder füge sie in der UI hinzu
```javascript
let jobCategories = [
    "Business Intelligence",
    "Dein Berufsfeld"
];
```

## 🤝 Kompatibilität

Beide Versionen können parallel genutzt werden:
- Streamlit für automatisches Scraping
- Webapp für schnelle Abfragen

## 📄 Lizenz

Dieses Projekt ist für Bildungszwecke erstellt. Die Nutzung der Arbeitsagentur-API unterliegt deren Nutzungsbedingungen.

## ⚠️ Hinweise

- Seien Sie respektvoll mit der API
- Die API hat möglicherweise Rate Limits
- Speichern Sie keine personenbezogenen Daten
- Dieses Tool dient nur zur Überwachung von Stellenangebotszahlen

## 🆘 Support

Bei Problemen:
1. Lesen Sie die jeweilige README in `backend/` oder `webapp/`
2. Überprüfen Sie die QUICKSTART.md
3. Prüfen Sie die Browser-Konsole (F12) auf Fehler
4. Stellen Sie sicher, dass alle Abhängigkeiten installiert sind

## 🎓 Lernziele

Dieses Projekt demonstriert:
- API-Integration (REST)
- Datenvisualisierung (Matplotlib, Plotly, Chart.js)
- Web-Entwicklung (Streamlit, Pure JS)
- Datenmanagement (JSON, CSV, localStorage)
- Scheduling (Python schedule)
- Client-Server-Architektur

---

**Viel Erfolg bei der Job-Suche! 🚀**