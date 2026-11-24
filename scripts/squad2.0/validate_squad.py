
import pandas as pd
from pathlib import Path
from numbers import Integral

base_path = Path("data/raw/squad_v2")

for split in ["train", "validation"]:
    df = pd.read_parquet(base_path / split / "0000.parquet")

    answerable = 0
    unanswerable = 0
    invalid_answers = 0
    invalid_offsets = 0
    total_answer_spans = 0

    for _, row in df.iterrows():
        answers = row["answers"]
        texts = answers["text"]
        starts = answers["answer_start"]

        if len(texts) == 0:
            unanswerable += 1
            continue

        answerable += 1
        context = row["context"]

        for text, start in zip(texts, starts):
            total_answer_spans += 1

            if not isinstance(start, Integral) or start < 0:
                invalid_offsets += 1
                continue

            start = int(start)

            if context[start:start + len(text)] != text:
                invalid_answers += 1

    print(f"\n{split.upper()} VALIDATION")
    print("Total questions:", len(df))
    print("Answerable:", answerable)
    print("Unanswerable:", unanswerable)
    print("Total answer spans:", total_answer_spans)
    print("Invalid answer texts:", invalid_answers)
    print("Invalid offsets:", invalid_offsets)
