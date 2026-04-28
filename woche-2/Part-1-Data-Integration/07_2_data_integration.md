# 🔄 Data Integration: Von Unstrukturiert zu Strukturiert

## 🎯 Was lernen wir hier?

In `06_beispiel_form.md` haben wir **unstrukturierte Daten** gesehen:
```python
data = {
    "Blerina": [False, False, 0, ["Data Analyzer"]],
    "Menjung": [True, True, 15, ["Quantum"]]
}
```

**Problem:** Pandas kann damit nicht arbeiten! ❌

**Lösung:** Data Integration - Wir wandeln die Daten **Schritt für Schritt** um! ✅

---

## 📚 Was ist Data Integration?

**Data Integration** = Daten aus verschiedenen Quellen **zusammenführen** und **strukturieren**

**In unserem Fall:**
- **Quelle:** Unstrukturiertes Python-Dictionary
- **Ziel:** Strukturiertes Pandas DataFrame (wie eine Excel-Tabelle)

**Warum?**
- ✅ Pandas kann damit arbeiten
- ✅ Wir können analysieren (`.mean()`, `.sum()`, etc.)
- ✅ Wir können visualisieren (`.plot()`)
- ✅ Wir können als CSV speichern

---

## 🐌 SEHR LANGSAM: Schritt für Schritt

### Schritt 1: Das Problem verstehen

**Unsere unstrukturierten Daten:**
```python
data = {
    "Blerina": [False, False, 0, ["Data Analyzer"]],
    "Menjung": [True, True, 15, ["Quantum"], "Fullstack"]
}
```

**Was bedeutet das?**
- `"Blerina"` = Name (ist ein **Key**)
- `[False, False, 0, ...]` = Werte (ist eine **Liste**)

**Problem:**
- ❌ Keine Spaltennamen!
- ❌ Was bedeutet `False`? Was bedeutet `0`?
- ❌ Pandas braucht Spaltennamen!

---

### Schritt 2: Spaltennamen definieren

**Wir müssen wissen, was jede Position bedeutet:**

```python
# Position 0 = attended_messe (Ja/Nein)
# Position 1 = spoke_to_people (Ja/Nein)
# Position 2 = positions_seen (Anzahl)
# Position 3 = companies_seen (Liste)
# Position 4 = career_fields_seen (Liste)

# Beispiel:
"Blerina": [False, False, 0, ["Data Analyzer"]]
#          ↑      ↑      ↑   ↑
#          |      |      |   └─ career_fields_seen
#          |      |      └───── positions_seen
#          |      └──────────── spoke_to_people
#          └─────────────────── attended_messe
```

**Jetzt wissen wir, was die Daten bedeuten!** ✅

---

### Schritt 3: Ein Beispiel umwandeln

**Vorher (unstrukturiert):**
```python
"Blerina": [False, False, 0, ["Data Analyzer"]]
```

**Nachher (strukturiert):**
```python
{
    "Student": "Blerina",
    "attended_messe": False,
    "spoke_to_people": False,
    "positions_seen": 0,
    "companies_seen": [],
    "career_fields_seen": ["Data Analyzer"]
}
```

**Was haben wir gemacht?**
1. ✅ Name ist jetzt eine **Spalte** (`"Student": "Blerina"`)
2. ✅ Jeder Wert hat einen **Namen** (`"attended_messe": False`)
3. ✅ Alles ist ein **Dictionary** (wie eine Zeile in einer Tabelle)

---

### Schritt 4: Alle Daten umwandeln

**Vorher (unstrukturiert):**
```python
data = {
    "Blerina": [False, False, 0, ["Data Analyzer"]],
    "Menjung": [True, True, 15, ["Quantum"], "Fullstack"]
}
```

**Nachher (strukturiert):**
```python
structured_data = {
    "Blerina": {
        "attended_messe": False,
        "spoke_to_people": False,
        "positions_seen": 0,
        "companies_seen": [],
        "career_fields_seen": ["Data Analyzer"]
    },
    "Menjung": {
        "attended_messe": True,
        "spoke_to_people": True,
        "positions_seen": 15,
        "companies_seen": ["Quantum"],
        "career_fields_seen": ["Fullstack"]
    }
}
```

**Jetzt haben alle Werte Namen!** ✅

---

### Schritt 5: In DataFrame umwandeln

**Pandas kann jetzt damit arbeiten:**

```python
import pandas as pd

# Dictionary → DataFrame
df = pd.DataFrame.from_dict(structured_data, orient='index')
```

**Was macht `orient='index'`?**
- `orient='index'` = Namen (`"Blerina"`, `"Menjung"`) werden zu **Zeilen-Index**
- Ohne `orient='index'` würden Namen zu **Spalten** werden (falsch!)

**Ergebnis:**
```
           attended_messe  spoke_to_people  positions_seen  companies_seen  career_fields_seen
Blerina            False            False               0              []     [Data Analyzer]
Menjung             True             True              15       [Quantum]          [Fullstack]
```

**Fast fertig!** ✅

---

### Schritt 6: Index zu Spalte machen

**Problem:** Namen sind im **Index**, nicht in einer Spalte

**Lösung:**
```python
df.index.name = 'Student'  # Index benennen
df = df.reset_index()       # Index zu Spalte machen
```

**Ergebnis:**
```
   Student  attended_messe  spoke_to_people  positions_seen  companies_seen  career_fields_seen
0  Blerina           False            False               0              []     [Data Analyzer]
1  Menjung            True             True              15       [Quantum]          [Fullstack]
```

**Perfekt!** ✅ Jetzt ist `Student` eine normale Spalte!

---

### Schritt 7: Als CSV speichern

**Jetzt können wir die Daten speichern:**

```python
df.to_csv('student_data_structured.csv', index=False)
```

**Was macht `index=False`?**
- Ohne `index=False`: CSV hätte eine extra Spalte mit Zahlen (0, 1, 2, ...)
- Mit `index=False`: Nur die echten Spalten werden gespeichert

**Ergebnis (CSV-Datei):**
```csv
Student,attended_messe,spoke_to_people,positions_seen,companies_seen,career_fields_seen
Blerina,False,False,0,[],"[""Data Analyzer""]"
Menjung,True,True,15,"[""Quantum""]","[""Fullstack""]"
```

**Fertig!** ✅ Jetzt können wir die Daten in Excel öffnen!

---

## 🔄 Zusammenfassung: Der komplette Prozess

```python
# ============================================
# SCHRITT 1: Unstrukturierte Daten
# ============================================
data = {
    "Blerina": [False, False, 0, ["Data Analyzer"]],
    "Menjung": [True, True, 15, ["Quantum"], "Fullstack"]
}

# ============================================
# SCHRITT 2: Spaltennamen definieren
# ============================================
# Position 0 = attended_messe
# Position 1 = spoke_to_people
# Position 2 = positions_seen
# Position 3 = companies_seen
# Position 4 = career_fields_seen

# ============================================
# SCHRITT 3: Strukturieren
# ============================================
structured_data = {}

for name, values in data.items():
    structured_data[name] = {
        "attended_messe": values[0] if len(values) > 0 else None,
        "spoke_to_people": values[1] if len(values) > 1 else None,
        "positions_seen": values[2] if len(values) > 2 else None,
        "companies_seen": values[3] if len(values) > 3 else [],
        "career_fields_seen": values[4] if len(values) > 4 else []
    }

# ============================================
# SCHRITT 4: DataFrame erstellen
# ============================================
import pandas as pd

df = pd.DataFrame.from_dict(structured_data, orient='index')
df.index.name = 'Student'
df = df.reset_index()

# ============================================
# SCHRITT 5: Als CSV speichern
# ============================================
df.to_csv('student_data_structured.csv', index=False)

# ============================================
# SCHRITT 6: Analysieren!
# ============================================
print(df.head())
print(df['attended_messe'].value_counts())
print(df['positions_seen'].mean())
```

---

## 🎯 Warum ist das wichtig?

### Vorher (unstrukturiert):
```python
# ❌ Kompliziert
data = {"Blerina": [False, False, 0, ["Data Analyzer"]]}
attended = data["Blerina"][0]  # Was ist Position 0?
```

### Nachher (strukturiert):
```python
# ✅ Einfach
df = pd.DataFrame(...)
attended = df[df['Student'] == 'Blerina']['attended_messe'].values[0]
# Oder noch einfacher:
attended = df.loc[0, 'attended_messe']
```

### Analyse vorher (unstrukturiert):
```python
# ❌ Sehr kompliziert
total = 0
count = 0
for name, values in data.items():
    if len(values) > 2 and values[2] is not None:
        total += values[2]
        count += 1
average = total / count if count > 0 else 0
```

### Analyse nachher (strukturiert):
```python
# ✅ Eine Zeile!
average = df['positions_seen'].mean()
```

---

## 📊 Von CSV zu DataFrame

**Wenn die Daten schon als CSV vorliegen** (wie `data/Sheet1.csv`):

```python
import pandas as pd

# CSV laden
df = pd.read_csv('data/Sheet1.csv', sep=';', encoding='utf-8')

# Fertig! Daten sind schon strukturiert!
print(df.head())
print(df.columns)
```

**Das ist viel einfacher!** ✅

**Aber:** Manchmal haben wir nur unstrukturierte Daten (wie unser RAW DATA Dictionary). Dann müssen wir Data Integration machen!

---

## 🔍 Vergleich: Drei Formate

### Format 1: Unstrukturiert (Dictionary mit Name als Key)
```python
data = {
    "Blerina": [False, False, 0, ["Data Analyzer"]]
}
```
**Verwendung:** ❌ Schwierig, nicht für Pandas geeignet

### Format 2: Strukturiert (Dictionary mit Spaltennamen)
```python
data = {
    "Blerina": {
        "attended_messe": False,
        "spoke_to_people": False,
        "positions_seen": 0,
        "career_fields_seen": ["Data Analyzer"]
    }
}
```
**Verwendung:** ✅ Kann in DataFrame umgewandelt werden

### Format 3: Strukturiert (DataFrame)
```python
df = pd.DataFrame({
    'Student': ['Blerina'],
    'attended_messe': [False],
    'spoke_to_people': [False],
    'positions_seen': [0],
    'career_fields_seen': [["Data Analyzer"]]
})
```
**Verwendung:** ✅✅ Perfekt für Analyse und Visualisierung!

### Format 4: Strukturiert (CSV)
```csv
Student,attended_messe,spoke_to_people,positions_seen,career_fields_seen
Blerina,False,False,0,"[""Data Analyzer""]"
```
**Verwendung:** ✅✅✅ Kann in Excel geöffnet werden, portabel, universell!

---

## 🚀 Übung: Mach es selbst!

### Aufgabe 1: Einfache Umwandlung

**Gegeben:**
```python
data = {
    "Alice": [True, True, 5],
    "Bob": [False, False, 0]
}
```

**Aufgabe:** Wandle in DataFrame um mit Spalten:
- `Student`
- `attended`
- `spoke`
- `positions`

**Lösung:**
```python
import pandas as pd

# Strukturieren
structured = {}
for name, values in data.items():
    structured[name] = {
        "attended": values[0],
        "spoke": values[1],
        "positions": values[2]
    }

# DataFrame erstellen
df = pd.DataFrame.from_dict(structured, orient='index')
df.index.name = 'Student'
df = df.reset_index()

print(df)
```

### Aufgabe 2: Mit echten Daten

**Öffne das Notebook:** `student_data_structured copy.ipynb`

**Schau dir an:**
1. Wie werden die RAW DATA strukturiert?
2. Wie wird das DataFrame erstellt?
3. Wie werden die Daten analysiert?

---

## 📚 Siehe auch

- **RAW DATA:** `06_beispiel_form.md` (Unstrukturierte Daten)
- **Notebook:** `student_data_structured copy.ipynb` (Komplettes Beispiel)
- **CSV-Daten:** `data/Sheet1.csv` (Schon strukturiert!)
- **Pandas Docs:** https://pandas.pydata.org/docs/

---

## 💡 Wichtigste Erkenntnisse

1. **Unstrukturierte Daten** = Name als Key, Werte in Listen ohne Namen
2. **Strukturierte Daten** = Spaltennamen, Zeilen als Records, Tabellen-Format
3. **Data Integration** = Umwandlung von unstrukturiert zu strukturiert
4. **Pandas braucht Struktur** = DataFrame funktioniert nur mit Spaltennamen
5. **CSV ist strukturiert** = Kann direkt geladen werden mit `pd.read_csv()`

**Merke:** 80% der Datenanalyse ist Datenbereinigung und -strukturierung! 🧹

---

*Data Integration macht Daten nutzbar!* 🔄✨