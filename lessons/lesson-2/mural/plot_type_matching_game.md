# Mural-Aktivität: Plot Type Matching Game

## Überblick

**Dauer:** 15–20 Minuten  
**Format:** Kollaborativ in Kleingruppen  
**Plattform:** [Mural.co](https://www.mural.co) oder [Miro](https://miro.com)  
**Lernziel:** Passende Plot-Typen für unterschiedliche Datensituationen auswählen und begründen

---

## Didaktischer Zweck

Diese Aktivität unterstützt Studierende dabei,

- Datensituationen genauer zu analysieren
- Variablentypen zu erkennen
- Plot-Typen nicht nur technisch, sondern konzeptionell auszuwählen
- Entscheidungen fachlich zu begründen
- Unterschiede zwischen Verteilung, Vergleich und Zusammenhang zu verstehen

Die Aktivität eignet sich besonders als Brücke zwischen:
- Seaborn-Basics
- statistischen Skalen
- Interpretationskompetenz

---

## Vorbereitung für Dozierende

### 1. Board anlegen
- Neues Board erstellen: **„Plot Type Matching Game – Lektion 2“**
- Freigabelink mit Bearbeitungsrechten vorbereiten
- Pro Gruppe einen Arbeitsbereich anlegen

### 2. Materialien auf dem Board vorbereiten
Lege auf dem Board drei Arten von Karten an:

#### A. Datensatzkarten
Kurze Beschreibungen realitätsnaher Datensituationen

#### B. Plot-Karten
Verschiedene Diagrammtypen als verschiebbare Karten

#### C. Begründungskarten
Leere Felder oder Sticky Notes für die Begründung:
- Datentyp
- Analyseziel
- warum passend / unpassend

---

## Durchführung

### Phase 1: Einführung (3 Min)

**Moderationstext:**
> „Ihr bekommt gleich mehrere kleine Datensituationen. Eure Aufgabe ist es, jeweils einen oder zwei passende Plot-Typen zuzuordnen. Entscheidend ist nicht nur die Wahl selbst, sondern eure Begründung:  
> Was möchtet ihr zeigen? Welcher Variablentyp liegt vor? Warum ist dieser Plot hier sinnvoll?“

### Phase 2: Matching in Gruppen (8–10 Min)
- Studierende arbeiten in Gruppen von 2–4 Personen
- Jede Gruppe ordnet Datensatzkarten passenden Plot-Karten zu
- Zusätzlich schreiben sie eine kurze Begründung auf Sticky Notes
- Optional markieren sie auch einen **ungeeigneten Plot-Typ**, um Fehlentscheidungen sichtbar zu machen

### Phase 3: Vergleich im Plenum (4–5 Min)
- 2–3 Gruppen stellen je ein Beispiel vor
- Dozentin/Dozent moderiert Unterschiede
- Fokus auf Begründung, nicht nur auf „richtig/falsch“

---

## Datensatzkarten (Vorlagen)

### Karte 1: Studienergebnisse
„Du hast Daten zu `study_hours` und `exam_score` von 60 Studierenden und möchtest wissen, ob mehr Lernzeit mit besseren Ergebnissen zusammenhängt.“

**Erwartbar passend:**
- Scatter Plot

**Mögliche Begründung:**
- zwei numerische Variablen
- Ziel ist ein Zusammenhang, kein reiner Vergleich

---

### Karte 2: Produktkategorien
„Du möchtest zeigen, wie viele Bestellungen auf die Kategorien Elektronik, Bücher, Kleidung und Haushalt entfallen.“

**Erwartbar passend:**
- Balkendiagramm

**Mögliche Begründung:**
- kategoriale Variable mit Häufigkeiten
- Ziel ist Vergleich zwischen Gruppen

---

### Karte 3: Umsatzverteilung
„Du möchtest untersuchen, wie sich `revenue` im Datensatz verteilt und ob es eher niedrige oder hohe Werte gibt.“

**Erwartbar passend:**
- Histogramm
- optional Boxplot

**Mögliche Begründung:**
- numerische Variable
- Ziel ist Verteilung sichtbar machen

---

### Karte 4: Kundensegmente
„Du möchtest `revenue` nach `customer_segment` vergleichen und dabei Median, Streuung und mögliche Ausreißer erkennen.“

**Erwartbar passend:**
- Boxplot
- Violinplot

**Mögliche Begründung:**
- numerische Werte nach Gruppen
- Fokus auf Verteilung pro Kategorie

---

### Karte 5: Zeitverlauf
„Du möchtest den Umsatz pro Monat darstellen, um Trends über die Zeit zu erkennen.“

**Erwartbar passend:**
- Liniendiagramm

**Mögliche Begründung:**
- geordnete Zeitachse
- Ziel ist Entwicklung oder Trend

---

### Karte 6: Vorbereitungstypen
„Die Variable `preparation_level` hat die Stufen low, medium und high. Du möchtest die Häufigkeit der drei Stufen zeigen.“

**Erwartbar passend:**
- geordnetes Balkendiagramm

**Mögliche Begründung:**
- ordinale Kategorien
- Reihenfolge sollte sichtbar bleiben

---

### Karte 7: Zwei Perspektiven auf dieselben Daten
„Du möchtest die Verteilung von `exam_score` und zusätzlich Unterschiede zwischen Semestern zeigen.“

**Erwartbar passend:**
- Histogramm + Boxplot
- alternativ Histogramm + Balkendiagramm aggregierter Mittelwerte

**Mögliche Begründung:**
- eine Visualisierung reicht oft nicht
- Verteilung und Gruppenvergleich sind unterschiedliche Analyseziele

---

## Plot-Karten (Vorlagen)

Erstelle verschiebbare Karten mit diesen Bezeichnungen:

- Scatter Plot
- Liniendiagramm
- Balkendiagramm
- Histogramm
- Boxplot
- Violinplot
- Stripplot

### Optional: Karten „eher ungeeignet“
- Pie Chart
- 3D-Bar-Chart
- Heatmap

Diese Karten können für Diskussionszwecke eingebaut werden.

---

## Begründungskarten

Jede Gruppe soll zu jeder Zuordnung mindestens eine kurze Begründung notieren.

### Vorlage
- **Variablentyp:** nominal / ordinal / numerisch
- **Ziel:** Verteilung / Vergleich / Zusammenhang / Entwicklung
- **Warum passend:** ...
- **Warum ggf. ungeeignet:** ...

---

## Mural-Board-Template

```text
┌────────────────────────────────────────────────────────────────────┐
│ Plot Type Matching Game – Lektion 2                               │
│ Wählt für jede Datensituation einen passenden Plot-Typ            │
├────────────────────────────────────────────────────────────────────┤
│ Gruppe A                 │ Gruppe B                 │ Gruppe C     │
│                          │                          │              │
│ [Datensatzkarte 1]       │ [Datensatzkarte 1]       │ [Datensatz]  │
│ [Plot-Karten]            │ [Plot-Karten]            │ [Plot-K.]    │
│ [Begründung]             │ [Begründung]             │ [Begründung] │
│                          │                          │              │
│ [Datensatzkarte 2]       │ [Datensatzkarte 2]       │ [Datensatz]  │
│ [Plot-Karten]            │ [Plot-Karten]            │ [Plot-K.]    │
│ [Begründung]             │ [Begründung]             │ [Begründung] │
├────────────────────────────────────────────────────────────────────┤
│ Gemeinsame Reflexion:                                            │
│ - Welche Fälle waren eindeutig?                                  │
│ - Wo gab es mehrere gute Lösungen?                               │
│ - Welche Fehlentscheidungen sind typisch?                        │
└────────────────────────────────────────────────────────────────────┘
```

---

## Facilitation Guide für Dozierende

### Beobachtungsschwerpunkte während der Gruppenarbeit
Achte darauf, ob Studierende:
- Datentyp und Analyseziel sauber trennen
- Plot-Typen wegen Gewohnheit statt Begründung wählen
- numerische und kategoriale Variablen korrekt unterscheiden
- mehrere sinnvolle Lösungen akzeptieren können

### Gute Nachfragen in der Moderation
- „Was genau möchtet ihr zeigen – Verteilung oder Zusammenhang?“
- „Welche Variable ist hier numerisch, welche kategorial?“
- „Warum ist ein Boxplot hier informativer als ein Balkendiagramm?“
- „Würde ein Liniendiagramm hier etwas suggerieren, was gar nicht gegeben ist?“
- „Braucht ihr einen Plot oder vielleicht zwei unterschiedliche?“

### Typische Fehlkonzepte
- Balkendiagramm für alles verwenden
- Liniendiagramm bei ungeordneten Kategorien einsetzen
- Verteilung und Mittelwert verwechseln
- Scatter Plot bei kategorialen Häufigkeiten nutzen
- Plot-Wahl nach Ästhetik statt Analyseziel treffen

---

## Erwartete Lernmomente

Nach der Aktivität sollten Studierende besser verstehen:

1. dass Plot-Auswahl von der Fragestellung abhängt
2. dass nicht jede numerische Variable gleich behandelt wird
3. dass kategoriale und numerische Daten unterschiedlich visualisiert werden
4. dass oft mehrere sinnvolle Visualisierungen existieren – aber aus unterschiedlichen Gründen

---

## Debrief im Plenum

### Leitfragen
1. Welche Datensatzkarte war am einfachsten?
2. Wo gab es Diskussionen oder mehrere gute Lösungen?
3. Welche Plot-Typen wurden zu schnell gewählt?
4. Wann braucht man eher einen Verteilungsplot als einen Vergleichsplot?

### Abschlussbotschaft
> „Gute Visualisierung beginnt nicht mit dem Tool, sondern mit der Frage: Welche Information soll sichtbar werden?“

---

## Varianten

### Variante 1: Wettbewerb
- Gruppen erhalten Punkte für passende Zuordnung + gute Begründung

### Variante 2: Fehlersuche
- Gruppen müssen zusätzlich einen bewusst unpassenden Plot identifizieren

### Variante 3: Skalenniveau-Fokus
- Jede Begründung muss explizit das Skalenniveau benennen

---

## Alternative ohne Mural

### Option 1: Ausdrucke + Karten
- Datensatzkarten und Plot-Karten ausdrucken
- Gruppen ordnen sie auf dem Tisch

### Option 2: Whiteboard
- Datensituationen an die Tafel schreiben
- Zuordnungen gemeinsam sammeln

### Option 3: Breakout-Rooms + geteiltes Dokument
- Jede Gruppe arbeitet in einem gemeinsamen Online-Dokument
- Ergebnisse werden anschließend verglichen

---

## Verbindung zur Hausaufgabe

Die Aktivität bereitet direkt auf die Hausaufgabe vor:
- passende Diagramme auswählen
- Entscheidungen begründen
- Datentypen mit Analysezielen verbinden

---

*Erstellt für HsH Data Visualization Kurs – April 2026*