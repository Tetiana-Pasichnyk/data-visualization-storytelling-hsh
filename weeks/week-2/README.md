# Lektion 2: Datenrepräsentationen & Seaborn I

## Überblick

**Dauer:** 270 Minuten (3 × 90 Minuten)  
**Format:** Präsenz oder Hybrid  
**Block:** 2 – Datenrepräsentationen & Seaborn I  

**Übergeordnete Lernziele:**
1. Die Figure-Axes-Architektur von Matplotlib verstehen und anwenden
2. Mit Matplotlib grundlegende Plot-Typen sicher erstellen und anpassen
3. Seaborn für statistische Visualisierungen mit sinnvollen Standards nutzen
4. Datentypen und Skalenniveaus korrekt erkennen und passende Visualisierungen auswählen
5. Visualisierungen fachlich interpretieren und typische Darstellungsfehler vermeiden

---

## Bezug zum Kurs

Diese Lektion vertieft die Grundlagen aus Block 1 und bereitet auf spätere Blöcke zu spezialisierten Visualisierungen, Storytelling und Dashboarding vor. Sie knüpft insbesondere an das bestehende Notebook `matplotlib_vs_seaborn.ipynb` an und erweitert es um:

- Figure- und Axes-Denken in Matplotlib
- Multi-Panel-Figuren und Layouts
- statistische Standardplots mit Seaborn
- Zusammenhang zwischen Datentyp, Skalenniveau und Visualisierung

---

## Ablaufplan gesamt

| Einheit | Thema | Dauer | Schwerpunkt |
|--------|-------|-------|-------------|
| 2.1 | Matplotlib Einführung | 90 Min | Figure, Axes, Basisplots, Layouts |
| 2.2 | Seaborn Basics | 90 Min | Statistische Plots, Themes, Kategorien |
| 2.3 | Statistische Skalen & Interpretation | 90 Min | Nominal, Ordinal, Intervall, Ratio, Plot-Wahl |

---

## Einheit 2.1: Matplotlib Einführung (90 Min)

### Lernziele
Nach dieser Einheit können die Studierenden:
- den Unterschied zwischen Figure und Axes erklären
- einfache Diagramme mit Matplotlib erstellen
- Achsen, Titel, Farben und Legenden anpassen
- Subplots für mehrere Visualisierungen in einer Figur nutzen
- Grafiken in geeigneten Formaten exportieren

### Zeitplan

#### 1. Aktivierung (10 Min)
- Kurze Rückfrage: Welche Diagrammtypen wurden bisher am häufigsten gesehen?
- Mini-Austausch: Wann reicht ein einfacher Plot und wann braucht man mehrere Ansichten?
- Verweis auf das bekannte Vergleichsnotebook `matplotlib_vs_seaborn.ipynb`

#### 2. Theorie (25 Min)
**Inhaltliche Schwerpunkte:**
- Was ist eine `Figure`?
- Was ist ein `Axes`-Objekt?
- Unterschied zwischen State-based API und Object-oriented API
- Basisplots:
  - Liniendiagramm
  - Scatter Plot
  - Balkendiagramm
  - Histogramm
- Plot-Anpassung:
  - Farben
  - Marker
  - Linienstile
  - Titel und Achsenbeschriftungen
  - Legenden
- Layout:
  - `plt.subplots()`
  - mehrere Achsen in einem Raster
  - `tight_layout()`
- Export:
  - PNG für Präsentationen
  - SVG/PDF für hochwertige Vektorformate

#### 3. Live-Coding Demonstration (20 Min)
**Demo-Ablauf:**
1. Einfachen Line Plot mit `fig, ax = plt.subplots()` erstellen
2. Beschriftungen, Titel und Legende ergänzen
3. Einen Scatter Plot hinzufügen
4. Ein 2×2-Subplot-Grid erzeugen
5. Vier Plot-Typen in einer Figur kombinieren
6. Grafik mit `savefig()` speichern

**Live-Coding-Ziele:**
- Denken in Axes statt nur in globalen `plt`-Befehlen
- Wiederverwendbarkeit von Code
- Lesbarkeit des Plots verbessern

#### 4. Praxis (25 Min)
- Bearbeitung von `exercises/exercise_1_matplotlib_basics.md`
- Arbeitsform: Partnerarbeit oder Einzelarbeit
- Fokus:
  - Multi-Panel-Figur
  - geeignete Achsenbeschriftungen
  - sauberer Aufbau und konsistente Gestaltung

#### 5. Überprüfung / Sicherung (10 Min)
- Zwei bis drei Lösungen kurz zeigen
- Häufige Fehler besprechen:
  - Achsen verwechselt
  - fehlende Labels
  - zu kleine Schrift
  - unpassende Farben oder Legenden
- Merksatz formulieren:
  - „Die Figure ist der Rahmen, die Axes sind die eigentlichen Zeichenflächen.“

### Materialien für Einheit 2.1
- Notebook-Referenz: `../../notebooks/matplotlib_vs_seaborn.ipynb`
- Demo-Spezifikation: `notebooks/matplotlib_seaborn_intro.ipynb`
- Übung: `exercises/exercise_1_matplotlib_basics.md`
- Datensätze:
  - `datasets/student_performance.csv`
  - `datasets/online_retail_sample.csv`

---

## Einheit 2.2: Seaborn Basics (90 Min)

### Lernziele
Nach dieser Einheit können die Studierenden:
- erklären, warum Seaborn auf Matplotlib aufbaut
- typische Seaborn-Plot-Typen für Verteilungen und Zusammenhänge auswählen
- kategoriale und statistische Plots interpretieren
- Themes und Styles sinnvoll einsetzen
- Seaborn-Plots mit Matplotlib nachbearbeiten

### Zeitplan

#### 1. Aktivierung (10 Min)
- Mentimeter-Impuls: „Wann würdest du Matplotlib, wann Seaborn verwenden?“
- Kurzgespräch zu Lesbarkeit, Geschwindigkeit und Standarddesign

#### 2. Theorie (25 Min)
**Inhaltliche Schwerpunkte:**
- Warum Seaborn?
  - statistischer Fokus
  - schöne Default-Einstellungen
  - gute Integration mit Pandas
- Relationale Plots:
  - `scatterplot()`
  - `lineplot()`
- Verteilungsplots:
  - `histplot()`
  - optional: KDE als Ergänzung
- Kategoriale Plots:
  - `barplot()`
  - `boxplot()`
  - `violinplot()`
  - `stripplot()`
- Styling:
  - `set_theme()`
  - `set_style()`
  - Farbpaletten
- Kombination mit Matplotlib:
  - Titel, Achsenbegrenzungen, Annotationen, Export

#### 3. Live-Coding Demonstration (20 Min)
**Demo-Ablauf:**
1. Dataset laden
2. `sns.set_theme(style="whitegrid")` anwenden
3. Histogramm und Scatter Plot erzeugen
4. Boxplot und Violinplot vergleichen
5. Ein Seaborn-Plot mit Matplotlib-Achsentitel und `ax.axhline()` ergänzen
6. Kurz diskutieren: Welcher Plot zeigt welche Information am besten?

#### 4. Praxis (25 Min)
- Bearbeitung von `exercises/exercise_2_seaborn_statistical_plots.md`
- Ziel:
  - Verteilungen visualisieren
  - Beziehungen zwischen Variablen zeigen
  - einen kategorialen Vergleich ergänzen
  - kurze Interpretation notieren

#### 5. Überprüfung / Sicherung (10 Min)
- Ergebnisvergleich im Plenum
- Leitfragen:
  - Was zeigt ein Boxplot, was ein Histogramm nicht direkt zeigt?
  - Wann kann ein Violinplot hilfreich sein?
  - Warum ist „schön“ nicht automatisch „richtig“?

### Materialien für Einheit 2.2
- Notebook-Referenz: `../../notebooks/matplotlib_vs_seaborn.ipynb`
- Demo-Spezifikation: `notebooks/matplotlib_seaborn_intro.ipynb`
- Übung: `exercises/exercise_2_seaborn_statistical_plots.md`
- Datensätze:
  - `datasets/student_performance.csv`
  - `datasets/online_retail_sample.csv`
  - externer Referenzdatensatz laut `datasets/README.md`

---

## Einheit 2.3: Statistische Skalen & Interpretation (90 Min)

### Lernziele
Nach dieser Einheit können die Studierenden:
- nominale, ordinale, intervallskalierte und ratioskalierte Variablen unterscheiden
- für verschiedene Datentypen passende Diagrammformen auswählen
- lineare und logarithmische Skalen bewusst einsetzen
- typische Fehlinterpretationen in Visualisierungen erkennen
- Ergebnisse präzise und fachlich korrekt beschreiben

### Zeitplan

#### 1. Aktivierung (10 Min)
- Kurzes Matching im Plenum: Variablentyp → sinnvolle Visualisierung
- Beispiele:
  - Studiengang
  - Kundenzufriedenheit 1–5
  - Temperatur in °C
  - Umsatz in Euro

#### 2. Theorie (25 Min)
**Inhaltliche Schwerpunkte:**
- Skalenniveaus:
  - nominal
  - ordinal
  - intervall
  - ratio
- Was darf man mit welchem Skalenniveau sinnvoll tun?
- Geeignete Diagramme:
  - nominal → Balkendiagramm
  - ordinal → geordnete Balkendiagramme / Punktdiagramme
  - intervall → Histogramm, Linie, Scatter je nach Fragestellung
  - ratio → Histogramm, Scatter, Boxplot, Log-Skalen bei Bedarf
- Interpretation:
  - Verteilung vs. Vergleich vs. Zusammenhang
  - Gefahr falscher Achsenskalierung
  - Problematische abgeschnittene Achsen
  - Log-Skalen nur mit Begründung
  - Korrelation ist nicht Kausalität

#### 3. Live-Coding Demonstration (20 Min)
**Demo-Ablauf:**
1. Variablen im Datensatz klassifizieren
2. Für jede Variable eine passende Darstellungsform auswählen
3. Dieselbe ratio-skalierte Variable einmal linear und einmal logarithmisch darstellen
4. Unterschiede in der Interpretation besprechen
5. Beispiel für eine irreführende Darstellung zeigen und verbessern

#### 4. Praxis (25 Min)
- Bearbeitung von `exercises/exercise_3_statistical_scales.md`
- Arbeitsauftrag:
  - Variablen einordnen
  - passende Visualisierungen auswählen
  - lineare vs. logarithmische Darstellung vergleichen
  - Entscheidungen begründen

#### 5. Überprüfung / Sicherung (10 Min)
- Mini-Quiz oder Kurzabfrage
- Sammlung häufiger Fehlannahmen:
  - „Jede Zahl ist automatisch intervall- oder ratioskaliert“
  - „Mehr Farbe bedeutet mehr Information“
  - „Log-Skalen darf man immer verwenden“
- Abschluss-Merksatz:
  - „Die beste Visualisierung hängt von Fragestellung, Datentyp und Interpretationsziel ab.“

### Materialien für Einheit 2.3
- Demo-Spezifikation: `notebooks/matplotlib_seaborn_intro.ipynb`
- Übung: `exercises/exercise_3_statistical_scales.md`
- Mural-Aktivität: `mural/plot_type_matching_game.md`
- Datensätze:
  - `datasets/student_performance.csv`
  - `datasets/online_retail_sample.csv`

---

## Übungen

### Pflichtübungen
1. `exercises/exercise_1_matplotlib_basics.md`
2. `exercises/exercise_2_seaborn_statistical_plots.md`
3. `exercises/exercise_3_statistical_scales.md`

### Empfohlene Bearbeitungsreihenfolge
1. Zuerst Struktur und Achsen mit Matplotlib verstehen
2. Dann mit Seaborn statistische Plot-Typen vergleichen
3. Zum Schluss Plot-Auswahl mit Skalenniveaus begründen

---

## Mentimeter

### Einsatz im Unterricht
- **Aktivierungsfragen:** `mentimeter/activation_questions.md`
- **Abschluss-Quiz:** `mentimeter/quiz_questions.md`

**Didaktische Funktion:**
- Vorwissen und Unsicherheiten sichtbar machen
- Diskussionen strukturieren
- Lernfortschritt schnell überprüfen
- Fehlkonzepte früh erkennen

---

## Kollaborative Aktivität (Mural)

**Datei:** `mural/plot_type_matching_game.md`

**Ziel:**
Studierende ordnen Datensituationen passenden Plot-Typen zu und begründen ihre Wahl. So wird sichtbar, dass Visualisierung kein reines „Tool-Thema“, sondern eine konzeptionelle Entscheidung ist.

---

## Datensätze

### Lokale Datensätze
- `datasets/student_performance.csv`
- `datasets/online_retail_sample.csv`

### Datensatz-Dokumentation
- `datasets/README.md`

**Hinweis:** Zusätzlich wird ein externer Referenzdatensatz dokumentiert, damit Studierende mit realistischeren Datenstrukturen weiterarbeiten können.

---

## Notebook-Spezifikationen

### 1. Demo-Notebook
**Datei:** `notebooks/matplotlib_seaborn_intro.ipynb`

**Inhalt:**
- Matplotlib-Basisplots
- Figure/Axes-Denken
- Seaborn-Grundplots
- Stil und Themes
- Skalenniveaus und Interpretationsbeispiele

### 2. Übungs-Notebook
**Datei:** `notebooks/lesson_2_exercises.ipynb`

**Inhalt:**
- strukturierte Starter-Zellen für alle drei Übungen
- Markdown-Anweisungen
- Platz für Reflexion und Interpretation

---

## Hausaufgabe

### Aufgabe
Wähle einen der bereitgestellten Datensätze und erstelle eine kleine explorative Analyse mit **mindestens vier Visualisierungen**.

### Anforderungen
Die Abgabe muss:
1. mindestens **zwei Matplotlib-Plots** enthalten
2. mindestens **zwei Seaborn-Plots** enthalten
3. für jede Visualisierung eine **kurze Begründung der Plot-Wahl** enthalten
4. mindestens **eine Aussage zum Skalenniveau** oder zur Skalierung enthalten
5. eine **kurze textliche Interpretation** der wichtigsten Beobachtungen enthalten

### Abgabeformat
- Jupyter Notebook oder Python-Skript mit Markdown/Kommentaren
- Abgabe bis zur nächsten Sitzung

### Bewertungskriterien
- Fachlich passende Plot-Auswahl (30 %)
- Technische Umsetzung (25 %)
- Lesbarkeit und Gestaltung (20 %)
- Interpretation der Ergebnisse (15 %)
- Dokumentation und Begründungen (10 %)

---

## Vorbereitung für Dozentinnen und Dozenten

### Technische Vorbereitung
- [ ] Jupyter/Notebook-Umgebung testen
- [ ] Matplotlib und Seaborn Versionen prüfen
- [ ] Lokale Datensätze bereitstellen
- [ ] Externe Datensatz-Links prüfen
- [ ] Mentimeter-Präsentation anlegen
- [ ] Mural-Board vorbereiten

### Inhaltliche Vorbereitung
- [ ] Live-Coding einmal vollständig durchspielen
- [ ] Musterlösungen für alle drei Übungen vorbereiten
- [ ] typische Fehlkonzepte notieren
- [ ] Unterschiede zwischen nominal/ordinal/intervall/ratio mit Beispielen vorbereiten
- [ ] lineare vs. logarithmische Darstellung an einem Beispiel testen

### Raum- und Ablaufvorbereitung
- [ ] Beamer/Screen testen
- [ ] WLAN und Zugriff auf Dateien sicherstellen
- [ ] Gruppenarbeitsphasen einplanen
- [ ] Backup-Variante ohne Mentimeter/Mural bereithalten

---

## Theorie-Checkliste für die Lehrperson

Vor der Sitzung sollte klar sein, wie folgende Fragen beantwortet werden:
- Wann ist Matplotlib die bessere Wahl?
- Wann spart Seaborn Zeit und verbessert Lesbarkeit?
- Welche Diagrammtypen eignen sich für Verteilungen, Vergleiche und Zusammenhänge?
- Woran erkennt man das Skalenniveau einer Variable?
- Wann ist eine logarithmische Skala sinnvoll – und wann irreführend?

---

## Erforderliche Materialien

### Software
- Python 3.10+
- Jupyter Notebook oder JupyterLab
- Bibliotheken:
  - pandas
  - numpy
  - matplotlib
  - seaborn

### Dateien
- `datasets/student_performance.csv`
- `datasets/online_retail_sample.csv`
- `notebooks/matplotlib_seaborn_intro.ipynb`
- `notebooks/lesson_2_exercises.ipynb`

### Externe Tools
- Mentimeter
- Mural oder Miro
- optional Kaggle oder Seaborn example datasets

---

## Zusätzliche Ressourcen

### Für Studierende
- [Matplotlib Dokumentation](https://matplotlib.org/stable/)
- [Matplotlib Cheat Sheets](https://matplotlib.org/cheatsheets/)
- [Seaborn Dokumentation](https://seaborn.pydata.org/)
- [Seaborn Examples](https://seaborn.pydata.org/examples/index.html)

### Für Lehrende
- [Data Viz Project](https://datavizproject.com/)
- [Storytelling with Data](https://www.storytellingwithdata.com/)
- [Kaggle Datasets](https://www.kaggle.com/datasets)

---

## Reflexion nach der Lektion

### Mögliche Leitfragen
- Welche Plot-Typen waren für die Gruppe intuitiv?
- Wo gab es Unsicherheiten bei Skalenniveaus?
- Welche Unterschiede zwischen Matplotlib und Seaborn wurden wirklich verstanden?
- Braucht die nächste Sitzung mehr Wiederholung oder mehr Transfer?

### Mögliche Anpassungen für nächste Durchführung
- mehr Zeit für Interpretation statt nur Code
- zusätzliche Beispiele für Log-Skalen
- schnellere Trennung zwischen Plot-Erstellung und Plot-Begründung

---

*Letzte Aktualisierung: April 2026*