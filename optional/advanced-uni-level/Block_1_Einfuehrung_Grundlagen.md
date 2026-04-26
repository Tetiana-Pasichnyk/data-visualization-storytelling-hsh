# Block 1: Einführung & Grundlagen
## Data Visualization & Storytelling - HsH

**Dauer:** 1 Tag (270 Minuten = 3 Einheiten à 90 Min)
**Voraussetzungen:** Keine (Kursstart)
**Schwierigkeitsgrad:** ⭐☆☆☆☆ (Einsteiger)
**Letzte Aktualisierung:** April 2026

---

## 📋 Block-Übersicht

Dieser erste Block führt in die Welt der Datenvisualisierung ein. Studierende lernen die Grundlagen, richten ihre Entwicklungsumgebung ein und erstellen ihre ersten Visualisierungen. Der Block kombiniert theoretische Grundlagen mit praktischen Übungen und legt den Fokus auf "Learning by Doing".

### 🎯 Lernziele

Nach diesem Block können Studierende:
1. ✓ Die Bedeutung von Datenvisualisierung erklären und begründen
2. ✓ Verschiedene Visualisierungstools und Frameworks benennen und vergleichen
3. ✓ Eine Python-Entwicklungsumgebung einrichten und nutzen
4. ✓ Daten aus verschiedenen Quellen laden und explorieren
5. ✓ Erste einfache Plots mit Matplotlib erstellen und anpassen
6. ✓ Jupyter Notebooks effektiv verwenden
7. ✓ Grundlegende Designprinzipien für Visualisierungen anwenden
8. ✓ Häufige Fehler in Visualisierungen erkennen und vermeiden

### 🎓 Pädagogischer Ansatz

**Lernphilosophie:**
- **Konstruktivistisch:** Studierende bauen Wissen durch eigene Erfahrungen auf
- **Iterativ:** Vom Einfachen zum Komplexen, mit vielen Wiederholungen
- **Praxisorientiert:** Jede Theorie wird sofort praktisch angewendet
- **Fehlerfreundlich:** Fehler sind Lernchancen, nicht Probleme

**Differenzierung:**
- **Anfänger:** Schritt-für-Schritt Anleitungen, viel Unterstützung
- **Fortgeschrittene:** Zusatzaufgaben, tiefere Erklärungen
- **Experten:** Herausforderungen, Optimierungsaufgaben

---

## 📚 Einheit 1.1: Was ist Datenvisualisierung?

**Dauer:** 90 Minuten  
**Format:** Vortrag + Diskussion + Aktivierung

### Zeitplan

| Zeit | Aktivität | Methode |
|------|-----------|---------|
| 0-10 Min | Begrüßung & Vorstellung | Präsentation |
| 10-20 Min | Mentimeter Aktivierung | Interaktiv |
| 20-40 Min | Theorie: Warum Visualisierung? | Vortrag |
| 40-60 Min | Kognitive Prinzipien | Vortrag + Beispiele |
| 60-75 Min | Diskussion: Gute vs. Schlechte Viz | Gruppenarbeit |
| 75-90 Min | Kursübersicht & Erwartungen | Präsentation |

### Inhalte

#### 1. Begrüßung & Vorstellung (10 Min)
- Dozent stellt sich vor
- Kursziele und -struktur
- Organisatorisches (Zeiten, Pausen, Bewertung)

#### 2. Mentimeter Aktivierung (10 Min)

**Ziel:** Vorwissen aktivieren, Erwartungen erfassen, Gruppendynamik aufbauen

**Frage 1: Word Cloud** ☁️
> "Was verbindest du mit Datenvisualisierung? (Ein Wort)"

*Erwartete Antworten:* Diagramme, Grafiken, Charts, Farben, Daten, Storytelling, Excel
*Dozentenreaktion:* Häufigste Begriffe aufgreifen und im Kursverlauf referenzieren

**Frage 2: Multiple Choice** 📊
> "Wie viel Erfahrung hast du mit Datenvisualisierung?"
- 🆕 Keine Erfahrung (erwarte: 30-40%)
- 📈 Grundkenntnisse - Excel-Charts (erwarte: 40-50%)
- 🐍 Fortgeschritten - Python/R (erwarte: 10-20%)
- 🎯 Experte - professionelle Projekte (erwarte: 0-5%)

*Dozentenreaktion:* Tempo und Tiefe an Gruppenzusammensetzung anpassen

**Frage 3: Skala** 📏
> "Wie wichtig ist Datenvisualisierung in deinem zukünftigen Beruf?"
(1 = unwichtig, 5 = sehr wichtig)

*Erwartung:* Durchschnitt 4-5 (hohe Relevanz)
*Dozentenreaktion:* Bei niedrigen Werten: Praxisbeispiele aus verschiedenen Branchen zeigen

**Frage 4: Open-Ended** 💭
> "Was möchtest du in diesem Kurs lernen?"

*Erwartete Themen:* Python, schöne Grafiken, Dashboards, Storytelling, Tools
*Dozentenreaktion:* Notieren und im Kursverlauf abhaken, was behandelt wurde

**Frage 5: Quiz (Bonus)** 🎮
> "Welche dieser Visualisierungen ist am effektivsten für Zeitreihen?"
- A) Pie Chart
- B) Line Chart ✓
- C) Bar Chart
- D) Scatter Plot

*Zweck:* Spielerischer Einstieg, zeigt dass es "richtige" und "falsche" Choices gibt

#### 3. Theorie: Warum Visualisierung? (20 Min)

**Kernbotschaften:**
- 🧠 Menschen verarbeiten visuelle Informationen 60.000x schneller als Text
- 👁️ 90% der ans Gehirn übermittelten Informationen sind visuell
- 🔍 Visualisierungen helfen bei Mustererkennung und Anomalie-Erkennung
- 💬 Effektive Kommunikation komplexer Daten an verschiedene Zielgruppen
- 📊 Daten werden durch Visualisierung "erlebbar" und verständlich

**Klassische Beispiele zeigen (10 Min):**

**1. Anscombe's Quartet (1973)** 📐
- Zeige 4 Datensätze mit identischen statistischen Eigenschaften
- Mittelwert, Varianz, Korrelation: alle gleich!
- Aber: Völlig unterschiedliche Muster in Scatter Plots
- **Lektion:** "Statistiken allein reichen nicht - visualisiere deine Daten!"

**2. Datasaurus Dozen (2017)** 🦖
- Moderne Version mit 13 Datensätzen
- Alle haben gleiche Statistiken, aber zeigen verschiedene Formen (Dinosaurier, Stern, etc.)
- **Lektion:** Bestätigt Anscombe's Prinzip mit modernen Daten
- **Interaktiv:** Studierende raten, welche Form sich hinter Statistiken verbirgt

**3. Florence Nightingale's Rose Chart (1858)** 🌹
- Historisches Beispiel: Visualisierung rettete Leben
- Zeigte Todesursachen im Krimkrieg
- Führte zu Hygienereformen im Militär
- **Lektion:** Visualisierung kann politische und soziale Veränderungen bewirken

**4. Hans Rosling's Gapminder (2006-heute)** 🌍
- Moderne Storytelling mit animierten Bubble Charts
- Zeigt globale Entwicklung über Zeit
- **Lektion:** Gute Visualisierung + Storytelling = unvergessliche Botschaft
- **Video zeigen:** 2-3 Min Ausschnitt aus Rosling's TED Talk

**Moderne Beispiele (5 Min):**

**5. COVID-19 Dashboards (2020-2023)** 🦠
- Johns Hopkins Dashboard: Echtzeit-Tracking weltweit
- **Lektion:** Visualisierung in Krisensituationen
- Diskussion: Was machte diese Dashboards effektiv?

**6. Climate Stripes (Ed Hawkins, 2018)** 🌡️
- Minimalistische Visualisierung der Erderwärmung
- Nur Farben, keine Achsen
- **Lektion:** Manchmal ist weniger mehr
- Viral auf Social Media → Visualisierung als Kommunikationsmittel

**Diskussionspunkte (5 Min):**

**Frage an Studierende:** "Wann ist eine Tabelle besser als eine Grafik?"
*Erwartete Antworten:*
- Wenn exakte Werte wichtig sind
- Bei wenigen Datenpunkten (< 10)
- Wenn Vergleiche zwischen spezifischen Werten nötig sind
- Für Nachschlagewerke

**Frage:** "Wann kann Visualisierung irreführend sein?"
*Beispiele zeigen:*
- Manipulierte Y-Achsen (nicht bei 0 startend)
- 3D-Effekte, die Proportionen verzerren
- Fehlende Kontext-Informationen
- Cherry-Picking von Daten

**Ethische Aspekte:**
- Verantwortung des Visualisierers
- Transparenz über Datenquellen
- Vermeidung von Manipulation
- Accessibility (Farbenblindheit, Screen Reader)

**💡 Merksatz für Studierende:**
> "Mit großer Visualisierungskraft kommt große Verantwortung!"
> (frei nach Spider-Man)

#### 4. Kognitive Prinzipien (20 Min)

**Ziel:** Verstehen, wie unser Gehirn visuelle Informationen verarbeitet

**A. Gestaltgesetze (10 Min)** 🧩

Diese Prinzipien aus der Gestaltpsychologie erklären, wie wir visuelle Elemente gruppieren:

**1. Gesetz der Nähe (Proximity)** 📍
- Nahe beieinander liegende Objekte werden als zusammengehörig wahrgenommen
- **Beispiel zeigen:** Scatter Plot mit Clustern
- **Anwendung:** Gruppiere verwandte Daten visuell zusammen
- **Demo:** Zeige Punkte mit unterschiedlichen Abständen

**2. Gesetz der Ähnlichkeit (Similarity)** 🎨
- Ähnliche Objekte (Farbe, Form, Größe) werden gruppiert
- **Beispiel zeigen:** Verschiedene Kategorien durch Farben
- **Anwendung:** Nutze Farbe für Kategorien, nicht willkürlich
- **Demo:** Gleiche Daten, einmal mit/ohne Farbkodierung

**3. Gesetz der Geschlossenheit (Closure)** ⭕
- Wir vervollständigen unvollständige Formen mental
- **Beispiel zeigen:** Gestrichelte Linien in Plots
- **Anwendung:** Trend-Linien müssen nicht durchgezogen sein
- **Demo:** Unvollständige Kreise werden als Kreise erkannt

**4. Gesetz der Kontinuität (Continuity)** 〰️
- Wir folgen Linien und Kurven natürlich
- **Beispiel zeigen:** Line Charts mit mehreren Serien
- **Anwendung:** Nutze Linien für zeitliche Verläufe
- **Demo:** Kreuzende Linien - welche gehören zusammen?

**5. Gesetz der Verbundenheit (Connectedness)** 🔗
- Verbundene Elemente werden als Einheit wahrgenommen
- **Beispiel zeigen:** Netzwerk-Diagramme
- **Anwendung:** Zeige Beziehungen durch Linien
- **Demo:** Punkte mit/ohne Verbindungslinien

**Interaktive Übung (3 Min):** 🎮
Zeige Folie mit gemischten Formen und frage:
- "Wie viele Gruppen seht ihr?" (testet Nähe + Ähnlichkeit)
- "Welche Elemente gehören zusammen?" (testet alle Gesetze)

**B. Präattentive Attribute (7 Min)** ⚡

Diese Eigenschaften werden vom Gehirn **sofort** (< 250ms) verarbeitet, ohne bewusste Aufmerksamkeit:

**1. Farbe (Hue, Saturation, Lightness)** 🌈
- **Hue (Farbton):** Rot, Blau, Grün, etc.
- **Saturation (Sättigung):** Intensität der Farbe
- **Lightness (Helligkeit):** Hell vs. Dunkel
- **Live-Demo:** "Finde das rote Quadrat unter 100 blauen" → Sofort!
- **Anwendung:** Nutze Farbe für wichtigste Unterscheidung

**2. Form (Size, Shape, Orientation)** 📐
- **Größe:** Größere Objekte fallen sofort auf
- **Form:** Kreis vs. Quadrat vs. Dreieck
- **Orientierung:** Horizontale vs. vertikale Linien
- **Live-Demo:** "Finde das große Quadrat" → Sofort!
- **Anwendung:** Größe für Wichtigkeit/Wert

**3. Position (X, Y, Spatial Grouping)** 📊
- **X/Y-Position:** Wo ist das Element?
- **Räumliche Gruppierung:** Cluster werden sofort erkannt
- **Live-Demo:** "Wo ist der Ausreißer?" → Sofort!
- **Anwendung:** Position ist stärkste visuelle Variable

**4. Bewegung** 🎬
- Bewegte Objekte ziehen sofort Aufmerksamkeit
- **Anwendung:** Animationen für Storytelling (z.B. Gapminder)
- **Warnung:** Zu viel Bewegung lenkt ab!

**Praktische Demonstration (3 Min):** 🔬

**Experiment 1: Präattentive Suche**
```
Zeige Folie mit:
- 99 blaue Kreise + 1 roter Kreis
- Frage: "Wo ist der rote Kreis?"
- Ergebnis: Sofort gefunden! (präattentiv)

Dann zeige:
- 99 blaue Kreise + 1 blauer Kreis mit "X"
- Frage: "Wo ist der Kreis mit X?"
- Ergebnis: Dauert länger! (nicht präattentiv)
```

**Experiment 2: Pop-Out Effekt**
```
Zeige verschiedene Kombinationen:
✓ Farbe allein: Rot unter Blau → Pop-Out!
✓ Größe allein: Groß unter Klein → Pop-Out!
✗ Farbe + Form: Roter Kreis unter blauen Quadraten UND blauen Kreisen → Kein Pop-Out!
```

**Lektion:** Nutze EIN präattentives Attribut für wichtigste Unterscheidung!

**Diskussion (2 Min):** 💬
"Wie können wir diese Prinzipien in Visualisierungen nutzen?"

*Erwartete Antworten:*
- Farbe für Kategorien
- Größe für Werte
- Position für Vergleiche
- Gruppierung für Zusammenhänge

**⚠️ Häufige Fehler:**
- Zu viele Farben (> 7-8 Kategorien)
- Farbe UND Form für gleiche Information (redundant)
- Ignorieren von Farbenblindheit
- Zu viele visuelle Variablen gleichzeitig

**💡 Merksatz:**
> "Weniger ist mehr - nutze präattentive Attribute gezielt, nicht verschwenderisch!"

#### 5. Diskussion: Gute vs. Schlechte Visualisierungen (15 Min)

**Ziel:** Kritisches Auge für Visualisierungsqualität entwickeln

**Gruppenarbeit (10 Min):** 👥

**Setup:**
- Gruppen à 3-4 Personen bilden
- Jede Gruppe erhält 6 Visualisierungen (3 gut, 3 schlecht)
- Aufgabe: Kategorisieren und begründen

**Arbeitsblatt für Gruppen:**
```
Für jede Visualisierung:
1. Gut oder Schlecht? (Daumen hoch/runter)
2. Warum? (3 Gründe nennen)
3. Wie würdet ihr es verbessern?
```

**Beispiele für SCHLECHTE Visualisierungen:** ❌

**1. 3D-Pie Chart** 🥧
- **Problem:** Perspektive verzerrt Proportionen
- **Problem:** Schwer zu vergleichen
- **Problem:** Unnötige visuelle Komplexität
- **Besser:** 2D Pie Chart oder Bar Chart

**2. Zu viele Farben** 🌈
- **Problem:** > 10 Kategorien in verschiedenen Farben
- **Problem:** Keine Farbenblind-freundliche Palette
- **Problem:** Legende ist zu lang
- **Besser:** Gruppiere Kategorien, nutze "Other"

**3. Unleserliche Achsenbeschriftungen** 🔍
- **Problem:** Zu kleine Schrift (< 10pt)
- **Problem:** Überlappende Labels
- **Problem:** Fehlende Einheiten
- **Besser:** Größere Schrift, rotierte Labels, Einheiten hinzufügen

**4. Irreführende Skalen** 📏
- **Problem:** Y-Achse startet nicht bei 0 (bei Bar Charts)
- **Problem:** Unterschiedliche Skalen ohne Hinweis
- **Problem:** Logarithmische Skala ohne Kennzeichnung
- **Besser:** Ehrliche Skalen, klare Kennzeichnung

**5. Chart Junk** 🎪
- **Problem:** Unnötige Dekorationen (Bilder, Schatten, 3D)
- **Problem:** Ablenkende Hintergründe
- **Problem:** Zu viele Grid-Linien
- **Besser:** Minimalistisch, Fokus auf Daten

**6. Falsche Chart-Typen** 🎯
- **Problem:** Pie Chart für Zeitreihen
- **Problem:** Line Chart für Kategorien
- **Problem:** Scatter Plot ohne Korrelation
- **Besser:** Wähle Chart-Typ passend zu Daten

**Beispiele für GUTE Visualisierungen:** ✅

**1. New York Times Graphics** 📰
- **Stärken:** Klare Storytelling
- **Stärken:** Minimalistisches Design
- **Stärken:** Interaktive Elemente
- **Beispiel zeigen:** COVID-19 Tracker, Election Maps

**2. FiveThirtyEight** 📊
- **Stärken:** Datengetriebener Journalismus
- **Stärken:** Konsistentes Branding
- **Stärken:** Statistische Transparenz
- **Beispiel zeigen:** Election Forecasts, Sports Analytics

**3. The Economist** 💼
- **Stärken:** Professionelles Design
- **Stärken:** Klare Botschaft
- **Stärken:** Effektive Farbnutzung (rot/blau)
- **Beispiel zeigen:** Weekly Charts

**4. Information is Beautiful** 🎨
- **Stärken:** Kreative Ansätze
- **Stärken:** Komplexe Daten verständlich
- **Stärken:** Ästhetisch ansprechend
- **Beispiel zeigen:** Data Visualization Awards

**5. Our World in Data** 🌍
- **Stärken:** Wissenschaftlich fundiert
- **Stärken:** Interaktive Charts
- **Stärken:** Open Source
- **Beispiel zeigen:** Global Development Charts

**Präsentation der Ergebnisse (5 Min):** 🎤
- Jede Gruppe präsentiert 1-2 Beispiele (30 Sek pro Gruppe)
- Dozent ergänzt und korrigiert
- Gemeinsame Diskussion: Was sind die wichtigsten Kriterien?

**Checkliste für gute Visualisierungen:** ✓
```
□ Klare Botschaft/Story
□ Passender Chart-Typ
□ Lesbare Beschriftungen
□ Ehrliche Skalen
□ Angemessene Farbnutzung
□ Minimales Chart Junk
□ Zugänglich (Farbenblindheit)
□ Quellenangabe
```

**💡 Merksatz:**
> "Eine gute Visualisierung erklärt sich selbst - eine schlechte verwirrt!"

#### 6. Kursübersicht & Erwartungen (15 Min)

**Kursstruktur:** 📅

**9 Blöcke à 3 Einheiten (je 90 Min):**
1. ✓ **Block 1:** Einführung & Grundlagen (heute!)
2. **Block 2:** Matplotlib & Seaborn Deep Dive
3. **Block 3:** Statistische Visualisierungen
4. **Block 4:** Interaktive Visualisierungen (Plotly)
5. **Block 5:** Dashboards & Storytelling
6. **Block 6:** Geospatial & Netzwerk-Visualisierungen
7. **Block 7:** Advanced Topics (D3.js, Custom Viz)
8. **Block 8:** Best Practices & Design
9. **Block 9:** Projekt-Präsentationen

**Lernformat:**
- 📚 Theorie (30%)
- 💻 Hands-On (50%)
- 👥 Diskussion & Feedback (20%)

**Bewertung:** 📊
- **60% Hausaufgaben** (9 Aufgaben, beste 8 zählen)
  - Wöchentliche Abgabe
  - Jupyter Notebooks
  - Peer-Review möglich
- **40% Abschlussprojekt**
  - Eigenes Thema wählen
  - Datenanalyse + Visualisierung
  - Präsentation (10 Min)
  - Dokumentation

**Erwartungen an Studierende:** 🎯
- ✓ **Aktive Teilnahme:** Fragen stellen, diskutieren
- ✓ **Regelmäßiges Üben:** 2-3h pro Woche außerhalb des Kurses
- ✓ **Feedback geben und nehmen:** Konstruktive Kritik
- ✓ **Respektvoller Umgang:** Fehler sind Lernchancen
- ✓ **Experimentieren:** Probiere neue Dinge aus!

**Erwartungen an Dozenten:** 👨‍🏫
- ✓ Klare Erklärungen
- ✓ Individuelle Unterstützung
- ✓ Zeitnahes Feedback
- ✓ Praxisnahe Beispiele

**Ressourcen & Support:** 🆘
- **Moodle:** Alle Materialien, Abgaben
- **Forum:** Fragen & Diskussionen
- **Sprechstunde:** Dienstags 14-16 Uhr (online)
- **Slack/Discord:** Schnelle Hilfe von Kommilitonen
- **Office Hours:** Nach Vereinbarung

**Tipps für Erfolg:** 💡
1. Beginne Hausaufgaben früh (nicht am Abgabetag!)
2. Nutze das Forum - andere haben ähnliche Fragen
3. Experimentiere mit Code - Fehler sind OK!
4. Baue ein Portfolio auf (GitHub)
5. Vernetze dich mit Kommilitonen

### 📝 Learning Checkpoint: Einheit 1.1

**Selbsttest (2 Min):** Kannst du diese Fragen beantworten?

1. ✓ Warum ist Visualisierung wichtig? (3 Gründe nennen)
2. ✓ Was ist Anscombe's Quartet und was lehrt es uns?
3. ✓ Nenne 3 Gestaltgesetze
4. ✓ Was sind präattentive Attribute? (2 Beispiele)
5. ✓ Nenne 3 Merkmale schlechter Visualisierungen
6. ✓ Wo findest du gute Visualisierungs-Beispiele?

**Wenn du < 4 Fragen beantworten kannst:** Wiederhole die Inhalte oder frage nach!

### Materialien

**Für Studierende:**
- 📊 **Präsentation:** `Block_1_Einheit_1_Einfuehrung.pptx`
- 🎮 **Mentimeter:** Link wird in Vorlesung geteilt
- 📁 **Beispiel-Visualisierungen:** `examples/good_bad_viz/`
- 📄 **Handout:** `Block_1_Handout_Kognitive_Prinzipien.pdf`
- 🎥 **Videos:** Hans Rosling TED Talk, Anscombe's Quartet Animation
- 🔗 **Links:** NYT Graphics, FiveThirtyEight, Information is Beautiful

**Für Dozenten:**
- 📋 **Dozentennotizen:** `Block_1_Einheit_1_Notizen.md`
- ⏱️ **Zeitplan-Vorlage:** `Block_1_Einheit_1_Timing.xlsx`
- 🎯 **Lernziel-Checkliste:** `Block_1_Einheit_1_Lernziele.pdf`
- 💬 **Diskussionsfragen:** `Block_1_Einheit_1_Diskussion.md`

### Dozentenhinweise

**Vorbereitung (1 Woche vorher):** 📅
- [ ] Mentimeter-Präsentation erstellen und testen
- [ ] Beispiel-Visualisierungen sammeln (gut/schlecht)
- [ ] Videos herunterladen (Backup falls Internet ausfällt)
- [ ] Handouts drucken (optional)
- [ ] Raum-Setup prüfen (Beamer, WLAN, Mikrofon)
- [ ] Gruppenarbeit-Material vorbereiten

**Am Tag selbst:** 🎬
- [ ] 30 Min vorher: Technik-Check
- [ ] Mentimeter-Link an Tafel schreiben
- [ ] Gruppengrößen planen (3-4 Personen)
- [ ] Zeitpuffer einplanen (Diskussionen dauern oft länger)

**Häufige Fragen & Antworten:** ❓

**Q: "Brauche ich Programmiererfahrung?"**
A: Grundkenntnisse Python sind hilfreich, aber nicht zwingend. Wir starten bei den Basics und bauen schrittweise auf. Wichtiger ist die Bereitschaft zu lernen!

**Q: "Welche Software brauche ich?"**
A: Wird in Einheit 1.3 im Detail erklärt. Kurz: Python + Jupyter Notebooks. Alles kostenlos und Open Source.

**Q: "Kann ich den Kurs bestehen ohne Vorkenntnisse?"**
A: Ja! Mit regelmäßiger Teilnahme, Üben und Nutzung der Ressourcen ist das absolut machbar. Viele erfolgreiche Studierende hatten keine Vorkenntnisse.

**Q: "Wie viel Zeit muss ich investieren?"**
A: Rechne mit 2-3 Stunden pro Woche außerhalb der Vorlesung für Hausaufgaben und Übungen.

**Q: "Kann ich das Abschlussprojekt in einer Gruppe machen?"**
A: Nein, das Projekt ist Einzelarbeit. Aber Peer-Review und Diskussionen sind erwünscht!

**Zeitmanagement-Tipps:** ⏰
- **Mentimeter:** Kann 12-15 Min dauern → 5 Min Puffer
- **Diskussionen:** Können ausufern → Aktiv moderieren, Zeitlimit setzen
- **Pausen:** Nach 45 Min kurze Pause (5 Min) einplanen
- **Fragen:** Sammle Fragen und beantworte am Ende, nicht zwischendurch
- **Backup-Plan:** Wenn Zeit knapp wird, kürze Diskussion, nicht Demos

**Differenzierung nach Niveau:** 🎚️

**Für Anfänger:**
- Mehr Zeit für Erklärungen
- Schritt-für-Schritt durchgehen
- Zusätzliche Beispiele zeigen
- Ermutige Fragen zu stellen

**Für Fortgeschrittene:**
- Stelle tiefergehende Fragen
- Gib Zusatzaufgaben
- Lass sie anderen helfen
- Diskutiere fortgeschrittene Konzepte

**Für Experten:**
- Binde sie als Co-Tutoren ein
- Stelle Herausforderungen
- Diskutiere Edge Cases
- Lass sie Best Practices teilen

**Troubleshooting:** 🔧

**Problem:** Mentimeter funktioniert nicht
**Lösung:** Backup mit Handzeichen oder Moodle-Umfrage

**Problem:** Diskussion wird zu hitzig
**Lösung:** Moderiere neutral, erinnere an Respekt, lenke zurück zu Fakten

**Problem:** Studierende sind passiv
**Lösung:** Direkte Fragen stellen, Kleingruppen bilden, Gamification

**Problem:** Zeit läuft davon
**Lösung:** Kürze Diskussion, verschiebe Details auf nächste Einheit

**Erfolgsmetriken:** 📈
- ✓ > 80% der Studierenden können Lernziele erklären
- ✓ Aktive Beteiligung in Diskussionen
- ✓ Positive Stimmung und Motivation
- ✓ Wenige Verständnisfragen zu Basics in späteren Einheiten

---

## 📚 Einheit 1.2: Überblick Frameworks

**Dauer:** 90 Minuten  
**Format:** Vortrag + Live-Demo + Diskussion

### Zeitplan

| Zeit | Aktivität | Methode |
|------|-----------|---------|
| 0-15 Min | Visualisierungs-Landschaft | Präsentation |
| 15-35 Min | Python-Bibliotheken | Vortrag + Demo |
| 35-55 Min | BI-Tools (Power BI, Tableau) | Vortrag + Demo |
| 55-70 Min | R & andere Tools | Überblick |
| 70-85 Min | Entscheidungshilfe: Wann welches Tool? | Diskussion |
| 85-90 Min | Q&A | Interaktiv |

### Inhalte

#### 1. Visualisierungs-Landschaft (15 Min)

**Kategorien:**

**A. Programmierbasiert**
- Python (Matplotlib, Seaborn, Plotly, Bokeh)
- R (ggplot2, plotly)
- JavaScript (D3.js, Chart.js, Highcharts)

**B. Business Intelligence**
- Power BI (Microsoft)
- Tableau (Salesforce)
- Qlik Sense
- Looker (Google)

**C. No-Code/Low-Code**
- Google Data Studio
- Flourish
- Datawrapper
- RAWGraphs

**D. Spezialisiert**
- Gephi (Netzwerke)
- Kepler.gl (Geospatial)
- Observable (Notebooks)

**Übersicht-Diagramm zeigen:**
```
Komplexität vs. Flexibilität
Hoch │     D3.js
     │     Matplotlib
     │     
     │     Plotly
     │     Seaborn
     │     
     │     Power BI
     │     Tableau
Niedrig│     Excel
     └─────────────────
     Niedrig    Hoch
     Flexibilität
```

#### 2. Python-Bibliotheken (20 Min)

**Matplotlib**
- **Beschreibung:** Basis-Bibliothek, volle Kontrolle
- **Stärken:** Flexibilität, Publikationsqualität
- **Schwächen:** Verbose Code, steile Lernkurve
- **Use Cases:** Wissenschaftliche Publikationen, Custom Plots

**Live-Demo (5 Min):**
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.title('Sine Wave')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True, alpha=0.3)
plt.show()
```

**Seaborn**
- **Beschreibung:** High-level Interface für Matplotlib
- **Stärken:** Schöne Defaults, statistische Plots
- **Schwächen:** Weniger Kontrolle als Matplotlib
- **Use Cases:** Explorative Datenanalyse, statistische Visualisierungen

**Live-Demo (5 Min):**
```python
import seaborn as sns
import pandas as pd

# Lade Beispieldaten
tips = sns.load_dataset('tips')

# Erstelle Plot
sns.scatterplot(data=tips, x='total_bill', y='tip', 
                hue='day', size='size')
plt.title('Tips Dataset')
plt.show()
```

**Plotly**
- **Beschreibung:** Interaktive Visualisierungen
- **Stärken:** Interaktivität, HTML-Export, schöne Defaults
- **Schwächen:** Größere Dateien, Online-Abhängigkeit (optional)
- **Use Cases:** Dashboards, interaktive Reports, Web-Apps

**Live-Demo (5 Min):**
```python
import plotly.express as px

# Lade Beispieldaten
df = px.data.gapminder()

# Erstelle interaktiven Plot
fig = px.scatter(df, x='gdpPercap', y='lifeExp',
                 size='pop', color='continent',
                 hover_name='country',
                 animation_frame='year',
                 log_x=True)
fig.show()
```

**Bokeh**
- **Beschreibung:** Interaktive Visualisierungen, Server-Apps
- **Stärken:** Widgets, Streaming-Daten, Server-Integration
- **Schwächen:** Komplexere API, größere Lernkurve
- **Use Cases:** Dashboards mit Widgets, Echtzeit-Daten

#### 3. BI-Tools (20 Min)

**Power BI**
- **Beschreibung:** Microsoft's BI-Plattform
- **Stärken:** Integration mit Microsoft-Ökosystem, DAX
- **Schwächen:** Windows-fokussiert, Lizenzkosten
- **Use Cases:** Business Dashboards, Reports

**Live-Demo (10 Min):**
- Power BI Desktop öffnen
- Daten importieren (CSV)
- Einfache Visualisierung erstellen
- Dashboard-Layout zeigen

**Tableau**
- **Beschreibung:** Führende BI-Software
- **Stärken:** Intuitive Bedienung, große Community
- **Schwächen:** Kosten, Lernkurve für komplexe Features
- **Use Cases:** Business Intelligence, interaktive Dashboards

**Live-Demo (10 Min):**
- Tableau Public öffnen
- Daten verbinden
- Drag-and-Drop Visualisierung
- Dashboard erstellen

#### 4. R & andere Tools (15 Min)

**R (ggplot2)**
- **Beschreibung:** Grammar of Graphics Implementation
- **Stärken:** Elegante Syntax, statistische Integration
- **Schwächen:** R-Kenntnisse erforderlich
- **Use Cases:** Statistische Analysen, akademische Forschung

**Kurzes Beispiel zeigen:**
```r
library(ggplot2)

ggplot(mtcars, aes(x=wt, y=mpg)) +
  geom_point() +
  geom_smooth(method='lm') +
  theme_minimal()
```

**JavaScript (D3.js)**
- **Beschreibung:** Data-Driven Documents
- **Stärken:** Maximale Flexibilität, Web-native
- **Schwächen:** Steile Lernkurve, viel Code
- **Use Cases:** Custom Web-Visualisierungen, interaktive Artikel

**Excel**
- **Beschreibung:** Spreadsheet mit Chart-Funktionen
- **Stärken:** Weit verbreitet, einfach
- **Schwächen:** Limitierte Anpassung, nicht reproduzierbar
- **Use Cases:** Schnelle Analysen, Business-Präsentationen

#### 5. Entscheidungshilfe (15 Min)

**Entscheidungsbaum:**

```
Brauche ich Interaktivität?
├─ Nein
│  ├─ Volle Kontrolle nötig? → Matplotlib
│  └─ Schnelle, schöne Plots? → Seaborn
│
└─ Ja
   ├─ Programmierung OK? → Plotly/Bokeh
   └─ Drag-and-Drop bevorzugt? → Power BI/Tableau
```

**Diskussion (10 Min):**
- Studierende nennen Use Cases
- Gemeinsam entscheiden: Welches Tool?
- Vor- und Nachteile diskutieren

**Faustregel:**
- **Explorative Analyse:** Seaborn
- **Publikation:** Matplotlib
- **Dashboard (Code):** Plotly/Streamlit
- **Dashboard (No-Code):** Power BI/Tableau
- **Web-Integration:** Plotly/D3.js

#### 6. Q&A (5 Min)

Offene Fragen beantworten

### Materialien

- **Präsentation:** `Block_1_Einheit_2_Frameworks.pptx`
- **Demo-Notebooks:** `demos/framework_comparison.ipynb`
- **Entscheidungsbaum:** `resources/tool_decision_tree.pdf`
- **Cheat Sheets:** Matplotlib, Seaborn, Plotly

### Dozentenhinweise

**Vorbereitung:**
- Alle Tools installiert und getestet
- Demo-Daten vorbereitet
- Internet-Verbindung prüfen (für Plotly)
- Power BI/Tableau Lizenzen prüfen

**Live-Demos:**
- Code vorher testen
- Backup-Screenshots falls Demo fehlschlägt
- Nicht zu tief in Details gehen
- Fokus auf Unterschiede

**Häufige Fragen:**
- "Welches Tool soll ich lernen?" → Kommt auf Karriereziel an
- "Ist Python schwer?" → Grundlagen sind machbar
- "Brauche ich alle Tools?" → Nein, Fokus auf 2-3

---

## 📚 Einheit 1.3: Erste Grafiken & Datenquellen

**Dauer:** 90 Minuten  
**Format:** Hands-On Workshop

### Zeitplan

| Zeit | Aktivität | Methode |
|------|-----------|---------|
| 0-20 Min | Setup: Jupyter Notebooks | Hands-On |
| 20-40 Min | Datenquellen & Import | Vortrag + Übung |
| 40-60 Min | Erste Matplotlib-Plots | Hands-On |
| 60-75 Min | Übung: Eigener Plot | Einzelarbeit |
| 75-90 Min | Troubleshooting & Q&A | Support |

### Inhalte

#### 1. Setup: Jupyter Notebooks (20 Min)

**Ziel:** Alle haben eine funktionierende Umgebung

**Option A: Lokale Installation (empfohlen)**

```bash
# Anaconda installieren (falls nicht vorhanden)
# Download: https://www.anaconda.com/download

# Neue Umgebung erstellen
conda create -n dataviz python=3.10
conda activate dataviz

# Bibliotheken installieren
conda install matplotlib seaborn plotly pandas numpy jupyter

# Jupyter starten
jupyter notebook
```

**Option B: Google Colab (Backup)**

1. Gehe zu https://colab.research.google.com
2. Neues Notebook erstellen
3. Bibliotheken sind vorinstalliert

**Setup-Check:**
```python
# Test-Code ausführen
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pandas as pd
import numpy as np

print("✓ Alle Bibliotheken erfolgreich importiert!")
```

**Jupyter Basics (5 Min):**
- Zellen erstellen und ausführen (Shift+Enter)
- Markdown vs. Code-Zellen
- Kernel neu starten
- Speichern und exportieren

#### 2. Datenquellen & Import (20 Min)

**Datenquellen-Übersicht:**

**A. Lokale Dateien**
```python
# CSV
df = pd.read_csv('data.csv')

# Excel
df = pd.read_excel('data.xlsx')

# JSON
df = pd.read_json('data.json')
```

**B. Online-Quellen**
```python
# URL
url = 'https://raw.githubusercontent.com/...'
df = pd.read_csv(url)

# Kaggle (nach Download)
df = pd.read_csv('kaggle_dataset.csv')
```

**C. Integrierte Datasets**
```python
# Seaborn Datasets
tips = sns.load_dataset('tips')
iris = sns.load_dataset('iris')
titanic = sns.load_dataset('titanic')

# Plotly Datasets
gapminder = px.data.gapminder()
```

**D. APIs (Überblick)**
```python
# Beispiel: OpenWeatherMap
import requests

api_key = 'YOUR_KEY'
url = f'https://api.openweathermap.org/data/2.5/weather?q=Hannover&appid={api_key}'
response = requests.get(url)
data = response.json()
```

**Praktische Übung (10 Min):**
```python
# Lade Tips-Dataset
tips = sns.load_dataset('tips')

# Erste Zeilen anzeigen
print(tips.head())

# Info über Dataset
print(tips.info())

# Beschreibende Statistiken
print(tips.describe())
```

**Kaggle-Integration (5 Min):**
- Kaggle Account erstellen
- Dataset suchen
- Download und Import
- Beispiel: Titanic Dataset

#### 3. Erste Matplotlib-Plots (20 Min)

**Grundstruktur:**
```python
import matplotlib.pyplot as plt

# Daten erstellen
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Plot erstellen
plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.title('Mein erster Plot')
plt.xlabel('X-Achse')
plt.ylabel('Y-Achse')
plt.grid(True)
plt.show()
```

**Verschiedene Plot-Typen:**

**Line Plot:**
```python
plt.figure(figsize=(10, 6))
plt.plot(x, y, marker='o', linestyle='-', color='blue')
plt.title('Line Plot')
plt.show()
```

**Scatter Plot:**
```python
plt.figure(figsize=(10, 6))
plt.scatter(x, y, s=100, c='red', alpha=0.5)
plt.title('Scatter Plot')
plt.show()
```

**Bar Plot:**
```python
categories = ['A', 'B', 'C', 'D']
values = [23, 45, 56, 78]

plt.figure(figsize=(10, 6))
plt.bar(categories, values)
plt.title('Bar Plot')
plt.show()
```

**Histogram:**
```python
data = np.random.randn(1000)

plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, edgecolor='black')
plt.title('Histogram')
plt.show()
```

**Mit echten Daten:**
```python
# Tips Dataset
tips = sns.load_dataset('tips')

# Scatter Plot
plt.figure(figsize=(10, 6))
plt.scatter(tips['total_bill'], tips['tip'])
plt.xlabel('Total Bill ($)')
plt.ylabel('Tip ($)')
plt.title('Tips vs. Total Bill')
plt.grid(True, alpha=0.3)
plt.show()
```

#### 4. Übung: Eigener Plot (15 Min)

**Aufgabe:**
Erstelle einen Plot mit dem Iris-Dataset:

```python
# Lade Daten
iris = sns.load_dataset('iris')

# Aufgabe:
# 1. Erstelle einen Scatter Plot
# 2. X-Achse: sepal_length
# 3. Y-Achse: sepal_width
# 4. Färbe nach species
# 5. Füge Titel und Achsenbeschriftungen hinzu
# 6. Füge ein Grid hinzu

# Dein Code hier:
```

**Musterlösung:**
```python
plt.figure(figsize=(10, 6))

# Für jede Species separat plotten
for species in iris['species'].unique():
    data = iris[iris['species'] == species]
    plt.scatter(data['sepal_length'], 
                data['sepal_width'],
                label=species,
                alpha=0.6)

plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.title('Iris Dataset: Sepal Dimensions')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

#### 5. Troubleshooting & Q&A (15 Min)

**Häufige Probleme:**

**Problem 1: Plot wird nicht angezeigt**
```python
# Lösung: plt.show() hinzufügen
plt.plot(x, y)
plt.show()  # ← Wichtig!
```

**Problem 2: Fehler beim Import**
```python
# Lösung: Bibliothek installieren
# !pip install matplotlib
```

**Problem 3: Daten nicht gefunden**
```python
# Lösung: Pfad prüfen
import os
print(os.getcwd())  # Aktuelles Verzeichnis
```

**Problem 4: Figure zu klein**
```python
# Lösung: figsize anpassen
plt.figure(figsize=(12, 8))  # Breite, Höhe in Inches
```

**Best Practices:**
- Immer `plt.figure()` vor neuem Plot
- Aussagekräftige Titel und Labels
- Grid für bessere Lesbarkeit
- Farben bewusst wählen
- Code kommentieren

### Materialien

- **Notebook:** `Block_1_Einheit_3_Erste_Plots.ipynb`
- **Datasets:** Tips, Iris, Titanic (Seaborn)
- **Cheat Sheet:** `Matplotlib_Basics_Cheatsheet.pdf`
- **Troubleshooting Guide:** `Common_Errors_Solutions.md`

### Dozentenhinweise

**Vorbereitung:**
- Alle Notebooks vorher testen
- Backup-Notebooks auf USB-Stick
- Google Colab als Fallback
- Hilfs-Tutoren einplanen (falls verfügbar)

**Während der Einheit:**
- Langsam vorgehen
- Regelmäßig fragen: "Alle dabei?"
- Zwischen Studierenden umhergehen
- Individuelle Hilfe anbieten

**Häufige Probleme:**
- Installation schlägt fehl → Google Colab
- Jupyter startet nicht → Browser-Cache leeren
- Import-Fehler → Umgebung prüfen
- Plot wird nicht angezeigt → plt.show() vergessen

**Zeitmanagement:**
- Setup kann länger dauern → Zeitpuffer
- Übung individuell → Schnelle bekommen Bonus-Aufgabe
- Q&A flexibel → Kann auch nach Einheit weitergehen

---

## 📝 Hausaufgabe Block 1

**Abgabe:** 1 Woche nach Block 1 (Sonntag, 23:59 Uhr)  
**Format:** Jupyter Notebook (.ipynb)  
**Dateiname:** `Nachname_Vorname_Block1.ipynb`

### Aufgabe

Erstelle ein Jupyter Notebook mit folgenden Komponenten:

#### Teil 1: Daten laden (20 Punkte)
1. Wähle ein Dataset von Kaggle ODER verwende ein Seaborn-Dataset
2. Lade die Daten in ein Pandas DataFrame
3. Zeige die ersten 10 Zeilen
4. Gib Informationen über das Dataset aus (Anzahl Zeilen, Spalten, Datentypen)
5. Erstelle beschreibende Statistiken

#### Teil 2: Drei verschiedene Plots (60 Punkte)
Erstelle drei verschiedene Visualisierungen mit Matplotlib:

**Plot 1: Scatter Plot (20 Punkte)**
- Zwei numerische Variablen
- Titel und Achsenbeschriftungen
- Grid
- Mindestens 100 Datenpunkte

**Plot 2: Histogram (20 Punkte)**
- Eine numerische Variable
- Mindestens 20 Bins
- Titel und Achsenbeschriftungen
- Verschiedene Farbe als Plot 1

**Plot 3: Bar Plot oder Line Plot (20 Punkte)**
- Frei wählbar
- Titel und Achsenbeschriftungen
- Professionelles Styling

#### Teil 3: Dokumentation (20 Punkte)
- Markdown-Zellen mit Erklärungen
- Was zeigen die Plots?
- Welche Erkenntnisse gewinnst du?
- Mindestens 3 Markdown-Zellen

### Bewertungskriterien

| Kriterium | Punkte | Beschreibung |
|-----------|--------|--------------|
| **Technische Umsetzung** | 40 | Code funktioniert, Bibliotheken korrekt verwendet |
| **Visuelle Gestaltung** | 30 | Titel, Labels, Grid, Farben, Lesbarkeit |
| **Dokumentation** | 20 | Markdown-Zellen, Erklärungen, Interpretation |
| **Kreativität** | 10 | Eigene Ideen, über Mindestanforderungen hinaus |
| **Gesamt** | 100 | |

### Bonus-Aufgaben (Optional, +10 Punkte)

1. **Subplots (+5 Punkte):** Erstelle ein Figure mit 2x2 Subplots
2. **Styling (+3 Punkte):** Verwende ein Matplotlib-Style (z.B. 'seaborn', 'ggplot')
3. **Annotations (+2 Punkte):** Füge Text-Annotationen zu interessanten Punkten hinzu

### Hilfestellungen

**Kaggle Datasets:**
- https://www.kaggle.com/datasets
- Empfohlen: Titanic, House Prices, Iris

**Seaborn Datasets:**
```python
# Verfügbare Datasets anzeigen
import seaborn as sns
print(sns.get_dataset_names())

# Dataset laden
df = sns.load_dataset('tips')  # oder 'iris', 'titanic', etc.
```

**Matplotlib Styles:**
```python
# Verfügbare Styles
print(plt.style.available)

# Style verwenden
plt.style.use('seaborn-v0_8')
```

### Abgabe

**Wo:** Moodle-Kurs  
**Format:** .ipynb Datei  
**Größe:** Max. 10 MB  
**Naming:** `Nachname_Vorname_Block1.ipynb`

---

## 📚 Ressourcen

### Dokumentation
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/)

### Tutorials
- [Matplotlib Tutorial](https://matplotlib.org/stable/tutorials/index.html)
- [Python Graph Gallery](https://python-graph-gallery.com/)
- [Kaggle Learn](https://www.kaggle.com/learn)

### Datasets
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [UCI ML Repository](https://archive.ics.uci.edu/ml/)
- [Seaborn Datasets](https://github.com/mwaskom/seaborn-data)

### Videos
- [Corey Schafer - Matplotlib Tutorial](https://www.youtube.com/watch?v=UO98lJQ3QGI)
- [Sentdex - Data Visualization](https://www.youtube.com/playlist?list=PLQVvvaa0QuDfefDfXb9Yf0la1fPDKluPF)

---

## ✅ Checkliste für Studierende

Nach Block 1 solltest du:
- [ ] Jupyter Notebook installiert und getestet haben
- [ ] Daten von Kaggle oder Seaborn laden können
- [ ] Einen einfachen Matplotlib-Plot erstellen können
- [ ] Titel und Achsenbeschriftungen hinzufügen können
- [ ] Die Hausaufgabe begonnen haben
- [ ] Bei Problemen Hilfe gesucht haben (Forum, Sprechstunde)

---

## 🎯 Ausblick auf Block 2

Im nächsten Block lernen wir:
- Matplotlib Figure-Axes Architektur im Detail
- Seaborn für statistische Visualisierungen
- Verschiedene Skalen (linear, logarithmisch)
- Statistische Kennzahlen visualisieren

**Vorbereitung:**
- Hausaufgabe Block 1 abschließen
- Matplotlib-Basics wiederholen
- Optional: Seaborn-Dokumentation durchblättern

---

**Erstellt:** April 2026  
**Version:** 1.0  
**Nächste Aktualisierung:** Nach Feedback Block 1