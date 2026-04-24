# 📚 Fundamentals Notebook Guide

## 🎯 Übersicht

Dieses Verzeichnis enthält verschiedene Matplotlib-Notebooks mit unterschiedlichen Schwerpunkten. Dieser Guide hilft dir, das richtige Notebook für deine Bedürfnisse zu finden.

---

## 📊 Die Notebooks im Überblick

### 1️⃣ **Kopie_von_Intro_to_matplotlib.ipynb** ⭐ HAUPTNOTEBOOK

**Status:** ✅ Empfohlen als Hauptmaterial

**Beschreibung:**
- Das **umfassendste und strukturierteste** Notebook
- Deckt alle wichtigen Matplotlib-Konzepte ab
- Gut organisiert mit klaren Abschnitten

**Inhalt:**
- Figure und Axes Konzepte
- Object-Oriented API
- Verschiedene Plot-Typen
- Styling und Anpassungen
- Best Practices

**Für wen:**
- Studierende, die Matplotlib von Grund auf lernen wollen
- Als Hauptreferenz für den Kurs

**Verwendung:**
```bash
# Öffne dieses Notebook zuerst!
jupyter notebook Kopie_von_Intro_to_matplotlib.ipynb
```

---

### 2️⃣ **2ndDay-introduction-to-matplotlib-video.ipynb** ⭐ PRAKTISCH

**Status:** ✅ Gut für praktische Anwendung

**Beschreibung:**
- Fokus auf **praktische Anwendung**
- Zeigt Übergang von stateful `plt` zu OO-API
- Plotting auf **echten Daten** (Pandas DataFrames)

**Inhalt:**
- Stateful API (`plt.plot()`)
- Object-Oriented API (`ax.plot()`)
- Integration mit Pandas
- Reale Datenbeispiele

**Stärken:**
- ✅ Praktischer Ansatz
- ✅ Zeigt beide APIs (stateful → OO)
- ✅ Pandas-Integration

**Schwächen:**
- ⚠️ Weniger strukturiert als Kopie_von_Intro
- ⚠️ Nicht so umfassend

**Für wen:**
- Studierende, die bereits Pandas kennen
- Praktische Übungen mit echten Daten
- Als Ergänzung zum Hauptnotebook

**Verwendung:**
```bash
# Nach dem Hauptnotebook für praktische Übungen
jupyter notebook 2ndDay-introduction-to-matplotlib-video.ipynb
```

---

### 3️⃣ **mlp_complete_guide.ipynb**

**Status:** ⚠️ Referenz / Fortgeschritten

**Beschreibung:**
- Sehr **umfangreiches** Referenz-Notebook
- Detaillierte technische Dokumentation
- Für fortgeschrittene Nutzer

**Für wen:**
- Als Nachschlagewerk
- Für fortgeschrittene Studierende
- Nicht als Einstieg empfohlen

---

### 4️⃣ **Kopie_von_Intro_to_matplotlib-Copy1.ipynb**

**Status:** ⚠️ Duplikat / Backup

**Beschreibung:**
- Kopie des Hauptnotebooks
- Wahrscheinlich für Backup oder Experimente

**Empfehlung:**
- Nutze das Original (`Kopie_von_Intro_to_matplotlib.ipynb`)

---

## 🎓 Empfohlene Lernreihenfolge

### Für Anfänger:

```
1. Kopie_von_Intro_to_matplotlib.ipynb
   ↓ (Grundlagen verstehen)
   
2. matplotlib_parameter_reference.md
   ↓ (Als Nachschlagewerk nutzen)
   
3. 2ndDay-introduction-to-matplotlib-video.ipynb
   ↓ (Praktische Anwendung mit Pandas)
   
4. mlp_complete_guide.ipynb
   (Optional: Für tiefere Details)
```

### Für Fortgeschrittene:

```
1. mlp_complete_guide.ipynb
   (Vollständige Referenz)
   
2. matplotlib_parameter_reference.md
   (Schnelle Parameter-Suche)
```

---

## 📋 Vergleichstabelle

| Notebook | Umfang | Struktur | Praxis | Empfehlung |
|----------|--------|----------|--------|------------|
| **Kopie_von_Intro** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐☆☆ | **HAUPTNOTEBOOK** |
| **2ndDay-intro** | ⭐⭐⭐☆☆ | ⭐⭐⭐☆☆ | ⭐⭐⭐⭐⭐ | Praktische Übungen |
| **mlp_complete** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐☆ | ⭐⭐☆☆☆ | Referenz |
| **Copy1** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐☆☆ | Backup |

---

## 🔍 Detaillierte Analyse

### Kopie_von_Intro_to_matplotlib.ipynb

**Warum das Hauptnotebook?**
1. ✅ **Beste Struktur:** Logischer Aufbau von einfach zu komplex
2. ✅ **Vollständig:** Alle wichtigen Konzepte abgedeckt
3. ✅ **Didaktisch:** Gut für Lehre geeignet
4. ✅ **Balance:** Theorie + Praxis gut ausgewogen

**Themen:**
- Figure/Axes Architektur
- Stateful vs. Object-Oriented API
- Plot-Typen (Line, Scatter, Bar, etc.)
- Styling (Colors, Markers, Lines)
- Layouts (Subplots, GridSpec)
- Annotations und Text
- Speichern und Export

---

### 2ndDay-introduction-to-matplotlib-video.ipynb

**Warum praktisch?**
1. ✅ **Pandas-Integration:** Zeigt, wie man mit echten DataFrames arbeitet
2. ✅ **API-Übergang:** Stateful `plt` → OO `ax`
3. ✅ **Reale Daten:** Nicht nur Beispieldaten
4. ⚠️ **Weniger strukturiert:** Nicht so didaktisch wie Hauptnotebook

**Besonderheiten:**
- Zeigt beide APIs parallel
- Praktische Beispiele mit Pandas
- Gut für "Learning by Doing"

**Wann nutzen:**
- Nach dem Hauptnotebook
- Wenn du mit Pandas arbeitest
- Für praktische Übungen

---

## 💡 Tipps für Studierende

### 1. Start mit dem Hauptnotebook
```python
# Öffne zuerst:
Kopie_von_Intro_to_matplotlib.ipynb

# Arbeite es komplett durch
# Mache alle Übungen
# Verstehe Figure/Axes Konzept
```

### 2. Nutze die Parameter-Referenz
```python
# Parallel zum Notebook:
matplotlib_parameter_reference.md

# Schnelles Nachschlagen von Parametern
# Verstehe die Verbindungen (plot() → Line2D)
```

### 3. Übe mit echten Daten
```python
# Dann:
2ndDay-introduction-to-matplotlib-video.ipynb

# Wende das Gelernte auf Pandas DataFrames an
# Experimentiere mit eigenen Daten
```

### 4. Vertiefe bei Bedarf
```python
# Optional:
mlp_complete_guide.ipynb

# Für spezielle Fragen
# Als Nachschlagewerk
```

---

## 🎯 Für Lehrende

### Kursstruktur-Empfehlung

**Woche 1: Grundlagen**
- Hauptnotebook: `Kopie_von_Intro_to_matplotlib.ipynb`
- Referenz: `matplotlib_parameter_reference.md`
- Übungen: Erste Plots erstellen

**Woche 2: Praxis**
- Praktisches Notebook: `2ndDay-introduction-to-matplotlib-video.ipynb`
- Gruppenübungen: `weeks/week-2/exercises/gruppenaufgaben_diagramme.md`
- Storytelling: `weeks/week-1/storytelling_leitfaden_b1.md`

**Optional: Vertiefung**
- Referenz: `mlp_complete_guide.ipynb`
- Für fortgeschrittene Studierende

---

## 📁 Zusätzliche Materialien

### In diesem Verzeichnis:

| Datei | Typ | Beschreibung |
|-------|-----|--------------|
| `matplotlib_parameter_reference.md` | Referenz | Vollständige Parameter-Liste |
| `mlp_complete_guide_structure_analysis.md` | Analyse | Struktur-Analyse des Complete Guide |
| `plot.py` | Code | Python-Skript mit Plot-Funktionen |

---

## 🚀 Quick Start

### Für Studierende:
```bash
# 1. Öffne das Hauptnotebook
jupyter notebook Kopie_von_Intro_to_matplotlib.ipynb

# 2. Halte die Referenz offen
# (in einem anderen Tab/Fenster)
open matplotlib_parameter_reference.md

# 3. Nach Abschluss: Praktische Übungen
jupyter notebook 2ndDay-introduction-to-matplotlib-video.ipynb
```

### Für Lehrende:
```bash
# Alle Notebooks auf einmal öffnen
jupyter notebook

# Dann im Browser:
# - Kopie_von_Intro (für Vorlesung)
# - 2ndDay-intro (für Übungen)
# - Parameter-Referenz (zum Teilen)
```

---

## ❓ FAQ

### Welches Notebook soll ich zuerst öffnen?
→ **`Kopie_von_Intro_to_matplotlib.ipynb`** - Das Hauptnotebook

### Ich kenne schon Pandas, welches Notebook?
→ **`2ndDay-introduction-to-matplotlib-video.ipynb`** - Praktischer Fokus

### Ich suche einen spezifischen Parameter?
→ **`matplotlib_parameter_reference.md`** - Schnelle Referenz

### Ich brauche alle Details?
→ **`mlp_complete_guide.ipynb`** - Vollständige Referenz

### Was ist mit Copy1?
→ Backup/Duplikat - nutze das Original

---

## 🔗 Verbindungen zu anderen Materialien

### Storytelling:
- `weeks/week-1/storytelling_leitfaden_b1.md`
- Nutze die Notebooks, um Daten zu visualisieren
- Dann erzähle die Story mit dem Leitfaden

### Gruppenübungen:
- `weeks/week-2/exercises/gruppenaufgaben_diagramme.md`
- Nutze die Notebooks als Werkzeug
- Erstelle die geforderten Plots

### Parameter-Referenz:
- `matplotlib_parameter_reference.md`
- Nutze während der Arbeit mit Notebooks
- Schnelles Nachschlagen

---

## ✅ Zusammenfassung

**Das musst du wissen:**

1. **Hauptnotebook:** `Kopie_von_Intro_to_matplotlib.ipynb`
   - Start hier!
   - Beste Struktur
   - Vollständig

2. **Praktisches Notebook:** `2ndDay-introduction-to-matplotlib-video.ipynb`
   - Nach dem Hauptnotebook
   - Pandas-Integration
   - Reale Daten

3. **Referenz:** `matplotlib_parameter_reference.md`
   - Immer griffbereit
   - Schnelles Nachschlagen
   - Verstehe Verbindungen

4. **Fortgeschritten:** `mlp_complete_guide.ipynb`
   - Optional
   - Sehr detailliert
   - Als Nachschlagewerk

---

*Letzte Aktualisierung: 23. April 2026*  
*Version: 1.0*