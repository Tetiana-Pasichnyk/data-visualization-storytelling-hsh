# Datensätze – Lektion 2

## Überblick

Für Lektion 2 stehen zwei **lokale CSV-Datensätze** und ein **externer Referenzdatensatz** zur Verfügung.

### Ziel der Datensätze
Die Datensätze wurden so ausgewählt, dass sie gezielt zu den Lernzielen von Block 2 passen:

- Matplotlib-Basisplots erstellen
- Seaborn-Standardplots anwenden
- Verteilungen, Vergleiche und Zusammenhänge analysieren
- Skalenniveaus erkennen und Plot-Entscheidungen begründen
- lineare und logarithmische Skalen diskutieren

---

## 1. Lokaler Datensatz: `student_performance.csv`

### Kurzbeschreibung
Ein kompakter Übungsdatensatz mit Leistungsdaten von Studierenden. Er eignet sich besonders für:

- Scatter Plots
- Histogramme
- Balkendiagramme mit Aggregation
- erste Überlegungen zu Skalenniveaus

### Variablen / Data Dictionary

| Variable | Typ | Beschreibung | Vermutetes Skalenniveau |
|----------|-----|--------------|--------------------------|
| `student_id` | Integer | laufende ID der Studierenden | nominal / Identifikator |
| `study_hours` | Float | Lernstunden pro Woche | ratio |
| `exam_score` | Integer | Prüfungsergebnis in Punkten | intervall oder ratio* |
| `attendance_rate` | Integer | Anwesenheit in Prozent | ratio |
| `semester` | String | Semesterkennung (`WS`, `SS`) | nominal |
| `preparation_level` | String | Vorbereitungsniveau (`low`, `medium`, `high`) | ordinal |

\* Für Unterrichtszwecke kann `exam_score` diskutiert werden. In vielen Visualisierungskontexten wird die Variable praktisch wie metrisch behandelt.

### Geeignete Analysen
- Zusammenhang zwischen `study_hours` und `exam_score`
- Verteilung von `attendance_rate`
- Mittelwerte nach `semester`
- Unterschiede nach `preparation_level`

### Beispiel zum Laden
```python
import pandas as pd

students = pd.read_csv("../datasets/student_performance.csv")
students.head()
```

---

## 2. Lokaler Datensatz: `online_retail_sample.csv`

### Kurzbeschreibung
Ein kleiner Retail-Beispieldatensatz mit Bestellungen über mehrere Monate. Er eignet sich besonders für:

- Histogramme und Verteilungsplots
- Scatter Plots
- gruppierte Vergleiche mit Seaborn
- Zeitreihen-Grundlagen
- lineare vs. logarithmische Skalen

### Variablen / Data Dictionary

| Variable | Typ | Beschreibung | Vermutetes Skalenniveau |
|----------|-----|--------------|--------------------------|
| `order_id` | Integer | Bestell-ID | nominal / Identifikator |
| `order_date` | Datum | Datum der Bestellung | intervall / Zeitvariable |
| `category` | String | Produktkategorie | nominal |
| `units_sold` | Integer | Anzahl verkaufter Einheiten | ratio |
| `revenue` | Integer | Umsatz in Euro | ratio |
| `customer_segment` | String | Kundensegment | nominal |
| `discount_pct` | Integer | Rabatt in Prozent | ratio |

### Geeignete Analysen
- Verteilung von `revenue`
- Zusammenhang zwischen `units_sold` und `revenue`
- Vergleich von `revenue` nach `customer_segment`
- Zeitliche Entwicklung von Bestellungen oder Umsatz
- Diskussion: Wann wäre eine Log-Skala sinnvoll?

### Beispiel zum Laden
```python
import pandas as pd

retail = pd.read_csv("../datasets/online_retail_sample.csv")
retail["order_date"] = pd.to_datetime(retail["order_date"])
retail.head()
```

---

## 3. Externer Referenzdatensatz

### Empfehlung: Seaborn Tips Dataset
Der `tips`-Datensatz eignet sich sehr gut für den Einstieg in Seaborn, da er direkt geladen werden kann und viele typische Variablen für Verteilungs-, Beziehungs- und kategoriale Plots enthält.

### Laden mit Seaborn
```python
import seaborn as sns

tips = sns.load_dataset("tips")
tips.head()
```

### Typische Variablen
- `total_bill`
- `tip`
- `sex`
- `smoker`
- `day`
- `time`
- `size`

### Geeignete Analysen
- `histplot` für `total_bill`
- `scatterplot` für `total_bill` vs. `tip`
- `boxplot` oder `violinplot` für `tip` nach `day`
- `barplot` für aggregierte Vergleiche
- Übung zu nominalen, ordinalen und numerischen Variablen

### Vorteil
- kein Download nötig
- ideal für Live-Coding
- in vielen Tutorials dokumentiert

---

## Alternative externer Datensatz (optional)

Falls ein externer CSV- oder Kaggle-Datensatz genutzt werden soll:

### Vorschlag
**Store Sales / Retail Sales Dataset** auf Kaggle oder einer offenen Bildungsplattform

### Worauf achten?
- kleine bis mittlere Dateigröße
- klare Variablennamen
- keine datenschutzkritischen Inhalte
- direkte Nutzbarkeit für:
  - Verteilungen
  - Kategorien
  - Trends über Zeit

---

## Didaktische Hinweise

### Warum zwei lokale Datensätze?
Die lokalen CSV-Dateien sorgen dafür, dass Übungen auch offline oder ohne zusätzliche Downloads zuverlässig funktionieren.

### Warum zusätzlich ein externer Datensatz?
Ein externer Referenzdatensatz zeigt, dass die gleichen Konzepte auch auf bekannte Real-World-Beispiele übertragbar sind.

### Unterrichtslogik
- `student_performance.csv` → ideal für erste Matplotlib-Übungen
- `online_retail_sample.csv` → ideal für Seaborn, Kategorien und Skalen
- `tips` → flexibel für Demos und spontane Erweiterungen

---

## Vorschlag zur Zuordnung in den Übungen

| Übung | Primärer Datensatz | Fokus |
|------|--------------------|-------|
| Übung 1 | `student_performance.csv` | Matplotlib, Multi-Panel-Figur |
| Übung 2 | `online_retail_sample.csv` | Seaborn, Verteilung & Beziehung |
| Übung 3 | beide lokalen Datensätze | Skalenniveaus, Plot-Wahl, Interpretation |

---

## Lizenz- und Nutzungshinweis

- Die lokalen Datensätze in diesem Ordner sind **didaktische Beispiel-Datensätze** für Unterrichtszwecke.
- Beim Einsatz externer Datensätze bitte die jeweilige Lizenz prüfen.
- Für Live-Coding und Übungsbetrieb sollten möglichst frei verfügbare oder eingebettete Datensätze bevorzugt werden.

---

*Erstellt für HsH Data Visualization Kurs – April 2026*