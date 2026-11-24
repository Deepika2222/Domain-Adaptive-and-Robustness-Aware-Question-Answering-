
import bz2
import json
from pathlib import Path
from collections import Counter

corpus_path = Path(
    "data/raw/TechQA/technote_corpus/"
    "full_technote_collection.txt.bz2"
)

total_docs = 0
empty_docs = 0
duplicate_ids = 0
missing_ids = 0
short_docs = 0
long_docs = 0

seen_ids = set()
lengths = []
samples = []

print("Starting TechQA quality analysis...")

with bz2.open(corpus_path, "rt", encoding="utf-8") as f:
    for line in f:
        records = json.loads(line)

        for doc in records:
            total_docs += 1

            doc_id = doc.get("id")
            text = doc.get("text") or ""
            title = doc.get("title") or ""

            if not doc_id:
                missing_ids += 1
            elif doc_id in seen_ids:
                duplicate_ids += 1
            else:
                seen_ids.add(doc_id)

            if not text.strip():
                empty_docs += 1
                continue

            length = len(text)
            lengths.append(length)

            if length < 100:
                short_docs += 1

            if length > 50000:
                long_docs += 1

            if len(samples) < 5:
                samples.append({
                    "id": doc_id,
                    "title": title,
                    "text_preview": text[:200]
                })

lengths.sort()

print("\nTECHQA QUALITY REPORT")
print("---------------------")
print("Total documents:", total_docs)
print("Empty documents:", empty_docs)
print("Missing document IDs:", missing_ids)
print("Duplicate document IDs:", duplicate_ids)
print("Documents under 100 characters:", short_docs)
print("Documents over 50,000 characters:", long_docs)

if lengths:
    print("Minimum text length:", lengths[0])
    print("Maximum text length:", lengths[-1])
    print("Average text length:", round(sum(lengths)/len(lengths), 2))
    print("Median text length:", lengths[len(lengths)//2])

print("\nSAMPLE DOCUMENTS")

for doc in samples:
    print("\nID:", doc["id"])
    print("Title:", doc["title"])
    print("Text:", doc["text_preview"])
