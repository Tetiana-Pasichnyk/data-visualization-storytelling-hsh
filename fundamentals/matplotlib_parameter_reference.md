# 📚 Matplotlib Parameter Reference (B1-Deutsch)

## 🎯 Welche Parameter solltest du lernen?

**Pädagogischer Filter:** Lerne nur Parameter, die **ändern, was du siehst**.

### Die 5 Kategorien:
1. **Color/Fill** — Welche Farbe hat es?
2. **Geometry** — Größe, Position, Grenzen
3. **Typography** — Text-Styling
4. **Visibility/Layering** — Sichtbarkeit, Transparenz, Reihenfolge
5. **Labels** — Für Legenden und Beschriftungen

---

## 🔗 Wichtige Verbindung verstehen!

### `plot()` erstellt ein `Line2D`-Objekt

```python
# Wenn du das machst:
line = ax.plot([1,2,3], [4,5,6], color='blue', linewidth=2)

# Dann erstellt Matplotlib ein Line2D-Objekt mit diesen Eigenschaften:
# line[0] ist ein Line2D-Objekt
# line[0].get_color() → 'blue'
# line[0].get_linewidth() → 2
```

**Das bedeutet:** Alle Parameter, die du in `plot()` verwendest, sind **Line2D-Parameter**!

---

## 📊 Line2D (Linien in Plots)

### ⚠️ Wichtig: `plot()` nutzt diese Parameter!

### Wichtige Parameter:

#### 1. Color/Fill
```python
color='blue'           # Farbe der Linie
alpha=0.7              # Transparenz (0=unsichtbar, 1=voll)
```

#### 2. Geometry
```python
linewidth=2            # Dicke der Linie
linestyle='--'         # Stil: '-', '--', '-.', ':'
xdata=[1,2,3]          # x-Koordinaten
ydata=[4,5,6]          # y-Koordinaten
```

#### 3. Markers
```python
marker='o'             # Marker-Typ: 'o', 's', '^', etc.
markersize=8           # Größe des Markers
markerfacecolor='red'  # Füllfarbe des Markers
markeredgecolor='black' # Randfarbe des Markers
```

#### 4. Visibility/Layering
```python
visible=True           # Sichtbar oder nicht
zorder=2               # Reihenfolge (höher = vorne)
```

#### 5. Labels
```python
label='Meine Linie'    # Name für Legende
```

### Beispiel mit `plot()`:
```python
# Diese beiden sind IDENTISCH:

# Methode 1: Direkt in plot()
line = ax.plot([1,2,3], [4,5,6],
               color='blue',
               linewidth=2,
               linestyle='--',
               marker='o',
               markersize=8,
               label='Verkäufe',
               alpha=0.7)

# Methode 2: Line2D-Objekt nachträglich ändern
line = ax.plot([1,2,3], [4,5,6])
line[0].set_color('blue')
line[0].set_linewidth(2)
line[0].set_linestyle('--')
line[0].set_marker('o')
line[0].set_markersize(8)
line[0].set_label('Verkäufe')
line[0].set_alpha(0.7)
```

**Fazit:** `plot()` Parameter = `Line2D` Parameter!

---

## 🎨 Patch (Flächen: Rechtecke, Kreise, etc.)

### Wichtige Parameter:

#### 1. Color/Fill
```python
facecolor='lightblue'  # Füllfarbe
edgecolor='black'      # Randfarbe
alpha=0.5              # Transparenz
```

#### 2. Geometry
```python
linewidth=2            # Dicke des Rands
linestyle='--'         # Stil des Rands
```

#### 3. Pattern
```python
hatch='//'             # Schraffur: '/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*'
fill=True              # Füllen oder nur Rand
```

#### 4. Visibility/Layering
```python
visible=True           # Sichtbar oder nicht
zorder=1               # Reihenfolge
```

#### 5. Labels
```python
label='Bereich A'      # Name für Legende
```

### Beispiel:
```python
from matplotlib.patches import Rectangle

rect = Rectangle((0, 0), 1, 1,
                 facecolor='lightblue',
                 edgecolor='black',
                 linewidth=2,
                 alpha=0.5,
                 label='Bereich')
ax.add_patch(rect)
```

---

## 📝 Text (Beschriftungen)

### Wichtige Parameter:

#### 1. Content & Position
```python
text='Hallo'           # Der Text
x=0.5                  # x-Position
y=0.5                  # y-Position
```

#### 2. Color/Fill
```python
color='black'          # Textfarbe
alpha=1.0              # Transparenz
backgroundcolor='yellow' # Hintergrundfarbe
```

#### 3. Typography
```python
fontsize=12            # Schriftgröße
fontweight='bold'      # Gewicht: 'normal', 'bold'
fontstyle='italic'     # Stil: 'normal', 'italic'
fontfamily='serif'     # Familie: 'serif', 'sans-serif', 'monospace'
```

#### 4. Alignment
```python
horizontalalignment='center'  # 'left', 'center', 'right'
verticalalignment='center'    # 'top', 'center', 'bottom'
rotation=45            # Drehung in Grad
wrap=True              # Automatischer Zeilenumbruch
```

#### 5. Visibility/Layering
```python
visible=True           # Sichtbar oder nicht
zorder=3               # Reihenfolge
```

### Beispiel:
```python
ax.text(0.5, 0.5, 'Wichtig!',
        fontsize=14,
        fontweight='bold',
        color='red',
        horizontalalignment='center',
        verticalalignment='center',
        backgroundcolor='yellow',
        alpha=0.8)
```

---

## 📐 Axes (Die Zeichenfläche)

### Wichtige Parameter:

#### 1. Color/Fill
```python
facecolor='white'      # Hintergrundfarbe
alpha=1.0              # Transparenz
```

#### 2. Geometry
```python
xlim=(0, 10)           # x-Achsen-Grenzen
ylim=(0, 100)          # y-Achsen-Grenzen
xscale='linear'        # Skala: 'linear', 'log'
yscale='linear'        # Skala: 'linear', 'log'
aspect='auto'          # Seitenverhältnis: 'auto', 'equal'
```

#### 3. Labels
```python
xlabel='Zeit'          # x-Achsen-Beschriftung
ylabel='Temperatur'    # y-Achsen-Beschriftung
title='Mein Plot'      # Titel
```

#### 4. Ticks
```python
xticks=[0,5,10]        # x-Tick-Positionen
yticks=[0,50,100]      # y-Tick-Positionen
xticklabels=['Start','Mitte','Ende'] # x-Tick-Labels
yticklabels=['0°C','50°C','100°C']   # y-Tick-Labels
```

#### 5. Frame
```python
frame_on=True          # Rahmen anzeigen
```

#### 6. Visibility/Layering
```python
visible=True           # Sichtbar oder nicht
zorder=0               # Reihenfolge
```

### Beispiel:
```python
ax.set_xlim(0, 10)
ax.set_ylim(0, 100)
ax.set_xlabel('Zeit (Tage)')
ax.set_ylabel('Temperatur (°C)')
ax.set_title('Temperaturverlauf')
ax.set_facecolor('lightgray')
```

---

## 🖼️ Figure (Die gesamte Figur)

### Wichtige Parameter:

#### 1. Color/Fill
```python
facecolor='white'      # Hintergrundfarbe
edgecolor='black'      # Randfarbe
alpha=1.0              # Transparenz
```

#### 2. Geometry
```python
figwidth=10            # Breite in Zoll
figheight=6            # Höhe in Zoll
dpi=100                # Auflösung (dots per inch)
```

#### 3. Frame
```python
frameon=True           # Rahmen anzeigen
```

### Beispiel:
```python
fig = plt.figure(figsize=(10, 6),
                 facecolor='white',
                 edgecolor='black',
                 dpi=100)
```

---

## 🎯 Speziell: `plot()` Parameter

### 🔗 Die Verbindung verstehen

```
ax.plot() → erstellt → Line2D-Objekt
           ↓
    Alle Parameter gehen direkt an Line2D!
```

`plot()` ist eine **Axes-Methode**, die ein **Line2D-Objekt** erstellt und zurückgibt.

**Wichtig:** Alle Parameter, die du in `plot()` verwendest, sind **Line2D-Parameter**!

### Die wichtigsten Parameter für `plot()` (= Line2D-Parameter):

#### 1. Daten
```python
ax.plot(x, y)          # x- und y-Daten
```

#### 2. Color/Fill
```python
color='blue'           # oder: c='blue'
alpha=0.7              # Transparenz
```

#### 3. Line Style
```python
linewidth=2            # oder: lw=2
linestyle='--'         # oder: ls='--'
                       # Optionen: '-', '--', '-.', ':'
```

#### 4. Markers
```python
marker='o'             # Marker-Typ
markersize=8           # oder: ms=8
markerfacecolor='red'  # oder: mfc='red'
markeredgecolor='black' # oder: mec='black'
markeredgewidth=1      # oder: mew=1
```

#### 5. Labels
```python
label='Meine Daten'    # Für Legende
```

#### 6. Format String (Kurzform)
```python
ax.plot(x, y, 'bo-')   # b=blue, o=circle, -=solid line
                       # Format: [color][marker][line]
```

**⚠️ Wichtig:** Format Strings sind eine **Abkürzung** für Line2D-Parameter!

```python
# Diese sind IDENTISCH:
ax.plot(x, y, 'bo-')

ax.plot(x, y, color='blue', marker='o', linestyle='-')
```

### Vollständiges Beispiel mit Verbindungen:
```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 6))

# Methode 1: plot() mit Line2D-Parametern
line1 = ax.plot([1, 2, 3, 4], [1, 4, 2, 3],
                color='blue',        # Line2D.color
                linewidth=2,         # Line2D.linewidth
                linestyle='--',      # Line2D.linestyle
                marker='o',          # Line2D.marker
                markersize=8,        # Line2D.markersize
                markerfacecolor='red',  # Line2D.markerfacecolor
                markeredgecolor='black', # Line2D.markeredgecolor
                label='Verkäufe',    # Line2D.label
                alpha=0.7)           # Line2D.alpha

# line1[0] ist jetzt ein Line2D-Objekt!
print(type(line1[0]))  # <class 'matplotlib.lines.Line2D'>

# Methode 2: Format String (Abkürzung für Line2D-Parameter)
line2 = ax.plot([1, 2, 3, 4], [2, 3, 4, 5],
                'go-',           # g=green, o=circle, -=solid
                label='Kosten')  # Entspricht: color='green', marker='o', linestyle='-'

# Methode 3: Nachträglich ändern (direkt am Line2D-Objekt)
line3 = ax.plot([1, 2, 3, 4], [3, 2, 4, 3])
line3[0].set_color('red')      # Ändert Line2D.color
line3[0].set_linewidth(3)      # Ändert Line2D.linewidth
line3[0].set_label('Gewinn')   # Ändert Line2D.label

ax.set_xlabel('Monat')
ax.set_ylabel('Betrag (€)')
ax.set_title('Verkäufe vs. Kosten')
ax.legend()
ax.grid(True, alpha=0.3)

plt.show()
```

### 🔗 Die Verbindung sehen:
```python
# plot() Parameter → Line2D Eigenschaften
line = ax.plot(x, y, color='blue', linewidth=2)

# Zugriff auf das Line2D-Objekt:
line_obj = line[0]

# Eigenschaften abfragen:
print(line_obj.get_color())      # 'blue'
print(line_obj.get_linewidth())  # 2

# Eigenschaften ändern:
line_obj.set_color('red')
line_obj.set_linewidth(3)
```

---

## 📋 Schnellreferenz: Format Strings

### 🔗 Format Strings = Abkürzung für Line2D-Parameter

Format Strings sind eine **Kurzschreibweise** für die wichtigsten Line2D-Parameter:
- **Color** → `Line2D.color`
- **Marker** → `Line2D.marker`
- **Line Style** → `Line2D.linestyle`

### Colors (Farben) → `Line2D.color`
```
'b' = blue      'g' = green     'r' = red       'c' = cyan
'm' = magenta   'y' = yellow    'k' = black     'w' = white
```

### Markers → `Line2D.marker`
```
'o' = circle    's' = square    '^' = triangle  'D' = diamond
'*' = star      '+' = plus      'x' = x         '.' = point
```

### Line Styles → `Line2D.linestyle`
```
'-'  = solid line
'--' = dashed line
'-.' = dash-dot line
':'  = dotted line
''   = no line
```

### Beispiele mit Übersetzung:
```python
# Format String → Line2D-Parameter
'bo-'   # color='blue', marker='o', linestyle='-'
'r^--'  # color='red', marker='^', linestyle='--'
'gs:'   # color='green', marker='s', linestyle=':'
'k*'    # color='black', marker='*', linestyle='' (keine Linie)
```

### Vollständiges Beispiel:
```python
# Diese drei sind IDENTISCH:

# 1. Format String
ax.plot(x, y, 'ro--')

# 2. Einzelne Parameter
ax.plot(x, y, color='red', marker='o', linestyle='--')

# 3. Line2D-Objekt nachträglich
line = ax.plot(x, y)
line[0].set_color('red')
line[0].set_marker('o')
line[0].set_linestyle('--')
```

---

## 💡 Tipps für Anfänger

### 1. Verstehe die Verbindung: plot() → Line2D
```python
# plot() erstellt ein Line2D-Objekt
line = ax.plot(x, y, 'b-')

# line[0] ist das Line2D-Objekt
print(type(line[0]))  # <class 'matplotlib.lines.Line2D'>

# Alle Parameter gehen an Line2D
line = ax.plot(x, y, color='blue', linewidth=2)
# = Line2D mit color='blue' und linewidth=2
```

### 2. Beginne einfach
```python
# Einfach: Format String
ax.plot(x, y, 'b-')  # = color='blue', linestyle='-'

# Dann erweitern mit mehr Line2D-Parametern
ax.plot(x, y, color='blue', linewidth=2, marker='o')
```

### 3. Nutze Abkürzungen
```python
# Lang
linewidth=2, linestyle='--', color='red'

# Kurz
lw=2, ls='--', c='r'
```

### 4. Kombiniere Format String + Parameter
```python
# Format String für Basics
ax.plot(x, y, 'bo-',
        # Parameter für Details
        linewidth=2,
        markersize=8,
        alpha=0.7,
        label='Daten')
```

### 5. Wichtigste Line2D-Parameter zuerst lernen
1. `color`, `linewidth`, `linestyle`
2. `marker`, `markersize`
3. `label`, `alpha`
4. Rest nach Bedarf

---

## 🎯 Zusammenfassung

### 🔗 Die wichtigste Verbindung:

```
ax.plot() → erstellt → Line2D-Objekt
           ↓
    Parameter von plot() = Parameter von Line2D
```

### Das musst du wissen:

**Für Linien (`plot()` = `Line2D`):**

**1. Farben (viele Optionen):**
- `color='blue'` (Name), `color='#FF5733'` (RGB hex), `color='0.5'` (Graustufe)
- `alpha=0.7` (Transparenz)
- `markerfacecolor='yellow'` (Marker-Füllung)
- `markeredgecolor='black'` (Marker-Rand)

**2. Format String (`fmt`):**
- Kurzform: `'bo-'` = `color='blue', marker='o', linestyle='-'`
- Nur für: color (8 Farben), marker, linestyle
- Kombinierbar mit anderen Parametern!

**3. Weitere wichtige Parameter:**
- `linewidth`, `linestyle`
- `marker`, `markersize`
- `label`, `zorder`

**Merke:** Format Strings (`fmt`) sind **Abkürzungen**, aber für volle Kontrolle nutze die einzelnen Parameter!

**Für Axes:**
- `xlim`, `ylim`
- `xlabel`, `ylabel`, `title`
- `facecolor`

**Für Figure:**
- `figsize`, `dpi`
- `facecolor`

**Für Text:**
- `fontsize`, `fontweight`, `color`
- `horizontalalignment`, `verticalalignment`

---

## 🔗 Verbindungen auf einen Blick

| Was du schreibst | Was Matplotlib macht | Objekt-Typ |
|------------------|---------------------|------------|
| `ax.plot(x, y, 'b-')` | Erstellt Line2D mit color='blue', linestyle='-' | Line2D |
| `ax.text(0, 0, 'Hi')` | Erstellt Text-Objekt | Text |
| `ax.add_patch(rect)` | Fügt Patch-Objekt hinzu | Patch |
| `ax.set_xlabel('X')` | Setzt Axes.xlabel | Axes |
| `fig = plt.figure()` | Erstellt Figure-Objekt | Figure |

**Merke:** Die Parameter, die du verwendest, sind die **Eigenschaften der Objekte**!

---

*Sprachniveau: B1 (Deutsch)*
*Basiert auf: Pedagogical filter - "Does it change what you see?"*
*Fokus: Verbindungen zwischen Methoden und Objekten verstehen*
*Letzte Aktualisierung: 23. April 2026*