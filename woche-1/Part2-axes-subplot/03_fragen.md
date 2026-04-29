# 🎯 Tag 3: Gruppenarbeit - Deine Frage

## 📊 Aufgabe

Heute arbeitet ihr in **5 Gruppen**. Jede Gruppe bekommt **eine Frage**, die ihr mit Daten beantworten sollt.

---

## 📝 Beispiel-Fragen

### Gruppe 1: Temperatur-Vergleich
**Frage:** Ist es in Hannover wärmer als in Berlin im Mai?

**Daten:** 
- `data/hannover_temp.csv`
- `data/berlin_temp.csv` (oder andere Stadt)

**Was sollt ihr machen:**
1. Beide Datensätze laden
2. Temperatur plotten (Liniendiagramm)
3. Vergleichen: Wo ist es wärmer?
4. Antwort finden!

---

### Gruppe 3: Temperatur-Trend
**Frage:** Wird es in Hannover im Mai wärmer?

**Daten:**
- `data/hannover_temp.csv`

**Was sollt ihr machen:**
1. Daten laden
2. Temperatur über Zeit plotten
3. Trend erkennen: Steigt die Temperatur?
4. Antwort finden!

---

### Gruppe 2: Auto-Preise
**Frage:** Wie beeinflusst der Kilometerstand den Autopreis?

**Daten:**
- `data/car-sales.csv`

**Was sollt ihr machen:**
1. Daten laden
2. Scatter Plot: Kilometer vs. Preis
3. Beziehung erkennen
4. Antwort finden!

---

### Gruppe 4: [Eure eigene Frage]
**Frage:** _______________________________________

**Daten:** _______________________________________

**Was sollt ihr machen:**
1. _______________________________________
2. _______________________________________
3. _______________________________________

---

### Gruppe 5: [Eure eigene Frage]
**Frage:** _______________________________________

**Daten:** _______________________________________

**Was sollt ihr machen:**
1. _______________________________________
2. _______________________________________
3. _______________________________________

---

## ✅ Checkliste für eure Gruppenarbeit

### Schritt 1: Frage verstehen (5 Min)
- [ ] Welche Frage haben wir?
- [ ] Was wollen wir herausfinden?
- [ ] Welche Daten brauchen wir?

### Schritt 2: Daten laden (10 Min)
```python
import pandas as pd
import matplotlib.pyplot as plt

# Daten laden
df = pd.read_csv('data/hannover_temp.csv')

# Erste Zeilen anschauen
print(df.head())
```

### Schritt 3: Plot erstellen (20 Min)
```python
# Beispiel: Liniendiagramm
plt.plot(df['datum'], df['temperatur'], color='teal')
plt.title('Eure Frage hier')
plt.xlabel('X-Achse')
plt.ylabel('Y-Achse')
plt.grid(True)
plt.show()
```

### Schritt 4: Antwort finden (10 Min)
- [ ] Was zeigt der Plot?
- [ ] Was ist die Antwort auf unsere Frage?
- [ ] Können wir das erklären?

### Schritt 5: Präsentation vorbereiten (15 Min)
- [ ] Plot speichern: `plt.savefig('unser_plot.png')`
- [ ] Antwort aufschreiben (1-2 Sätze)
- [ ] Wer präsentiert?

---

## 🎤 Präsentation (5 Min pro Gruppe)

Erzählt uns:
1. **Eure Frage:** Was wolltet ihr herausfinden?
2. **Euer Plot:** Zeigt euren Plot
3. **Eure Antwort:** Was habt ihr herausgefunden?

**Beispiel:**
> "Unsere Frage war: Ist es in Hannover wärmer als in Berlin?
> Unser Plot zeigt die Temperatur in beiden Städten.
> Unsere Antwort: Ja, Hannover ist im Durchschnitt 2°C wärmer!"

---

## 💡 Tipps

### Wenn ihr nicht weiterkommt:
1. Schaut in die Notebooks von Tag 1 und 2
2. Fragt die anderen Gruppen
3. Fragt den Dozenten

### Wenn ihr fertig seid:
1. Verbessert euren Plot (Farben, Titel, etc.)
2. Findet eine zweite Beobachtung in den Daten
3. Helft anderen Gruppen

---

## 📚 Hilfreiche Befehle

```python
# Daten anschauen
df.head()           # Erste 5 Zeilen
df.info()           # Informationen über Spalten
df.describe()       # Statistiken

# Plotten
plt.plot(x, y)              # Liniendiagramm
plt.scatter(x, y)           # Scatter Plot
plt.bar(x, y)               # Balkendiagramm

# Beschriftungen
plt.title('Titel')
plt.xlabel('X-Achse')
plt.ylabel('Y-Achse')
plt.legend()
plt.grid(True)

# Speichern
plt.savefig('mein_plot.png')
```

---

## 🎯 Ziel des Tages

Am Ende des Tages sollt ihr:
- ✅ Eine Frage mit Daten beantwortet haben
- ✅ Einen Plot erstellt haben
- ✅ Eure Ergebnisse präsentieren können

**Viel Erfolg!** 🚀

---

*Sprachniveau: B1 (Deutsch)*  
*Dauer: 60 Minuten Gruppenarbeit + 25 Minuten Präsentationen*