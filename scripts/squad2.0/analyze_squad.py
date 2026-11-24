
import pandas as pd
from pathlib import Path
from collections import Counter

base_path = Path("data/raw/squad_v2")

for split in ["train", "validation"]:
    df = pd.read_parquet(base_path / split / "0000.parquet")

    answerable = df["answers"].apply(
        lambda x: len(x["text"]) > 0
    )

    question_lengths = df["question"].str.split().str.len()
    context_lengths = df["context"].str.split().str.len()

    answer_lengths = [
        len(answer.split())
        for answers in df["answers"]
        for answer in answers["text"]
    ]

    duplicate_ids = df["id"].duplicated().sum()

    print(f"\n{'=' * 45}")
    print(f"SQUAD 2.0 {split.upper()} ANALYSIS")
    print("=" * 45)

    print("Total questions:", len(df))
    print("Answerable:", answerable.sum())
    print("Unanswerable:", (~answerable).sum())
    print("Answerable percentage:", round(answerable.mean() * 100, 2), "%")
    print("Unanswerable percentage:", round((~answerable).mean() * 100, 2), "%")
    print("Average question length (words):", round(question_lengths.mean(), 2))
    print("Average context length (words):", round(context_lengths.mean(), 2))
    print("Average answer length (words):", round(sum(answer_lengths) / len(answer_lengths), 2))
    print("Duplicate question IDs:", duplicate_ids)
