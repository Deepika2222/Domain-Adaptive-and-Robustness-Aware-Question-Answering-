# Research datasets

This directory contains local copies of the public datasets used by the
project. Raw files are intentionally excluded from Git; see
[`docs/dataset_analysis.md`](../docs/dataset_analysis.md) for the inspection
report and limitations.

## Sources and layout

- `raw/squad_v2/` — Hugging Face `rajpurkar/squad_v2`, train and validation
  Parquet files.
- `raw/adversarial_qa/` — Hugging Face `UCLNLP/adversarial_qa`, configurations
  `adversarialQA`, `dbert`, `dbidaf`, and `droberta`, each with train,
  validation, and test files.
- `raw/techqa/` — reserved for IBM TechQA. The requested official
  `IBM/techqa` repository currently returns HTTP 404, so no TechQA files were
  fabricated or substituted.
- `processed/` — reserved for derived data; no preprocessing was performed.
- `adversarial/` — reserved for generated variants; none were generated.

The downloaded Parquet files are Hugging Face's lossless dataset conversion,
not transformed examples. They preserve the source columns and annotations.

## Reproducible download

The public files can be downloaded with the Python helper:

```bash
python3 data/download_datasets.py
```

It obtains current Parquet metadata from the Hugging Face datasets-server,
uses `curl -C -` for resumable downloads, writes `.part` files until the
expected byte size is reached, and never overwrites a verified file.

## Licensing and limitations

Consult the upstream dataset cards and repositories before redistribution:

- [SQuAD 2.0](https://huggingface.co/datasets/rajpurkar/squad_v2) and its
  [official repository](https://github.com/rajpurkar/SQuAD-explorer).
- [AdversarialQA](https://huggingface.co/datasets/UCLNLP/adversarial_qa) and
  its [official repository](https://github.com/ibm-aur-nlp/AdversarialQA).
- [IBM TechQA](https://github.com/IBM/techqa), which was unavailable at
  download time. The blind test set is not publicly available and is not
  reconstructed here.

Dataset terms may differ from the project license. Keep raw files local and
do not upload them to GitHub.
