# Project Completion Status & Roadmap Report

**Project Title:** Domain-Adaptive and Robustness-Aware Question Answering: A Comparative Study of Fine-Tuned BERT Variants Under Data-Scarce and Adversarial Conditions  
**Evaluation Date:** November 18, 2026 (dataset status updated November 26, 2026)  
**Repository State:** `main` branch (Latest commit at evaluation: `76845e8 - data exploration done`; at update: `58ac1ca - little changes`)  

> **Update, November 26, 2026:** TechQA is no longer a blocker. The full release (train/dev, validation sample, and 801,998-document Technote corpus) is stored locally under `data/raw/TechQA/` and has been audited (see `docs/dataset_audit.md`). Percentages below were not re-estimated, except Phase 3 / WP2.

---

## 1. Executive Summary

| Metric | Status |
| :--- | :--- |
| **Overall Estimated Completion** | **~32%** |
| **Phase 1: Research Design & Documentation** | **100% Completed** |
| **Phase 2: Repository Architecture & Environment** | **100% Completed** |
| **Phase 3: Dataset Ingestion, Audit & EDA** | **~90% Completed** (All three datasets acquired and audited; TechQA and AdversarialQA exploration notebooks still empty) |
| **Phase 4: Preprocessing & Tokenization Pipeline** | **0% Not Started** (Placeholders present) |
| **Phase 5: Baseline QA Modeling & Benchmarking** | **0% Not Started** (Placeholders present) |
| **Phase 6: Domain Adaptation Experiments** | **0% Not Started** (TechQA Technote corpus available for DAPT) |
| **Phase 7: Data Scarcity Experiments** | **0% Not Started** (Placeholders present) |
| **Phase 8: Adversarial Robustness Evaluation** | **0% Not Started** (Placeholders present) |
| **Phase 9: Results Synthesis & Manuscript** | **20% Drafted** (Literature review & methodology ready) |

---

## 2. Component-by-Component Audit

### 2.1 Research Foundation & Documentation (100% Complete)
- [x] **Literature Review**: [`docs/literature_review.md`](literature_review.md) & [`docs/QA_Literature_Review_Verified_with_Research_Gap.pdf`](QA_Literature_Review_Verified_with_Research_Gap.pdf) covering extractive QA, domain transfer, data scarcity, and adversarial perturbations.
- [x] **Research Objectives & Questions**: Defined in [`docs/research_objectives.md`](research_objectives.md) and [`docs/research_questions.md`](research_questions.md).
- [x] **Research Gap & Methodology**: Articulated in [`docs/research_gap.md`](research_gap.md) and [`docs/methodology.md`](methodology.md).

### 2.2 Environment & Project Structure (100% Complete)
- [x] **Standard Directory Layout**: `configs/`, `data/`, `docs/`, `experiments/`, `notebooks/`, `results/`, `src/`, `tests/`.
- [x] **Configuration Files**: YAML configurations in `configs/` (`dataset_config.yaml`, `experiment_config.yaml`, `model_config.yaml`).
- [x] **Dependencies & Licensing**: Defined in `requirements.txt` and `LICENSE` (MIT).

### 2.3 Dataset Acquisition & Exploratory Data Analysis (EDA) (~90% Complete)
- [x] **Download Automation**: `data/download_datasets.py` implemented for automated HF Parquet ingestion.
- [x] **Dataset Audit**: In-depth audit in [`docs/dataset_audit.md`](dataset_audit.md) verifying 14 Parquet files (214,192 rows, 29.80 MiB), plus TechQA dev-answer alignment and Technote corpus checks.
- [x] **SQuAD 2.0 Exploration Notebook**: [`notebooks/01_exploration/squad_exploration.ipynb`](../notebooks/01_exploration/squad_exploration.ipynb) executed with visualizations and statistics.
- [ ] **TechQA and AdversarialQA Exploration Notebooks**: `notebooks/01_exploration/techqa_exploration.ipynb` and `adversarialqa_exploration.ipynb` are empty files; the analysis currently lives in `scripts/techqa/` and `scripts/adversarial/`.
- [x] **Dataset Analysis Summary**: [`docs/dataset_analysis.md`](dataset_analysis.md).
- [x] **Technical Domain Corpus (resolved)**: The IBM GitHub route returned HTTP 404, but the full TechQA release was obtained from the PrimeQA/TechQA archive on Hugging Face and is stored at `data/raw/TechQA/` (CDLA-Permissive-1.0). It provides 600 training and 310 dev questions, 28,482 train/dev Technotes, and a 801,998-document corpus for DAPT. The official test set is blind and not included.
- [ ] **TechQA span mismatches**: 11 of 160 answerable dev answers do not exactly match their stored text (2 whitespace, 9 content); resolve during preprocessing.

### 2.4 Modeling & Experimental Pipelines (0% Complete)
- [ ] **Data Preprocessing & Tokenization**: `src/preprocessing/` and the per-dataset notebooks in `notebooks/02_data_preprocessing/` are empty. Needs sliding window tokenization (`stride`), offset mapping for char-to-token span alignment, and handling unanswerable QA pairs.
- [ ] **Baseline Models**: `src/training/`, `src/evaluation/`, `experiments/baseline/`, and `notebooks/03_baseline_experiments.ipynb` are stubs. Models to implement: BERT, RoBERTa, DeBERTa (and optional DistilBERT/ALBERT) on SQuAD 2.0 (EM / F1 metrics).
- [ ] **Domain Adaptation**: `src/domain_adaptation/`, `experiments/domain_adaptation/`, and `notebooks/04_domain_adaptation.ipynb` are stubs. Requires DAPT (Masked Language Modeling on target domain corpus) followed by task fine-tuning.
- [ ] **Data Scarcity Studies**: `src/data_scarcity/`, `experiments/data_scarcity/`, and `notebooks/05_data_scarcity.ipynb` are stubs. Evaluates 100%, 10%, and 1% training splits under controlled random seeds.
- [ ] **Adversarial Robustness Evaluation**: `src/adversarial/`, `experiments/adversarial/`, and `notebooks/06_adversarial_robustness.ipynb` are stubs. Evaluates against AdversarialQA (dbert, dbidaf, droberta splits) and perturbed contexts (distractors, typos, paraphrasing).
- [ ] **Comparative Analysis & Syntheses**: `notebooks/07_comparative_analysis.ipynb` and `results/` are stubs.

---

## 3. Work Breakdown Structure (WBS) & Progress Tracker

```mermaid
pie title Project Stage Completion Ratio
    "Completed (Theory, Structure, Datasets, EDA)" : 32
    "Data Preprocessing Pipeline" : 10
    "Baseline QA Training & Eval" : 15
    "Domain Adaptation Pipeline" : 12
    "Data Scarcity & Robustness" : 16
    "Final Paper & Results Synthesis" : 15
```

| Work Package (WP) | Deliverables | Current Status | % Done |
| :--- | :--- | :--- | :---: |
| **WP1: Research Design** | Literature review, gap analysis, hypotheses, objectives | Completed | 100% |
| **WP2: Data Foundation** | Ingestion script, audit, EDA notebook, visualizations | SQuAD 2.0, AdversarialQA & TechQA acquired and audited; TechQA/AdversarialQA EDA notebooks empty | ~90% |
| **WP3: Tokenizer & Pipeline** | FastTokenizer alignment, sliding window, negative samples | Notebook 02 & `src/preprocessing/` skeleton | 0% |
| **WP4: Baseline QA** | BERT/RoBERTa/DeBERTa fine-tuning on SQuAD 2.0, EM/F1 eval | Skeletons in `src/training`, `experiments/baseline` | 0% |
| **WP5: Domain Adaptation** | MLM pretraining on technical domain + downstream QA | TechQA Technote corpus available; not started | 0% |
| **WP6: Scarcity & Robustness**| 100%/10%/1% training subsets, AdversarialQA evaluations | Skeletons in `src/data_scarcity`, `src/adversarial` | 0% |
| **WP7: Synthesis & Writing** | Comparative metrics tables, radar/line plots, final paper | Docs drafted; experimental writeup pending | 20% |

---

## 4. Immediate Critical Path & Next Steps

1. **Technical Domain Dataset Blocker — resolved (November 26, 2026)**: TechQA obtained from the PrimeQA/TechQA archive on Hugging Face; no substitute dataset is needed.
2. **Implement Preprocessing Pipeline (`src/preprocessing/` & `notebooks/02_data_preprocessing/`)**:
   - Write Hugging Face `AutoTokenizer` sliding window span extraction logic.
   - Resolve the 11 TechQA dev answers whose offsets do not match their stored text.
   - Cache preprocessed tensors into `data/processed/`.
3. **Build Baseline Training & Evaluation Engine (`src/training/` & `src/evaluation/`)**:
   - Setup Hugging Face `Trainer` or PyTorch training loops with mixed precision (`fp16`).
   - Implement official SQuAD evaluation script for Exact Match (EM) and Macro F1 scores.
4. **Execute Baseline Experiments (`03_baseline_experiments.ipynb`)**:
   - Benchmark `bert-base-uncased`, `roberta-base`, and `microsoft/deberta-base`.
