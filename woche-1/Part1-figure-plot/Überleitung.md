# 🔄 Überleitung: Von Part 1 zu Part 2

## 📚 Was haben wir in Part 1 gelernt?

In **Part 1** haben wir die Grundlagen von Matplotlib kennengelernt:
- ✅ **Figure & Axes Konzept** - Die Leinwand und der Plot-Bereich
- ✅ **Pyplot API** - Das einfache MATLAB-ähnliche Interface
- ✅ **Echte Daten** - CSV-Dateien laden und plotten

---

## 🎯 Was kommt jetzt? Die Gruppenarbeit!

**Jetzt wendet ihr das Gelernte an!**

📋 **Eure Aufgaben:** [`woche-1/Part2/03_fragen.md`](../Part2/03_fragen.md)
- 5 Gruppen
- 5 verschiedene Fragen
- Echte Datensätze

**Beispiel-Fragen:**
- Ist es in Hannover wärmer als in Berlin?
- Wie beeinflusst der Kilometerstand den Autopreis?
- Wird es im Mai wärmer?

---

## ⚠️ Häufige Probleme

### Problem 1: "FileNotFoundError"
**Ursache:** Datei nicht gefunden
**Lösung:** Prüfe den Pfad! Richtig: `'data/hannover_temp.csv'`

### Problem 2: "KeyError"
**Ursache:** Spaltenname falsch geschrieben
**Lösung:** Mit `print(df.columns)` alle Spaltennamen anzeigen

### Problem 3: Plot sieht komisch aus
**Ursache:** Datentyp falsch (z.B. Datum als Text)
**Lösung:** Datum konvertieren:
```python
df['datum'] = pd.to_datetime(df['datum'])
```

### Problem 4: Achsenbeschriftung fehlt
**Ursache:** `xlabel` oder `ylabel` vergessen
**Lösung:** Immer hinzufügen! Siehe Checkliste unten.

---

## ✅ Checkliste vor der Präsentation

Prüft euer Diagramm:
- [ ] Hat es einen **Titel**?
- [ ] Ist die **X-Achse** beschriftet?
- [ ] Ist die **Y-Achse** beschriftet?
- [ ] Gibt es eine **Legende** (falls mehrere Linien)?
- [ ] Sind die **Farben** gut sichtbar?
- [ ] Ist das **Gitter** aktiviert? (`plt.grid(True)`)
- [ ] Habt ihr alle **4 Fragen** beantwortet?

---

## 🎤 Präsentation (5 Minuten pro Gruppe)

### Was ihr zeigen sollt:
1. **Euer Diagramm** (Screenshot oder live)
2. **Die Antworten** auf die 4 Fragen
3. **Eine Beobachtung** (z.B. "Die Temperatur steigt am Ende stark an")

### Tipps:
- Sprecht langsam und deutlich
- Zeigt auf das Diagramm, wenn ihr etwas erklärt
- Sagt, warum eure Beobachtung interessant ist

---

## 🚀 Nach der Gruppenarbeit: Part 2 beginnt!

**Tag 4:** Wir lernen, wie man Plots **bewertet** und **verbessert**.
- Siehe: [`woche-1/Part2/leitfaden_langsam.md`](../Part2/leitfaden_langsam.md)
- Siehe: [`docs/checkliste_plot.md`](../../docs/checkliste_plot.md)

**Dann vertiefen wir die Matplotlib-Grundlagen:**

### 📐 Part 2: Vertiefung der Figure & Axes Beziehungen

#### 1️⃣ Axes Platzierung: Subplots erstellen
**Leitfaden:** [`woche-1/Part2/04_axes_platzierung.md`](../Part2/04_axes_platzierung.md)
**Notebook:** [`woche-1/Part2/04_Axes.ipynb`](../Part2/04_Axes.ipynb)

**Was lernen wir:**
- Die **Hierarchie** verstehen: Figure → Axes → Plot-Elemente
- **Figure** = Die gesamte Leinwand (wie ein Blatt Papier)
- **Axes** = Der Plot-Bereich (wie ein Koordinatensystem auf dem Papier)
- Eine Figure kann **mehrere Axes** enthalten (Subplots!)

**Wichtig:** Axes ≠ Axis!
- **Axes** = Der gesamte Chart/Plot-Bereich
- **Axis** = Die X- oder Y-Achse

**Drei Wege, Axes zu erstellen:**
1. `.subplots()` - **Standard-Weg** (95% der Fälle!)
2. `.add_subplot()` - Grid-basiert (1,3,1 = 1 Zeile, 3 Spalten, Position 1)
3. `.add_axes()` - Manuelle Positionierung (für Überlappungen)

---

#### 2️⃣ Axes 1 ↔ {2...*} Axis (Appearance)
**Notebook:** [`woche-1/Part2/05_axes_1^<-->^{2...}_axis.ipynb`](../Part2/05_axes_1^<-->^{2...}_axis.ipynb)

**Was lernen wir:**
- **Axes** hat **2 Axis-Objekte**: `xaxis` und `yaxis`
- Wie man Achsen **anpasst**: Ticks, Labels, Limits, Scales
- **10 wichtige Properties:**
  1. `facecolor` - Hintergrundfarbe
  2. `xlim/ylim` - Achsengrenzen
  3. `xscale/yscale` - Skalierung (linear, log)
  4. `xlabel/ylabel` - Achsenbeschriftung
  5. `title` - Titel
  6. `xticks/yticks` - Tick-Positionen
  7. `xticklabels/yticklabels` - Tick-Labels
  8. `frame_on` - Rahmen an/aus
  9. `aspect` - Seitenverhältnis
  10. **Kombination** - Alle zusammen!

**Wichtige Unterscheidung:**
- `.set_ylim()` - Setzt Grenzen, kann Reihenfolge ändern
- `.set_ybound()` - Setzt Grenzen, **behält** Reihenfolge bei (z.B. für invertierte Achsen)

---

## 📚 Hilfe

- **Fragen zu den Aufgaben:** [`woche-1/Part2/03_fragen.md`](../Part2/03_fragen.md)
- **Matplotlib-Parameter:** [`woche-2/04_matplotlib_parameter.md`](../../woche-2/04_matplotlib_parameter.md)
- **Was haben wir gelernt:** [`woche-1/Part1/01_was_haben_wir_gelernt.md`](01_was_haben_wir_gelernt.md)
- **Gruppenarbeit-Anleitung:** [`woche-1/Part1/03_anleitung.md`](03_anleitung.md)

---

## 🎯 Zusammenfassung

**Part 1:** Grundlagen verstehen → Anwenden in Gruppenarbeit
**Part 2:** Vertiefung → Figure/Axes Beziehungen → Axes/Axis Anpassungen

**Lernpfad:**
```
01 Figure & Axes Konzept
    ↓
02 Pyplot API
    ↓
03 Echte Daten & Gruppenarbeit
    ↓
[Überleitung - Du bist hier! 🎯]
    ↓
Part 2: Foundation (Figure ↔ Axes)
    ↓
Part 2: Axes ↔ Axis (Appearance)
```

---

*Viel Erfolg! 🎉*

*Sprachniveau: B1 (Deutsch)*

## ⚠️ Häufige Probleme

### Problem 1: "FileNotFoundError"
**Ursache:** Datei nicht gefunden  
**Lösung:** Prüfe den Pfad! Richtig: `'data/hannover_temp.csv'`

### Problem 2: "KeyError"
**Ursache:** Spaltenname falsch geschrieben  
**Lösung:** Mit `print(df.columns)` alle Spaltennamen anzeigen

### Problem 3: Plot sieht komisch aus
**Ursache:** Datentyp falsch (z.B. Datum als Text)  
**Lösung:** Datum konvertieren:
```python
df['datum'] = pd.to_datetime(df['datum'])
```

### Problem 4: Achsenbeschriftung fehlt
**Ursache:** `xlabel` oder `ylabel` vergessen  
**Lösung:** Immer hinzufügen! Siehe Checkliste unten.

---

## ✅ Checkliste vor der Präsentation

Prüft euer Diagramm:
- [ ] Hat es einen **Titel**?
- [ ] Ist die **X-Achse** beschriftet?
- [ ] Ist die **Y-Achse** beschriftet?
- [ ] Gibt es eine **Legende** (falls mehrere Linien)?
- [ ] Sind die **Farben** gut sichtbar?
- [ ] Ist das **Gitter** aktiviert? (`plt.grid(True)`)
- [ ] Habt ihr alle **4 Fragen** beantwortet?

---

## 🎤 Präsentation (5 Minuten pro Gruppe)

### Was ihr zeigen sollt:
1. **Euer Diagramm** (Screenshot oder live)
2. **Die Antworten** auf die 4 Fragen
3. **Eine Beobachtung** (z.B. "Die Temperatur steigt am Ende stark an")

### Tipps:
- Sprecht langsam und deutlich
- Zeigt auf das Diagramm, wenn ihr etwas erklärt
- Sagt, warum eure Beobachtung interessant ist

---

## 🚀 Nach der Gruppenarbeit

**Tag 4:** Wir lernen, wie man Plots **bewertet** und **verbessert**.
- Siehe: [`woche-1/Part2/leitfaden_langsam.md`](../Part2/leitfaden_langsam.md)
- Siehe: [`docs/checkliste_plot.md`](../../docs/checkliste_plot.md)
- Siehe: [`woche-1/Part2/04_axes_platzierung.md`](../Part2/04_axes_platzierung.md) - Subplots erstellen

---

## 📚 Hilfe

- **Fragen zu den Aufgaben:** `03_fragen.md`
- **Matplotlib-Befehle:** `notebooks/01_intro_matplotlib.ipynb`
- **Pandas-Befehle:** `notebooks/02_pandas_plotting.ipynb`
- **Parameter-Referenz:** `woche-2/04_matplotlib_parameter.md`

---

*Viel Erfolg! 🎉*