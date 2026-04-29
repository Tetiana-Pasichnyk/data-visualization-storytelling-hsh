# 📓 Was haben wir gelernt? (Tag 1-2)

## 🎯 Überblick

In den ersten zwei Tagen haben wir die **Grundlagen der Datenvisualisierung** gelernt.

---

## 📚 Tag 1: Matplotlib Introduction

### Was ist Matplotlib?
- Eine Python-Bibliothek zum Erstellen von Diagrammen
- Die Basis für viele andere Visualisierungs-Tools
- Sehr flexibel und mächtig

### Wichtigste Befehle:

```python
import matplotlib.pyplot as plt

# 1. Daten vorbereiten
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# 2. Plot erstellen
plt.plot(x, y)

# 3. Beschriftungen hinzufügen
plt.title("Mein erstes Diagramm")
plt.xlabel("X-Achse")
plt.ylabel("Y-Achse")

# 4. Anzeigen
plt.show()
```

### Was wir gelernt haben:
- ✅ Einfache Liniendiagramme erstellen
- ✅ Farben ändern (`color='red'`)
- ✅ Linientypen ändern (`linestyle='--'`)
- ✅ Marker hinzufügen (`marker='o'`)
- ✅ Titel und Achsenbeschriftungen
- ✅ Legende hinzufügen (`plt.legend()`)
- ✅ Gitter anzeigen (`plt.grid(True)`)

---

## 📊 Tag 2: Pandas Plotting

### Was ist Pandas?
- Eine Bibliothek zum Arbeiten mit Tabellen (DataFrames)
- Kann direkt aus Tabellen plotten
- Sehr praktisch für echte Daten

### Wichtigste Befehle:

```python
import pandas as pd

# 1. Daten laden
df = pd.read_csv('data/hannover_temp.csv')

# 2. Daten anschauen
print(df.head())  # Erste 5 Zeilen

# 3. Direkt plotten
df.plot(x='datum', y='temperatur', kind='line')
plt.show()
```

### Was wir gelernt haben:
- ✅ CSV-Dateien laden (`pd.read_csv()`)
- ✅ Daten anschauen (`.head()`, `.info()`, `.describe()`)
- ✅ Direkt aus DataFrame plotten (`.plot()`)
- ✅ Verschiedene Plot-Typen (`kind='line'`, `kind='scatter'`, `kind='bar'`)
- ✅ Mehrere Spalten gleichzeitig plotten

---

## 🎨 Die wichtigsten Parameter

### Farben:
- `'red'`, `'blue'`, `'green'`, `'orange'`, `'purple'`
- Oder Hex-Codes: `'#FF5733'`

### Linientypen:
- `'-'` = durchgezogen (Standard)
- `'--'` = gestrichelt
- `'-.'` = Strich-Punkt
- `':'` = gepunktet

### Marker:
- `'o'` = Kreis
- `'s'` = Quadrat
- `'^'` = Dreieck
- `'*'` = Stern
- `'+'` = Plus

---

## 🤔 Häufige Probleme

### Problem 1: Plot wird nicht angezeigt
**Lösung:** `plt.show()` nicht vergessen!

### Problem 2: Datei nicht gefunden
**Lösung:** Pfad prüfen! Richtig: `'data/hannover_temp.csv'`

### Problem 3: Spaltenname falsch
**Lösung:** Mit `df.columns` alle Spaltennamen anzeigen

### Problem 4: Legende fehlt
**Lösung:** `label='Name'` beim Plotten + `plt.legend()` am Ende

---

## 📝 Checkliste: Kann ich das?

- [ ] Ich kann ein einfaches Liniendiagramm erstellen
- [ ] Ich kann Farben und Linientypen ändern
- [ ] Ich kann Titel und Achsenbeschriftungen hinzufügen
- [ ] Ich kann eine CSV-Datei laden
- [ ] Ich kann direkt aus einem DataFrame plotten
- [ ] Ich kann mehrere Linien in einem Diagramm zeigen
- [ ] Ich kann eine Legende hinzufügen

---

## 🚀 Nächste Schritte

**Tag 3:** Gruppenarbeit mit echten Daten!
- Wir arbeiten in 5 Gruppen
- Jede Gruppe bekommt eine Frage
- Wir erstellen unsere ersten eigenen Plots

**Siehe:** `02_anleitung.md` und `03_fragen.md`

---

## 📚 Zum Nachschlagen

- **Matplotlib Dokumentation:** https://matplotlib.org/
- **Pandas Dokumentation:** https://pandas.pydata.org/
- **Unsere Parameter-Referenz:** `woche-2/04_matplotlib_parameter.md`

---

*Wenn du Fragen hast, frag deinen Dozenten!* 💬