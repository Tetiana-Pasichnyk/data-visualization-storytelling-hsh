# Data Directory

This directory contains sample datasets used in the matplotlib introduction notebooks for the Data Visualization course.

## Purpose

These datasets are used for hands-on practice with matplotlib plotting techniques in the following notebooks:
- [`fundamentals/2ndDay-introduction-to-matplotlib-video.ipynb`](../fundamentals/2ndDay-introduction-to-matplotlib-video.ipynb)
- [`fundamentals/2ndDay-introduction-to-matplotlib-video (1).ipynb`](../fundamentals/2ndDay-introduction-to-matplotlib-video%20(1).ipynb)

## Datasets

### 1. car-sales.csv

**Description:** A dataset containing information about used car sales.

**Columns:**
- `Make` - Car manufacturer (e.g., Toyota, Honda, BMW)
- `Colour` - Car color
- `Odometer (KM)` - Mileage in kilometers
- `Doors` - Number of doors
- `Price` - Sale price in dollars (formatted as string with $ and commas)

**Use Cases in Notebooks:**
- Creating scatter plots (price vs. odometer)
- Bar charts (comparing prices by make)
- Practicing data cleaning (converting price strings to numbers)
- Demonstrating pandas integration with matplotlib

**Sample Data:**
```
Make,Colour,Odometer (KM),Doors,Price
Toyota,White,150043,4,"$4,000.00"
Honda,Red,87899,4,"$5,000.00"
```

### 2. heart-disease.csv

**Description:** A medical dataset containing patient information related to heart disease diagnosis.

**Columns:**
- `age` - Patient age
- `sex` - Patient sex (1 = male, 0 = female)
- `cp` - Chest pain type
- `trestbps` - Resting blood pressure
- `chol` - Serum cholesterol in mg/dl
- `fbs` - Fasting blood sugar > 120 mg/dl (1 = true, 0 = false)
- `restecg` - Resting electrocardiographic results
- `thalach` - Maximum heart rate achieved
- `exang` - Exercise induced angina (1 = yes, 0 = no)
- `oldpeak` - ST depression induced by exercise
- `slope` - Slope of peak exercise ST segment
- `ca` - Number of major vessels colored by fluoroscopy
- `thal` - Thalassemia type
- `target` - Heart disease diagnosis (1 = disease, 0 = no disease)

**Use Cases in Notebooks:**
- Creating histograms (age distribution)
- Scatter plots with multiple variables
- Comparing different plot types for the same data
- Demonstrating correlation visualization

**Sample Data:**
```
age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,target
63,1,3,145,233,1,0,150,0,2.3,0,0,1,1
37,1,2,130,250,0,1,187,0,3.5,0,0,2,1
```

## Original Source

These notebooks and datasets are based on the excellent matplotlib tutorial by Daniel Bourke:
- **Original Repository:** [Zero to Mastery ML - Introduction to Matplotlib](https://github.com/mrdbourke/zero-to-mastery-ml/blob/master/section-2-data-science-and-ml-tools/introduction-to-matplotlib-video.ipynb)
- **Author:** Daniel Bourke ([@mrdbourke](https://github.com/mrdbourke))

The materials have been adapted for the Data Visualization course at Hochschule Hannover.

## Usage

To load these datasets in your notebooks:

```python
import pandas as pd

# Load car sales data
car_sales = pd.read_csv("../data/car-sales.csv")

# Load heart disease data
heart_disease = pd.read_csv("../data/heart-disease.csv")
```

**Note:** The relative path `../data/` assumes you're running the notebook from the `fundamentals/` directory.

## Learning Objectives

Working with these datasets helps you:
1. Practice loading real-world data with pandas
2. Understand different data types (numeric, categorical, formatted strings)
3. Create various plot types (scatter, bar, histogram, line)
4. Learn data cleaning techniques (e.g., converting price strings to numbers)
5. Visualize relationships between variables
6. Compare different visualization approaches for the same data

## Data Cleaning Notes

### Car Sales Dataset - The Price Column Challenge

**The Problem:**
The `Price` column contains values like `"$4,000.00"` which are stored as **strings**, not numbers. This prevents mathematical operations and numerical plotting.

**Why This Happens:**
Pandas treats columns with special characters (`$`, `,`) as text (object/string type) instead of numbers.

---

### 🔧 Multiple Solutions to Clean the Price Column

#### **Method 1: Pandas String Methods with Regex (Most Common)**
```python
# Remove $ and commas using regex, then convert to float
car_sales['Price'] = car_sales['Price'].str.replace('[\$,]', '', regex=True).astype(float)

# Explanation:
# - .str.replace() works on string columns
# - [\$,] matches either $ or , characters
# - regex=True enables pattern matching
# - .astype(float) converts to numeric
```

#### **Method 2: Multiple Replace Calls (More Explicit)**
```python
# Remove symbols one at a time
car_sales['Price'] = car_sales['Price'].str.replace('$', '', regex=False)
car_sales['Price'] = car_sales['Price'].str.replace(',', '', regex=False)
car_sales['Price'] = car_sales['Price'].astype(float)

# Or chain them:
car_sales['Price'] = (car_sales['Price']
                      .str.replace('$', '', regex=False)
                      .str.replace(',', '', regex=False)
                      .astype(float))
```

#### **Method 3: Using Python's Built-in String Methods with Apply**
```python
# Define a cleaning function
def clean_price(price_string):
    """Remove $ and commas, convert to float"""
    cleaned = price_string.replace('$', '').replace(',', '')
    return float(cleaned)

# Apply to entire column
car_sales['Price'] = car_sales['Price'].apply(clean_price)
```

#### **Method 4: Lambda Function (One-liner)**
```python
# Compact version using lambda
car_sales['Price'] = car_sales['Price'].apply(
    lambda x: float(x.replace('$', '').replace(',', ''))
)
```

#### **Method 5: Using NumPy's char Module**
```python
import numpy as np

# Convert to numpy array, clean, convert back
prices = car_sales['Price'].values
prices = np.char.replace(prices, '$', '')
prices = np.char.replace(prices, ',', '')
car_sales['Price'] = prices.astype(float)
```

#### **Method 6: List Comprehension (Pythonic)**
```python
# Process all values at once
car_sales['Price'] = [
    float(price.replace('$', '').replace(',', ''))
    for price in car_sales['Price']
]
```

#### **Method 7: Using pd.to_numeric with errors='coerce'**
```python
# First remove symbols, then use to_numeric for safety
car_sales['Price'] = car_sales['Price'].str.replace('[\$,]', '', regex=True)
car_sales['Price'] = pd.to_numeric(car_sales['Price'], errors='coerce')

# errors='coerce' converts invalid values to NaN instead of raising error
```

#### **Method 8: Creating a New Clean Column (Preserves Original)**
```python
# Keep original, create new clean column
car_sales['Price_Clean'] = (
    car_sales['Price']
    .str.replace('[\$,]', '', regex=True)
    .astype(float)
)

# Now you have both:
# - car_sales['Price'] = "$4,000.00" (original)
# - car_sales['Price_Clean'] = 4000.0 (numeric)
```

#### **Method 9: Using str.extract with Regex (Advanced)**
```python
# Extract only the numeric parts
car_sales['Price'] = (
    car_sales['Price']
    .str.extract(r'(\d+,?\d*\.?\d*)', expand=False)  # Extract numbers
    .str.replace(',', '')                             # Remove commas
    .astype(float)
)
```

#### **Method 10: Using locale for Currency Parsing (Professional)**
```python
import locale

# Set locale for currency parsing (US format)
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

def parse_currency(price_string):
    """Parse currency string using locale"""
    return locale.atof(price_string.strip('$'))

car_sales['Price'] = car_sales['Price'].apply(parse_currency)
```

---

### 📊 Comparison of Methods

| Method | Pros | Cons | Best For |
|--------|------|------|----------|
| **1. Regex** | Fast, concise, handles multiple chars | Regex can be confusing | Most situations |
| **2. Multiple Replace** | Very clear, easy to understand | More verbose | Beginners |
| **3. Apply with Function** | Flexible, reusable | Slower on large datasets | Custom logic |
| **4. Lambda** | Compact | Less readable | Quick scripts |
| **5. NumPy** | Fast for large data | Requires NumPy knowledge | Performance-critical |
| **6. List Comp** | Pythonic, readable | Not pandas-native | Small datasets |
| **7. to_numeric** | Handles errors gracefully | Two-step process | Messy data |
| **8. New Column** | Preserves original | Uses more memory | Data exploration |
| **9. Extract** | Powerful pattern matching | Complex regex | Complex formats |
| **10. Locale** | Handles international formats | Locale-dependent | Production code |

---

### 🎓 Pandas/NumPy Refresher

**Key Concepts:**

1. **String Methods (`.str`)**: Access string operations on pandas Series
   ```python
   df['column'].str.replace()  # String replacement
   df['column'].str.upper()    # Convert to uppercase
   df['column'].str.split()    # Split strings
   ```

2. **Type Conversion (`.astype()`)**: Change data types
   ```python
   df['column'].astype(float)   # Convert to float
   df['column'].astype(int)     # Convert to integer
   df['column'].astype(str)     # Convert to string
   ```

3. **Apply Functions (`.apply()`)**: Apply custom functions
   ```python
   df['column'].apply(function_name)        # Named function
   df['column'].apply(lambda x: x * 2)      # Lambda function
   ```

4. **Regex Patterns**: Pattern matching for text
   ```python
   [\$,]     # Match $ or ,
   \d+       # Match one or more digits
   [a-z]+    # Match lowercase letters
   ```

---

### ✅ Verification Steps

After cleaning, always verify your data:

```python
# 1. Check data type
print(car_sales['Price'].dtype)  # Should be float64

# 2. Look at values
print(car_sales['Price'].head())

# 3. Check for NaN values
print(car_sales['Price'].isna().sum())

# 4. Basic statistics
print(car_sales['Price'].describe())

# 5. Try a calculation
print(f"Average price: ${car_sales['Price'].mean():,.2f}")

# 6. Try plotting
car_sales['Price'].plot(kind='hist')
```

---

### Heart Disease Dataset
- All columns are already numeric (no cleaning needed!)
- Binary columns (0/1) represent categorical data
- The `target` column is the prediction variable (presence of heart disease)

## Attribution

These datasets are used for educational purposes in the Data Visualization course. Original materials by Daniel Bourke are used under their respective licenses.