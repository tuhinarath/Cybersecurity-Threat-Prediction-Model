import pandas as pd

df = pd.read_csv("cicids_sample.csv")

df.columns = df.columns.str.strip()

df.to_csv("cleaned_cicids_sample.csv", index=False)

print("✔️ Column names cleaned and saved to 'cleaned_cicids_sample.csv'")

