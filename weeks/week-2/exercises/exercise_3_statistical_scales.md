# Übung 3: Statistische Skalen – Passende Skalen und Visualisierungen auswählen

## Lernziele
Nach dieser Übung kannst du:
- nominale, ordinale, intervallskalierte und ratioskalierte Variablen unterscheiden
- für verschiedene Variablentypen passende Visualisierungen auswählen
- lineare und logarithmische Skalen bewusst vergleichen
- Darstellungsentscheidungen fachlich begründen

---

## Kontext

Eine gute Visualisierung beginnt nicht mit dem Code, sondern mit einer konzeptionellen Entscheidung:

1. Welcher Datentyp liegt vor?
2. Was möchte ich zeigen – Verteilung, Vergleich oder Zusammenhang?
3. Welche Skala oder Darstellungsform ist dafür geeignet?

In dieser Übung verbindest du statistisches Denken mit Visualisierungspraxis.

---

## Datengrundlage

Nutze die Datensätze:

- `../datasets/student_performance.csv`
- `../datasets/online_retail_sample.csv`

### Beispiel zum Laden
```python
import pandas as pd

students = pd.read_csv("../datasets/student_performance.csv")
retail = pd.read_csv("../datasets/online_retail_sample.csv")
```

---

## Teil A: Variablen klassifizieren

Ordne die folgenden Variablen einem Skalenniveau zu:

| Variable | Datensatz | Deine Einordnung |
|----------|-----------|------------------|
| `semester` | student_performance | ? |
| `preparation_level` | student_performance | ? |
| `exam_score` | student_performance | ? |
| `study_hours` | student_performance | ? |
| `category` | online_retail_sample | ? |
| `customer_segment` | online_retail_sample | ? |
| `discount_pct` | online_retail_sample | ? |
| `revenue` | online_retail_sample | ? |

### Mögliche Kategorien
- nominal
- ordinal
- intervall
- ratio

---

## Teil B: Passende Plot-Typen auswählen

Wähle für jede der folgenden Analysefragen einen **geeigneten Plot-Typ** und begründe deine Wahl in 1–2 Sätzen.

1. Wie verteilen sich die `exam_score`-Werte?
2. Gibt es einen Zusammenhang zwischen `study_hours` und `exam_score`?
3. Unterscheiden sich die Umsätze nach `customer_segment`?
4. Welche Produktkategorien kommen wie häufig vor?
5. Wie entwickelt sich der Umsatz über die Zeit?

### Mögliche Plot-Typen
- Balkendiagramm
- Histogramm
- Scatter Plot
- Liniendiagramm
- Boxplot
- Violinplot

---

## Teil C: Linear vs. logarithmisch

Nutze `revenue` aus dem Retail-Datensatz und visualisiere die Verteilung zweimal:

1. mit einer **linearen Skala**
2. mit einer **logarithmischen Skala**

### Starter-Code
```python
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Linear
axes[0].hist(retail["revenue"], bins=12)
axes[0].set_title("Revenue – lineare Skala")

# Logarithmisch
axes[1].hist(retail["revenue"], bins=12)
axes[1].set_xscale("log")
axes[1].set_title("Revenue – logarithmische Skala")

plt.tight_layout()
plt.show()
```

### Analysefragen
Beantworte:
1. Welche Darstellung zeigt die Struktur der Daten besser?
2. Wann wäre eine logarithmische Skala sinnvoll?
3. Wann könnte sie irreführend oder erklärungsbedürftig sein?

---

## Teil D: Mini-Entscheidungsaufgabe

Für jede Situation: Entscheide dich für **einen Plot-Typ** und begründe deine Wahl.

### Situation 1
Du möchtest zeigen, wie viele Studierende in welchem `semester` sind.

### Situation 2
Du möchtest zeigen, ob höhere `attendance_rate` mit besseren `exam_score` zusammenhängt.

### Situation 3
Du möchtest die Verteilung von `discount_pct` untersuchen.

### Situation 4
Du möchtest den Median und die Streuung von `revenue` nach `customer_segment` vergleichen.

---

## Starter-Template für deine Antworten

```python
# Teil A: Skalenniveaus notieren
scale_levels = {
    "semester": "",
    "preparation_level": "",
    "exam_score": "",
    "study_hours": "",
    "category": "",
    "customer_segment": "",
    "discount_pct": "",
    "revenue": ""
}

# Teil B / D: Entscheidungen dokumentieren
answers = {
    "exam_score_distribution": {
        "plot": "",
        "reason": ""
    },
    "study_hours_vs_exam_score": {
        "plot": "",
        "reason": ""
    },
    "revenue_by_customer_segment": {
        "plot": "",
        "reason": ""
    }
}
```

---

## Erwartetes Ergebnis

Am Ende solltest du zeigen, dass du:

- Variablen fachlich sauber unterscheiden kannst
- Plot-Typen nicht zufällig auswählst
- die Wirkung von linearen und logarithmischen Skalen erklären kannst
- Visualisierungen argumentativ begründen kannst

---

## Hilfestellung

### Hinweise zu Skalenniveaus
- **Nominal:** Kategorien ohne Reihenfolge  
  Beispiel: Produktkategorie
- **Ordinal:** geordnete Kategorien  
  Beispiel: niedrig / mittel / hoch
- **Intervall:** Abstände sinnvoll, Nullpunkt nicht absolut  
  Beispiel: Temperatur in °C
- **Ratio:** Abstände sinnvoll und echter Nullpunkt vorhanden  
  Beispiel: Umsatz, Lernstunden

### Hinweise zu Plot-Wahl
- **Histogramm** → Verteilungen numerischer Variablen
- **Scatter Plot** → Beziehungen zwischen zwei numerischen Variablen
- **Balkendiagramm** → Häufigkeiten oder aggregierte Werte pro Kategorie
- **Liniendiagramm** → Entwicklungen über geordnete Zeitpunkte
- **Boxplot** → Median, Quartile, Streuung, Ausreißer

### Hinweise zu Log-Skalen
Eine logarithmische Skala ist sinnvoll, wenn:
- Werte stark schief verteilt sind
- große und kleine Werte gleichzeitig sichtbar sein sollen
- Größenordnungen wichtiger sind als absolute Unterschiede

---

## Bewertungsschema

| Kriterium | Punkte |
|----------|--------|
| Skalenniveaus korrekt erkannt | 4 |
| Plot-Typen passend ausgewählt | 4 |
| Begründungen fachlich überzeugend | 4 |
| Linear vs. Log sinnvoll verglichen | 3 |
| Antworten klar und strukturiert formuliert | 2 |

**Gesamt:** 17 Punkte

### Bewertungsrubrik
- **15–17 Punkte:** Sehr gut – konzeptionell stark, gut begründet, sauber formuliert
- **12–14 Punkte:** Gut – überwiegend korrekt mit kleineren Unsicherheiten
- **8–11 Punkte:** Befriedigend – Grundidee stimmt, Begründungen teils zu knapp
- **0–7 Punkte:** Überarbeiten – zentrale Konzepte noch unsicher

---

## Lösungshinweise

- `semester` und `category` sind nominal, weil keine natürliche Reihenfolge besteht.
- `preparation_level` ist ordinal, wenn Stufen wie „low“, „medium“, „high“ gemeint sind.
- `study_hours` und `revenue` sind typischerweise ratio-skaliert.
- Für Häufigkeiten von Kategorien ist ein Balkendiagramm sinnvoller als ein Histogramm.
- Für numerische Zusammenhänge ist ein Scatter Plot meistens die beste erste Wahl.
- Eine Log-Skala sollte immer erklärt werden, damit die Lesenden die Achse korrekt interpretieren.

---

## Bonus-Aufgaben

### Bonus 1
Erstelle eine kleine Tabelle:
**Fragestellung → Variablentyp → empfohlener Plot**

### Bonus 2
Zeige ein Beispiel für eine **ungeeignete** Plot-Wahl und erkläre, warum sie problematisch wäre.

### Bonus 3
Ergänze zum linearen/logarithmischen Vergleich einen kurzen Kommentar zur Lesbarkeit für ein nicht-technisches Publikum.

---

## Abgabe

Speichere deine Lösung als:
- Jupyter Notebook **oder**
- `exercise_3_solution.py`

**Empfohlene Bearbeitungszeit:** 20–25 Minuten

---

*Schwierigkeitsgrad: ⭐⭐⭐☆☆*