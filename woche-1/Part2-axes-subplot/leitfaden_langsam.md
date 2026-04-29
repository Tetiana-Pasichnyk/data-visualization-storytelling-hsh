# 🐢 Tag 4: Plot-Bewertung - LANGSAM Schritt-für-Schritt

## ⚠️ Wichtig: Heute nehmen wir uns ZEIT!

Gestern war es zu schnell. Heute machen wir es **langsam** und **gründlich**.

---

## 📊 Was ist ein guter Plot?

Ein guter Plot hat **5 wichtige Elemente**:

1. ✅ **Titel** - Was zeigt der Plot?
2. ✅ **Achsen** - Was ist X? Was ist Y?
3. ✅ **Legende** - Welche Linie ist welche?
4. ✅ **Farben** - Sind die Farben klar?
5. ✅ **Story** - Welche Frage beantwortet der Plot?

---

## 🎯 Schritt 1: Der Titel (10 Minuten)

### Was macht einen guten Titel?

**❌ Schlechte Titel:**
- "Daten"
- "Plot"
- "Grafik 1"

**✅ Gute Titel:**
- "Temperatur in Hannover steigt im Mai"
- "Autopreis sinkt mit höherem Kilometerstand"
- "Studierende mit mehr Lernzeit haben bessere Noten"

### Übung 1: Titel verbessern

Schau dir deinen Plot von gestern an:
```python
# Dein alter Titel:
plt.title('Daten')

# Neuer, besserer Titel:
plt.title('Temperatur in Hannover steigt von 12°C auf 20°C')
```

**Frage dich:**
- Versteht jemand SOFORT, worum es geht?
- Ist die Hauptbotschaft im Titel?

**✍️ Schreib deinen neuen Titel hier:**
```
Mein neuer Titel: _______________________________________________
```

---

## 🎯 Schritt 2: Die Achsen (10 Minuten)

### Was brauchen gute Achsen?

1. **Namen** - Was ist auf der X-Achse? Was ist auf der Y-Achse?
2. **Einheiten** - °C, Euro, Kilometer, etc.
3. **Lesbarkeit** - Nicht zu klein, nicht zu groß

### Übung 2: Achsen beschriften

```python
# ❌ Schlecht - keine Beschriftung
plt.plot(x, y)

# ✅ Gut - mit Beschriftung und Einheiten
plt.xlabel('Datum (Mai 2026)')
plt.ylabel('Temperatur (°C)')
```

**Checkliste:**
- [ ] X-Achse hat einen Namen
- [ ] Y-Achse hat einen Namen
- [ ] Einheiten sind klar (°C, €, km, etc.)
- [ ] Text ist groß genug zum Lesen

**✍️ Schreib deine Achsenbeschriftungen hier:**
```
X-Achse: _______________________________________________
Y-Achse: _______________________________________________
```

---

## 🎯 Schritt 3: Die Legende (10 Minuten)

### Wann brauche ich eine Legende?

**Legende brauchen:**
- ✅ Wenn du 2 oder mehr Linien hast
- ✅ Wenn du verschiedene Gruppen vergleichst

**Keine Legende brauchen:**
- ❌ Wenn du nur 1 Linie hast
- ❌ Wenn alles im Titel steht

### Übung 3: Legende hinzufügen

```python
# Zwei Städte vergleichen
plt.plot(df['datum'], df['hannover'], label='Hannover', color='teal')
plt.plot(df['datum'], df['berlin'], label='Berlin', color='coral')
plt.legend()  # ← Nicht vergessen!
```

**Checkliste:**
- [ ] Jede Linie hat ein `label=`
- [ ] `plt.legend()` ist im Code
- [ ] Labels sind kurz und klar
- [ ] Legende stört den Plot nicht

---

## 🎯 Schritt 4: Die Farben (10 Minuten)

### Welche Farben sind gut?

**✅ Gute Farben:**
- `'teal'` - Türkis (neutral, professionell)
- `'coral'` - Koralle (warm, freundlich)
- `'steelblue'` - Stahlblau (vertrauenswürdig)
- `'forestgreen'` - Waldgrün (natürlich)

**❌ Schlechte Kombinationen:**
- Rot + Grün (Farbenblindheit!)
- Zu viele verschiedene Farben (verwirrend!)
- Gelb auf weißem Hintergrund (nicht lesbar!)

### Übung 4: Farben wählen

```python
# ❌ Schlecht - Standard-Blau
plt.plot(x, y)

# ✅ Gut - Klare Farbe
plt.plot(x, y, color='teal', linewidth=2)
```

**Frage dich:**
- Sind die Farben gut unterscheidbar?
- Funktioniert es auch für farbenblinde Menschen?
- Sind es nicht zu viele Farben?

---

## 🎯 Schritt 5: Die Story (15 Minuten)

### Welche Frage beantwortet dein Plot?

Das ist das **WICHTIGSTE**!

**Beispiele:**

| Frage | Plot-Typ | Antwort |
|-------|----------|---------|
| Wird es wärmer? | Liniendiagramm | Ja, +8°C in 2 Wochen |
| Welche Stadt ist wärmer? | 2 Linien | Hannover ist 2°C wärmer |
| Wie viele Autos? | Balkendiagramm | 150 Autos verkauft |

### Übung 5: Deine Story

**Beantworte diese 3 Fragen:**

1. **PERCEIVING** - Was zeigt der Plot?
```
Der Plot zeigt: _______________________________________________
```

2. **INTERPRETING** - Was bedeutet das?
```
Das bedeutet: _______________________________________________
```

3. **COMPREHENDING** - Was habe ich gelernt?
```
Ich habe gelernt: _______________________________________________
```

---

## ✅ Vollständiges Beispiel

### Vorher (❌ Schlecht):
```python
plt.plot(x, y)
plt.show()
```

### Nachher (✅ Gut):
```python
import matplotlib.pyplot as plt
import pandas as pd

# Daten laden
df = pd.read_csv('data/hannover_temp.csv')

# Plot erstellen
fig, ax = plt.subplots(figsize=(10, 6))

# Daten plotten
ax.plot(df['datum'], df['temperatur'], 
        color='teal', 
        linewidth=2,
        label='Hannover')

# 1. TITEL ✅
ax.set_title('Temperatur in Hannover steigt von 12°C auf 20°C im Mai', 
             fontsize=14, fontweight='bold')

# 2. ACHSEN ✅
ax.set_xlabel('Datum (Mai 2026)', fontsize=12)
ax.set_ylabel('Temperatur (°C)', fontsize=12)

# 3. LEGENDE ✅ (wenn nötig)
ax.legend(loc='upper left')

# 4. FARBEN ✅ (schon oben: color='teal')

# Gitter (optional, aber hilfreich)
ax.grid(True, alpha=0.3)

# Layout optimieren
plt.tight_layout()

# Anzeigen
plt.show()

# 5. STORY ✅
# Frage: Wird es in Hannover wärmer?
# Antwort: Ja! Die Temperatur steigt von 12°C auf 20°C.
# Das ist perfekt für einen Ausflug Anfang Mai!
```

---

## 🎯 Deine Aufgabe für heute

Nimm deinen Plot von gestern und verbessere ihn:

### Checkliste:
- [ ] **Schritt 1:** Titel verbessert (10 Min)
- [ ] **Schritt 2:** Achsen beschriftet (10 Min)
- [ ] **Schritt 3:** Legende hinzugefügt (wenn nötig) (10 Min)
- [ ] **Schritt 4:** Farben gewählt (10 Min)
- [ ] **Schritt 5:** Story aufgeschrieben (15 Min)

**Pause:** 5 Minuten

**Gesamt:** 60 Minuten (mit Pausen!)

---

## 💡 Häufige Fehler

### Fehler 1: Zu schnell arbeiten
**Lösung:** Nimm dir Zeit! Jeder Schritt ist wichtig.

### Fehler 2: Keine Einheiten
**Lösung:** Immer Einheiten angeben (°C, €, km, etc.)

### Fehler 3: Zu viele Farben
**Lösung:** Maximal 3-4 verschiedene Farben

### Fehler 4: Keine Story
**Lösung:** Beantworte immer: "Welche Frage beantwortet dieser Plot?"

---

## 📚 Hilfreiche Befehle (Referenz)

```python
# Titel
plt.title('Mein Titel', fontsize=14, fontweight='bold')

# Achsen
plt.xlabel('X-Achse (Einheit)', fontsize=12)
plt.ylabel('Y-Achse (Einheit)', fontsize=12)

# Legende
plt.legend(loc='upper left')  # oder 'upper right', 'lower left', etc.

# Farben
color='teal'        # Türkis
color='coral'       # Koralle
color='steelblue'   # Stahlblau
color='forestgreen' # Waldgrün

# Linienstil
linewidth=2         # Dicke Linie
linestyle='--'      # Gestrichelt
marker='o'          # Punkte auf der Linie

# Gitter
plt.grid(True, alpha=0.3)  # alpha = Transparenz

# Speichern
plt.savefig('mein_plot.png', dpi=300, bbox_inches='tight')
```

---

## 🎤 Am Ende des Tages

Zeigt eure verbesserten Plots!

**Jede Person (2 Minuten):**
1. Zeig deinen alten Plot (von gestern)
2. Zeig deinen neuen Plot (von heute)
3. Was hast du verbessert?

---

## ✅ Erfolg!

Wenn du alle 5 Schritte gemacht hast, hast du einen **professionellen Plot**!

**Checkliste:**
- [x] Titel ist klar und aussagekräftig
- [x] Achsen sind beschriftet mit Einheiten
- [x] Legende ist vorhanden (wenn nötig)
- [x] Farben sind gut gewählt
- [x] Story ist klar

**Glückwunsch!** 🎉

---

*Sprachniveau: B1 (Deutsch)*  
*Dauer: 60 Minuten (mit Pausen!)*  
*Wichtig: LANGSAM arbeiten!*