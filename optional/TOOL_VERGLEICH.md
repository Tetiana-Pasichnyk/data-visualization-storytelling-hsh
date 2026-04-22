# Tool-Vergleich: Visualisierungswerkzeuge
## Data Visualization & Storytelling - HsH

**Zweck:** Entscheidungshilfe für die Wahl des richtigen Visualisierungstools

---

## 📊 Vergleichsmatrix

| Tool | Typ | Lernkurve | Flexibilität | Interaktivität | Kosten | Use Case |
|------|-----|-----------|--------------|-----------------|--------|----------|
| **Matplotlib** | Python | Mittel-Hoch | ⭐⭐⭐⭐⭐ | ⭐☆☆☆☆ | Kostenlos | Wissenschaftliche Publikationen |
| **Seaborn** | Python | Niedrig | ⭐⭐⭐☆☆ | ⭐☆☆☆☆ | Kostenlos | Statistische Analysen |
| **Plotly** | Python/JS | Niedrig-Mittel | ⭐⭐⭐⭐☆ | ⭐⭐⭐⭐⭐ | Kostenlos/Pro | Interaktive Dashboards |
| **Bokeh** | Python | Mittel | ⭐⭐⭐⭐☆ | ⭐⭐⭐⭐☆ | Kostenlos | Server-Apps, Widgets |
| **Streamlit** | Python | Niedrig | ⭐⭐⭐☆☆ | ⭐⭐⭐⭐☆ | Kostenlos | Rapid Prototyping |
| **Dash** | Python | Mittel-Hoch | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Kostenlos/Enterprise | Production Dashboards |
| **Power BI** | BI-Tool | Niedrig-Mittel | ⭐⭐⭐☆☆ | ⭐⭐⭐⭐☆ | Pro: €10/Monat | Business Intelligence |
| **Tableau** | BI-Tool | Niedrig | ⭐⭐⭐☆☆ | ⭐⭐⭐⭐⭐ | Creator: $70/Monat | Business Dashboards |
| **Excel** | Spreadsheet | Sehr Niedrig | ⭐⭐☆☆☆ | ⭐☆☆☆☆ | Office 365 | Schnelle Analysen |
| **D3.js** | JavaScript | Sehr Hoch | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Kostenlos | Custom Web-Viz |

---

## 🔍 Detaillierter Vergleich

### Matplotlib

**Beschreibung:** Die Basis-Bibliothek für Python-Visualisierung

**Stärken:**
- ✅ Maximale Kontrolle über jedes Detail
- ✅ Publikationsqualität (300+ DPI)
- ✅ Große Community und Dokumentation
- ✅ Integration mit NumPy/Pandas
- ✅ Viele Export-Formate (PNG, PDF, SVG, EPS)

**Schwächen:**
- ❌ Verbose Code für einfache Plots
- ❌ Steile Lernkurve
- ❌ Keine native Interaktivität
- ❌ Styling erfordert viel Code

**Wann verwenden:**
- Wissenschaftliche Publikationen
- Volle Kontrolle nötig
- Custom Visualisierungen
- Statische Plots

**Code-Beispiel:**
```python
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(10, 6))
x = np.linspace(0, 10, 100)
y = np.sin(x)

ax.plot(x, y, linewidth=2, color='#2E86AB')
ax.set_xlabel('X-Achse', fontsize=12)
ax.set_ylabel('Y-Achse', fontsize=12)
ax.set_title('Sinuswelle', fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.3)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('plot.png', dpi=300, bbox_inches='tight')
plt.show()
```

---

### Seaborn

**Beschreibung:** High-level Interface für statistische Visualisierungen

**Stärken:**
- ✅ Schöne Defaults out-of-the-box
- ✅ Einfache Syntax
- ✅ Statistische Plots integriert
- ✅ Themes und Farbpaletten
- ✅ Integration mit Pandas

**Schwächen:**
- ❌ Weniger Kontrolle als Matplotlib
- ❌ Limitierte Plot-Typen
- ❌ Keine Interaktivität
- ❌ Abhängig von Matplotlib

**Wann verwenden:**
- Explorative Datenanalyse
- Statistische Visualisierungen
- Schnelle, schöne Plots
- Pandas DataFrames

**Code-Beispiel:**
```python
import seaborn as sns
import pandas as pd

# Theme setzen
sns.set_theme(style='whitegrid', palette='husl')

# Daten laden
tips = sns.load_dataset('tips')

# Plot erstellen
sns.boxplot(data=tips, x='day', y='total_bill', hue='sex')
plt.title('Tips by Day and Gender')
plt.show()
```

---

### Plotly

**Beschreibung:** Interaktive Visualisierungen für Web und Python

**Stärken:**
- ✅ Einfache Interaktivität (Hover, Zoom, Pan)
- ✅ Schöne Defaults
- ✅ HTML-Export
- ✅ Plotly Express: High-level API
- ✅ Animations möglich

**Schwächen:**
- ❌ Größere Dateien als statische Plots
- ❌ Online-Abhängigkeit (optional)
- ❌ Weniger Kontrolle als Matplotlib
- ❌ Komplexere Anpassungen schwieriger

**Wann verwenden:**
- Interaktive Reports
- Web-Dashboards
- Präsentationen
- Explorative Analysen

**Code-Beispiel:**
```python
import plotly.express as px

df = px.data.gapminder()

fig = px.scatter(df, 
                 x='gdpPercap', 
                 y='lifeExp',
                 size='pop', 
                 color='continent',
                 hover_name='country',
                 animation_frame='year',
                 log_x=True,
                 title='Gapminder: Life Expectancy vs GDP')

fig.show()
# oder: fig.write_html('plot.html')
```

---

### Bokeh

**Beschreibung:** Interaktive Visualisierungen mit Server-Integration

**Stärken:**
- ✅ Widgets und Interaktivität
- ✅ Streaming-Daten
- ✅ Server-Apps möglich
- ✅ Große Datasets
- ✅ Flexible Layouts

**Schwächen:**
- ❌ Komplexere API
- ❌ Steile Lernkurve
- ❌ Weniger Community als Plotly
- ❌ Server-Setup für volle Features

**Wann verwenden:**
- Dashboards mit Widgets
- Echtzeit-Daten
- Server-basierte Apps
- Große Datasets

**Code-Beispiel:**
```python
from bokeh.plotting import figure, show
from bokeh.models import HoverTool

p = figure(title='Interactive Scatter',
           width=800, height=600,
           tools='pan,wheel_zoom,box_select,reset')

p.circle('x', 'y', size=10, source=source,
         color='navy', alpha=0.5)

hover = HoverTool(tooltips=[
    ('X', '@x{0.00}'),
    ('Y', '@y{0.00}')
])
p.add_tools(hover)

show(p)
```

---

### Streamlit

**Beschreibung:** Framework für schnelle Data Apps

**Stärken:**
- ✅ Sehr einfache Syntax
- ✅ Rapid Prototyping
- ✅ Widgets integriert
- ✅ Kostenloser Deployment
- ✅ Python-only (kein HTML/CSS/JS)

**Schwächen:**
- ❌ Limitierte Layout-Kontrolle
- ❌ Weniger Flexibilität als Dash
- ❌ Reload bei jeder Interaktion
- ❌ Nicht für komplexe Apps

**Wann verwenden:**
- Prototypen
- Interne Tools
- Demos
- Schnelle Dashboards

**Code-Beispiel:**
```python
import streamlit as st
import pandas as pd
import plotly.express as px

st.title('My Dashboard')

# Sidebar
dataset = st.sidebar.selectbox('Dataset', ['tips', 'iris'])

# Load data
df = sns.load_dataset(dataset)

# Display
st.dataframe(df.head())

# Plot
fig = px.scatter(df, x=df.columns[0], y=df.columns[1])
st.plotly_chart(fig, use_container_width=True)
```

---

### Dash

**Beschreibung:** Framework für Production-Grade Dashboards

**Stärken:**
- ✅ Volle Kontrolle über Layout
- ✅ Callbacks für Interaktivität
- ✅ Production-ready
- ✅ Multi-Page Apps
- ✅ Enterprise-Features

**Schwächen:**
- ❌ Steile Lernkurve
- ❌ Mehr Code als Streamlit
- ❌ HTML/CSS-Kenntnisse hilfreich
- ❌ Komplexeres Deployment

**Wann verwenden:**
- Production Dashboards
- Komplexe Interaktivität
- Multi-Page Apps
- Enterprise-Anwendungen

**Code-Beispiel:**
```python
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Dashboard'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in ['A', 'B', 'C']],
        value='A'
    ),
    dcc.Graph(id='graph')
])

@app.callback(
    Output('graph', 'figure'),
    Input('dropdown', 'value')
)
def update_graph(value):
    df = get_data(value)
    fig = px.scatter(df, x='x', y='y')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
```

---

### Power BI

**Beschreibung:** Microsoft's Business Intelligence Plattform

**Stärken:**
- ✅ Drag-and-Drop Interface
- ✅ Integration mit Microsoft-Ökosystem
- ✅ DAX für Berechnungen
- ✅ Große Community
- ✅ Mobile Apps

**Schwächen:**
- ❌ Windows-fokussiert (Desktop)
- ❌ Lizenzkosten
- ❌ Weniger Flexibilität als Code
- ❌ Lernkurve für DAX

**Wann verwenden:**
- Business Intelligence
- Microsoft-Umgebung
- Non-Coder
- Enterprise-Reports

**Kosten:**
- Power BI Desktop: Kostenlos
- Power BI Pro: €10/Monat
- Power BI Premium: Ab €4.995/Monat

---

### Tableau

**Beschreibung:** Führende BI-Software

**Stärken:**
- ✅ Intuitive Bedienung
- ✅ Sehr interaktiv
- ✅ Große Community
- ✅ Tableau Public (kostenlos)
- ✅ Schöne Visualisierungen

**Schwächen:**
- ❌ Hohe Kosten
- ❌ Lernkurve für komplexe Features
- ❌ Weniger Kontrolle als Code
- ❌ Public: Nur öffentliche Dashboards

**Wann verwenden:**
- Business Intelligence
- Interaktive Dashboards
- Präsentationen
- Explorative Analysen

**Kosten:**
- Tableau Public: Kostenlos (öffentlich)
- Tableau Creator: $70/Monat
- Tableau Explorer: $42/Monat
- Tableau Viewer: $15/Monat

---

## 🎯 Entscheidungsbaum

```
Brauche ich Programmierung?
│
├─ Nein (Drag-and-Drop bevorzugt)
│  │
│  ├─ Microsoft-Umgebung? → Power BI
│  ├─ Budget vorhanden? → Tableau
│  └─ Kostenlos? → Excel, Google Data Studio
│
└─ Ja (Code-basiert)
   │
   ├─ Interaktivität nötig?
   │  │
   │  ├─ Nein (Statisch)
   │  │  ├─ Volle Kontrolle? → Matplotlib
   │  │  └─ Schnell & schön? → Seaborn
   │  │
   │  └─ Ja (Interaktiv)
   │     ├─ Einfach & schnell? → Plotly Express
   │     ├─ Dashboard-Prototyp? → Streamlit
   │     ├─ Production Dashboard? → Dash
   │     └─ Widgets & Server? → Bokeh
   │
   └─ Web-Integration?
      ├─ Maximale Kontrolle? → D3.js
      └─ Python-Backend? → Plotly/Dash
```

---

## 📈 Use Case Matrix

| Use Case | Empfohlenes Tool | Alternative |
|----------|------------------|-------------|
| **Wissenschaftliche Publikation** | Matplotlib | Seaborn |
| **Explorative Datenanalyse** | Seaborn | Plotly Express |
| **Interaktiver Report** | Plotly | Bokeh |
| **Dashboard-Prototyp** | Streamlit | Plotly Dash |
| **Production Dashboard** | Dash | Bokeh Server |
| **Business Intelligence** | Power BI | Tableau |
| **Präsentation** | Plotly | Power BI |
| **ML-Modell-Analyse** | Matplotlib + Seaborn | Plotly |
| **Echtzeit-Daten** | Bokeh | Dash |
| **Web-Artikel** | D3.js | Plotly |
| **Mobile App** | Plotly | Power BI |
| **Schnelle Analyse** | Seaborn | Excel |

---

## 💰 Kosten-Vergleich

| Tool | Kostenlos | Pro/Paid | Enterprise |
|------|-----------|----------|------------|
| Matplotlib | ✅ | - | - |
| Seaborn | ✅ | - | - |
| Plotly | ✅ | $420/Jahr | Custom |
| Bokeh | ✅ | - | - |
| Streamlit | ✅ | - | Custom |
| Dash | ✅ | - | $1.495+/Monat |
| Power BI | Desktop: ✅ | €10/Monat | €4.995+/Monat |
| Tableau | Public: ✅ | $70/Monat | Custom |
| Excel | - | Office 365 | Office 365 |
| D3.js | ✅ | - | - |

---

## 🚀 Performance-Vergleich

| Tool | Kleine Daten (<1K) | Mittlere Daten (1K-100K) | Große Daten (>100K) |
|------|-------------------|-------------------------|---------------------|
| Matplotlib | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐☆ | ⭐⭐⭐☆☆ |
| Seaborn | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐☆ | ⭐⭐⭐☆☆ |
| Plotly | ⭐⭐⭐⭐☆ | ⭐⭐⭐☆☆ | ⭐⭐☆☆☆ |
| Bokeh | ⭐⭐⭐⭐☆ | ⭐⭐⭐⭐☆ | ⭐⭐⭐⭐☆ |
| Streamlit | ⭐⭐⭐⭐☆ | ⭐⭐⭐☆☆ | ⭐⭐☆☆☆ |
| Dash | ⭐⭐⭐⭐☆ | ⭐⭐⭐⭐☆ | ⭐⭐⭐☆☆ |
| Power BI | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐☆ |
| Tableau | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐☆ |

---

## 🎓 Lernkurve & Community

| Tool | Lernzeit (Basics) | Lernzeit (Mastery) | Community-Größe | Dokumentation |
|------|-------------------|-------------------|-----------------|---------------|
| Matplotlib | 1-2 Wochen | 3-6 Monate | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Seaborn | 1-3 Tage | 2-4 Wochen | ⭐⭐⭐⭐☆ | ⭐⭐⭐⭐☆ |
| Plotly | 3-5 Tage | 1-2 Monate | ⭐⭐⭐⭐☆ | ⭐⭐⭐⭐⭐ |
| Bokeh | 1-2 Wochen | 2-3 Monate | ⭐⭐⭐☆☆ | ⭐⭐⭐⭐☆ |
| Streamlit | 1-2 Tage | 1-2 Wochen | ⭐⭐⭐⭐☆ | ⭐⭐⭐⭐☆ |
| Dash | 1-2 Wochen | 2-4 Monate | ⭐⭐⭐⭐☆ | ⭐⭐⭐⭐☆ |
| Power BI | 3-5 Tage | 2-3 Monate | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Tableau | 2-3 Tage | 1-2 Monate | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| D3.js | 2-4 Wochen | 6-12 Monate | ⭐⭐⭐⭐☆ | ⭐⭐⭐⭐☆ |

---

## 🔄 Tool-Kombinationen

### Empfohlene Kombinationen

**1. Data Science Stack**
- Pandas (Datenverarbeitung)
- Seaborn (EDA)
- Matplotlib (Custom Plots)
- Plotly (Interaktive Reports)

**2. Dashboard Stack**
- Pandas (Datenverarbeitung)
- Plotly (Visualisierungen)
- Streamlit oder Dash (Framework)

**3. Business Intelligence Stack**
- Power BI oder Tableau (Haupttool)
- Python (Datenaufbereitung)
- Excel (Ad-hoc Analysen)

**4. Research Stack**
- Matplotlib (Publikationen)
- Seaborn (Statistische Analysen)
- Jupyter Notebooks (Dokumentation)

---

## 📊 Zusammenfassung

### Für Anfänger
**Start mit:** Seaborn → Matplotlib → Plotly Express

### Für Fortgeschrittene
**Erweitere mit:** Bokeh, Streamlit, Dash

### Für Business
**Fokus auf:** Power BI oder Tableau

### Für Research
**Fokus auf:** Matplotlib + Seaborn

### Für Web-Entwicklung
**Fokus auf:** Plotly, D3.js, Dash

---

## 🎯 Empfehlungen für diesen Kurs

### Pflicht (Alle lernen)
1. **Matplotlib** - Basis-Verständnis
2. **Seaborn** - Statistische Plots
3. **Plotly** - Interaktivität

### Optional (Nach Interesse)
4. **Bokeh** - Erweiterte Interaktivität
5. **Streamlit** - Rapid Prototyping
6. **Power BI** - Business Intelligence

### Bonus (Selbststudium)
7. **Dash** - Production Dashboards
8. **Tableau** - BI Alternative
9. **D3.js** - Web-Visualisierungen

---

**Erstellt:** April 2026  
**Version:** 1.0  
**Nächste Aktualisierung:** Nach Kurs-Feedback