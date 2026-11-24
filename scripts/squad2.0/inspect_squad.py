
import pandas as pd
from pathlib import Path

base_path = Path("data/raw/squad_v2")

for split in ["train", "validation"]:
    file_path = base_path / split / "0000.parquet"

    df = pd.read_parquet(file_path)

    print(f"\n{'=' * 50}")
    print(f"SQUAD 2.0 - {split.upper()}")
    print("=" * 50)

    print("Number of records:", len(df))
    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData types:")
    print(df.dtypes)

    print("\nMissing values:")
    print(df.isnull().sum())

    print("\nSample records:")
    print(df.head(3).to_string())
