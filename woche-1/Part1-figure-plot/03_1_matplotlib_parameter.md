# 🎨 Matplotlib Parameter-Referenz

## 🎯 Überblick

Diese Referenz zeigt dir die wichtigsten Parameter für Matplotlib-Plots.

---

## 📊 Plot-Typen

### Line Chart (Liniendiagramm)
```python
plt.plot(x, y, 
         color='blue',           # Farbe
         linestyle='-',          # Linientyp
         linewidth=2,            # Linienstärke
         marker='o',             # Marker-Typ
         markersize=5,           # Marker-Größe
         label='Meine Linie',    # Label für Legende
         alpha=0.8)              # Transparenz (0-1)
```

### Scatter Plot (Streudiagramm)
```python
plt.scatter(x, y,
            color='red',         # Farbe
            s=50,                # Größe der Punkte
            marker='o',          # Marker-Typ
            alpha=0.5,           # Transparenz
            edgecolors='black',  # Rand-Farbe
            linewidths=1,        # Rand-Breite
            label='Meine Punkte')
```

### Bar Chart (Balkendiagramm)
```python
plt.bar(x, y,
        color='green',           # Farbe
        width=0.8,               # Breite der Balken
        alpha=0.7,               # Transparenz
        edgecolor='black',       # Rand-Farbe
        label='Meine Balken')
```

---

## 🎨 Farben

### Farbnamen (Englisch)
```python
'red', 'blue', 'green', 'yellow', 'orange', 'purple', 
'pink', 'brown', 'gray', 'black', 'white'
```

### Hex-Codes
```python
'#FF5733'  # Orange-Rot
'#3498DB'  # Blau
'#2ECC71'  # Grün
'#F39C12'  # Orange
'#9B59B6'  # Lila
```

### RGB-Werte (0-1)
```python
(1.0, 0.0, 0.0)    # Rot
(0.0, 0.0, 1.0)    # Blau
(0.0, 1.0, 0.0)    # Grün
(0.5, 0.5, 0.5)    # Grau
```

### Farbpaletten
```python
# Matplotlib Standard-Farben
'C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'
```

---

## 📏 Linientypen

```python
'-'   # Durchgezogen (Standard)
'--'  # Gestrichelt
'-.'  # Strich-Punkt
':'   # Gepunktet
''    # Keine Linie
```

**Beispiel:**
```python
plt.plot(x, y1, linestyle='-', label='Durchgezogen')
plt.plot(x, y2, linestyle='--', label='Gestrichelt')
plt.plot(x, y3, linestyle='-.', label='Strich-Punkt')
plt.plot(x, y4, linestyle=':', label='Gepunktet')
```

---

## 🔵 Marker

### Häufig verwendet:
```python
'o'   # Kreis
's'   # Quadrat
'^'   # Dreieck (oben)
'v'   # Dreieck (unten)
'*'   # Stern
'+'   # Plus
'x'   # Kreuz
'D'   # Diamant
'.'   # Punkt
```

**Beispiel:**
```python
plt.plot(x, y, marker='o', markersize=8, markerfacecolor='red', 
         markeredgecolor='black', markeredgewidth=1)
```

---

## 🏷️ Beschriftungen

### Titel
```python
plt.title('Mein Titel',
          fontsize=16,           # Schriftgröße
          fontweight='bold',     # Fett
          color='black',         # Farbe
          pad=20)                # Abstand
```

### Achsenbeschriftungen
```python
plt.xlabel('X-Achse',
           fontsize=12,
           fontweight='normal',
           color='black')

plt.ylabel('Y-Achse',
           fontsize=12,
           fontweight='normal',
           color='black')
```

### Legende
```python
plt.legend(loc='best',           # Position (automatisch)
           fontsize=10,
           frameon=True,         # Rahmen
           shadow=True,          # Schatten
           title='Legende')
```

**Legende-Positionen:**
```python
'best'          # Automatisch (beste Position)
'upper right'   # Oben rechts
'upper left'    # Oben links
'lower right'   # Unten rechts
'lower left'    # Unten links
'center'        # Mitte
```

---

## 📐 Achsen

### Achsen-Bereiche
```python
plt.xlim(0, 10)      # X-Achse von 0 bis 10
plt.ylim(-5, 5)      # Y-Achse von -5 bis 5
```

### Achsen-Ticks
```python
plt.xticks([0, 2, 4, 6, 8, 10],           # Positionen
           ['A', 'B', 'C', 'D', 'E', 'F'], # Labels
           rotation=45,                     # Rotation
           fontsize=10)
```

### Achsen-Skala
```python
plt.xscale('linear')   # Linear (Standard)
plt.xscale('log')      # Logarithmisch
plt.yscale('log')      # Y-Achse logarithmisch
```

---

## 🔲 Gitter

```python
plt.grid(True,              # Aktivieren
         color='gray',      # Farbe
         linestyle='--',    # Linientyp
         linewidth=0.5,     # Linienstärke
         alpha=0.5)         # Transparenz
```

---

## 📏 Figure & Axes

### Figure-Größe
```python
plt.figure(figsize=(10, 6))  # Breite x Höhe in Zoll
```

### Subplots
```python
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
# 2 Zeilen, 2 Spalten
axes[0, 0].plot(x, y1)
axes[0, 1].plot(x, y2)
axes[1, 0].plot(x, y3)
axes[1, 1].plot(x, y4)
```

### Tight Layout
```python
plt.tight_layout()  # Automatische Anpassung
```

---

## 📝 Annotationen

### Text hinzufügen
```python
plt.text(x=5, y=10,              # Position
         s='Wichtiger Punkt',    # Text
         fontsize=12,
         color='red',
         ha='center',            # Horizontal alignment
         va='bottom')            # Vertical alignment
```

### Pfeil hinzufügen
```python
plt.annotate('Maximum',          # Text
             xy=(5, 10),         # Punkt, auf den gezeigt wird
             xytext=(6, 12),     # Position des Textes
             arrowprops=dict(arrowstyle='->', color='red'))
```

### Vertikale/Horizontale Linien
```python
plt.axvline(x=5, color='red', linestyle='--', label='Wichtiges Datum')
plt.axhline(y=10, color='blue', linestyle='--', label='Durchschnitt')
```

---

## 🎨 Styling

### Style verwenden
```python
plt.style.use('seaborn-v0_8')    # Seaborn-Style
plt.style.use('ggplot')          # ggplot-Style
plt.style.use('bmh')             # Bayesian Methods for Hackers
```

### Verfügbare Styles anzeigen
```python
print(plt.style.available)
```

---

## 💾 Speichern

```python
plt.savefig('mein_plot.png',
            dpi=300,              # Auflösung
            bbox_inches='tight',  # Ränder entfernen
            transparent=False,    # Transparenter Hintergrund
            facecolor='white')    # Hintergrundfarbe
```

**Formate:**
- `.png` - Für Web und Präsentationen
- `.pdf` - Für Druck und Publikationen
- `.svg` - Für Vektorgrafiken
- `.jpg` - Für Fotos

---

## 🔧 Häufige Kombinationen

### Professioneller Line Chart
```python
plt.figure(figsize=(10, 6))
plt.plot(x, y, color='#3498DB', linewidth=2.5, marker='o', 
         markersize=6, label='Daten')
plt.title('Mein Titel', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('X-Achse', fontsize=12)
plt.ylabel('Y-Achse', fontsize=12)
plt.grid(True, alpha=0.3, linestyle='--')
plt.legend(loc='best', fontsize=10)
plt.tight_layout()
plt.savefig('plot.png', dpi=300, bbox_inches='tight')
plt.show()
```

### Vergleich mit zwei Linien
```python
plt.figure(figsize=(12, 6))
plt.plot(x, y1, color='blue', linewidth=2, marker='o', label='Stadt A')
plt.plot(x, y2, color='red', linewidth=2, marker='s', label='Stadt B')
plt.title('Temperatur-Vergleich', fontsize=16, fontweight='bold')
plt.xlabel('Datum', fontsize=12)
plt.ylabel('Temperatur (°C)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend(loc='upper left', fontsize=11)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

### Scatter Plot mit Highlights
```python
plt.figure(figsize=(10, 8))
plt.scatter(x, y, c='blue', s=50, alpha=0.6, label='Normal')
plt.scatter(x_outliers, y_outliers, c='red', s=100, marker='*', 
            label='Ausreißer')
plt.title('Zusammenhang mit Ausreißern', fontsize=16, fontweight='bold')
plt.xlabel('Alter (Jahre)', fontsize=12)
plt.ylabel('Cholesterin (mg/dL)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend(loc='best', fontsize=11)
plt.tight_layout()
plt.show()
```

---

## 📚 Siehe auch

- **Plot-Qualitäts-Checkliste:** [`docs/checkliste_plot.md`](../../docs/checkliste_plot.md)
- **Langsamer Leitfaden:** [`woche-1/Part2/leitfaden_langsam.md`](../Part2/leitfaden_langsam.md)
- **Axes-Platzierung:** [`woche-1/Part2/04_axes_platzierung.md`](../Part2/04_axes_platzierung.md)
- **Matplotlib Dokumentation:** https://matplotlib.org/stable/api/pyplot_summary.html

---

*Nutze diese Referenz beim Erstellen deiner Plots!* 🎨