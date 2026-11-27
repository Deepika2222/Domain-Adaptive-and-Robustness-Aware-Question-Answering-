# Project Architecture & Repository Guide

**Domain-Adaptive and Robustness-Aware Question Answering**  
A Comparative Study of Fine-Tuned BERT Variants Under Data-Scarce and Adversarial Conditions.

---

## 1. Directory Structure

```text
Domain-Adaptive-and-Robustness-Aware-Question-Answering-/
├── configs/                  # Experiment, model, and dataset configuration files
│   ├── dataset_config.yaml   # Dataset sources, formats, and paths
│   ├── experiment_config.yaml# Seed, data budget fractions, and dimensions
│   └── model_config.yaml     # Model architectures, tokenizers, and checkpoints
├── data/                     # Local data storage (excluded from Git tracking)
│   ├── raw/                  # Pristine source datasets
│   │   ├── TechQA/           # IBM TechQA corpus and QA annotations
│   │   ├── squad_v2/         # General-domain SQuAD 2.0 Parquet files
│   │   └── adversarial_qa/   # AdversarialQA splits (dbert, dbidaf, droberta, advQA)
│   ├── processed/            # Cleaned, stratified, and tokenized datasets
│   │   ├── squad2/           # Processed subsets (1%, 5%, 10%, val) & tokenized/
│   │   └── squad_v2 -> squad2 # Symlink for backwards-compatible path access
│   ├── adversarial/          # Generated adversarial perturbations & stress tests
│   └── download_datasets.py  # Automated downloader script for public benchmarks
├── docs/                     # Study planning, literature review, and audit documentation
│   ├── PROJECT_GUIDE.md      # Repository architecture and directory standards (this file)
│   ├── NOTEBOOKS_GUIDE.md    # Guide to exploratory, preprocessing, and experiment notebooks
│   ├── PROJECT_COMPLETION_STATUS.md # Live project milestone and progress report
│   ├── literature_review.md  # Comprehensive extractive QA & domain adaptation review
│   ├── methodology.md        # Experimental methodology and evaluation framework
│   ├── dataset_audit.md      # PyArrow verification of raw dataset schemas and offsets
│   └── dataset_analysis.md   # Analysis of dataset distributions and answerability
├── experiments/              # Experiment entry points grouped by research dimension
│   ├── baseline/             # Standard general-domain extractive QA fine-tuning
│   ├── domain_adaptation/    # DAPT MLM pretraining + technical transfer
│   ├── data_scarcity/        # Low-resource training runs (1%, 5%, 10%)
│   └── adversarial/          # Adversarial evaluation and perturbation testing
├── notebooks/                # Numbered progression of research notebooks
│   ├── 01_exploration/       # Dataset discovery and EDA (squad, techqa, adversarialqa)
│   ├── 02_data_preprocessing/# Preprocessing, sliding window chunking, tokenization
│   ├── 03_baseline_experiments.ipynb # Baseline model fine-tuning and evaluation
│   ├── 04_domain_adaptation.ipynb    # DAPT and domain transfer experiments
│   ├── 05_data_scarcity.ipynb        # Data scarcity scaling curves
│   ├── 06_adversarial_robustness.ipynb# Adversarial stress tests
│   └── 07_comparative_analysis.ipynb # Results synthesis and cross-model comparison
├── results/                  # Generated metrics, comparison tables, and figures
│   ├── metrics/              # JSON/CSV evaluation outputs (EM, F1, latency)
│   ├── comparison/           # Cross-condition comparative summaries
│   └── plots/                # High-resolution figures for paper manuscript
├── scripts/                  # Standalone CLI tools for inspection and validation
│   ├── adversarial/          # Verification scripts for AdversarialQA
│   ├── squad2.0/             # Verification scripts for SQuAD 2.0
│   └── techqa/               # Corpus quality & Technotes extraction scripts
├── src/                      # Modular Python package for core logic
│   ├── data/                 # Dataset loaders and schema definitions
│   ├── preprocessing/        # FastTokenizer offset mapping & sliding window logic
│   ├── training/             # PyTorch / HF Trainer pipelines & training loops
│   ├── evaluation/           # Exact Match (EM) & Macro F1 metric computation
│   ├── domain_adaptation/    # MLM masking & continual pretraining
│   ├── data_scarcity/        # Stratified subset samplers & few-shot harnesses
│   ├── adversarial/          # Perturbation generators (typo, distractor, paraphrase)
│   └── utils/                # Reproducibility seeds, logging, and I/O helpers
├── tests/                    # Automated unit and integration test suite
├── .gitignore                # Excludes large binaries, cache, and processed data
├── requirements.txt          # Python environment dependencies
└── README.md                 # Project introduction and quick-start instructions
```

---

## 2. Path Conventions & Best Practices

1. **Root-Relative Paths**:
   All scripts, notebooks, and source modules should resolve paths using the repository root:
   ```python
   from pathlib import Path
   PROJECT_ROOT = Path.cwd().resolve()
   while PROJECT_ROOT.name != "Domain-Adaptive-and-Robustness-Aware-Question-Answering-" and PROJECT_ROOT.parent != PROJECT_ROOT:
       PROJECT_ROOT = PROJECT_ROOT.parent
   ```
2. **Processed Data Storage**:
   Processed artifacts (subsets, tokenized caches) must always be saved under `data/processed/` at the repository root, never inside notebook subdirectories.
3. **No Heavy Binaries in Git**:
   Large parquet files, models, and virtual environments are strictly ignored via `.gitignore`.
