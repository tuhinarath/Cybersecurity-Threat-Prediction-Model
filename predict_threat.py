import pandas as pd
import joblib

# Load the trained model
model = joblib.load("threat_model.pkl")

# Load the cleaned dataset
df = pd.read_csv("cleaned_cicids_sample.csv")

# Clean column names (remove leading/trailing spaces)
df.columns = df.columns.str.strip()

# Drop 'Label' column if present
if 'Label' in df.columns:
    df = df.drop(columns=['Label'])

# Ensure only the columns used during training are selected
expected_features = model.feature_names_in_
df = df[expected_features]

# Make predictions
prediction = model.predict(df)

# Show predictions
print("Predictions:\n", prediction)
