import pandas as pd
import os

# Path to your folder with 2000–2026 EPA files
folder_path = "C:/Users/Dre Sistena/Desktop/Projects/ev-vs-hybrid-vs-gas-capstone/epa-capstone/data/EPA-By-Year"
output_path = "C:/Users/Dre Sistena/Desktop/Projects/ev-vs-hybrid-vs-gas-capstone/epa-capstone/data/epa_fuel_economy_2000_2024.csv"

# Get all CSV files in that folder
all_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# Initialize an empty DataFrame
combined_df = pd.DataFrame()

# Loop through and merge
for file in all_files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_csv(file_path)
    
    # Add a year column from filename (e.g., 2001.csv -> 2001)
    try:
        year = int(file.split('.')[0])
        df['Year'] = year
    except ValueError:
        print(f"Skipping file: {file} (unable to extract year)")
        continue

    combined_df = pd.concat([combined_df, df], ignore_index=True)

# Save combined file
combined_df.to_csv(output_path, index=False)
print(f"✅ Combined file saved to:\n{output_path}")