
import json

base = "data/raw/TechQA/training_and_dev/"

with open(base + "dev_Q_A.json") as f:
    questions = json.load(f)

with open(base + "training_dev_technotes.json") as f:
    documents = json.load(f)

answerable = 0
missing_docs = 0
invalid_offsets = 0
answer_mismatches = 0
missing_candidate_ids = 0

for q in questions:
    if q["ANSWERABLE"] != "Y":
        continue

    answerable += 1
    doc_id = q["DOCUMENT"]

    if doc_id not in documents:
        missing_docs += 1
        continue

    if doc_id not in q["DOC_IDS"]:
        missing_candidate_ids += 1

    text = documents[doc_id]["text"]
    start = int(q["START_OFFSET"])
    end = int(q["END_OFFSET"])

    if start < 0 or end > len(text) or start >= end:
        invalid_offsets += 1
        continue

    if text[start:end] != q["ANSWER"]:
        answer_mismatches += 1
        expected = " ".join(q["ANSWER"].split())
        extracted = " ".join(text[start:end].split())
        if expected == extracted:
            print("TYPE: WHITESPACE DIFFERENCE")
        else:
            print("TYPE: CONTENT DIFFERENCE")       

        print("\nMISMATCH FOUND")
        print("Question ID:", q["QUESTION_ID"])
        print("Document ID:", doc_id)
        print("Start:", start)
        print("End:", end)
        print("Expected:", repr(q["ANSWER"]))
        print("Extracted:", repr(text[start:end]))

print("\nTECHQA VALIDATION REPORT")
print("-----------------------")
print("Answerable questions:", answerable)
print("Missing documents:", missing_docs)
print("Missing candidate IDs:", missing_candidate_ids)
print("Invalid offsets:", invalid_offsets)
print("Answer mismatches:", answer_mismatches)
