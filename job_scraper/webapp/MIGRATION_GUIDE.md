# 🔄 Migrations- und Aktualisierungsanleitung

## Problem: Alte Daten nach Updates

Nach dem Update auf die neue Version mit getrennten Praktikum/Ausbildung-Kategorien müssen alte Daten migriert werden.

## Lösung 1: Datenmigration (Schnell)

### Schritt 1: Migration ausführen

```bash
cd job_scraper/webapp
python3 migrate_data.py
```

Das Script aktualisiert:
- ✅ `job_data.json` - Umbenennung "Ausbildung" → "Ausbildung/Duales Studium"
- ✅ `job_details.json` - Trennung Praktikum/Ausbildung basierend auf Keywords
- ✅ `locations_data.json` - Trennung Praktikum/Ausbildung
- ✅ `companies_data.json` - Umbenennung der Kategorie

### Schritt 2: Server neu starten

```bash
# Server stoppen (Ctrl+C)
# Server neu starten
python3 backend.py
```

### ⚠️ Einschränkung

Die Migration kann Praktika nur anhand von Keywords im Titel erkennen:
- "praktikum", "praktikant", "intern", "internship"

Für 100% Genauigkeit → **Lösung 2** verwenden.

---

## Lösung 2: Neu Scrapen (Empfohlen)

### Warum neu scrapen?

1. **Garantierte Trennung**: Praktikum wird während des Scrapens korrekt klassifiziert
2. **Aktuelle Daten**: Neueste Stellenangebote
3. **Vollständige Statistiken**: Korrekte Anzahl in Diagrammen und Heatmap

### Schritte:

1. **Alte Daten löschen** (optional):
   ```bash
   cd job_scraper/webapp
   rm job_data.json job_details.json locations_data.json companies_data.json
   ```

2. **Webapp öffnen**: http://localhost:5000

3. **Detailliert Scrapen klicken** in der Sidebar

4. **Warten**: Je nach Anzahl der Kategorien 5-15 Minuten

5. **Fertig**: Alle Tabs aktualisieren sich automatisch

---

## Neue Features nach Update

### 📊 Heatmap Statistiken

Die Heatmap zeigt jetzt:
- **Gesamt Jobs**: Alle gescrapten Jobs
- **Mit Standort**: Jobs mit Geo-Koordinaten (für Karte)
- **Ohne Standort**: Jobs ohne Geo-Daten
- **Coverage %**: Prozentsatz der Jobs mit Standort

**Warum unterschiedliche Zahlen?**
- **Diagramme**: Zeigen ALLE Jobs (auch ohne Standort)
- **Heatmap**: Zeigt nur Jobs MIT Standort
- **Differenz**: Jobs ohne Standort werden in Statistik aufgelistet

### 🔍 Jobs ohne Standort anzeigen

Klicke auf "⚠️ Jobs ohne Standort anzeigen" um zu sehen:
- Welche Jobs keinen Standort haben
- Warum (z.B. "Homeoffice", "Deutschlandweit", etc.)
- Titel, Firma, Kategorie

### 📈 Getrennte Praktikum-Kategorie

- **Ausbildung/Duales Studium**: Nur Ausbildungsplätze
- **Praktikum**: Nur Praktika/Internships
- Beide haben eigene Charts in "Diagramme"
- Beide sind in Heatmap-Filter verfügbar

---

## Häufige Probleme

### Problem: "Anzahl in Diagramme ≠ Anzahl in Heatmap"

**Ursache**: Diagramme zeigen alle Jobs, Heatmap nur Jobs mit Standort

**Lösung**: Normal! Siehe Statistiken für Details.

### Problem: "Praktikum und Ausbildung noch gemischt"

**Ursache**: Alte Daten vor dem Update

**Lösung**: 
1. Migration ausführen (Lösung 1)
2. ODER neu scrapen (Lösung 2 - empfohlen)

### Problem: "Viele Jobs ohne Standort"

**Ursache**: API liefert manchmal keine Geo-Koordinaten

**Mögliche Gründe**:
- Homeoffice-Stellen
- Deutschlandweite Stellen
- Remote-Positionen
- Unvollständige API-Daten

**Keine Lösung nötig**: Das ist normal und wird in Statistiken angezeigt.

---

## Technische Details

### Keyword-basierte Klassifizierung

Das System erkennt Praktika anhand dieser Keywords im Titel:
```python
PRAKTIKUM_KEYWORDS = ['praktikum', 'praktikant', 'intern', 'internship']
```

### API Parameter

- **Arbeit**: `angebotsart=1`
- **Ausbildung/Duales Studium**: `angebotsart=34` (ohne Praktikum-Keywords)
- **Praktikum**: `angebotsart=34` (mit Praktikum-Keywords)
- **Selbstständigkeit**: `angebotsart=4`

### Datenstruktur

```json
{
  "title": "Praktikant Business Intelligence",
  "job_type": "Praktikum",  // Automatisch klassifiziert
  "category": "Business Intelligence",
  "location": {
    "city": "München",
    "lat": 48.1351,
    "lon": 11.5820
  }
}
```

---

## Support

Bei Problemen:
1. Server-Logs prüfen
2. Browser-Konsole öffnen (F12)
3. Migration erneut ausführen
4. Als letztes Mittel: Neu scrapen