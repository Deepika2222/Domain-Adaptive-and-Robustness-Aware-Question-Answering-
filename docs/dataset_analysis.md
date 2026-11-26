# Dataset analysis

**Inspection date:** 2026-11-12  
**Storage format:** Hugging Face Parquet conversion; raw records and
annotations were not transformed.

## Download status

| Dataset | Source | Status |
|---|---|---|
| IBM TechQA train/dev/Technotes | PrimeQA/TechQA archive on Hugging Face (`TechQA.tar.gz`); the original [IBM/techqa](https://github.com/IBM/techqa) URL returned HTTP 404 | Downloaded (updated 2026-11-26) to `data/raw/TechQA/`; original release files, not Parquet. The blind test set is not public and is not included. |
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

**Updated 2026-11-26.** The original IBM route returned HTTP 404 on
2026-11-12, but the full release was later obtained from the PrimeQA/TechQA
archive on Hugging Face and is stored locally at `data/raw/TechQA/`
(CDLA-Permissive-1.0; kept out of Git). It contains:

| Component | Location | Contents |
|---|---|---|
| Training questions | `training_and_dev/training_Q_A.json` | 600 questions, 450 answerable |
| Development questions | `training_and_dev/dev_Q_A.json` | 310 questions, 160 answerable |
| Train/dev Technotes | `training_and_dev/training_dev_technotes.json` | 28,482 candidate documents |
| Validation sample | `validation/` | 20 questions with reference output and 995 Technotes |
| Technote corpus | `technote_corpus/` | 801,998 documents (about 11 GB) for DAPT |

Each question lists candidate `DOC_IDS`; answerable questions give the answer
document and character offsets (`START_OFFSET`, `END_OFFSET`). Answers are
long: the median answerable span is about 250 characters in both train and
dev. The official test set is blind and not public, so the dev set is the
held-out evaluation set. Dev-answer alignment checks and corpus statistics
are in `docs/dataset_audit.md`.

## Comparability and research use

- SQuAD 2.0 is a general-domain extractive QA baseline with explicit
  answerable/unanswerable examples and character offsets.
- AdversarialQA is useful for robustness evaluation, but its model-specific
  configurations are separate datasets rather than ordinary model splits.
  Keep the configuration name in evaluation results.
- The empty AdversarialQA test answers make exact-match/F1 against gold spans
  impossible for those files without an authorized answer key. They can still
  be retained for prediction-only or qualitative robustness workflows.
- TechQA supplies the technical-domain QA data and the unlabeled Technote
  corpus for domain-adaptive pretraining. Its 600 training questions make it
  a naturally low-resource target; dev Technotes must be excluded from any
  pretraining text to avoid leakage.
