# Block 1: Einführung & Grundlagen
## Data Visualization & Storytelling - HsH

**Dauer:** 1 Tag (270 Minuten = 3 Einheiten à 90 Min)  
**Voraussetzungen:** Keine (Kursstart)  
**Schwierigkeitsgrad:** ⭐☆☆☆☆ (Einsteiger)

---

## 📋 Block-Übersicht

Dieser erste Block führt in die Welt der Datenvisualisierung ein. Studierende lernen die Grundlagen, richten ihre Entwicklungsumgebung ein und erstellen ihre ersten Visualisierungen.

### Lernziele

Nach diesem Block können Studierende:
1. ✓ Die Bedeutung von Datenvisualisierung erklären
2. ✓ Verschiedene Visualisierungstools und Frameworks benennen
3. ✓ Eine Python-Entwicklungsumgebung einrichten
4. ✓ Daten aus verschiedenen Quellen laden
5. ✓ Erste einfache Plots mit Matplotlib erstellen
6. ✓ Jupyter Notebooks verwenden

---

## 📚 Einheit 1.1: Was ist Datenvisualisierung?

**Dauer:** 90 Minuten  
**Format:** Vortrag + Diskussion + Aktivierung

### Zeitplan

| Zeit | Aktivität | Methode |
|------|-----------|---------|
| 0-10 Min | Begrüßung & Vorstellung | Präsentation |
| 10-20 Min | Mentimeter Aktivierung | Interaktiv |
| 20-40 Min | Theorie: Warum Visualisierung? | Vortrag |
| 40-60 Min | Kognitive Prinzipien | Vortrag + Beispiele |
| 60-75 Min | Diskussion: Gute vs. Schlechte Viz | Gruppenarbeit |
| 75-90 Min | Kursübersicht & Erwartungen | Präsentation |

### Inhalte

#### 1. Begrüßung & Vorstellung (10 Min)
- Dozent stellt sich vor
- Kursziele und -struktur
- Organisatorisches (Zeiten, Pausen, Bewertung)

#### 2. Mentimeter Aktivierung (10 Min)

**Frage 1: Word Cloud**
> "Was verbindest du mit Datenvisualisierung? (Ein Wort)"

**Frage 2: Multiple Choice**
> "Wie viel Erfahrung hast du mit Datenvisualisierung?"
- Keine Erfahrung
- Grundkenntnisse (Excel-Charts)
- Fortgeschritten (Python/R)
- Experte (professionelle Projekte)

**Frage 3: Skala**
> "Wie wichtig ist Datenvisualisierung in deinem zukünftigen Beruf?"
(1 = unwichtig, 5 = sehr wichtig)

**Frage 4: Open-Ended**
> "Was möchtest du in diesem Kurs lernen?"

#### 3. Theorie: Warum Visualisierung? (20 Min)

**Kernbotschaften:**
- Menschen verarbeiten visuelle Informationen 60.000x schneller als Text
- 90% der ans Gehirn übermittelten Informationen sind visuell
- Visualisierungen helfen bei Mustererkennung
- Effektive Kommunikation komplexer Daten

**Beispiele zeigen:**
- Anscombe's Quartet (gleiche Statistiken, unterschiedliche Muster)
- Datasaurus Dozen (moderne Version)
- Florence Nightingale's Rose Chart (historisches Beispiel)
- Hans Rosling's Gapminder (moderne Storytelling)

**Diskussionspunkte:**
- Wann ist eine Tabelle besser als eine Grafik?
- Wann kann Visualisierung irreführend sein?
- Ethische Aspekte der Datenvisualisierung

#### 4. Kognitive Prinzipien (20 Min)

**Gestaltgesetze:**
- **Nähe:** Nahe Objekte werden als zusammengehörig wahrgenommen
- **Ähnlichkeit:** Ähnliche Objekte werden gruppiert
- **Geschlossenheit:** Wir vervollständigen unvollständige Formen
- **Kontinuität:** Wir folgen Linien und Kurven

**Präattentive Attribute:**
- Farbe (Hue, Saturation, Lightness)
- Form (Größe, Orientierung)
- Position (X, Y)
- Bewegung

**Praktische Demonstration:**
- Zeige Beispiele für jedes Gestaltgesetz
- Interaktive Übung: Finde das rote Quadrat (präattentiv)
- Diskussion: Wie nutzen wir das in Visualisierungen?

#### 5. Diskussion: Gute vs. Schlechte Visualisierungen (15 Min)

**Gruppenarbeit (3-4 Personen):**
- Zeige 4-6 Visualisierungen (Mix aus gut und schlecht)
- Gruppen diskutieren: Was funktioniert? Was nicht?
- Kurze Präsentation der Ergebnisse

**Beispiele für schlechte Visualisierungen:**
- 3D-Pie Charts
- Zu viele Farben
- Unleserliche Achsenbeschriftungen
- Irreführende Skalen

**Beispiele für gute Visualisierungen:**
- New York Times Graphics
- FiveThirtyEight
- The Economist
- Information is Beautiful

#### 6. Kursübersicht & Erwartungen (15 Min)

**Kursstruktur:**
- 9 Blöcke à 3 Einheiten
- Wöchentliche Hausaufgaben
- Abschlussprojekt

**Bewertung:**
- 60% Hausaufgaben
- 40% Abschlussprojekt

**Erwartungen:**
- Aktive Teilnahme
- Regelmäßiges Üben
- Feedback geben und nehmen
- Respektvoller Umgang

### Materialien

- **Präsentation:** `Block_1_Einheit_1_Einfuehrung.pptx`
- **Mentimeter:** Link wird bereitgestellt
- **Beispiel-Visualisierungen:** `examples/good_bad_viz/`
- **Handout:** `Block_1_Handout_Kognitive_Prinzipien.pdf`

### Dozentenhinweise

**Vorbereitung:**
- Mentimeter-Präsentation erstellen (30 Min vorher)
- Beispiel-Visualisierungen testen
- Raum-Setup prüfen (Beamer, WLAN)

**Häufige Fragen:**
- "Brauche ich Programmiererfahrung?" → Grundkenntnisse Python hilfreich
- "Welche Software brauche ich?" → Wird in Einheit 1.3 erklärt
- "Kann ich den Kurs bestehen ohne Vorkenntnisse?" → Ja, mit Engagement

**Zeitmanagement:**
- Mentimeter kann länger dauern → Zeitpuffer einplanen
- Diskussion kann ausufern → Moderieren
- Pausen wichtig → Nach 45 Min kurze Pause

---

## 📚 Einheit 1.2: Überblick Frameworks

**Dauer:** 90 Minuten  
**Format:** Vortrag + Live-Demo + Diskussion

### Zeitplan

| Zeit | Aktivität | Methode |
|------|-----------|---------|
| 0-15 Min | Visualisierungs-Landschaft | Präsentation |
| 15-35 Min | Python-Bibliotheken | Vortrag + Demo |
| 35-55 Min | BI-Tools (Power BI, Tableau) | Vortrag + Demo |
| 55-70 Min | R & andere Tools | Überblick |
| 70-85 Min | Entscheidungshilfe: Wann welches Tool? | Diskussion |
| 85-90 Min | Q&A | Interaktiv |

### Inhalte

#### 1. Visualisierungs-Landschaft (15 Min)

**Kategorien:**

**A. Programmierbasiert**
- Python (Matplotlib, Seaborn, Plotly, Bokeh)
- R (ggplot2, plotly)
- JavaScript (D3.js, Chart.js, Highcharts)

**B. Business Intelligence**
- Power BI (Microsoft)
- Tableau (Salesforce)
- Qlik Sense
- Looker (Google)

**C. No-Code/Low-Code**
- Google Data Studio
- Flourish
- Datawrapper
- RAWGraphs

**D. Spezialisiert**
- Gephi (Netzwerke)
- Kepler.gl (Geospatial)
- Observable (Notebooks)

**Übersicht-Diagramm zeigen:**
```
Komplexität vs. Flexibilität
Hoch │     D3.js
     │     Matplotlib
     │     
     │     Plotly
     │     Seaborn
     │     
     │     Power BI
     │     Tableau
Niedrig│     Excel
     └─────────────────
     Niedrig    Hoch
     Flexibilität
```

#### 2. Python-Bibliotheken (20 Min)

**Matplotlib**
- **Beschreibung:** Basis-Bibliothek, volle Kontrolle
- **Stärken:** Flexibilität, Publikationsqualität
- **Schwächen:** Verbose Code, steile Lernkurve
- **Use Cases:** Wissenschaftliche Publikationen, Custom Plots

**Live-Demo (5 Min):**
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.title('Sine Wave')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True, alpha=0.3)
plt.show()
```

**Seaborn**
- **Beschreibung:** High-level Interface für Matplotlib
- **Stärken:** Schöne Defaults, statistische Plots
- **Schwächen:** Weniger Kontrolle als Matplotlib
- **Use Cases:** Explorative Datenanalyse, statistische Visualisierungen

**Live-Demo (5 Min):**
```python
import seaborn as sns
import pandas as pd

# Lade Beispieldaten
tips = sns.load_dataset('tips')

# Erstelle Plot
sns.scatterplot(data=tips, x='total_bill', y='tip', 
                hue='day', size='size')
plt.title('Tips Dataset')
plt.show()
```

**Plotly**
- **Beschreibung:** Interaktive Visualisierungen
- **Stärken:** Interaktivität, HTML-Export, schöne Defaults
- **Schwächen:** Größere Dateien, Online-Abhängigkeit (optional)
- **Use Cases:** Dashboards, interaktive Reports, Web-Apps

**Live-Demo (5 Min):**
```python
import plotly.express as px

# Lade Beispieldaten
df = px.data.gapminder()

# Erstelle interaktiven Plot
fig = px.scatter(df, x='gdpPercap', y='lifeExp',
                 size='pop', color='continent',
                 hover_name='country',
                 animation_frame='year',
                 log_x=True)
fig.show()
```

**Bokeh**
- **Beschreibung:** Interaktive Visualisierungen, Server-Apps
- **Stärken:** Widgets, Streaming-Daten, Server-Integration
- **Schwächen:** Komplexere API, größere Lernkurve
- **Use Cases:** Dashboards mit Widgets, Echtzeit-Daten

#### 3. BI-Tools (20 Min)

**Power BI**
- **Beschreibung:** Microsoft's BI-Plattform
- **Stärken:** Integration mit Microsoft-Ökosystem, DAX
- **Schwächen:** Windows-fokussiert, Lizenzkosten
- **Use Cases:** Business Dashboards, Reports

**Live-Demo (10 Min):**
- Power BI Desktop öffnen
- Daten importieren (CSV)
- Einfache Visualisierung erstellen
- Dashboard-Layout zeigen

**Tableau**
- **Beschreibung:** Führende BI-Software
- **Stärken:** Intuitive Bedienung, große Community
- **Schwächen:** Kosten, Lernkurve für komplexe Features
- **Use Cases:** Business Intelligence, interaktive Dashboards

**Live-Demo (10 Min):**
- Tableau Public öffnen
- Daten verbinden
- Drag-and-Drop Visualisierung
- Dashboard erstellen

#### 4. R & andere Tools (15 Min)

**R (ggplot2)**
- **Beschreibung:** Grammar of Graphics Implementation
- **Stärken:** Elegante Syntax, statistische Integration
- **Schwächen:** R-Kenntnisse erforderlich
- **Use Cases:** Statistische Analysen, akademische Forschung

**Kurzes Beispiel zeigen:**
```r
library(ggplot2)

ggplot(mtcars, aes(x=wt, y=mpg)) +
  geom_point() +
  geom_smooth(method='lm') +
  theme_minimal()
```

**JavaScript (D3.js)**
- **Beschreibung:** Data-Driven Documents
- **Stärken:** Maximale Flexibilität, Web-native
- **Schwächen:** Steile Lernkurve, viel Code
- **Use Cases:** Custom Web-Visualisierungen, interaktive Artikel

**Excel**
- **Beschreibung:** Spreadsheet mit Chart-Funktionen
- **Stärken:** Weit verbreitet, einfach
- **Schwächen:** Limitierte Anpassung, nicht reproduzierbar
- **Use Cases:** Schnelle Analysen, Business-Präsentationen

#### 5. Entscheidungshilfe (15 Min)

**Entscheidungsbaum:**

```
Brauche ich Interaktivität?
├─ Nein
│  ├─ Volle Kontrolle nötig? → Matplotlib
│  └─ Schnelle, schöne Plots? → Seaborn
│
└─ Ja
   ├─ Programmierung OK? → Plotly/Bokeh
   └─ Drag-and-Drop bevorzugt? → Power BI/Tableau
```

**Diskussion (10 Min):**
- Studierende nennen Use Cases
- Gemeinsam entscheiden: Welches Tool?
- Vor- und Nachteile diskutieren

**Faustregel:**
- **Explorative Analyse:** Seaborn
- **Publikation:** Matplotlib
- **Dashboard (Code):** Plotly/Streamlit
- **Dashboard (No-Code):** Power BI/Tableau
- **Web-Integration:** Plotly/D3.js

#### 6. Q&A (5 Min)

Offene Fragen beantworten

### Materialien

- **Präsentation:** `Block_1_Einheit_2_Frameworks.pptx`
- **Demo-Notebooks:** `demos/framework_comparison.ipynb`
- **Entscheidungsbaum:** `resources/tool_decision_tree.pdf`
- **Cheat Sheets:** Matplotlib, Seaborn, Plotly

### Dozentenhinweise

**Vorbereitung:**
- Alle Tools installiert und getestet
- Demo-Daten vorbereitet
- Internet-Verbindung prüfen (für Plotly)
- Power BI/Tableau Lizenzen prüfen

**Live-Demos:**
- Code vorher testen
- Backup-Screenshots falls Demo fehlschlägt
- Nicht zu tief in Details gehen
- Fokus auf Unterschiede

**Häufige Fragen:**
- "Welches Tool soll ich lernen?" → Kommt auf Karriereziel an
- "Ist Python schwer?" → Grundlagen sind machbar
- "Brauche ich alle Tools?" → Nein, Fokus auf 2-3

---

## 📚 Einheit 1.3: Erste Grafiken & Datenquellen

**Dauer:** 90 Minuten  
**Format:** Hands-On Workshop

### Zeitplan

| Zeit | Aktivität | Methode |
|------|-----------|---------|
| 0-20 Min | Setup: Jupyter Notebooks | Hands-On |
| 20-40 Min | Datenquellen & Import | Vortrag + Übung |
| 40-60 Min | Erste Matplotlib-Plots | Hands-On |
| 60-75 Min | Übung: Eigener Plot | Einzelarbeit |
| 75-90 Min | Troubleshooting & Q&A | Support |

### Inhalte

#### 1. Setup: Jupyter Notebooks (20 Min)

**Ziel:** Alle haben eine funktionierende Umgebung

**Option A: Lokale Installation (empfohlen)**

```bash
# Anaconda installieren (falls nicht vorhanden)
# Download: https://www.anaconda.com/download

# Neue Umgebung erstellen
conda create -n dataviz python=3.10
conda activate dataviz

# Bibliotheken installieren
conda install matplotlib seaborn plotly pandas numpy jupyter

# Jupyter starten
jupyter notebook
```

**Option B: Google Colab (Backup)**

1. Gehe zu https://colab.research.google.com
2. Neues Notebook erstellen
3. Bibliotheken sind vorinstalliert

**Setup-Check:**
```python
# Test-Code ausführen
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pandas as pd
import numpy as np

print("✓ Alle Bibliotheken erfolgreich importiert!")
```

**Jupyter Basics (5 Min):**
- Zellen erstellen und ausführen (Shift+Enter)
- Markdown vs. Code-Zellen
- Kernel neu starten
- Speichern und exportieren

#### 2. Datenquellen & Import (20 Min)

**Datenquellen-Übersicht:**

**A. Lokale Dateien**
```python
# CSV
df = pd.read_csv('data.csv')

# Excel
df = pd.read_excel('data.xlsx')

# JSON
df = pd.read_json('data.json')
```

**B. Online-Quellen**
```python
# URL
url = 'https://raw.githubusercontent.com/...'
df = pd.read_csv(url)

# Kaggle (nach Download)
df = pd.read_csv('kaggle_dataset.csv')
```

**C. Integrierte Datasets**
```python
# Seaborn Datasets
tips = sns.load_dataset('tips')
iris = sns.load_dataset('iris')
titanic = sns.load_dataset('titanic')

# Plotly Datasets
gapminder = px.data.gapminder()
```

**D. APIs (Überblick)**
```python
# Beispiel: OpenWeatherMap
import requests

api_key = 'YOUR_KEY'
url = f'https://api.openweathermap.org/data/2.5/weather?q=Hannover&appid={api_key}'
response = requests.get(url)
data = response.json()
```

**Praktische Übung (10 Min):**
```python
# Lade Tips-Dataset
tips = sns.load_dataset('tips')

# Erste Zeilen anzeigen
print(tips.head())

# Info über Dataset
print(tips.info())

# Beschreibende Statistiken
print(tips.describe())
```

**Kaggle-Integration (5 Min):**
- Kaggle Account erstellen
- Dataset suchen
- Download und Import
- Beispiel: Titanic Dataset

#### 3. Erste Matplotlib-Plots (20 Min)

**Grundstruktur:**
```python
import matplotlib.pyplot as plt

# Daten erstellen
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Plot erstellen
plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.title('Mein erster Plot')
plt.xlabel('X-Achse')
plt.ylabel('Y-Achse')
plt.grid(True)
plt.show()
```

**Verschiedene Plot-Typen:**

**Line Plot:**
```python
plt.figure(figsize=(10, 6))
plt.plot(x, y, marker='o', linestyle='-', color='blue')
plt.title('Line Plot')
plt.show()
```

**Scatter Plot:**
```python
plt.figure(figsize=(10, 6))
plt.scatter(x, y, s=100, c='red', alpha=0.5)
plt.title('Scatter Plot')
plt.show()
```

**Bar Plot:**
```python
categories = ['A', 'B', 'C', 'D']
values = [23, 45, 56, 78]

plt.figure(figsize=(10, 6))
plt.bar(categories, values)
plt.title('Bar Plot')
plt.show()
```

**Histogram:**
```python
data = np.random.randn(1000)

plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, edgecolor='black')
plt.title('Histogram')
plt.show()
```

**Mit echten Daten:**
```python
# Tips Dataset
tips = sns.load_dataset('tips')

# Scatter Plot
plt.figure(figsize=(10, 6))
plt.scatter(tips['total_bill'], tips['tip'])
plt.xlabel('Total Bill ($)')
plt.ylabel('Tip ($)')
plt.title('Tips vs. Total Bill')
plt.grid(True, alpha=0.3)
plt.show()
```

#### 4. Übung: Eigener Plot (15 Min)

**Aufgabe:**
Erstelle einen Plot mit dem Iris-Dataset:

```python
# Lade Daten
iris = sns.load_dataset('iris')

# Aufgabe:
# 1. Erstelle einen Scatter Plot
# 2. X-Achse: sepal_length
# 3. Y-Achse: sepal_width
# 4. Färbe nach species
# 5. Füge Titel und Achsenbeschriftungen hinzu
# 6. Füge ein Grid hinzu

# Dein Code hier:
```

**Musterlösung:**
```python
plt.figure(figsize=(10, 6))

# Für jede Species separat plotten
for species in iris['species'].unique():
    data = iris[iris['species'] == species]
    plt.scatter(data['sepal_length'], 
                data['sepal_width'],
                label=species,
                alpha=0.6)

plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.title('Iris Dataset: Sepal Dimensions')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

#### 5. Troubleshooting & Q&A (15 Min)

**Häufige Probleme:**

**Problem 1: Plot wird nicht angezeigt**
```python
# Lösung: plt.show() hinzufügen
plt.plot(x, y)
plt.show()  # ← Wichtig!
```

**Problem 2: Fehler beim Import**
```python
# Lösung: Bibliothek installieren
# !pip install matplotlib
```

**Problem 3: Daten nicht gefunden**
```python
# Lösung: Pfad prüfen
import os
print(os.getcwd())  # Aktuelles Verzeichnis
```

**Problem 4: Figure zu klein**
```python
# Lösung: figsize anpassen
plt.figure(figsize=(12, 8))  # Breite, Höhe in Inches
```

**Best Practices:**
- Immer `plt.figure()` vor neuem Plot
- Aussagekräftige Titel und Labels
- Grid für bessere Lesbarkeit
- Farben bewusst wählen
- Code kommentieren

### Materialien

- **Notebook:** `Block_1_Einheit_3_Erste_Plots.ipynb`
- **Datasets:** Tips, Iris, Titanic (Seaborn)
- **Cheat Sheet:** `Matplotlib_Basics_Cheatsheet.pdf`
- **Troubleshooting Guide:** `Common_Errors_Solutions.md`

### Dozentenhinweise

**Vorbereitung:**
- Alle Notebooks vorher testen
- Backup-Notebooks auf USB-Stick
- Google Colab als Fallback
- Hilfs-Tutoren einplanen (falls verfügbar)

**Während der Einheit:**
- Langsam vorgehen
- Regelmäßig fragen: "Alle dabei?"
- Zwischen Studierenden umhergehen
- Individuelle Hilfe anbieten

**Häufige Probleme:**
- Installation schlägt fehl → Google Colab
- Jupyter startet nicht → Browser-Cache leeren
- Import-Fehler → Umgebung prüfen
- Plot wird nicht angezeigt → plt.show() vergessen

**Zeitmanagement:**
- Setup kann länger dauern → Zeitpuffer
- Übung individuell → Schnelle bekommen Bonus-Aufgabe
- Q&A flexibel → Kann auch nach Einheit weitergehen

---

## 📝 Hausaufgabe Block 1

**Abgabe:** 1 Woche nach Block 1 (Sonntag, 23:59 Uhr)  
**Format:** Jupyter Notebook (.ipynb)  
**Dateiname:** `Nachname_Vorname_Block1.ipynb`

### Aufgabe

Erstelle ein Jupyter Notebook mit folgenden Komponenten:

#### Teil 1: Daten laden (20 Punkte)
1. Wähle ein Dataset von Kaggle ODER verwende ein Seaborn-Dataset
2. Lade die Daten in ein Pandas DataFrame
3. Zeige die ersten 10 Zeilen
4. Gib Informationen über das Dataset aus (Anzahl Zeilen, Spalten, Datentypen)
5. Erstelle beschreibende Statistiken

#### Teil 2: Drei verschiedene Plots (60 Punkte)
Erstelle drei verschiedene Visualisierungen mit Matplotlib:

**Plot 1: Scatter Plot (20 Punkte)**
- Zwei numerische Variablen
- Titel und Achsenbeschriftungen
- Grid
- Mindestens 100 Datenpunkte

**Plot 2: Histogram (20 Punkte)**
- Eine numerische Variable
- Mindestens 20 Bins
- Titel und Achsenbeschriftungen
- Verschiedene Farbe als Plot 1

**Plot 3: Bar Plot oder Line Plot (20 Punkte)**
- Frei wählbar
- Titel und Achsenbeschriftungen
- Professionelles Styling

#### Teil 3: Dokumentation (20 Punkte)
- Markdown-Zellen mit Erklärungen
- Was zeigen die Plots?
- Welche Erkenntnisse gewinnst du?
- Mindestens 3 Markdown-Zellen

### Bewertungskriterien

| Kriterium | Punkte | Beschreibung |
|-----------|--------|--------------|
| **Technische Umsetzung** | 40 | Code funktioniert, Bibliotheken korrekt verwendet |
| **Visuelle Gestaltung** | 30 | Titel, Labels, Grid, Farben, Lesbarkeit |
| **Dokumentation** | 20 | Markdown-Zellen, Erklärungen, Interpretation |
| **Kreativität** | 10 | Eigene Ideen, über Mindestanforderungen hinaus |
| **Gesamt** | 100 | |

### Bonus-Aufgaben (Optional, +10 Punkte)

1. **Subplots (+5 Punkte):** Erstelle ein Figure mit 2x2 Subplots
2. **Styling (+3 Punkte):** Verwende ein Matplotlib-Style (z.B. 'seaborn', 'ggplot')
3. **Annotations (+2 Punkte):** Füge Text-Annotationen zu interessanten Punkten hinzu

### Hilfestellungen

**Kaggle Datasets:**
- https://www.kaggle.com/datasets
- Empfohlen: Titanic, House Prices, Iris

**Seaborn Datasets:**
```python
# Verfügbare Datasets anzeigen
import seaborn as sns
print(sns.get_dataset_names())

# Dataset laden
df = sns.load_dataset('tips')  # oder 'iris', 'titanic', etc.
```

**Matplotlib Styles:**
```python
# Verfügbare Styles
print(plt.style.available)

# Style verwenden
plt.style.use('seaborn-v0_8')
```

### Abgabe

**Wo:** Moodle-Kurs  
**Format:** .ipynb Datei  
**Größe:** Max. 10 MB  
**Naming:** `Nachname_Vorname_Block1.ipynb`

---

## 📚 Ressourcen

### Dokumentation
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/)

### Tutorials
- [Matplotlib Tutorial](https://matplotlib.org/stable/tutorials/index.html)
- [Python Graph Gallery](https://python-graph-gallery.com/)
- [Kaggle Learn](https://www.kaggle.com/learn)

### Datasets
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [UCI ML Repository](https://archive.ics.uci.edu/ml/)
- [Seaborn Datasets](https://github.com/mwaskom/seaborn-data)

### Videos
- [Corey Schafer - Matplotlib Tutorial](https://www.youtube.com/watch?v=UO98lJQ3QGI)
- [Sentdex - Data Visualization](https://www.youtube.com/playlist?list=PLQVvvaa0QuDfefDfXb9Yf0la1fPDKluPF)

---

## ✅ Checkliste für Studierende

Nach Block 1 solltest du:
- [ ] Jupyter Notebook installiert und getestet haben
- [ ] Daten von Kaggle oder Seaborn laden können
- [ ] Einen einfachen Matplotlib-Plot erstellen können
- [ ] Titel und Achsenbeschriftungen hinzufügen können
- [ ] Die Hausaufgabe begonnen haben
- [ ] Bei Problemen Hilfe gesucht haben (Forum, Sprechstunde)

---

## 🎯 Ausblick auf Block 2

Im nächsten Block lernen wir:
- Matplotlib Figure-Axes Architektur im Detail
- Seaborn für statistische Visualisierungen
- Verschiedene Skalen (linear, logarithmisch)
- Statistische Kennzahlen visualisieren

**Vorbereitung:**
- Hausaufgabe Block 1 abschließen
- Matplotlib-Basics wiederholen
- Optional: Seaborn-Dokumentation durchblättern

---

**Erstellt:** April 2026  
**Version:** 1.0  
**Nächste Aktualisierung:** Nach Feedback Block 1