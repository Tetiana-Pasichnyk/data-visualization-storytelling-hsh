# Übung 1: Matplotlib Basics – Multi-Panel Figure erstellen

## Lernziele
Nach dieser Übung kannst du:
- mit `matplotlib` mehrere Plots in einer gemeinsamen Figur anordnen
- die Figure-Axes-Struktur praktisch anwenden
- grundlegende Plot-Typen passend einsetzen
- Achsen, Titel, Legenden und Layout gezielt verbessern

---

## Kontext

In vielen realen Projekten reicht ein einzelnes Diagramm nicht aus. Häufig müssen mehrere Perspektiven auf denselben Datensatz gleichzeitig gezeigt werden, zum Beispiel:

- Entwicklung über die Zeit
- Zusammenhang zwischen zwei Variablen
- Vergleich zwischen Kategorien
- Verteilung einer numerischen Variable

Genau dafür sind **Subplots** besonders wichtig.

---

## Datengrundlage

Verwende den Datensatz `../datasets/student_performance.csv`.

### Beispiel zum Laden
```python
import pandas as pd

df = pd.read_csv("../datasets/student_performance.csv")
df.head()
```

### Verfügbare Spalten
- `student_id`
- `study_hours`
- `exam_score`
- `attendance_rate`
- `semester`
- `preparation_level`

---

## Aufgabenstellung

Erstelle eine **2×2-Multi-Panel-Figur** mit Matplotlib.

### Anforderungen

#### Plot 1: Liniendiagramm
Zeige die Entwicklung der `exam_score` über die `student_id`.

#### Plot 2: Scatter Plot
Zeige den Zusammenhang zwischen `study_hours` und `exam_score`.

#### Plot 3: Balkendiagramm
Vergleiche den **durchschnittlichen Exam Score pro Semester**.

#### Plot 4: Histogramm
Zeige die Verteilung von `attendance_rate`.

---

## Zusätzliche Anforderungen

Deine Figur soll außerdem:

1. eine sinnvolle `figsize` haben
2. für jeden Teilplot einen Titel haben
3. Achsenbeschriftungen enthalten
4. bei Bedarf eine Legende enthalten
5. mit `tight_layout()` lesbar angeordnet sein
6. als Datei gespeichert werden, z. B. als `exercise_1_multipanel.png`

---

## Starter-Code

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../datasets/student_performance.csv")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Plot 1: Liniendiagramm
# DEIN CODE HIER

# Plot 2: Scatter Plot
# DEIN CODE HIER

# Plot 3: Balkendiagramm
# DEIN CODE HIER

# Plot 4: Histogramm
# DEIN CODE HIER

plt.tight_layout()
plt.savefig("exercise_1_multipanel.png", dpi=300)
plt.show()
```

---

## Schritt-für-Schritt Hinweise

### Teil A: Liniendiagramm
Nutze z. B.:
```python
axes[0, 0].plot(df["student_id"], df["exam_score"])
```

### Teil B: Scatter Plot
Nutze z. B.:
```python
axes[0, 1].scatter(df["study_hours"], df["exam_score"], alpha=0.7)
```

### Teil C: Balkendiagramm
Bilde zuerst einen Mittelwert pro `semester`:
```python
mean_scores = df.groupby("semester")["exam_score"].mean()
```

### Teil D: Histogramm
Nutze z. B.:
```python
axes[1, 1].hist(df["attendance_rate"], bins=10)
```

---

## Erwartetes Ergebnis

Deine Abbildung sollte:
- vier klar getrennte Teilplots enthalten
- gut lesbare Beschriftungen haben
- unterschiedliche Blickwinkel auf denselben Datensatz zeigen
- professionell und aufgeräumt wirken

**Inhaltlich erwartbar:**
- mehr Lernstunden führen tendenziell zu besseren Ergebnissen
- es können Unterschiede zwischen Semestern sichtbar werden
- die Anwesenheit zeigt eine Verteilung statt eines Vergleichs oder Zusammenhangs

---

## Reflexionsfragen

Beantworte kurz im Notebook oder als Kommentar:

1. Welcher der vier Plot-Typen war am einfachsten umzusetzen?
2. Welcher Plot liefert die wichtigste Information?
3. Warum ist ein Histogramm für `attendance_rate` sinnvoll?
4. Warum ist ein Scatter Plot besser geeignet als ein Balkendiagramm für `study_hours` vs. `exam_score`?

---

## Bewertungsschema

| Kriterium | Punkte |
|----------|--------|
| 2×2-Layout korrekt erstellt | 2 |
| Alle vier geforderten Plot-Typen vorhanden | 4 |
| Titel und Achsenbeschriftungen korrekt | 3 |
| Daten fachlich passend dargestellt | 3 |
| Layout sauber und lesbar | 2 |
| Datei gespeichert und sinnvoll benannt | 1 |
| Code ist verständlich strukturiert | 1 |

**Gesamt:** 16 Punkte

### Bewertungsrubrik
- **14–16 Punkte:** Sehr gut – fachlich korrekt, sauber gestaltet, gut lesbar
- **11–13 Punkte:** Gut – kleine Mängel, aber insgesamt überzeugend
- **8–10 Punkte:** Befriedigend – zentrale Anforderungen erfüllt, aber unvollständig oder unklar
- **0–7 Punkte:** Überarbeiten – mehrere Anforderungen fehlen oder sind fachlich problematisch

---

## Lösungshinweise

- Verwende `fig, axes = plt.subplots(...)` statt mehrere einzelne Figuren zu erzeugen.
- Greife auf einzelne Achsen mit `axes[0, 0]`, `axes[0, 1]` usw. zu.
- Wenn Beschriftungen überlappen, erhöhe `figsize` oder nutze `tight_layout()`.
- Verwende für das Balkendiagramm aggregierte Daten, nicht die Rohdaten.
- Achte darauf, dass ein Plot-Typ zur Fragestellung passt:
  - Entwicklung → Linie
  - Zusammenhang → Scatter
  - Vergleich → Balken
  - Verteilung → Histogramm

---

## Bonus-Aufgaben

### Bonus 1
Färbe den Scatter Plot nach `semester`.

### Bonus 2
Ergänze im Histogramm eine vertikale Linie für den Mittelwert.

### Bonus 3
Optimiere die Figur im Tufte-Stil:
- unnötige Rahmen entfernen
- nur dezente Gridlines
- konsistente Farben verwenden

---

## Abgabe

Speichere deine Lösung als:
- Jupyter Notebook **oder**
- `exercise_1_solution.py`

**Empfohlene Bearbeitungszeit:** 20–25 Minuten

---

*Schwierigkeitsgrad: ⭐⭐☆☆☆*