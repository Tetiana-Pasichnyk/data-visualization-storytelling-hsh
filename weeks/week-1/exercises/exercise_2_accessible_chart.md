# Übung 2: Barrierefreies Diagramm erstellen

## Lernziele
- WCAG-Standards anwenden
- Farbenblind-sichere Paletten verwenden
- Redundante Kodierung implementieren

---

## Aufgabenstellung

Verbessere ein nicht-barrierefreies Diagramm!

### Gegeben: Problematischer Code

```python
import matplotlib.pyplot as plt
import numpy as np

categories = ['Produkt A', 'Produkt B', 'Produkt C', 'Produkt D']
values = [85, 72, 91, 68]

# PROBLEMATISCH: Rot/Grün, kein Kontrast
colors = ['#FF0000', '#00FF00', '#FFFF00', '#00FFFF']

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(categories, values, color=colors)
ax.set_title('Verkaufszahlen Q1')
ax.set_ylabel('Umsatz (Tsd. €)')
plt.show()
```

### Deine Aufgabe

Verbessere diesen Code, sodass er:

1. **Farbenblind-sichere Palette** verwendet (Okabe-Ito oder Paul Tol)
2. **Muster** zusätzlich zu Farben hat
3. **Hohen Kontrast** hat (teste mit `contrast_ratio()`)
4. **Direkte Beschriftungen** statt nur Farben verwendet
5. **Tufte-Prinzipien** befolgt (minimale Tinte)

---

## Schritt-für-Schritt Anleitung

### Schritt 1: Farbenblind-sichere Palette (2 Min)

Ersetze die Farben:
```python
# Okabe-Ito Palette
colors_accessible = ['#E69F00', '#56B4E9', '#009E73', '#F0E442']
```

### Schritt 2: Muster hinzufügen (3 Min)

```python
patterns = ['/', '\\', '|', '-']
bars = ax.bar(categories, values, color=colors_accessible)

for bar, pattern in zip(bars, patterns):
    bar.set_hatch(pattern)
    bar.set_edgecolor('black')
    bar.set_linewidth(1)
```

### Schritt 3: Werte direkt anzeigen (2 Min)

```python
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'{int(height)}',
            ha='center', va='bottom', fontsize=10, weight='bold')
```

### Schritt 4: Tufte-Style (3 Min)

```python
# Entferne unnötige Elemente
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)  # Werte sind direkt beschriftet!

# Entferne y-Achse (Werte sind auf Balken)
ax.set_yticks([])

# Subtile Gridlines (optional)
ax.grid(True, axis='y', alpha=0.3, linestyle='-', linewidth=0.5)
ax.set_axisbelow(True)
```

---

## Bonus-Aufgaben

### Bonus 1: Kontrast testen
Teste deine Farben mit der `contrast_ratio()` Funktion:
```python
from matplotlib.colors import to_rgb

def contrast_ratio(c1, c2):
    # ... (aus dem Notebook kopieren)
    pass

# Teste jede Farbe gegen Weiß
for color in colors_accessible:
    ratio = contrast_ratio(color, '#FFFFFF')
    print(f"{color}: {ratio:.2f}:1")
```

### Bonus 2: Zielwert-Linie
Füge eine horizontale Linie bei 80 hinzu (Zielwert):
```python
ax.axhline(y=80, color='gray', linestyle='--', linewidth=1, alpha=0.7)
ax.text(len(categories)-0.5, 81, 'Ziel: 80', fontsize=9, color='gray')
```

### Bonus 3: Farbe mit Bedeutung
Färbe Balken unter dem Zielwert anders:
```python
colors_meaningful = ['#009E73' if v >= 80 else '#D55E00' for v in values]
```

---

## Checkliste

Dein finales Diagramm sollte:
- [ ] Farbenblind-sichere Farben verwenden
- [ ] Muster für zusätzliche Unterscheidung haben
- [ ] Werte direkt auf den Balken zeigen
- [ ] Minimale nicht-Daten-Tinte haben
- [ ] Ohne Legende verständlich sein
- [ ] WCAG AA bestehen (Kontrast ≥ 3:1 für Grafiken)

---

## Erwartetes Ergebnis

**Vorher:**
- Rot/Grün (nicht unterscheidbar für 8% der Männer)
- Keine Muster
- Keine direkten Werte
- Viele unnötige Elemente

**Nachher:**
- Okabe-Ito Farben (für alle unterscheidbar)
- Muster + Farbe (doppelte Kodierung)
- Werte direkt sichtbar
- Minimalistisch (Tufte-Style)

---

## Abgabe

Speichere deinen verbesserten Code als `exercise_2_solution.py`.

**Deadline:** Ende der Übungszeit (10 Min)

---

## Reflexionsfragen

1. Wie viel besser ist dein verbessertes Diagramm?
2. Welche Änderung hatte den größten Effekt?
3. Würdest du diese Prinzipien in Zukunft anwenden?

---

*Schwierigkeitsgrad: ⭐⭐⭐☆☆ (Mittel)*