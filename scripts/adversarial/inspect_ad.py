
import pandas as pd
from pathlib import Path

base_path = Path("data/raw/adversarial_qa")

configurations = ["dbert", "dbidaf", "adversarialQA", "droberta"]
splits = ["train", "validation", "test"]

for config in configurations:
    print("\n" + "=" * 60)
    print(f"CONFIGURATION: {config.upper()}")
    print("=" * 60)

    for split in splits:
        file_path = base_path / config / split / "0000.parquet"

        df = pd.read_parquet(file_path)

        print(f"\n--- {split.upper()} ---")
        print("Number of records:", len(df))
        print("Columns:", df.columns.tolist())

        print("\nData types:")
        print(df.dtypes)

        print("\nMissing values:")
        print(df.isnull().sum())

        print("\nSample record:")
        print(df.head(1).to_string(index=False))
