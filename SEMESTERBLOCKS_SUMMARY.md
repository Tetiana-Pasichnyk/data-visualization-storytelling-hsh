# Alle Blöcke: Zusammenfassung
## Data Visualization & Storytelling - HsH

**Hinweis:** Block 1 ist vollständig dokumentiert in [`optional/Block_1_Einfuehrung_Grundlagen.md`](optional/Block_1_Einfuehrung_Grundlagen.md). Dieses Dokument bietet eine strukturierte Übersicht aller 9 Blöcke.

---

## 📋 Block-Übersicht

| Block | Titel | Schwierigkeit | Hauptthemen |
|-------|-------|---------------|-------------|
| 1 | Einführung & Grundlagen | ⭐☆☆☆☆ | Setup, Basics, erste Plots |
| 2 | Datenrepräsentationen & Seaborn I | ⭐⭐☆☆☆ | Matplotlib, Seaborn, Skalen |
| 3 | Fokus I - Spezialisierte Visualisierungen | ⭐⭐⭐☆☆ | Erweiterte Techniken, Tufte |
| 4 | Plotly I & Bokeh | ⭐⭐☆☆☆ | Interaktivität, HTML-Export |
| 5 | Barrierefreiheit I | ⭐⭐⭐☆☆ | WCAG, Farbenblindheit |
| 6 | Storytelling I | ⭐⭐☆☆☆ | Narrative, Kommunikation |
| 7 | Research I | ⭐⭐⭐⭐☆ | ML-Metriken, EDA |
| 8 | Dashboard I | ⭐⭐⭐☆☆ | Streamlit, Dashboard-Design |
| 9 | Erweiterte Tools II | ⭐⭐⭐⭐☆ | Power BI, Dash, Mastery |

---

## Block 2: Datenrepräsentationen & Seaborn I

### Einheit 2.1: Matplotlib Einführung (90 Min)

**Lernziele:**
- Figure-Axes Architektur verstehen
- Subplots erstellen
- Styling und Anpassung
- Best Practices

**Inhalte:**
- Figure und Axes Objekte
- `plt.subplots()` vs. `plt.subplot()`
- Styling: Colors, Linestyles, Markers
- Legends und Annotations
- Saving Figures (PNG, PDF, SVG)

**Praktische Übung:**
```python
# 2x2 Subplot Grid erstellen
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Verschiedene Plot-Typen
axes[0, 0].plot(x, y)
axes[0, 1].scatter(x, y)
axes[1, 0].bar(categories, values)
axes[1, 1].hist(data, bins=30)

plt.tight_layout()
plt.savefig('my_plots.png', dpi=300)
```

**Hausaufgabe-Komponente:**
Erstelle ein 2x3 Subplot-Grid mit verschiedenen Visualisierungen

### Einheit 2.2: Seaborn Basics (90 Min)

**Lernziele:**
- Seaborn-Philosophie verstehen
- Statistische Plots erstellen
- Themes und Paletten nutzen
- Integration mit Matplotlib

**Inhalte:**
- Seaborn vs. Matplotlib
- Distribution Plots: `histplot`, `kdeplot`, `ecdfplot`
- Categorical Plots: `boxplot`, `violinplot`, `swarmplot`
- Relational Plots: `scatterplot`, `lineplot`
- Themes: `set_theme()`, `set_style()`, `set_palette()`

**Praktische Übung:**
```python
import seaborn as sns

# Theme setzen
sns.set_theme(style='whitegrid', palette='husl')

# Tips Dataset
tips = sns.load_dataset('tips')

# Verschiedene Plots
sns.boxplot(data=tips, x='day', y='total_bill')
sns.violinplot(data=tips, x='day', y='total_bill')
sns.swarmplot(data=tips, x='day', y='total_bill', color='black', alpha=0.5)
```

**Hausaufgabe-Komponente:**
Explorative Analyse mit mindestens 5 verschiedenen Seaborn-Plots

### Einheit 2.3: Statistische Skalen & Interpretation (90 Min)

**Lernziele:**
- Skalen-Typen verstehen
- Logarithmische Skalen anwenden
- Normalisierung und Standardisierung
- Statistische Kennzahlen visualisieren

**Inhalte:**
- Lineare vs. Logarithmische Skalen
- Wann welche Skala?
- `plt.xscale('log')`, `plt.yscale('log')`
- Fehlerbalken und Konfidenzintervalle
- Statistische Annotationen

**Praktische Übung:**
```python
# Exponentielles Wachstum
x = np.linspace(0, 10, 100)
y = np.exp(x)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Linear
ax1.plot(x, y)
ax1.set_title('Linear Scale')

# Logarithmisch
ax2.plot(x, y)
ax2.set_yscale('log')
ax2.set_title('Logarithmic Scale')
```

**Hausaufgabe-Komponente:**
Vergleiche lineare und logarithmische Darstellung für exponentielles Wachstum

---

## Block 3: Fokus I - Spezialisierte Visualisierungen

### Einheit 3.1: Erweiterte Matplotlib-Techniken (90 Min)

**Lernziele:**
- Komplexe Layouts erstellen
- Annotations und Text
- Custom Styles
- 3D-Plots (Überblick)

**Inhalte:**
- GridSpec für flexible Layouts
- Text und Annotations: `annotate()`, `text()`
- Custom Colormaps
- Inset Axes
- 3D Plotting mit `mpl_toolkits.mplot3d`

**Praktische Übung:**
```python
from matplotlib.gridspec import GridSpec

fig = plt.figure(figsize=(12, 8))
gs = GridSpec(3, 3, figure=fig)

# Hauptplot
ax1 = fig.add_subplot(gs[0:2, :])
ax1.plot(x, y)

# Kleinere Plots
ax2 = fig.add_subplot(gs[2, 0])
ax3 = fig.add_subplot(gs[2, 1])
ax4 = fig.add_subplot(gs[2, 2])
```

**Referenz:** `tufte_principles_improved.ipynb`

### Einheit 3.2: Seaborn Spezialisierte Plots (90 Min)

**Lernziele:**
- Pairplots und Jointplots
- Heatmaps und Clustermaps
- Regression Plots
- FacetGrid für Small Multiples

**Inhalte:**
- `pairplot()` für multivariate Analyse
- `jointplot()` für bivariate Verteilungen
- `heatmap()` für Korrelationsmatrizen
- `clustermap()` für hierarchisches Clustering
- `lmplot()` für Regression
- `FacetGrid` für konditionierte Plots

**Praktische Übung:**
```python
# Pairplot
sns.pairplot(iris, hue='species', diag_kind='kde')

# Korrelations-Heatmap
corr = tips.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)

# FacetGrid
g = sns.FacetGrid(tips, col='time', row='sex')
g.map(sns.scatterplot, 'total_bill', 'tip')
```

### Einheit 3.3: Praktische Übungen mit realen Datasets (90 Min)

**Lernziele:**
- Reale Daten analysieren
- Tufte-Prinzipien anwenden
- Professionelle Visualisierungen erstellen
- Storytelling beginnen

**Inhalte:**
- Kaggle Dataset auswählen
- Explorative Datenanalyse
- Tufte-Prinzipien: Data-Ink Ratio, Chartjunk
- Vorher/Nachher-Vergleiche
- Peer-Review

**Praktische Übung:**
- Wähle ein Kaggle Dataset
- Erstelle 3 Visualisierungen
- Verbessere nach Tufte-Prinzipien
- Präsentiere in Kleingruppe

**Referenz:** `intensity_chart_accurate.ipynb`

---

## Block 4: Plotly I & Bokeh

### Einheit 4.1: Einführung Interaktive Visualisierungen (90 Min)

**Lernziele:**
- Interaktivität verstehen
- Use Cases identifizieren
- Tools vergleichen
- HTML-Export

**Inhalte:**
- Warum Interaktivität?
- Hover, Zoom, Pan, Select
- Plotly vs. Bokeh vs. Altair
- HTML-Export und Embedding
- Performance-Überlegungen

### Einheit 4.2: Plotly Basics (90 Min)

**Lernziele:**
- Plotly Express nutzen
- Graph Objects verstehen
- Interaktive Features
- Subplots und Layouts

**Inhalte:**
- Plotly Express: High-level API
- Graph Objects: Low-level Kontrolle
- Hover-Informationen anpassen
- Buttons und Dropdowns
- Animations
- Subplots mit `make_subplots()`

**Praktische Übung:**
```python
import plotly.express as px

# Gapminder Dataset
df = px.data.gapminder()

# Animated Scatter
fig = px.scatter(df, 
                 x='gdpPercap', 
                 y='lifeExp',
                 size='pop', 
                 color='continent',
                 hover_name='country',
                 animation_frame='year',
                 log_x=True,
                 range_x=[100, 100000],
                 range_y=[25, 90])

fig.show()
```

### Einheit 4.3: Bokeh Grundlagen (90 Min)

**Lernziele:**
- Bokeh-Architektur verstehen
- Glyphs und Layouts
- Widgets integrieren
- Server-Apps (Überblick)

**Inhalte:**
- Figure und Glyphs
- ColumnDataSource
- Layouts: row, column, gridplot
- Widgets: Slider, Button, Select
- Callbacks (JavaScript und Python)
- Bokeh Server (Überblick)

**Praktische Übung:**
```python
from bokeh.plotting import figure, show
from bokeh.models import HoverTool

p = figure(title='Interactive Scatter',
           tools='pan,wheel_zoom,box_select,reset')

p.circle('x', 'y', size=10, source=source,
         color='navy', alpha=0.5)

hover = HoverTool(tooltips=[('X', '@x'), ('Y', '@y')])
p.add_tools(hover)

show(p)
```

---

## Block 5: Barrierefreiheit I - Best Practices

### Einheit 5.1: WCAG Standards für Datenvisualisierung (90 Min)

**Lernziele:**
- WCAG 2.1 verstehen
- Kontrastverhältnisse berechnen
- AA vs. AAA Standards
- Testing-Tools nutzen

**Inhalte:**
- WCAG 2.1 Überblick
- Kontrast-Anforderungen: 4.5:1 (AA), 7:1 (AAA)
- Text-Größe und Lesbarkeit
- Tastaturnavigation
- Screen Reader Kompatibilität
- Testing: WebAIM Contrast Checker

**Referenz:** `color_accessibility_guide.ipynb`

### Einheit 5.2: Farbenblindheit & Barrierefreie Farbpaletten (90 Min)

**Lernziele:**
- Farbenblindheit-Typen verstehen
- Barrierefreie Paletten nutzen
- Kontrast-Tests durchführen
- Simulationstools verwenden

**Inhalte:**
- Deuteranopie, Protanopie, Tritanopie
- Okabe-Ito Palette
- Paul Tol Paletten
- IBM Accessible Colors
- ColorBrewer
- Simulationstools: Coblis, Color Oracle

**Praktische Übung:**
```python
# Okabe-Ito Palette
okabe_ito = ['#E69F00', '#56B4E9', '#009E73', '#F0E442',
             '#0072B2', '#D55E00', '#CC79A7', '#000000']

# Verwenden
plt.scatter(x, y, c=okabe_ito[0])
```

### Einheit 5.3: Praktische Tipps für Inklusives Design (90 Min)

**Lernziele:**
- Muster und Texturen nutzen
- Direkte Beschriftung
- Alt-Text erstellen
- Checkliste anwenden

**Inhalte:**
- Muster zusätzlich zu Farben
- Direkte Beschriftung vs. Legenden
- Alt-Text für Grafiken
- Accessible PDFs
- Checkliste für Barrierefreiheit

**Praktische Übung:**
- Bestehende Visualisierung verbessern
- WCAG AA erfüllen
- Accessibility-Report schreiben

---

## Block 6: Storytelling I

### Einheit 6.1: Visual Storytelling Prinzipien (90 Min)

**Lernziele:**
- Storytelling-Prinzipien verstehen
- Aufmerksamkeit lenken
- Emotionale Verbindung
- Cole Nussbaumer Knaflic's Prinzipien

**Inhalte:**
- Warum Storytelling?
- Narrative Strukturen
- Aufmerksamkeit durch Farbe, Größe, Position
- Emotionale Resonanz
- "Storytelling with Data" Prinzipien

### Einheit 6.2: Narrative Strukturen für Daten (90 Min)

**Lernziele:**
- Setup-Conflict-Resolution
- Zeitliche Abfolge
- Vergleiche und Kontraste
- Call-to-Action

**Inhalte:**
- Klassische Erzählstrukturen
- Daten-Story-Typen: Change over time, Comparison, Distribution
- Sequenzierung von Visualisierungen
- Übergänge und Verbindungen
- Abschluss mit Handlungsempfehlung

### Einheit 6.3: Überzeugende Datengeschichten erstellen (90 Min)

**Lernziele:**
- Zielgruppen-Analyse
- Kernbotschaft definieren
- Visualisierungs-Sequenz
- Präsentationstechniken

**Inhalte:**
- Zielgruppe verstehen
- Eine klare Botschaft
- Visualisierungs-Hierarchie
- Präsentations-Best Practices
- Q&A vorbereiten

**Praktische Übung:**
- Erstelle eine 5-Slide Daten-Story
- Präsentiere in Kleingruppe
- Peer-Feedback

---

## Block 7: Research I

### Einheit 7.1: Bilddaten & NLP-Daten Visualisierung (90 Min)

**Lernziele:**
- Image Embeddings visualisieren
- t-SNE und UMAP
- Word Clouds
- Topic Modeling Visualisierung

**Inhalte:**
- Dimensionsreduktion: PCA, t-SNE, UMAP
- Image Grid Visualisierung
- Word Clouds mit `wordcloud`
- Topic Modeling mit pyLDAvis
- Embedding Spaces

**Praktische Übung:**
```python
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

# t-SNE auf hochdimensionalen Daten
tsne = TSNE(n_components=2, random_state=42)
embeddings_2d = tsne.fit_transform(embeddings)

plt.scatter(embeddings_2d[:, 0], embeddings_2d[:, 1], 
            c=labels, cmap='tab10')
plt.colorbar()
```

### Einheit 7.2: Modell-Metriken Visualisierung (90 Min)

**Lernziele:**
- Confusion Matrix
- ROC Curves und AUC
- Precision-Recall Curves
- Learning Curves
- Feature Importance

**Inhalte:**
- Classification Metrics
- Confusion Matrix mit Seaborn
- ROC und PR Curves
- Learning Curves für Overfitting-Diagnose
- Feature Importance Plots
- SHAP Values (Überblick)

**Praktische Übung:**
```python
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# Confusion Matrix
cm = confusion_matrix(y_true, y_pred)
disp = ConfusionMatrixDisplay(cm, display_labels=class_names)
disp.plot(cmap='Blues')
```

### Einheit 7.3: Explorative Datenanalyse (EDA) Techniken (90 Min)

**Lernziele:**
- EDA-Workflow
- Pandas Profiling
- Sweetviz
- Manuelle EDA Best Practices

**Inhalte:**
- EDA-Prozess
- Automated EDA: pandas-profiling, sweetviz
- Univariate Analyse
- Bivariate Analyse
- Multivariate Analyse
- Missing Data Visualisierung

**Praktische Übung:**
```python
import pandas_profiling

# Automated EDA
profile = pandas_profiling.ProfileReport(df)
profile.to_file('eda_report.html')
```

---

## Block 8: Dashboard I

### Einheit 8.1: Dashboard Design Prinzipien (90 Min)

**Lernziele:**
- Dashboard-Prinzipien verstehen
- Layout und Hierarchie
- KPI-Auswahl
- Interaktivität planen

**Inhalte:**
- Dashboard vs. Report
- Layout-Prinzipien: F-Pattern, Z-Pattern
- KPI-Auswahl und Priorisierung
- Interaktivität: Filter, Drill-Down
- Performance-Überlegungen
- Best Practices

### Einheit 8.2: Streamlit für Rapid Prototyping (90 Min)

**Lernziele:**
- Streamlit Basics
- Widgets und Interaktivität
- Caching und Performance
- Deployment

**Inhalte:**
- Streamlit Installation und Setup
- Widgets: slider, selectbox, multiselect
- Layouts: columns, expander, tabs
- Caching mit `@st.cache_data`
- File Upload
- Deployment auf Streamlit Cloud

**Praktische Übung:**
```python
import streamlit as st
import pandas as pd
import plotly.express as px

st.title('My Dashboard')

# Sidebar
dataset = st.sidebar.selectbox('Dataset', ['tips', 'iris'])

# Load data
df = sns.load_dataset(dataset)

# Plot
fig = px.scatter(df, x=df.columns[0], y=df.columns[1])
st.plotly_chart(fig)
```

### Einheit 8.3: Praktische Dashboard-Erstellung (90 Min)

**Lernziele:**
- Vollständiges Dashboard erstellen
- Daten-Upload
- Filter und Selektion
- Export-Funktionen

**Inhalte:**
- Multi-Page App
- Session State
- Daten-Upload und Verarbeitung
- Dynamische Visualisierungen
- Export als PDF/PNG
- Zoo Plot Beispiel

**Praktische Übung:**
- Erstelle ein Dashboard mit:
  - File Upload
  - Mindestens 3 Visualisierungen
  - Interaktive Filter
  - Download-Button

---

## Block 9: Erweiterte Tools II

### Einheit 9.1: Power BI Einführung (90 Min)

**Lernziele:**
- Power BI Desktop nutzen
- Datenimport und Transformation
- Grundlegende Visualisierungen
- DAX Basics

**Inhalte:**
- Power BI Desktop Installation
- Datenquellen verbinden
- Power Query Editor
- Visualisierungen erstellen
- DAX Formeln: SUM, AVERAGE, CALCULATE
- Dashboard-Layout
- Veröffentlichung (Überblick)

**Praktische Übung:**
- Importiere CSV-Daten
- Erstelle 5 verschiedene Visualisierungen
- Erstelle ein Dashboard
- Füge Slicer hinzu

### Einheit 9.2: Seaborn II - Erweiterte Anpassung (90 Min)

**Lernziele:**
- Custom Themes
- Komplexe FacetGrids
- Statistische Annotationen
- Publication-Ready Plots

**Inhalte:**
- Custom Seaborn Themes erstellen
- Komplexe FacetGrid-Layouts
- Statistische Tests visualisieren
- Annotations und Text
- Export für Publikationen
- Matplotlib + Seaborn Kombination

**Praktische Übung:**
```python
# Custom Theme
custom_params = {
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.grid': True,
    'grid.alpha': 0.3
}
sns.set_theme(rc=custom_params)

# Komplexer FacetGrid
g = sns.FacetGrid(data, col='var1', row='var2', 
                  hue='var3', height=4)
g.map(sns.scatterplot, 'x', 'y')
g.add_legend()
```

### Einheit 9.3: Plotly II - Erweiterte Interaktivität (90 Min)

**Lernziele:**
- Dash Framework
- Callbacks und Updates
- Komplexe Layouts
- Deployment

**Inhalte:**
- Dash Installation und Setup
- Dash Components: dcc, html
- Callbacks für Interaktivität
- Multi-Page Apps
- Deployment auf Heroku/Render
- Performance-Optimierung

**Praktische Übung:**
```python
import dash
from dash import dcc, html, Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(id='dropdown', options=[...]),
    dcc.Graph(id='graph')
])

@app.callback(
    Output('graph', 'figure'),
    Input('dropdown', 'value')
)
def update_graph(value):
    # Update logic
    return fig

app.run_server(debug=True)
```

---

## 📝 Hausaufgaben-Übersicht

| Block | Thema | Schwierigkeit | Zeitaufwand |
|-------|-------|---------------|-------------|
| 1 | Erste Plots & Datenquellen | ⭐☆☆☆☆ | 2-3h |
| 2 | Matplotlib & Seaborn Exploration | ⭐⭐☆☆☆ | 3-4h |
| 3 | Tufte-Prinzipien anwenden | ⭐⭐⭐☆☆ | 3-4h |
| 4 | Interaktive Visualisierung | ⭐⭐☆☆☆ | 3-4h |
| 5 | Accessibility Audit | ⭐⭐⭐☆☆ | 2-3h |
| 6 | Daten-Story erstellen | ⭐⭐⭐☆☆ | 4-5h |
| 7 | ML-Modell analysieren | ⭐⭐⭐⭐☆ | 4-5h |
| 8 | Dashboard entwickeln | ⭐⭐⭐☆☆ | 4-5h |
| 9 | Tool-Vergleich | ⭐⭐⭐☆☆ | 3-4h |

---

## 🎯 Lernziel-Progression

### Woche 1-3: Grundlagen
- Python-Setup
- Matplotlib & Seaborn
- Erste Visualisierungen
- Datenquellen

### Woche 4-6: Erweiterte Techniken
- Interaktivität
- Barrierefreiheit
- Storytelling
- Design-Prinzipien

### Woche 7-9: Spezialisierung
- Research-Visualisierungen
- Dashboards
- BI-Tools
- Professionalisierung

### Woche 10-11: Abschlussprojekt
- Vollständige Daten-Story
- Dashboard
- Präsentation
- Portfolio

---

## 📚 Referenzen zu bestehenden Notebooks

| Notebook | Verwendung in Blöcken | Themen |
|----------|----------------------|--------|
| `tufte_principles_improved.ipynb` | Block 3, 5 | Data-Ink Ratio, Chartjunk |
| `intensity_chart_accurate.ipynb` | Block 2, 3 | Zeitreihen, Styling |
| `matplotlib_vs_seaborn.ipynb` | Block 2 | Tool-Vergleich |
| `color_accessibility_guide.ipynb` | Block 5 | WCAG, Farbenblindheit |

---

## ✅ Vollständige Dokumentation

**Block 1** ist vollständig dokumentiert mit:
- Detailliertem Zeitplan für alle 3 Einheiten
- Lernzielen und Inhalten
- Praktischen Übungen mit Code
- Hausaufgabe mit Bewertungskriterien
- Ressourcen und Dozentenhinweisen

**Blöcke 2-9** folgen der gleichen Struktur und können nach dem Block-1-Template erstellt werden.

---

**Erstellt:** April 2026  
**Version:** 1.0  
**Nächste Schritte:** Vollständige Dokumentation aller Blöcke nach Block-1-Vorlage