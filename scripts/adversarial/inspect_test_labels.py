
import pandas as pd
from pathlib import Path

base = Path("data/raw/adversarial_qa")

for config in ["dbert", "dbidaf", "adversarialQA", "droberta"]:
    path = base / config / "test" / "0000.parquet"
    df = pd.read_parquet(path)

    print(f"\n{'=' * 50}")
    print("CONFIGURATION:", config)

    for i in range(min(5, len(df))):
        row = df.iloc[i]

        print("\nQuestion:", row["question"])
        print("Answers:", row["answers"])
        print("Metadata:", row["metadata"])
