import pandas as pd
import os

# Define input and output paths
input_path = "data/raw/banking_dataset.csv"
output_path = "data/processed/processed_data.csv"

# Ensure the input file exists
if not os.path.exists(input_path):
    raise FileNotFoundError(f"Input file not found at {input_path}")

# Read the raw dataset
df = pd.read_csv(input_path)

# Preprocessing steps
print("Initial DataFrame:")
print(df.head())

# 1. Remove rows with missing values
df_cleaned = df.dropna()

# 2. Select important columns for analysis
columns_to_keep = ['age', 'job', 'balance', 'y']  # Keep only these columns
df_cleaned = df_cleaned[columns_to_keep]

# 3. Encode target column (convert 'y' from yes/no to 1/0)
df_cleaned['y'] = df_cleaned['y'].map({'yes': 1, 'no': 0})

# Save the processed dataset
os.makedirs(os.path.dirname(output_path), exist_ok=True)
df_cleaned.to_csv(output_path, index=False)

print(f"Processed data saved to {output_path}")
