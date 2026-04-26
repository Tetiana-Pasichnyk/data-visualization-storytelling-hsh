# Übung 1: Scatter Plot erstellen

## Lernziele
- Matplotlib UND Seaborn für denselben Plot verwenden
- Unterschiede zwischen beiden Bibliotheken verstehen
- Daten aus Pandas DataFrame visualisieren

---

## Aufgabenstellung

Erstelle einen Scatter Plot, der die Beziehung zwischen zwei Variablen zeigt.

### Gegeben: Datensatz

```python
import pandas as pd
import numpy as np

# Datensatz erstellen
np.random.seed(42)
df = pd.DataFrame({
    'study_hours': np.random.uniform(0, 10, 50),
    'exam_score': np.random.uniform(40, 100, 50),
    'semester': np.random.choice(['WS', 'SS'], 50)
})

# Korrelation hinzufügen
df['exam_score'] = 40 + 5 * df['study_hours'] + np.random.normal(0, 10, 50)
df['exam_score'] = df['exam_score'].clip(0, 100)
```

### Teil A: Mit Matplotlib (10 Min)

Erstelle einen Scatter Plot mit Matplotlib, der:
1. `study_hours` auf der x-Achse zeigt
2. `exam_score` auf der y-Achse zeigt
3. Nach `semester` färbt (WS = blau, SS = orange)
4. Achsenbeschriftungen hat
5. Einen Titel hat
6. Eine Legende hat

**Starter-Code:**
```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 6))

# DEIN CODE HIER

plt.show()
```

### Teil B: Mit Seaborn (5 Min)

Erstelle denselben Plot mit Seaborn.

**Starter-Code:**
```python
import seaborn as sns

fig, ax = plt.subplots(figsize=(10, 6))

# DEIN CODE HIER (sollte viel kürzer sein!)

plt.show()
```

### Teil C: Vergleich (5 Min)

Beantworte diese Fragen:
1. Wie viele Zeilen Code brauchtest du für Matplotlib?
2. Wie viele Zeilen Code brauchtest du für Seaborn?
3. Welche Version findest du einfacher? Warum?
4. Welche Version sieht besser aus? Warum?

---

## Bonus-Aufgaben

### Bonus 1: Regression Line
Füge eine Regressionslinie hinzu (Tipp: `sns.regplot`)

### Bonus 2: Größe
Lass die Punktgröße von einer dritten Variable abhängen

### Bonus 3: Tufte-Style
Verbessere den Plot nach Tufte-Prinzipien:
- Entferne unnötige Elemente
- Verwende direkte Beschriftungen statt Legende
- Maximiere Data-Ink Ratio

---

## Hilfestellung

### Matplotlib Scatter Plot
```python
# Für jede Gruppe separat plotten
for semester in df['semester'].unique():
    mask = df['semester'] == semester
    ax.scatter(df[mask]['study_hours'], 
               df[mask]['exam_score'],
               label=semester)
```

### Seaborn Scatter Plot
```python
# Alles in einer Zeile!
sns.scatterplot(data=df, x='study_hours', y='exam_score', 
                hue='semester', ax=ax)
```

---

## Erwartetes Ergebnis

Dein Plot sollte zeigen:
- Positive Korrelation zwischen Lernstunden und Punktzahl
- Zwei verschiedene Farben für WS und SS
- Klare Achsenbeschriftungen
- Professionelles Aussehen

---

## Abgabe

Speichere deinen Code als `exercise_1_solution.py` oder in einem Jupyter Notebook.

**Deadline:** Ende der Übungszeit (15 Min)

---

*Schwierigkeitsgrad: ⭐⭐☆☆☆ (Einfach)*