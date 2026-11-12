# Dataset analysis

**Inspection date:** 2026-11-12  
**Storage format:** Hugging Face Parquet conversion; raw records and
annotations were not transformed.

## Download status

| Dataset | Source | Status |
|---|---|---|
| IBM TechQA train/dev/Technotes | [IBM/techqa](https://github.com/IBM/techqa) | **Unavailable**: the official URL returned HTTP 404. No mirror, blind test set, or synthetic replacement was used. |
| SQuAD 2.0 | [rajpurkar/squad_v2](https://huggingface.co/datasets/rajpurkar/squad_v2) | Downloaded |
| AdversarialQA | [UCLNLP/adversarial_qa](https://huggingface.co/datasets/UCLNLP/adversarial_qa) | Downloaded; all four available configurations |

## SQuAD 2.0

| Split | Examples | Columns | Answerable | Unanswerable | Disk |
|---|---:|---|---:|---:|---:|
| train | 130,319 | `id`, `title`, `context`, `question`, `answers` | 86,821 | 43,498 | 15.6 MiB |
| validation | 11,873 | same as train | 5,928 | 5,945 | 1.3 MiB |

Example question: “When did Beyonce start becoming popular?”  
Example context: begins “Beyoncé Giselle Knowles-Carter ...”  
Example answer: `in the late 1990s`, start `269`, end `285`.

The `answers` object contains parallel `text` and `answer_start` lists.
All inspected records had non-empty questions and contexts, matching list
lengths, and answer spans matching the context text.

## AdversarialQA

Every configuration has columns `id`, `title`, `context`, `question`,
`answers`, and `metadata`; `metadata` contains `split` and
`model_in_the_loop`. The configurations and splits are:

| Configuration | Train | Validation | Test | Disk |
|---|---:|---:|---:|---:|
| `adversarialQA` | 30,000 | 3,000 | 3,000 | 5.1 MiB |
| `dbert` | 10,000 | 1,000 | 1,000 | 2.6 MiB |
| `dbidaf` | 10,000 | 1,000 | 1,000 | 2.6 MiB |
| `droberta` | 10,000 | 1,000 | 1,000 | 2.7 MiB |
| **Total** | **60,000** | **6,000** | **6,000** | **13.0 MiB** |

Train and validation records are answerable in all four configurations.
The downloaded test splits contain empty `answers.text` and
`answers.answer_start` arrays for every record (1,000 or 3,000 records,
depending on configuration). This is an upstream format characteristic and
must be treated as an unanswerable/no-gold-answer evaluation condition, not
as a missing-download error.

Example answerable record: question “what concept is mentioned last?”,
answer `subjective idealism`, start `742`, end `761`. Example test record:
the answer arrays are empty, so no answer span can be reported.

Across all downloaded files, the inspection found zero malformed records and
zero answer spans whose recorded text disagreed with the corresponding
context substring.

## TechQA assessment

TechQA is therefore **not available locally**. The requested official source
could not be downloaded, and the blind test set is explicitly not public.
Consequently, candidate Technotes, TechQA answer spans, and answerability
labels could not be inspected. TechQA cannot yet support this repository's
extractive QA experiments or domain-adaptive pretraining. Once an authorized
official release is obtained, it should be placed under
`data/raw/techqa/{train,dev,technotes}/` and inspected before use.

## Comparability and research use

- SQuAD 2.0 is a general-domain extractive QA baseline with explicit
  answerable/unanswerable examples and character offsets.
- AdversarialQA is useful for robustness evaluation, but its model-specific
  configurations are separate datasets rather than ordinary model splits.
  Keep the configuration name in evaluation results.
- The empty AdversarialQA test answers make exact-match/F1 against gold spans
  impossible for those files without an authorized answer key. They can still
  be retained for prediction-only or qualitative robustness workflows.
- No downloaded dataset supplies the requested technical-domain corpus.
  Domain-adaptive pretraining and the technical-domain comparison must wait
  for an authorized TechQA/Technotes release.
