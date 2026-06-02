
import pandas as pd
import os

raw_path = "data/raw"

files = [f for f in os.listdir(raw_path) if f.endswith(".csv")]

for file in files:

    print("=" * 60)
    print("Dataset:", file)

    df = pd.read_csv(os.path.join(raw_path, file))

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\n")
