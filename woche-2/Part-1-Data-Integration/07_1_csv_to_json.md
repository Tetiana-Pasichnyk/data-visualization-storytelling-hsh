# 📊 Von CSV zu JSON: Schritt für Schritt

## 🎯 Was lernen wir hier?

Wir haben eine **CSV-Datei** (`Sheet1.csv`) mit Namen von Studenten.  
Wir wollen diese Namen in unser **JSON-Objekt** (`messe_data`) hinzufügen.

**Warum?** Weil manche Studenten nur in der CSV sind, aber nicht in unserem Dictionary!

---

## 📂 Was ist eine CSV-Datei?

**CSV** = **C**omma **S**eparated **V**alues (Komma-getrennte Werte)

**Beispiel:**
```csv
Name;Wart ihr auf der Messe?;Mit Leuten gesprochen?;Wieviele Leute gesehen?
Rowaida;Nein;Nein;0
Hadis;Ja;Ja;3
Anton;Nein;Nein;0
```

**Was bedeutet das?**
- Erste Zeile = **Spaltennamen** (Header)
- Jede weitere Zeile = **Ein Student** (eine Zeile = ein Record)
- `;` = **Trennzeichen** (Separator) - trennt die Spalten

**In Excel sieht das so aus:**

| Name    | Wart ihr auf der Messe? | Mit Leuten gesprochen? | Wieviele Leute gesehen? |
|---------|-------------------------|------------------------|-------------------------|
| Rowaida | Nein                    | Nein                   | 0                       |
| Hadis   | Ja                      | Ja                     | 3                       |
| Anton   | Nein                    | Nein                   | 0                       |

---

## 🎯 Unser Ziel

**Vorher (nur Dictionary):**
```python
messe_data = {
    "Blerina": {...},
    "Menjung": {...},
    "Hani": {...}
}
# 15 Studenten
```

**Nachher (Dictionary + CSV):**
```python
messe_data = {
    "Blerina": {...},
    "Menjung": {...},
    "Hani": {...},
    "Rowaida": {...},  # ← NEU aus CSV!
    "Anton": {...},    # ← NEU aus CSV!
    "Bernard": {...}   # ← NEU aus CSV!
}
# 20 Studenten
```

---

## 🐌 SEHR LANGSAM: Schritt für Schritt

### Schritt 1: CSV-Datei laden

**Code:**
```python
import pandas as pd

# CSV laden
df = pd.read_csv('./Sheet1.csv', delimiter=';', encoding='latin-1')
```

**Was macht das?**
- `pd.read_csv()` = Pandas liest die CSV-Datei
- `delimiter=';'` = Trennzeichen ist `;` (nicht `,`)
- `encoding='latin-1'` = Zeichensatz für deutsche Umlaute (ä, ö, ü)

**Ergebnis:**
```python
print(df.head())
```
```
      Name Wart ihr auf der Messe? Mit Leuten gesprochen? Wieviele Leute gesehen?
0  Rowaida                    Nein                   Nein                        0
1    Hadis                      Ja                     Ja                        3
2    Anton                    Nein                   Nein                        0
```

**Jetzt haben wir ein DataFrame!** ✅

---

### Schritt 2: Namen aus CSV extrahieren

**Problem:** Wir brauchen nur die **Namen**, nicht alle Spalten!

**Code:**
```python
# Nur die Spalte "Name" nehmen
x = df['Name']
print(x)
```

**Ergebnis:**
```
0    Rowaida
1      Hadis
2      Anton
3          x
4    Bernard
5     Yasser
Name: Name, dtype: object
```

**Was ist `x`?**
- `x` ist eine **Pandas Series** (wie eine Liste, aber mit Index)
- Enthält alle Namen aus der CSV

---

### Schritt 3: Leere Werte entfernen

**Problem:** Manchmal gibt es **leere Zellen** in der CSV!

**Beispiel:**
```csv
Name
Rowaida
Hadis

Anton
```
Die dritte Zeile ist leer! Das ist `NaN` (Not a Number).

**Code:**
```python
# Liste für saubere Namen
sauberx = []

# Durch alle Namen gehen
for elem in x:
    # Wenn der Name NICHT leer ist
    if not pd.isna(elem):
        # Dann zur Liste hinzufügen
        sauberx.append(elem)

print(sauberx)
```

**Ergebnis:**
```python
['Rowaida', 'Hadis', 'Anton', 'x', 'Bernard', 'Yasser']
```

**Was macht `pd.isna(elem)`?**
- `pd.isna()` = Prüft, ob ein Wert leer ist (NaN)
- `not pd.isna()` = Prüft, ob ein Wert NICHT leer ist
- Nur nicht-leere Namen kommen in `sauberx`

**Jetzt haben wir eine saubere Liste mit Namen!** ✅

---

### Schritt 4: Namen zum JSON-Objekt hinzufügen

**Unser JSON-Objekt (Dictionary):**
```python
messe_data = {
    "Blerina": {
        "attended_messe": False,
        "spoke_to_people": False,
        "positions_seen": 0,
        "companies_seen": [],
        "career_fields_seen": ["Data Analyzer"]
    },
    "Menjung": {...},
    "Hani": {...}
}
```

**Wir wollen hinzufügen:**
```python
"Rowaida": {
    "attended_messe": None,
    "spoke_to_people": None,
    "positions_seen": None,
    "companies_seen": None,
    "career_fields_seen": None,
    "notes": "Added from CSV"
}
```

**Code:**
```python
# Kopie vom Original machen (wichtig!)
ziel = messe_data.copy()

# Durch alle Namen aus CSV gehen
for name in sauberx:
    # Neuen Eintrag erstellen
    ziel[name] = {
        "attended_messe": None,
        "spoke_to_people": None,
        "positions_seen": None,
        "companies_seen": None,
        "career_fields_seen": None,
        "notes": "Added from CSV"
    }

print(f"Vorher: {len(messe_data)} Studenten")
print(f"Nachher: {len(ziel)} Studenten")
```

**Ergebnis:**
```
Vorher: 15 Studenten
Nachher: 20 Studenten
```

**Was macht `.copy()`?**
- Ohne `.copy()`: Wir ändern das Original!
- Mit `.copy()`: Wir erstellen eine Kopie und ändern die Kopie
- Das Original bleibt unverändert

**Jetzt haben wir alle Namen im JSON-Objekt!** ✅

---

### Schritt 5: Daten aus CSV übernehmen (BONUS)

**Problem:** Wir haben nur `None` für die neuen Studenten. Aber die CSV hat echte Daten!

**Beispiel für Rowaida:**
```csv
Name;Wart ihr auf der Messe?;Mit Leuten gesprochen?;Wieviele Leute gesehen?
Rowaida;Nein;Nein;0
```

**Wir wollen:**
```python
"Rowaida": {
    "attended_messe": False,  # ← aus CSV: "Nein"
    "spoke_to_people": False, # ← aus CSV: "Nein"
    "positions_seen": 0,      # ← aus CSV: 0
    "companies_seen": [],
    "career_fields_seen": [],
    "notes": "Added from CSV"
}
```

**Code:**
```python
def appendCsvToJsonObject(df, messe_data):
    """
    Fügt CSV-Daten zu messe_data hinzu
    """
    # Kopie erstellen
    ziel = messe_data.copy()
    
    # Durch alle Namen aus CSV gehen
    for name in sauberx:
        # Finde die Zeile für diesen Namen
        row = df[df['Name'] == name]
        
        # Wenn der Name gefunden wurde
        if not row.empty:
            # Erste (und einzige) Zeile nehmen
            row = row.iloc[0]
            
            # Daten aus CSV übernehmen
            ziel[name] = {
                "attended_messe": row['Wart ihr auf der Messe?'] == 'Ja',
                "spoke_to_people": row['Mit Leuten gesprochen?'] == 'Ja',
                "positions_seen": int(row['Wieviele Leute gesehen?']) if pd.notna(row['Wieviele Leute gesehen?']) else 0,
                "companies_seen": [],
                "career_fields_seen": [],
                "notes": "Added from CSV"
            }
    
    return ziel

# Funktion aufrufen
messe_data_complete = appendCsvToJsonObject(df, messe_data)
```

**Was macht das?**
1. `df[df['Name'] == name]` = Finde die Zeile, wo Name = "Rowaida"
2. `row.iloc[0]` = Nimm die erste (und einzige) Zeile
3. `row['Wart ihr auf der Messe?'] == 'Ja'` = Prüfe, ob "Ja" → `True` oder `False`
4. `int(row['...'])` = Wandle Text in Zahl um
5. `pd.notna()` = Prüfe, ob Wert nicht leer ist

**Jetzt haben wir echte Daten aus der CSV!** ✅

---

## 🔄 Zusammenfassung: Der komplette Prozess

```python
# ============================================
# SCHRITT 1: CSV laden
# ============================================
import pandas as pd

df = pd.read_csv('./Sheet1.csv', delimiter=';', encoding='latin-1')

# ============================================
# SCHRITT 2: Namen extrahieren
# ============================================
x = df['Name']

# ============================================
# SCHRITT 3: Leere Werte entfernen
# ============================================
sauberx = []
for elem in x:
    if not pd.isna(elem):
        sauberx.append(elem)

# ============================================
# SCHRITT 4: Zum JSON-Objekt hinzufügen
# ============================================
ziel = messe_data.copy()

for name in sauberx:
    # Finde Zeile in CSV
    row = df[df['Name'] == name]
    
    if not row.empty:
        row = row.iloc[0]
        
        # Daten übernehmen
        ziel[name] = {
            "attended_messe": row['Wart ihr auf der Messe?'] == 'Ja',
            "spoke_to_people": row['Mit Leuten gesprochen?'] == 'Ja',
            "positions_seen": int(row['Wieviele Leute gesehen?']) if pd.notna(row['Wieviele Leute gesehen?']) else 0,
            "companies_seen": [],
            "career_fields_seen": [],
            "notes": "Added from CSV"
        }

# ============================================
# SCHRITT 5: Ergebnis prüfen
# ============================================
print(f"Vorher: {len(messe_data)} Studenten")
print(f"Nachher: {len(ziel)} Studenten")
print(f"Neue Studenten: {len(ziel) - len(messe_data)}")
```

---

## 📊 Visualisierung: Was passiert?

```
CSV-Datei (Sheet1.csv)
    ↓
Pandas DataFrame (df)
    ↓
Namen extrahieren (df['Name'])
    ↓
Leere Werte entfernen (sauberx)
    ↓
Durch Namen iterieren (for name in sauberx)
    ↓
Zeile in CSV finden (df[df['Name'] == name])
    ↓
Daten übernehmen (row['Spalte'])
    ↓
Zum JSON-Objekt hinzufügen (ziel[name] = {...})
    ↓
Fertig! (messe_data_complete)
```

---

## 🎯 Warum ist das wichtig?

### Vorher (nur manuelles Dictionary):
```python
# ❌ Mühsam: Jeden Studenten manuell eingeben
messe_data = {
    "Blerina": {...},
    "Menjung": {...},
    # ... 15 Studenten
}
```

### Nachher (CSV + Dictionary):
```python
# ✅ Einfach: CSV laden und automatisch hinzufügen
df = pd.read_csv('Sheet1.csv')
messe_data = appendCsvToJsonObject(df, messe_data)
# ... 20 Studenten (15 + 5 aus CSV)
```

**Vorteile:**
- ✅ Schneller: Keine manuelle Eingabe
- ✅ Weniger Fehler: CSV ist schon strukturiert
- ✅ Flexibel: Neue Studenten einfach zur CSV hinzufügen
- ✅ Wiederverwendbar: Funktion kann für andere CSVs genutzt werden

---

## 🔍 Vergleich: Drei Datenquellen

### 1. Manuelles Dictionary (Python-Code)
```python
messe_data = {
    "Blerina": {
        "attended_messe": False,
        "spoke_to_people": False,
        "positions_seen": 0
    }
}
```
**Verwendung:** ✅ Gut für kleine Datenmengen, volle Kontrolle

### 2. CSV-Datei (Excel/Google Sheets)
```csv
Name;Wart ihr auf der Messe?;Mit Leuten gesprochen?
Rowaida;Nein;Nein
```
**Verwendung:** ✅✅ Gut für viele Daten, einfach zu bearbeiten

### 3. JSON-Datei (strukturiert)
```json
{
  "Blerina": {
    "attended_messe": false,
    "spoke_to_people": false,
    "positions_seen": 0
  }
}
```
**Verwendung:** ✅✅✅ Perfekt für Datenaustausch, APIs, Web

---

## 🚀 Übung: Mach es selbst!

### Aufgabe 1: Namen extrahieren

**Gegeben:**
```python
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', None, 'Charlie', 'David']
})
```

**Aufgabe:** Extrahiere alle Namen (ohne `None`) in eine Liste `names`.

**Lösung:**
```python
names = []
for name in df['Name']:
    if not pd.isna(name):
        names.append(name)

print(names)  # ['Alice', 'Bob', 'Charlie', 'David']
```

### Aufgabe 2: CSV zu Dictionary

**Gegeben:**
```csv
Name;Age
Alice;25
Bob;30
```

**Aufgabe:** Erstelle ein Dictionary:
```python
{
    "Alice": {"age": 25},
    "Bob": {"age": 30}
}
```

**Lösung:**
```python
import pandas as pd

df = pd.read_csv('data.csv', delimiter=';')
result = {}

for index, row in df.iterrows():
    result[row['Name']] = {
        "age": row['Age']
    }

print(result)
```

### Aufgabe 3: Mit echten Daten

**Öffne das Notebook:** `student_data_structured copy.ipynb`

**Schau dir an:**
1. Wie wird die CSV geladen? (Zeile 275)
2. Wie werden Namen extrahiert? (Zeile 279-283)
3. Wie werden Daten zum Dictionary hinzugefügt? (Zeile 441-462)

---

## 📚 Siehe auch

- **CSV-Daten:** `data/Sheet1.csv` (Unsere Studenten-Daten)
- **Dictionary-Daten:** `06_beispiel_form.md` (Manuell erfasste Daten)
- **Data Integration:** `07_2_data_integration.md` (Dictionary → DataFrame)
- **Notebook:** `student_data_structured copy.ipynb` (Komplettes Beispiel)
- **Pandas Docs:** https://pandas.pydata.org/docs/

---

## 💡 Wichtigste Erkenntnisse

1. **CSV = Tabelle** = Zeilen und Spalten, wie Excel
2. **Pandas liest CSV** = `pd.read_csv()` macht CSV zu DataFrame
3. **Namen extrahieren** = `df['Name']` gibt eine Spalte zurück
4. **Leere Werte entfernen** = `pd.isna()` prüft auf leere Werte
5. **Zum Dictionary hinzufügen** = `dict[key] = value` fügt neuen Eintrag hinzu
6. **Daten übernehmen** = `row['Spalte']` gibt Wert aus CSV zurück

**Merke:** CSV ist strukturiert, aber nicht so flexibel wie JSON. Wir kombinieren beide! 📊✨

---

## 🔗 Nächster Schritt

**Jetzt weißt du:**
- ✅ Wie man CSV lädt
- ✅ Wie man Namen extrahiert
- ✅ Wie man zum JSON-Objekt hinzufügt

**Als Nächstes:** `07_2_data_integration.md`
- Wie man Dictionary → DataFrame umwandelt
- Wie man strukturierte Daten analysiert
- Wie man CSV speichert

---

*Von CSV zu JSON - Daten zusammenführen!* 📊→📦