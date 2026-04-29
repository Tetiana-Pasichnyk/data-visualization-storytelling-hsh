# 📐 Axes Platzierung: Subplots erstellen

## 🎯 Was lernen wir hier?

Nach der Gruppenarbeit habt ihr gelernt, wie man **einen Plot** erstellt.
Jetzt lernen wir, wie man **mehrere Plots** auf einer Figure platziert!

**Wichtig:** Axes ≠ Axis!
- **Axes** = Der gesamte Plot-Bereich (das Koordinatensystem)
- **Axis** = Die X- oder Y-Achse

---

## 🏗️ Die Hierarchie verstehen

```
Figure (Leinwand)
    ↓
Axes (Plot-Bereich 1)
    ↓
Axis (X-Achse, Y-Achse)
    ↓
Plot-Elemente (Linien, Punkte, etc.)
```

**Eine Figure kann mehrere Axes enthalten!**

---

## 🔧 Drei Wege, Axes zu erstellen

### 1️⃣ `.subplots()` - Der Standard-Weg (95% der Fälle!)

**Am einfachsten und am häufigsten verwendet:**

```python
import matplotlib.pyplot as plt

# Eine Figure mit einem Axes
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 9])
ax.set_title("Ein Plot")
plt.show()
```

**Mehrere Subplots nebeneinander:**

```python
# 1 Zeile, 2 Spalten
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.plot([1, 2, 3], [1, 4, 9])
ax1.set_title("Plot 1")

ax2.plot([1, 2, 3], [1, 2, 3])
ax2.set_title("Plot 2")

plt.tight_layout()  # Verhindert Überlappungen
plt.show()
```

**Mehrere Subplots untereinander:**

```python
# 2 Zeilen, 1 Spalte
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))

ax1.plot([1, 2, 3], [1, 4, 9])
ax1.set_title("Oben")

ax2.plot([1, 2, 3], [1, 2, 3])
ax2.set_title("Unten")

plt.tight_layout()
plt.show()
```

**Grid von Subplots (2x2):**

```python
# 2 Zeilen, 2 Spalten
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# axes ist jetzt ein 2D-Array!
axes[0, 0].plot([1, 2, 3], [1, 4, 9])
axes[0, 0].set_title("Oben Links")

axes[0, 1].plot([1, 2, 3], [1, 2, 3])
axes[0, 1].set_title("Oben Rechts")

axes[1, 0].plot([1, 2, 3], [3, 2, 1])
axes[1, 0].set_title("Unten Links")

axes[1, 1].plot([1, 2, 3], [2, 4, 6])
axes[1, 1].set_title("Unten Rechts")

plt.tight_layout()
plt.show()
```

---

### 2️⃣ `.add_subplot()` - Grid-basiert

**Für mehr Kontrolle über die Position:**

```python
fig = plt.figure(figsize=(12, 5))

# add_subplot(Zeilen, Spalten, Position)
ax1 = fig.add_subplot(1, 3, 1)  # 1 Zeile, 3 Spalten, Position 1
ax1.plot([1, 2, 3], [1, 4, 9])
ax1.set_title("Links")

ax2 = fig.add_subplot(1, 3, 2)  # Position 2
ax2.plot([1, 2, 3], [1, 2, 3])
ax2.set_title("Mitte")

ax3 = fig.add_subplot(1, 3, 3)  # Position 3
ax3.plot([1, 2, 3], [3, 2, 1])
ax3.set_title("Rechts")

plt.tight_layout()
plt.show()
```

**Kurzschreibweise (ohne Kommas):**

```python
ax1 = fig.add_subplot(131)  # Gleich wie (1, 3, 1)
ax2 = fig.add_subplot(132)  # Gleich wie (1, 3, 2)
ax3 = fig.add_subplot(133)  # Gleich wie (1, 3, 3)
```

---

### 3️⃣ `.add_axes()` - Manuelle Positionierung

**Für spezielle Layouts (z.B. Inset-Plots):**

```python
fig = plt.figure(figsize=(10, 6))

# add_axes([left, bottom, width, height])
# Werte zwischen 0 und 1 (relativ zur Figure)
ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])  # Haupt-Plot
ax1.plot([1, 2, 3], [1, 4, 9])
ax1.set_title("Haupt-Plot")

# Kleiner Plot oben rechts (Inset)
ax2 = fig.add_axes([0.6, 0.6, 0.25, 0.25])
ax2.plot([1, 2, 3], [1, 2, 3])
ax2.set_title("Inset", fontsize=10)

plt.show()
```

---

## 🎨 Wichtige Axes-Properties

Jedes Axes-Objekt hat viele Eigenschaften, die du anpassen kannst:

| Property | Was macht es? | Beispiel |
|----------|---------------|----------|
| `facecolor` | Hintergrundfarbe | `ax.set_facecolor('lightgray')` |
| `xlim` | X-Achsen-Grenzen | `ax.set_xlim(0, 10)` |
| `ylim` | Y-Achsen-Grenzen | `ax.set_ylim(-5, 5)` |
| `xscale` | X-Achsen-Skalierung | `ax.set_xscale('log')` |
| `yscale` | Y-Achsen-Skalierung | `ax.set_yscale('log')` |
| `xlabel` | X-Achsen-Beschriftung | `ax.set_xlabel('Zeit')` |
| `ylabel` | Y-Achsen-Beschriftung | `ax.set_ylabel('Temperatur')` |
| `title` | Titel | `ax.set_title('Mein Plot')` |
| `aspect` | Seitenverhältnis | `ax.set_aspect('equal')` |

---

## 💡 Praktische Beispiele

### Beispiel 1: Vergleich von zwei Datensätzen

```python
import pandas as pd
import matplotlib.pyplot as plt

# Daten laden
df_hannover = pd.read_csv('data/hannover_temp.csv')
df_berlin = pd.read_csv('data/berlin_temp.csv')

# Zwei Plots nebeneinander
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Plot 1: Hannover
ax1.plot(df_hannover['datum'], df_hannover['temperatur'], color='blue')
ax1.set_title('Temperatur in Hannover')
ax1.set_xlabel('Datum')
ax1.set_ylabel('Temperatur (°C)')
ax1.grid(True)

# Plot 2: Berlin
ax2.plot(df_berlin['datum'], df_berlin['temperatur'], color='red')
ax2.set_title('Temperatur in Berlin')
ax2.set_xlabel('Datum')
ax2.set_ylabel('Temperatur (°C)')
ax2.grid(True)

plt.tight_layout()
plt.show()
```

---

### Beispiel 2: Verschiedene Plot-Typen kombinieren

```python
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Oben Links: Line Plot
axes[0, 0].plot([1, 2, 3, 4], [1, 4, 9, 16])
axes[0, 0].set_title('Line Plot')

# Oben Rechts: Scatter Plot
axes[0, 1].scatter([1, 2, 3, 4], [1, 4, 9, 16], color='red')
axes[0, 1].set_title('Scatter Plot')

# Unten Links: Bar Chart
axes[1, 0].bar(['A', 'B', 'C', 'D'], [1, 4, 9, 16], color='green')
axes[1, 0].set_title('Bar Chart')

# Unten Rechts: Histogram
axes[1, 1].hist([1, 2, 2, 3, 3, 3, 4, 4, 4, 4], bins=4, color='orange')
axes[1, 1].set_title('Histogram')

plt.tight_layout()
plt.show()
```

---

## ✅ Checkliste für Subplots

- [ ] **Richtige Methode gewählt?**
  - `.subplots()` für Standard-Layouts
  - `.add_subplot()` für mehr Kontrolle
  - `.add_axes()` für spezielle Layouts

- [ ] **Alle Plots beschriftet?**
  - Jeder Axes braucht Titel, xlabel, ylabel

- [ ] **`plt.tight_layout()` verwendet?**
  - Verhindert Überlappungen

- [ ] **Figsize angepasst?**
  - Mehr Subplots = größere Figure nötig

---

## 🚫 Häufige Fehler

### ❌ Fehler 1: Überlappende Labels

```python
# SCHLECHT - Labels überlappen sich
fig, (ax1, ax2) = plt.subplots(1, 2)
# ... plots ...
plt.show()  # Labels können überlappen!
```

```python
# GUT - tight_layout() verwenden
fig, (ax1, ax2) = plt.subplots(1, 2)
# ... plots ...
plt.tight_layout()  # ✅ Verhindert Überlappungen
plt.show()
```

---

### ❌ Fehler 2: Falsche Indexierung bei Grid

```python
# SCHLECHT - Vergessen, dass axes ein 2D-Array ist
fig, axes = plt.subplots(2, 2)
axes[0].plot([1, 2, 3])  # ❌ Fehler!
```

```python
# GUT - Beide Indizes angeben
fig, axes = plt.subplots(2, 2)
axes[0, 0].plot([1, 2, 3])  # ✅ Richtig!
```

---

### ❌ Fehler 3: Figure zu klein

```python
# SCHLECHT - 4 Plots auf kleiner Figure
fig, axes = plt.subplots(2, 2)  # Standard: 6.4 x 4.8
# Plots sind zu klein!
```

```python
# GUT - Größere Figure für mehr Plots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))  # ✅ Besser!
```

---

## 🎯 Zusammenfassung

**Wann welche Methode?**

| Situation | Methode | Beispiel |
|-----------|---------|----------|
| Ein Plot | `.subplots()` | `fig, ax = plt.subplots()` |
| Mehrere Plots (Grid) | `.subplots()` | `fig, axes = plt.subplots(2, 2)` |
| Mehr Kontrolle | `.add_subplot()` | `ax = fig.add_subplot(131)` |
| Spezial-Layout | `.add_axes()` | `ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])` |

**Wichtigste Regel:** Verwende `.subplots()` für 95% der Fälle!

---

## 📚 Siehe auch

- **Notebook:** `woche-1/Part2/04_Axes.ipynb` (Vollständige Beispiele)
- **Plot-Qualität:** `docs/checkliste_plot.md` (Wie man gute Plots macht)
- **Parameter-Referenz:** `woche-1/04_matplotlib_parameter.md`

---

## 🚀 Übung

**Aufgabe:** Erstelle eine Figure mit 3 Subplots:
1. Oben: Line Plot mit Temperatur-Daten
2. Unten Links: Scatter Plot mit den gleichen Daten
3. Unten Rechts: Bar Chart mit Durchschnittswerten

**Tipp:** Verwende `plt.subplots(2, 2)` und lass einen Subplot leer!

---

*Viel Erfolg beim Erstellen von Subplots! 📐*