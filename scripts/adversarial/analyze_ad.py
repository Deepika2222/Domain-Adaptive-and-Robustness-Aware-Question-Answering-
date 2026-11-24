
import pandas as pd
from pathlib import Path

base = Path("data/raw/adversarial_qa")

configs = ["dbert", "dbidaf", "adversarialQA", "droberta"]
splits = ["train", "validation", "test"]

for config in configs:
    print(f"\n{'=' * 55}")
    print(f"CONFIGURATION: {config.upper()}")
    print("=" * 55)

    for split in splits:
        path = base / config / split / "0000.parquet"
        df = pd.read_parquet(path)

        question_lengths = df["question"].fillna("").apply(
            lambda x: len(x.split())
        )

        context_lengths = df["context"].fillna("").apply(
            lambda x: len(x.split())
        )

        answer_lengths = df["answers"].apply(
            lambda x: [
                len(answer.split()) for answer in x["text"]
            ]
        )

        all_answer_lengths = [
            length
            for answers in answer_lengths
            for length in answers
        ]

        print(f"\n{split.upper()}")
        print("Total examples:", len(df))
        print("Duplicate IDs:", df["id"].duplicated().sum())
        print("Average question words:", round(question_lengths.mean(), 2))
        print("Average context words:", round(context_lengths.mean(), 2))

        if all_answer_lengths:
            print(
                "Average answer words:",
                round(sum(all_answer_lengths) / len(all_answer_lengths), 2)
            )
        else:
            print("Average answer words: Not available (test labels withheld)")
