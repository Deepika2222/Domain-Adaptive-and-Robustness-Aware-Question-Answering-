
import bz2
import json
from pathlib import Path

corpus_path = Path(
    "data/raw/TechQA/technote_corpus/"
    "full_technote_collection.txt.bz2"
)

total_lines = 0
valid_lines = 0
invalid_lines = 0
total_documents = 0
empty_text = 0
sample_shown = False

print("Starting TechQA corpus inspection...")

with bz2.open(corpus_path, "rt", encoding="utf-8") as f:
    for line in f:
        total_lines += 1

        try:
            records = json.loads(line)
            valid_lines += 1

            if not isinstance(records, list):
                invalid_lines += 1
                continue

            total_documents += len(records)

            for doc in records:
                if not doc.get("text", "").strip():
                    empty_text += 1

                if not sample_shown:
                    print("\nSample document:")
                    print("ID:", doc.get("id"))
                    print("Title:", doc.get("title"))
                    print("Text preview:", doc.get("text", "")[:300])
                    sample_shown = True

        except (json.JSONDecodeError, UnicodeDecodeError):
            invalid_lines += 1

print("\nTECHQA CORPUS REPORT")
print("--------------------")
print("Total lines:", total_lines)
print("Valid JSON lines:", valid_lines)
print("Invalid lines:", invalid_lines)
print("Total documents:", total_documents)
print("Empty documents:", empty_text)
