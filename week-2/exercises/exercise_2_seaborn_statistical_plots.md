# Übung 2: Seaborn Statistical Plots – Verteilungen und Beziehungen visualisieren

## Lernziele
Nach dieser Übung kannst du:
- mit Seaborn schnell statistische Plots erstellen
- Verteilungen, Gruppenunterschiede und Zusammenhänge visualisieren
- geeignete Plot-Typen für unterschiedliche Analyseziele auswählen
- Themes und Stile bewusst einsetzen

---

## Kontext

Seaborn ist besonders nützlich, wenn Daten bereits in einem Pandas DataFrame vorliegen und du schnell zu gut lesbaren statistischen Visualisierungen kommen möchtest.

In dieser Übung arbeitest du mit einem kleinen Retail-Datensatz und beantwortest drei typische Analysefragen:

1. Wie sind Werte verteilt?
2. Gibt es Zusammenhänge zwischen Variablen?
3. Unterscheiden sich Gruppen sichtbar voneinander?

---

## Datengrundlage

Verwende den Datensatz `../datasets/online_retail_sample.csv`.

### Beispiel zum Laden
```python
import pandas as pd

df = pd.read_csv("../datasets/online_retail_sample.csv")
df.head()
```

### Verfügbare Spalten
- `order_id`
- `order_date`
- `category`
- `units_sold`
- `revenue`
- `customer_segment`
- `discount_pct`

---

## Aufgabenstellung

Erstelle **mindestens drei verschiedene Seaborn-Plots**, die jeweils eine andere Frage beantworten.

### Pflichtteil

#### Teil A: Verteilung
Erstelle einen Plot, der die Verteilung von `revenue` zeigt.

**Geeignete Optionen:**
- `sns.histplot()`
- optional mit KDE
- alternativ zusätzlich Vergleich zwischen Segmenten

#### Teil B: Zusammenhang
Erstelle einen Plot, der den Zusammenhang zwischen `units_sold` und `revenue` zeigt.

**Geeignete Optionen:**
- `sns.scatterplot()`
- optional mit `hue="category"` oder `style="customer_segment"`

#### Teil C: Kategorialer Vergleich
Erstelle einen Plot, der Unterschiede zwischen Gruppen zeigt, z. B.:

- `revenue` nach `customer_segment`
- `units_sold` nach `category`

**Geeignete Optionen:**
- `sns.boxplot()`
- `sns.violinplot()`
- `sns.barplot()`
- optional zusätzlich `sns.stripplot()`

---

## Zusätzliche Anforderungen

Deine Visualisierungen sollen:
1. ein einheitliches Theme verwenden
2. sinnvolle Titel und Achsenbeschriftungen enthalten
3. gut lesbar und nicht überladen sein
4. jeweils **eine kurze Interpretation** erhalten

---

## Starter-Code

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("../datasets/online_retail_sample.csv")

sns.set_theme(style="whitegrid", palette="deep")

# Teil A: Verteilung
fig, ax = plt.subplots(figsize=(10, 6))
# DEIN CODE HIER
plt.show()

# Teil B: Zusammenhang
fig, ax = plt.subplots(figsize=(10, 6))
# DEIN CODE HIER
plt.show()

# Teil C: Kategorialer Vergleich
fig, ax = plt.subplots(figsize=(10, 6))
# DEIN CODE HIER
plt.show()
```

---

## Mögliche Lösungswege

### Teil A: Verteilung mit Histogramm
```python
sns.histplot(data=df, x="revenue", bins=12, kde=True, ax=ax)
ax.set_title("Verteilung des Umsatzes")
```

### Teil B: Zusammenhang mit Scatter Plot
```python
sns.scatterplot(
    data=df,
    x="units_sold",
    y="revenue",
    hue="category",
    ax=ax
)
ax.set_title("Zusammenhang zwischen Absatz und Umsatz")
```

### Teil C: Gruppierter Vergleich mit Boxplot
```python
sns.boxplot(
    data=df,
    x="customer_segment",
    y="revenue",
    ax=ax
)
ax.set_title("Umsatz nach Kundensegment")
```

---

## Erwartetes Ergebnis

Deine Abgabe sollte drei unterschiedliche Perspektiven sichtbar machen:

- **Verteilung:** Ist `revenue` eher gleichmäßig, schief oder breit gestreut?
- **Zusammenhang:** Steigt `revenue`, wenn `units_sold` steigt?
- **Gruppenvergleich:** Welche Kategorie oder welches Segment zeigt höhere Werte oder größere Streuung?

**Wichtig:** Es geht nicht nur um „schöne“ Plots, sondern darum, dass jeder Plot eine analytische Funktion erfüllt.

---

## Interpretationsauftrag

Schreibe unter jeden Plot 2–4 Sätze, zum Beispiel:

- Was fällt auf?
- Gibt es Ausreißer?
- Gibt es Gruppenunterschiede?
- Welche Visualisierung war für die jeweilige Frage besonders geeignet?

---

## Reflexionsfragen

1. Warum ist ein Histogramm für `revenue` sinnvoll?
2. Warum ist ein Scatter Plot geeignet, um `units_sold` und `revenue` zu vergleichen?
3. Wann wäre ein Boxplot hilfreicher als ein Balkendiagramm?
4. Was hat Seaborn in dieser Übung einfacher gemacht als reines Matplotlib?

---

## Bewertungsschema

| Kriterium | Punkte |
|----------|--------|
| Drei passende Plot-Typen gewählt | 4 |
| Seaborn korrekt eingesetzt | 3 |
| Theme/Style konsistent verwendet | 2 |
| Titel und Achsenbeschriftungen vorhanden | 2 |
| Fachlich sinnvolle Interpretation | 3 |
| Lesbarkeit und Übersichtlichkeit | 2 |

**Gesamt:** 16 Punkte

### Bewertungsrubrik
- **14–16 Punkte:** Sehr gut – passende Plot-Wahl, gute Interpretation, saubere Gestaltung
- **11–13 Punkte:** Gut – kleine Schwächen, aber analytisch solide
- **8–10 Punkte:** Befriedigend – wesentliche Anforderungen erfüllt, Interpretation noch ausbaufähig
- **0–7 Punkte:** Überarbeiten – Plot-Wahl oder Erklärung noch nicht passend

---

## Lösungshinweise

- Verwende `sns.set_theme()` früh, damit alle Plots einheitlich aussehen.
- Nutze `hue` nur dann, wenn es eine analytische Bedeutung hat.
- Vermeide zu viele Farben oder Kategorien gleichzeitig.
- Ein `boxplot` eignet sich besonders gut, wenn du Median, Quartile und Ausreißer sehen willst.
- Ein `violinplot` kann zusätzlich die Form der Verteilung zeigen.
- Falls Werte stark schief verteilt sind, notiere das in deiner Interpretation.

---

## Bonus-Aufgaben

### Bonus 1
Kombiniere `boxplot` und `stripplot` in derselben Figur.

### Bonus 2
Vergleiche zwei verschiedene Themes:
- `"whitegrid"`
- `"ticks"`

### Bonus 3
Teste, ob eine logarithmische Skala auf der y-Achse bei `revenue` sinnvoll wäre.

---

## Abgabe

Speichere deine Lösung als:
- Jupyter Notebook **oder**
- `exercise_2_solution.py`

**Empfohlene Bearbeitungszeit:** 20–25 Minuten

---

*Schwierigkeitsgrad: ⭐⭐⭐☆☆*