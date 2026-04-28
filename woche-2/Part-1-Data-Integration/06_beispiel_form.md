# 📝 Beispiel-Formular: Umfrage zur Hannover Messe

## 🎯 Echtes Beispiel aus dem Kurs

Dies ist ein **echtes Formular**, das im Kurs verwendet wurde!

---

## 📋 Entstehungsgeschichte

### Ursprüngliche Datensammlung (Manuell) - UNSTRUKTURIERTE DATEN

Die Daten wurden **zuerst manuell** als Python-Dictionary gesammelt. **Dies sind UNSTRUKTURIERTE DATEN** - das bedeutet:

❌ **Keine festen Spaltennamen** - Jeder Student ist ein Key (z.B. `"Blerina"`)
❌ **Keine Zeilen wie in einer Tabelle** - Daten sind verschachtelt
❌ **Nicht wie CSV** - Kann nicht direkt in Excel geöffnet werden
❌ **Nicht wie DataFrame** - Pandas kann damit nicht direkt arbeiten

**Dies ist die ECHTE, unbearbeitete Version** mit allen Fehlern und Inkonsistenzen:

```python
# ============================================
# RAW DATA - Genau so wie es gesammelt wurde!
# ============================================

# Spezialisierung (aus separater Umfrage)
data1 = {'full-stack': 7, 'BI/DA': 3}

# Messe-Daten (manuell gesammelt)
# Format: [Messe besucht?, Leute gesprochen?, Wieviele Stellen?, Unternehmen gesehen, Welche Berufe]
data1 = {
    "Blerina": [False, False, 0, ["Data Analyzer"]],
    'Menjung': [True, True, 15, ["","","","","",""], "Quantum (Fullstack)"],
    'Hani': [True, True, 7, [], ["Siemens", "Nestle", "SudiArabia", "Adesso"]], "Frontend / UX" "BI"
    "Hadis": [True, True, 3, ["Siemens"], "WebEntwicklung"]
    'Yarema': [True, True, 5, ['Software-Entwickler'], ["Microsoft"]]
    'Viktoriia': [False, False, 0, ["Marketing/Data Analytics"]]
    "Andi": False, False, 0, ["Technician"], "System-Administrator" #https://careers.ibm.com/en_US/careersint/JobDetail?jobId=102605
    "Ihor": "['Bundeswehr', 'Siemens']", "System-Administrator" #https://careers.ibm.com/en_US/careersint/JobDetail?jobId=102605
    'Svitlana': [True, True, 7, ['KI Engineer'], ['AWS', 'Agile Robots', "Bosch", {"HsH":False}, "Siemens", "Leibniz Uni"]], "Data Science"
    
    'Sofiia': [True, True, 5, ["AWS", "Microsoft", "Bundeswehr", 'Food Court']], ["FullStack"],
    'Kareem': [True, True, 2, ["SAP", "Microsoft", "Bundeswehr", "Lenovo"]], ["Frontend"],
    'Omar': [True, True, 2, ["Bundeswehr"]], [""]
    'Tetiana': [True, True, ["Bundeswehr", "BMW"]], ["Frontend"]
    "Yevhen": ["Samsung", "Bundeswehr", "BMW"], ["FullStack"]
}

# Json (Kommentar im Original-Code)
```

**⚠️ Probleme in den RAW DATA:**
1. **Inkonsistente Syntax:** Mal `"`, mal `'`, fehlende Kommas
2. **Fehlende Werte:** Leere Strings `""`, fehlende Felder
3. **Gemischte Datentypen:** Strings, Listen, Dicts durcheinander
4. **Kommentare mit URLs:** IBM-Job-Links in den Daten
5. **Verschachtelte Strukturen:** `{"HsH":False}` mitten in der Liste
6. **Inkonsistente Formatierung:** Mal Listen, mal einzelne Strings

---

## 🔄 UNSTRUKTURIERT vs. STRUKTURIERT

### Was bedeutet "unstrukturiert"?

**Unstrukturierte Daten (JSON-ähnlich):**
```python
# Name ist der KEY (nicht eine Spalte!)
data = {
    "Blerina": [False, False, 0, ["Data Analyzer"]],
    "Menjung": [True, True, 15, ["Quantum"], "Fullstack"]
}
```

**Problem:**
- ❌ Jeder Student ist ein **eigener Key**
- ❌ Keine **Spaltennamen** wie "attended_messe", "spoke_to_people"
- ❌ Werte sind in **Listen** ohne Beschreibung
- ❌ Pandas kann damit **nicht direkt** arbeiten
- ❌ Kann **nicht als CSV** gespeichert werden

### Was bedeutet "strukturiert"?

**Strukturierte Daten (CSV/DataFrame):**
```csv
Student,attended_messe,spoke_to_people,positions_seen,companies_seen
Blerina,False,False,0,"Data Analyzer"
Menjung,True,True,15,Quantum
```

**Vorteile:**
- ✅ **Spaltennamen** beschreiben die Daten
- ✅ **Zeilen** sind einzelne Datensätze (Records)
- ✅ **Tabellen-Format** wie in Excel
- ✅ Pandas kann es **direkt laden**: `pd.read_csv()`
- ✅ Kann in **Excel geöffnet** werden

### Vergleich: Gleiche Daten, verschiedene Formate

#### Format 1: UNSTRUKTURIERT (JSON-ähnlich)
```python
# Name als KEY
data = {
    "Blerina": {
        "attended_messe": False,
        "spoke_to_people": False,
        "positions_seen": 0
    }
}
```

**Zugriff:**
```python
# Kompliziert!
name = "Blerina"
attended = data[name]["attended_messe"]  # False
```

#### Format 2: STRUKTURIERT (DataFrame)
```python
# Name als SPALTE
df = pd.DataFrame({
    'Student': ['Blerina'],
    'attended_messe': [False],
    'spoke_to_people': [False],
    'positions_seen': [0]
})
```

**Zugriff:**
```python
# Einfach!
attended = df[df['Student'] == 'Blerina']['attended_messe'].values[0]  # False
# Oder noch einfacher:
attended = df.loc[0, 'attended_messe']  # False
```

#### Format 3: STRUKTURIERT (CSV)
```csv
Student,attended_messe,spoke_to_people,positions_seen
Blerina,False,False,0
```

**Zugriff:**
```python
# Laden und nutzen
df = pd.read_csv('data.csv')
print(df['attended_messe'])  # Spalte anzeigen
```

### Warum ist CSV/DataFrame besser?

| Aspekt | Unstrukturiert (JSON) | Strukturiert (CSV/DataFrame) |
|--------|----------------------|------------------------------|
| **Spaltennamen** | ❌ Keine festen Namen | ✅ Klare Spaltennamen |
| **Zeilen** | ❌ Verschachtelt | ✅ Eine Zeile = Ein Datensatz |
| **Pandas** | ❌ Kompliziert | ✅ Direkt nutzbar |
| **Excel** | ❌ Nicht möglich | ✅ Kann geöffnet werden |
| **Analyse** | ❌ Schwierig | ✅ Einfach mit `.mean()`, `.sum()` etc. |
| **Visualisierung** | ❌ Erst umwandeln | ✅ Direkt plotten |

### Das Problem mit unserem RAW DATA

Unsere RAW DATA haben **zwei Probleme**:

1. **Unstrukturiert:** Name ist Key, nicht Spalte
2. **Chaotisch:** Syntax-Fehler, fehlende Werte, gemischte Typen

**Lösung:** Data Integration (siehe `07_2_data_integration.md`)

### Datenverarbeitung: Von RAW zu STRUKTURIERT

Diese chaotischen RAW DATA wurden in **3 Schritten** bereinigt:

#### **Schritt 1: Datenstruktur verstehen**

Die RAW DATA folgen diesem Muster (mit vielen Fehlern):
```python
# Format (sollte sein):
"Name": [attended_messe, spoke_to_people, positions_seen, companies_seen, career_fields_seen]

# Beispiele:
"Blerina": [False, False, 0, ["Data Analyzer"]]  # ✅ Korrekt
"Andi": False, False, 0, ["Technician"], "System-Administrator"  # ❌ Fehlt Liste
"Ihor": "['Bundeswehr', 'Siemens']", "System-Administrator"  # ❌ String statt Liste
```

#### **Schritt 2: Manuelle Bereinigung**

Jeder Eintrag wurde **manuell korrigiert** und in ein strukturiertes Dictionary umgewandelt:

```python
# BEREINIGT - Strukturiertes Dictionary
messe_data = {
    "Blerina": {
        "attended_messe": False,
        "spoke_to_people": False,
        "positions_seen": 0,
        "companies_seen": [],
        "career_fields_seen": ["Data Analyzer"],
        "notes": "Did not attend but interested in Data Analyzer field"
    },
    "Menjung": {
        "attended_messe": True,
        "spoke_to_people": True,
        "positions_seen": 15,
        "companies_seen": ["Quantum"],
        "career_fields_seen": ["Fullstack"],
        "notes": None
    },
    "Hani": {
        "attended_messe": True,
        "spoke_to_people": True,
        "positions_seen": 7,
        "companies_seen": ["Siemens", "Nestle", "Saudi Arabia", "Adesso"],
        "career_fields_seen": ["Frontend/UX", "BI"],
        "notes": None
    },
    # ... weitere 11 Studenten
}
```

**Bereinigungsregeln:**
1. **Fehlende Werte → `None` oder `[]`**
   - `"Andi": False, False, 0` → `"attended_messe": False, "spoke_to_people": False, ...`
2. **Strings → Listen**
   - `"['Bundeswehr', 'Siemens']"` → `["Bundeswehr", "Siemens"]`
3. **Verschachtelte Dicts → Flache Listen**
   - `{"HsH":False}` → Entfernt oder als String
4. **Leere Strings → Entfernt**
   - `["","","","","",""]` → `[]` oder sinnvolle Werte
5. **Kommentare → `notes` Feld**
   - `#https://careers.ibm.com/...` → `"notes": "IBM job link"`

#### **Schritt 3: Konvertierung zu DataFrame**

Das bereinigte Dictionary wird in ein Pandas DataFrame umgewandelt:

```python
import pandas as pd

# Dictionary → DataFrame
df = pd.DataFrame.from_dict(messe_data, orient='index')
df.index.name = 'Student'
df = df.reset_index()

# Ergebnis:
#     Student  attended_messe  spoke_to_people  positions_seen  companies_seen  career_fields_seen
# 0   Blerina           False            False               0              []     [Data Analyzer]
# 1   Menjung            True             True              15       [Quantum]          [Fullstack]
# 2      Hani            True             True               7  [Siemens, ...]  [Frontend/UX, BI]
```

#### **Schritt 4: Export zu CSV**

Das DataFrame wird als CSV exportiert:

```python
df.to_csv('student_data_structured.csv', index=False)
```

#### **Schritt 5: Microsoft Forms Integration**

Die strukturierten Daten wurden dann in ein **Microsoft Forms Formular** übertragen und als `data/Sheet1.csv` exportiert.

**Vorteil dieser Methode:**
- ✅ Manuelle Sammlung ist **schnell** (keine Form-Erstellung nötig)
- ✅ Bereinigung macht Daten **konsistent**
- ✅ DataFrame ermöglicht **einfache Analyse**
- ✅ CSV-Export macht Daten **portabel**
- ✅ Forms macht Daten **für alle zugänglich**

---

## 🔄 Zusammenfassung: Von RAW zu STRUKTURIERT

```
RAW DATA (chaotisch)
    ↓
Manuelle Bereinigung
    ↓
Strukturiertes Dictionary
    ↓
Pandas DataFrame
    ↓
CSV Export
    ↓
Microsoft Forms
    ↓
Analyse & Visualisierung
```

**Lernziel:**
- Echte Daten sind **immer chaotisch**!
- Datenbereinigung ist **80% der Arbeit**
- Strukturierung macht Analyse **möglich**
- Verschiedene Formate haben **verschiedene Vorteile**

---

## Formular-Titel
**"Umfrage zu euch"**

## Beschreibung
```
Eine Umfrage zur Hannover Messe
```

---

## Fragen

### 1. Wie ist dein Vorname?
**Typ:** Einzeiliger Text  
**Pflicht:** Nein

**Beispiel-Antworten:**
- Oleh
- Sofiia
- Maxim
- Kareem Ramadan
- Ihor

---

### 2. Wart ihr auf der Messe?
**Typ:** Einzelauswahl (Choice)  
**Pflicht:** Nein

**Optionen:**
- Ja
- Nein

**Ergebnis:** 13 von 15 Personen waren auf der Messe (87%)

---

### 3. Mit Leuten gesprochen?
**Typ:** Einzelauswahl (Choice)  
**Pflicht:** Nein

**Optionen:**
- Ja
- Nein

**Ergebnis:** 12 von 15 haben mit Leuten gesprochen (80%)

---

### 4. Wieviele Leute gesehen?
**Typ:** Einzeiliger Text (Zahl)  
**Pflicht:** Nein

**Beispiel-Antworten:**
- 5
- 10
- 12
- 3
- 2
- 7

**Durchschnitt:** ~5-6 Leute

---

### 5. Frage (Mehrfachauswahl)
**Typ:** Mehrfachauswahl  
**Pflicht:** Nein

**Optionen:**
- Frontend
- AI
- Technician
- Fullstack
- Data Analysis
- Sonstiges

**Häufigste Antworten:**
1. AI (8 Personen)
2. Fullstack (6 Personen)
3. Frontend (5 Personen)
4. Data Analysis (4 Personen)

---

### 6. Total IT work experience in months?
**Typ:** Einzeiliger Text (Integer)  
**Pflicht:** Nein

**Hinweis:** 
- Type: Integer (months)
- Guidance: Convert part-time to full-time equivalent (e.g., 6 months part-time = 3 months FTE)

**Beispiel-Antworten:**
- 100 months
- 40 months
- 220 months
- 64 months
- 10 months
- 1 month
- 0 months
- 6 months
- 216 months FTE

**Bereich:** 0-220 Monate (0-18 Jahre)

---

### 7. How much liked you the specific topic? (Likert-Skala)
**Typ:** Likert (Rating)  
**Pflicht:** Nein

**Sub-Fragen:**
1. **Messe Satisfaction**
2. **Python Skills Satisfaction**
3. **SQL**

**Optionen:**
- Liked it a lot
- Liked it
- A bit
- Not so much

**Ergebnisse:**
- **Messe:** Gemischt (viele "Not so much", einige "Liked it")
- **Python Skills:** Ähnlich gemischt
- **SQL:** Nur wenige Antworten

---

### 8. Welche Unternehmen gesehen, getrennt mit ","
**Typ:** Einzeiliger Text  
**Pflicht:** Nein

**Beispiel-Antworten:**
- "Siemens"
- "Aws, coreflux, team viewer, siemens"
- "Beckhoff, AWS, Siemens, Teamviewer, SAP, LAPP, ifak, Maxon"
- "Amazon, Coreflux, Schwarz Digit, Microsoft"
- "Siemens, AWS, Coreflux, Team Viewer"
- "Microsoft, AWS, core flux, Unity, Bundeswehr"
- "Bundeswehr, Siemens"
- "Siemens, Aws, Agile Roboter"

**Häufigste Unternehmen:**
1. Siemens (7x)
2. AWS (6x)
3. Coreflux (4x)
4. Microsoft (3x)
5. Teamviewer (3x)

---

## 📊 Echte Daten (CSV)

Die exportierte CSV-Datei (`data/Sheet1.csv`) hat diese Struktur:

```csv
Id;Startzeit;Fertigstellungszeit;E-Mail;Name;Wie ist dein Vorname?;Wart ihr auf der Messe?;Mit Leuten gesprochen?;Wieviele Leute gesehen?;Frage;Total IT work experience in months?;How much liked you the specific topic?.Messe Satisfaction;How much liked you the specific topic?.Python Skills Satisfaction;How much liked you the specific topic?.SQL;Welche Unternehmen gesehen, getrennt mit ","
1;27.04.2026 11:34;27.04.2026 11:35;anonymous;;;Ja;Ja;5;"Frontend;AI;";;Not so much;Not so much;;
2;27.04.2026 11:33;27.04.2026 11:35;anonymous;;;Ja;Ja;10;"Frontend;AI;Technician;Fullstack;";100;Not so much;Not so much;;
```

**Wichtig:** 
- Trennzeichen ist `;` (Semikolon), nicht `,` (Komma)!
- Mehrfachauswahl-Felder haben Semikolons innerhalb von Anführungszeichen

---

## 🐍 Python-Code zum Analysieren

```python
import pandas as pd
import matplotlib.pyplot as plt

# Daten laden (WICHTIG: sep=';' für Semikolon!)
df = pd.read_csv('data/Sheet1.csv', sep=';', encoding='utf-8')

# Daten anschauen
print(df.head())
print(df.columns)
print(f"Anzahl Antworten: {len(df)}")

# 1. Waren auf der Messe?
messe_teilnahme = df['Wart ihr auf der Messe?'].value_counts()
print("\nMesse-Teilnahme:")
print(messe_teilnahme)

# Plot 1: Messe-Teilnahme
plt.figure(figsize=(8, 6))
messe_teilnahme.plot(kind='bar', color=['green', 'red'])
plt.title('Wart ihr auf der Messe?')
plt.xlabel('Antwort')
plt.ylabel('Anzahl')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('messe_teilnahme.png')
plt.show()

# 2. Wieviele Leute gesehen? (nur numerische Werte)
leute = df['Wieviele Leute gesehen?'].dropna()
leute = pd.to_numeric(leute, errors='coerce').dropna()

if len(leute) > 0:
    print(f"\nDurchschnittlich gesehene Leute: {leute.mean():.1f}")
    print(f"Minimum: {leute.min()}, Maximum: {leute.max()}")
    
    # Plot 2: Leute gesehen
    plt.figure(figsize=(10, 6))
    leute.hist(bins=10, color='skyblue', edgecolor='black')
    plt.title('Wieviele Leute wurden gesehen?')
    plt.xlabel('Anzahl Leute')
    plt.ylabel('Häufigkeit')
    plt.axvline(leute.mean(), color='red', linestyle='--', 
                label=f'Durchschnitt: {leute.mean():.1f}')
    plt.legend()
    plt.tight_layout()
    plt.savefig('leute_gesehen.png')
    plt.show()

# 3. IT Experience (nur numerische Werte)
experience_col = 'Total IT work experience in months?�- Type: Integer (months)   -�Guidance: Convert part-time to full-time equivalent (e.g., 6 months part-time = 3 months FTE)\n'
experience = df[experience_col].dropna()
# Extrahiere nur Zahlen
experience = experience.str.extract(r'(\d+)')[0]
experience = pd.to_numeric(experience, errors='coerce').dropna()

if len(experience) > 0:
    print(f"\nDurchschnittliche IT-Erfahrung: {experience.mean():.1f} Monate")
    print(f"Das sind ca. {experience.mean()/12:.1f} Jahre")
    
    # Plot 3: IT Experience
    plt.figure(figsize=(10, 6))
    experience.hist(bins=15, color='coral', edgecolor='black')
    plt.title('IT Work Experience (Monate)')
    plt.xlabel('Monate')
    plt.ylabel('Anzahl')
    plt.axvline(experience.mean(), color='red', linestyle='--',
                label=f'Durchschnitt: {experience.mean():.0f} Monate')
    plt.legend()
    plt.tight_layout()
    plt.savefig('it_experience.png')
    plt.show()

# 4. Unternehmen analysieren
unternehmen_col = 'Welche Unternehmen gesehen, getrennt mit ","'
alle_unternehmen = []

for antwort in df[unternehmen_col].dropna():
    # Split by comma
    unternehmen = [u.strip() for u in str(antwort).split(',')]
    alle_unternehmen.extend(unternehmen)

# Zählen
from collections import Counter
unternehmen_count = Counter(alle_unternehmen)
top_10 = dict(unternehmen_count.most_common(10))

print("\nTop 10 Unternehmen:")
for firma, anzahl in top_10.items():
    print(f"{firma}: {anzahl}x")

# Plot 4: Top Unternehmen
plt.figure(figsize=(12, 6))
plt.barh(list(top_10.keys()), list(top_10.values()), color='lightgreen')
plt.title('Top 10 Unternehmen auf der Messe')
plt.xlabel('Anzahl Nennungen')
plt.ylabel('Unternehmen')
plt.tight_layout()
plt.savefig('top_unternehmen.png')
plt.show()

# 5. Interessengebiete (Mehrfachauswahl)
interessen_col = 'Frage'
alle_interessen = []

for antwort in df[interessen_col].dropna():
    # Split by semicolon (innerhalb der Anführungszeichen)
    interessen = [i.strip() for i in str(antwort).split(';') if i.strip()]
    alle_interessen.extend(interessen)

# Zählen
interessen_count = Counter(alle_interessen)

print("\nInteressengebiete:")
for gebiet, anzahl in interessen_count.most_common():
    print(f"{gebiet}: {anzahl}x")

# Plot 5: Interessengebiete
plt.figure(figsize=(10, 6))
plt.bar(interessen_count.keys(), interessen_count.values(), color='purple', alpha=0.7)
plt.title('Interessengebiete der Teilnehmer')
plt.xlabel('Gebiet')
plt.ylabel('Anzahl')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('interessengebiete.png')
plt.show()
```

---

## 📈 Echte Ergebnisse (15 Antworten)

### Messe-Teilnahme:
- **Ja:** 13 Personen (87%)
- **Nein:** 2 Personen (13%)

### Gespräche:
- **Ja:** 12 Personen (80%)
- **Nein:** 1 Person (7%)
- **Keine Angabe:** 2 Personen (13%)

### Durchschnittlich gesehene Leute:
- **Durchschnitt:** ~5-6 Leute
- **Minimum:** 2 Leute
- **Maximum:** 12 Leute

### IT-Erfahrung:
- **Durchschnitt:** ~80 Monate (6-7 Jahre)
- **Bereich:** 0-220 Monate (0-18 Jahre)
- **Median:** ~40 Monate (3-4 Jahre)

### Top 5 Interessengebiete:
1. **AI:** 8 Personen (53%)
2. **Fullstack:** 6 Personen (40%)
3. **Frontend:** 5 Personen (33%)
4. **Data Analysis:** 4 Personen (27%)
5. **Technician:** 3 Personen (20%)

### Top 5 Unternehmen:
1. **Siemens:** 7 Nennungen
2. **AWS:** 6 Nennungen
3. **Coreflux:** 4 Nennungen
4. **Microsoft:** 3 Nennungen
5. **Teamviewer:** 3 Nennungen

---

## ⚠️ Wichtige Hinweise für CSV-Import

### Problem 1: Semikolon als Trennzeichen
```python
# FALSCH
df = pd.read_csv('data/Sheet1.csv')  # Verwendet Komma

# RICHTIG
df = pd.read_csv('data/Sheet1.csv', sep=';')  # Verwendet Semikolon
```

### Problem 2: Encoding
```python
# Falls Umlaute nicht funktionieren
df = pd.read_csv('data/Sheet1.csv', sep=';', encoding='utf-8')
# Oder
df = pd.read_csv('data/Sheet1.csv', sep=';', encoding='latin-1')
```

### Problem 3: Mehrfachauswahl-Felder
```python
# Mehrfachauswahl ist als "Option1;Option2;" gespeichert
# Muss gesplittet werden:
for antwort in df['Frage'].dropna():
    optionen = [o.strip() for o in str(antwort).split(';') if o.strip()]
    print(optionen)
```

### Problem 4: Lange Spaltennamen
```python
# Spaltennamen sind sehr lang!
print(df.columns)

# Umbenennen:
df.columns = ['Id', 'Start', 'Ende', 'Email', 'Name', 'Vorname', 
              'Messe', 'Gesprochen', 'Leute', 'Interessen', 
              'Experience', 'Messe_Sat', 'Python_Sat', 'SQL_Sat', 
              'Unternehmen']
```

---

## 💡 Was können wir aus diesen Daten lernen?

### 1. Messe war erfolgreich
- 87% waren auf der Messe
- 80% haben mit Leuten gesprochen
- Durchschnittlich 5-6 Kontakte pro Person

### 2. Teilnehmer-Profile
- **Hauptinteresse:** AI und Fullstack
- **Erfahrung:** Sehr gemischt (0-18 Jahre)
- **Durchschnitt:** 6-7 Jahre IT-Erfahrung

### 3. Beliebte Unternehmen
- **Tech-Giganten:** AWS, Microsoft
- **Industrie:** Siemens (sehr beliebt!)
- **Startups:** Coreflux

### 4. Verbesserungspotenzial
- Likert-Skala hatte viele "Not so much" Antworten
- Vielleicht war die Messe nicht für alle relevant?
- Oder die Fragen waren unklar?

---

## 🚀 Übung

### Analysiere die echten Daten!

1. **Lade die Datei:** `data/Sheet1.csv`
2. **Nutze den Code oben**
3. **Erstelle eigene Visualisierungen:**
   - Scatter Plot: IT-Erfahrung vs. Anzahl gesehener Leute
   - Bar Chart: Interessengebiete nach IT-Erfahrung
   - Word Cloud: Unternehmen (fortgeschritten)

4. **Beantworte Fragen:**
   - Haben erfahrenere Leute mehr Kontakte geknüpft?
   - Welches Interessengebiet war am beliebtesten?
   - Gibt es einen Zusammenhang zwischen Interesse und besuchten Unternehmen?

---

## 📚 Siehe auch

- **Anleitung:** `woche-2/Part-1-Data-Integration/06_forms_anleitung.md`
- **Tool:** `forms_to_csv_adapter.py` (im Root-Verzeichnis)
- **Parameter-Referenz:** `woche-2/04_matplotlib_parameter.md`
- **Echte Daten:** `data/Sheet1.csv`

---

*Dies ist ein echtes Beispiel aus dem Kurs!* 📝✨