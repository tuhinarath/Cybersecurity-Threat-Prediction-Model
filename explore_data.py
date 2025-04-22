import pandas as pd

df = pd.read_csv("cicids_sample.csv", low_memory=False)

# Clean column names
df.columns = df.columns.str.strip()

print("Dataset Shape:", df.shape)
print("\nColumns:\n", df.columns.tolist())
print("\nFirst 5 rows:\n", df.head())
print("\nLabel Distribution:\n", df['Label'].value_counts())
