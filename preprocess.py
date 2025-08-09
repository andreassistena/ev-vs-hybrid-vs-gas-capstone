
import pandas as pd

def clean_vehicle_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and prepare vehicle dataset.
    - Ensures proper data types
    - Drops rows with missing values in key columns
    - Standardizes column names

    Args:
        df (pd.DataFrame): Raw vehicle data

    Returns:
        pd.DataFrame: Cleaned vehicle data
    """
    # Standardize column names
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    # Convert Year and Combined MPG (cmb) to proper types
    df['year'] = pd.to_numeric(df['year'], errors='coerce')
    df['cmb'] = pd.to_numeric(df['cmb'], errors='coerce')

    # Drop rows with missing values in essential columns
    df = df.dropna(subset=['year', 'cmb', 'fuel_type'])

    # Cast year to int after dropping NaNs
    df['year'] = df['year'].astype(int)

    # Standardize fuel types to upper case
    df['fuel_type'] = df['fuel_type'].str.upper()

    return df


def load_and_prepare_data(filepath: str) -> pd.DataFrame:
    """
    Load dataset and apply cleaning steps.

    Args:
        filepath (str): Path to the CSV or Excel file

    Returns:
        pd.DataFrame: Cleaned dataset
    """
    if filepath.endswith('.csv'):
        df = pd.read_csv(filepath)
    elif filepath.endswith(('.xls', '.xlsx')):
        df = pd.read_excel(filepath)
    else:
        raise ValueError("Unsupported file type. Please use .csv or .xlsx")

    return clean_vehicle_data(df)


if __name__ == "__main__":
    # Example usage
    input_path = "data/vehicles_combined.csv"  # Adjust path as needed
    cleaned_df = load_and_prepare_data(input_path)

    print("Preview of cleaned data:")
    print(cleaned_df.head())