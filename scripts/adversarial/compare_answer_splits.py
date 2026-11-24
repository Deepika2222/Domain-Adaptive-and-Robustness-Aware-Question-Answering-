import pandas as pd
from pathlib import Path

base = Path("data/raw/adversarial_qa")
configs = ["dbert", "dbidaf", "adversarialQA", "droberta"]
splits = ["train", "validation", "test"]

for config in configs:
    print(f"\n{'=' * 45}")
    print(config.upper())
    print("=" * 45)

    for split in splits:
        path = base / config / split / "0000.parquet"
        df = pd.read_parquet(path)

        counts = df["answers"].apply(
            lambda x: len(x["text"])
        )

        print(
            f"{split:10} | "
            f"Rows: {len(df):5} | "
            f"Empty answers: {(counts == 0).sum():5} | "
            f"Non-empty answers: {(counts > 0).sum():5}"
        )