import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv('cicids_sample.csv')

# Clean column names
df.columns = df.columns.str.strip()

# Drop columns that are not helpful
cols_to_drop = ['Flow Bytes/s', 'Flow Packets/s', ' Destination Port']
df.drop(columns=cols_to_drop, inplace=True, errors='ignore')

# Drop rows with any missing or infinite values
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.dropna(inplace=True)

# Encode label column (0 = BENIGN, 1 = ATTACK)
df['Label'] = df['Label'].apply(lambda x: 0 if x == 'BENIGN' else 1)

# Save the cleaned data
df.to_csv('preprocessed_data.csv', index=False)

print("Preprocessing complete. Cleaned dataset saved as 'preprocessed_data.csv'.")

