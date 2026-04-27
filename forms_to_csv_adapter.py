#!/usr/bin/env python3
"""
Microsoft Forms to Student Data CSV Adapter

This script converts Microsoft Forms survey exports to the standardized
student_data_structured.csv format used for Hannover Messe analysis.

Usage:
    python forms_to_csv_adapter.py <input_forms_export.csv> [output.csv]

Example:
    python forms_to_csv_adapter.py forms_responses.csv student_data_structured.csv
"""

import pandas as pd
import sys
from datetime import datetime
import os


# ============================================
# CONFIGURATION - Customize for your form
# ============================================

# Column mapping: Map your Microsoft Forms column names to standardized names
COLUMN_MAPPING = {
    'Name': 'Student',
    'Did you attend Hannover Messe?': 'attended_messe',
    'Did you speak to company representatives?': 'spoke_to_people',
    'How many job positions did you discover?': 'positions_seen',
    'Which companies did you visit? (separate with commas)': 'companies_seen',
    'Which career fields interested you? (separate with commas)': 'career_fields_seen',
    'Additional notes': 'notes'
}

# Alternative column names (if your form uses different questions)
# Uncomment and modify as needed:
# COLUMN_MAPPING = {
#     'Student Name': 'Student',
#     'Attended?': 'attended_messe',
#     'Networked?': 'spoke_to_people',
#     'Positions Count': 'positions_seen',
#     'Companies': 'companies_seen',
#     'Career Fields': 'career_fields_seen',
#     'Notes': 'notes'
# }


# ============================================
# DATA CLEANING FUNCTIONS
# ============================================

def normalize_boolean(value):
    """Convert various boolean representations to True/False/empty string."""
    if pd.isna(value) or value == '' or value is None:
        return ''
    
    if isinstance(value, bool):
        return value
    
    value_str = str(value).strip().lower()
    
    if value_str in ['yes', 'true', '1', 'ja', 'y']:
        return True
    elif value_str in ['no', 'false', '0', 'nein', 'n']:
        return False
    else:
        return ''


def parse_list_field(value, separators=[',', ';', '/']):
    """Parse comma/semicolon/slash-separated list and return as semicolon-separated string."""
    if pd.isna(value) or value == '' or value is None:
        return ''
    
    if isinstance(value, list):
        items = [str(item).strip() for item in value if str(item).strip()]
        return '; '.join(items)
    
    value_str = str(value)
    
    # Try each separator
    for sep in separators:
        if sep in value_str:
            items = [item.strip() for item in value_str.split(sep)]
            items = [item for item in items if item]
            return '; '.join(items)
    
    # No separator found, return cleaned value
    cleaned = value_str.strip()
    return cleaned if cleaned else ''


def normalize_numeric(value):
    """Convert to numeric, handling various formats."""
    if pd.isna(value) or value == '' or value is None:
        return ''
    
    try:
        return int(float(value))
    except (ValueError, TypeError):
        return ''


def clean_dataframe(df):
    """Apply all cleaning transformations to the dataframe."""
    df = df.copy()
    
    # Ensure all required columns exist
    required_cols = ['Student', 'attended_messe', 'spoke_to_people', 
                    'positions_seen', 'companies_seen', 'career_fields_seen', 'notes']
    
    for col in required_cols:
        if col not in df.columns:
            print(f"Warning: Column '{col}' not found. Creating empty column.")
            df[col] = ''
    
    # Normalize boolean fields
    df['attended_messe'] = df['attended_messe'].apply(normalize_boolean)
    df['spoke_to_people'] = df['spoke_to_people'].apply(normalize_boolean)
    
    # Normalize numeric fields
    df['positions_seen'] = df['positions_seen'].apply(normalize_numeric)
    
    # Parse list fields (convert to semicolon-separated strings)
    df['companies_seen'] = df['companies_seen'].apply(parse_list_field)
    df['career_fields_seen'] = df['career_fields_seen'].apply(parse_list_field)
    
    # Clean notes field
    df['notes'] = df['notes'].fillna('')
    
    return df


def convert_forms_to_csv(input_path, output_path, column_mapping):
    """
    Convert Microsoft Forms export to standardized CSV format.
    
    Args:
        input_path: Path to Microsoft Forms CSV export
        output_path: Path for output standardized CSV
        column_mapping: Dictionary mapping form columns to standard names
    
    Returns:
        True if successful, False otherwise
    """
    try:
        # Load the Forms export
        print(f"Loading Microsoft Forms export from: {input_path}")
        df = pd.read_csv(input_path)
        print(f"✓ Loaded {len(df)} rows")
        print(f"  Original columns: {list(df.columns)}")
        
        # Rename columns based on mapping
        df = df.rename(columns=column_mapping)
        print(f"\n✓ Columns mapped to standardized names")
        
        # Clean the data
        print("\nCleaning data...")
        df = clean_dataframe(df)
        
        # Select only the required columns in the correct order
        output_cols = ['Student', 'attended_messe', 'spoke_to_people', 'positions_seen',
                      'companies_seen', 'career_fields_seen', 'notes']
        df = df[output_cols]
        
        # Export to CSV
        df.to_csv(output_path, index=False)
        print(f"\n✓ Data exported to: {output_path}")
        print(f"  Rows exported: {len(df)}")
        
        # Display preview
        print("\nPreview of converted data:")
        print(df.head())
        
        return True
        
    except FileNotFoundError:
        print(f"✗ Error: File '{input_path}' not found.")
        return False
    except KeyError as e:
        print(f"✗ Error: Column mapping issue - {e}")
        print("\nAvailable columns in your file:")
        try:
            temp_df = pd.read_csv(input_path)
            for i, col in enumerate(temp_df.columns, 1):
                print(f"  {i}. {col}")
            print("\nPlease update COLUMN_MAPPING in this script to match your form's columns.")
        except:
            pass
        return False
    except Exception as e:
        print(f"✗ Error: {e}")
        return False


def main():
    """Main function to handle command-line execution."""
    print("=" * 60)
    print("Microsoft Forms to Student Data CSV Adapter")
    print("=" * 60)
    
    # Check command-line arguments
    if len(sys.argv) < 2:
        print("\nUsage: python forms_to_csv_adapter.py <input_forms_export.csv> [output.csv]")
        print("\nExample:")
        print("  python forms_to_csv_adapter.py forms_responses.csv student_data_structured.csv")
        sys.exit(1)
    
    input_path = sys.argv[1]
    
    # Generate output filename if not provided
    if len(sys.argv) >= 3:
        output_path = sys.argv[2]
    else:
        # Generate timestamped filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = f"student_data_structured_{timestamp}.csv"
    
    print(f"\nInput:  {input_path}")
    print(f"Output: {output_path}")
    print()
    
    # Convert the file
    success = convert_forms_to_csv(input_path, output_path, COLUMN_MAPPING)
    
    if success:
        print("\n" + "=" * 60)
        print("✓ Conversion completed successfully!")
        print("=" * 60)
        sys.exit(0)
    else:
        print("\n" + "=" * 60)
        print("✗ Conversion failed. Please check the errors above.")
        print("=" * 60)
        sys.exit(1)


if __name__ == "__main__":
    main()

# Made with Bob
