
import pandas as pd
from pathlib import Path
from numbers import Integral

base_path = Path("data/raw/adversarial_qa")

configurations = ["dbert", "dbidaf", "adversarialQA", "droberta"]
splits = ["train", "validation", "test"]

for config in configurations:
    print(f"\n{'=' * 55}")
    print(f"CONFIGURATION: {config.upper()}")
    print("=" * 55)

    for split in splits:
        file_path = base_path / config / split / "0000.parquet"
        df = pd.read_parquet(file_path)

        answerable = 0
        unanswerable = 0
        invalid_answers = 0
        invalid_offsets = 0
        total_spans = 0

        for _, row in df.iterrows():
            answers = row["answers"]
            texts = answers["text"]
            starts = answers["answer_start"]

            if len(texts) == 0:
                unanswerable += 1
                continue

            answerable += 1
            context = row["context"]

            if len(texts) != len(starts):
                invalid_answers += 1
                continue

            for text, start in zip(texts, starts):
                total_spans += 1

                if not isinstance(start, Integral) or start < 0:
                    invalid_offsets += 1
                    continue

                start = int(start)

                if context[start:start + len(text)] != text:
                    invalid_answers += 1

        print(f"\n{split.upper()}")
        print("Total questions:", len(df))
        print("Answerable:", answerable)
        print("Unanswerable:", unanswerable)
        print("Total answer spans:", total_spans)
        print("Invalid answer texts:", invalid_answers)
        print("Invalid offsets:", invalid_offsets)
