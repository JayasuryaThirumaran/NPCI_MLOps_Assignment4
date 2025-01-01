import pandas as pd
import os
from sklearn.preprocessing import OneHotEncoder, StandardScaler, LabelEncoder

# Define input and output paths
input_path = "data/raw/banking_dataset.csv"
output_path = "data/processed/processed_data.csv"




# Load dataset
data = pd.read_csv(input_path)

# Drop irrelevant columns
columns_to_drop = ["contact", "poutcome", "month", "day"]
data = data.drop(columns=columns_to_drop)

# Handle categorical data with OneHotEncoder
categorical_cols = ["job", "marital", "education", "default", "housing", "loan"]
data = pd.get_dummies(data, columns=categorical_cols, drop_first=True)

# Normalize numerical features
numerical_cols = ["age", "balance", "duration", "campaign", "pdays", "previous"]
scaler = StandardScaler()
data[numerical_cols] = scaler.fit_transform(data[numerical_cols])

# Encode the target column
label_encoder = LabelEncoder()
data["y"] = label_encoder.fit_transform(data["y"])  # 'yes' -> 1, 'no' -> 0

# Save preprocessed data to a new CSV file
data.to_csv(output_path, index=False)

print("Preprocessing complete. Preprocessed dataset saved to 'preprocessed_banking_dataset.csv'.")

