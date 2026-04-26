# Mentimeter Abschluss-Quiz – Lektion 2

## Quiz-Setup

**Typ:** Quiz-Modus in Mentimeter  
**Dauer:** 10–12 Minuten  
**Zweck:** Wissensüberprüfung zu Matplotlib, Seaborn, Plot-Auswahl und statistischen Skalen

### Hinweise für Dozierende
- Fragen möglichst im Quiz-Modus anlegen
- Antwortzeit pro Frage auf 20–30 Sekunden setzen
- nach jeder Frage die Erklärung kurz besprechen
- Fehlannahmen direkt an Beispielen aufgreifen

---

## Frage 1: Figure und Axes

**Frage:** „Welche Aussage beschreibt den Unterschied zwischen Figure und Axes am besten?“

### Optionen
- A) Die Figure ist immer nur der Titel eines Diagramms
- B) Axes sind nur für 3D-Plots nötig
- C) Die Figure ist der gesamte Rahmen, Axes sind die einzelnen Zeichenflächen ✓
- D) Figure und Axes bedeuten in Matplotlib dasselbe

### Richtige Antwort
**C**

### Erklärung
Die Figure ist das gesamte Container-Objekt. Axes sind die Bereiche, auf denen tatsächlich geplottet wird.

### Zeit
20 Sekunden

---

## Frage 2: Multi-Panel-Figur

**Frage:** „Welche Funktion wird typischerweise verwendet, um mehrere Teilplots in einer Figur zu erzeugen?“

### Optionen
- A) `plt.subplots()` ✓
- B) `plt.legend()`
- C) `plt.savefig()`
- D) `plt.grid()`

### Richtige Antwort
**A**

### Erklärung
Mit `plt.subplots()` lassen sich Figure und ein oder mehrere Axes-Objekte in einem Schritt erzeugen.

### Zeit
20 Sekunden

---

## Frage 3: Geeigneter Plot-Typ

**Frage:** „Welcher Plot eignet sich am besten, um den Zusammenhang zwischen zwei numerischen Variablen zu zeigen?“

### Optionen
- A) Histogramm
- B) Scatter Plot ✓
- C) Balkendiagramm
- D) Boxplot

### Richtige Antwort
**B**

### Erklärung
Scatter Plots zeigen Beziehungen, Streuung, Ausreißer und mögliche Muster zwischen zwei numerischen Variablen.

### Zeit
20 Sekunden

---

## Frage 4: Seaborn-Vorteil

**Frage:** „Was ist ein typischer Vorteil von Seaborn gegenüber reinem Matplotlib?“

### Optionen
- A) Seaborn funktioniert ohne Python
- B) Seaborn bietet gute statistische Plots und schöne Defaults ✓
- C) Seaborn kann keine Farben nutzen
- D) Seaborn ersetzt Pandas vollständig

### Richtige Antwort
**B**

### Erklärung
Seaborn baut auf Matplotlib auf und macht viele statistische Visualisierungen mit weniger Code und guten Standardstilen einfacher.

### Zeit
20 Sekunden

---

## Frage 5: Kategorialer Vergleich

**Frage:** „Welcher Plot ist besonders nützlich, wenn du Median, Quartile und Ausreißer zwischen Gruppen vergleichen möchtest?“

### Optionen
- A) Boxplot ✓
- B) Histogramm
- C) Liniendiagramm
- D) Pie Chart

### Richtige Antwort
**A**

### Erklärung
Ein Boxplot zeigt zentrale Lage, Streuung und potenzielle Ausreißer kompakt und ist für Gruppenvergleiche sehr geeignet.

### Zeit
20 Sekunden

---

## Frage 6: Skalenniveau

**Frage:** „Welches Skalenniveau hat eine Variable wie `preparation_level` mit den Ausprägungen low, medium, high?“

### Optionen
- A) Nominal
- B) Ordinal ✓
- C) Intervall
- D) Ratio

### Richtige Antwort
**B**

### Erklärung
Die Werte besitzen eine sinnvolle Reihenfolge, aber die Abstände zwischen den Stufen sind nicht exakt messbar.

### Zeit
20 Sekunden

---

## Frage 7: Ratio-Skala

**Frage:** „Welche der folgenden Variablen ist typischerweise ratio-skaliert?“

### Optionen
- A) Produktkategorie
- B) Kundensegment
- C) Umsatz in Euro ✓
- D) Zufriedenheitsstufe niedrig/mittel/hoch

### Richtige Antwort
**C**

### Erklärung
Umsatz besitzt einen echten Nullpunkt und sinnvolle Verhältnisse. 200 € sind tatsächlich doppelt so viel wie 100 €.

### Zeit
20 Sekunden

---

## Frage 8: Logarithmische Skala

**Frage:** „Wann ist eine logarithmische Skala besonders sinnvoll?“

### Optionen
- A) Wenn Daten starke Größenordnungsunterschiede oder eine schiefe Verteilung haben ✓
- B) Immer bei Balkendiagrammen
- C) Nur wenn der Plot schöner aussehen soll
- D) Wenn Kategorien alphabetisch sortiert sind

### Richtige Antwort
**A**

### Erklärung
Log-Skalen helfen, große und kleine Werte gleichzeitig sichtbar zu machen, besonders bei stark schiefen oder exponentiellen Daten.

### Zeit
20 Sekunden

---

## Frage 9: Best Practice Plot-Wahl

**Frage:** „Welche Zuordnung ist am sinnvollsten?“

### Optionen
- A) Verteilung numerischer Werte → Histogramm ✓
- B) Zusammenhang zweier numerischer Variablen → Balkendiagramm
- C) Häufigkeit von Kategorien → Scatter Plot
- D) Gruppenvergleich von Medianen → Liniendiagramm

### Richtige Antwort
**A**

### Erklärung
Histogramme sind ein Standardwerkzeug für Verteilungen numerischer Variablen. Die anderen Zuordnungen passen fachlich nicht gut.

### Zeit
20 Sekunden

---

## Frage 10: Kombination von Tools

**Frage:** „Welche Arbeitsweise ist oft am sinnvollsten?“

### Optionen
- A) Nur Matplotlib verwenden
- B) Nur Seaborn verwenden
- C) Seaborn für schnellen Plot, Matplotlib für Feintuning ✓
- D) Nie beide Bibliotheken zusammen einsetzen

### Richtige Antwort
**C**

### Erklärung
In der Praxis ist die Kombination besonders stark: Seaborn liefert schnell gute statistische Plots, Matplotlib übernimmt Feinanpassungen und Layoutkontrolle.

### Zeit
20 Sekunden

---

## Auswertung

### Orientierung für die Ergebnisse
- **9–10 richtige Antworten:** Sehr sicherer Umgang mit den Grundlagen
- **7–8 richtige Antworten:** Gute Basis, einzelne Konzepte festigen
- **5–6 richtige Antworten:** Zentrale Inhalte verstanden, Wiederholung sinnvoll
- **0–4 richtige Antworten:** Inhalte noch einmal mit Übungen und Demo-Notebook durchgehen

---

## Nachbesprechung im Unterricht

### Leitfragen
- Welche Frage war am schwierigsten?
- Wo besteht noch Unsicherheit: Plot-Wahl, Skalen oder Tool-Unterschiede?
- Welche Entscheidung fällt euch jetzt leichter als vor der Lektion?

### Didaktischer Übergang
Nutze die Nachbesprechung als Brücke zur Hausaufgabe:
- passende Visualisierung wählen
- fachlich begründen
- Interpretation sauber formulieren

---

## Alternative ohne Mentimeter

Falls Mentimeter nicht verfügbar ist:

### Option 1: Papier-Quiz
- Fragen ausdrucken
- Antworten einzeln oder in Zweiergruppen bearbeiten

### Option 2: Moodle-Test
- automatisch auswertbar
- gut für asynchrone Wiederholung

### Option 3: Kurzquiz im Plenum
- Antwortkarten A/B/C/D
- schnelle gemeinsame Besprechung

---

*Erstellt für HsH Data Visualization Kurs – April 2026*