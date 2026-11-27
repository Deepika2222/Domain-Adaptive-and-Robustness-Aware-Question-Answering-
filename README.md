# Domain-Adaptive and Robustness-Aware Question Answering

### A Comparative Study of Fine-Tuned BERT Variants Under Data-Scarce and Adversarial Conditions

A research project investigating the performance, domain adaptability, and robustness of transformer-based extractive Question Answering (QA) models under technical-domain shift, limited labelled data, and adversarial input conditions.

---

## Research Overview

Extractive Question Answering (QA) systems identify and extract answer spans from a given context in response to natural-language questions.

Although transformer-based models achieve strong performance on standard QA benchmarks, their performance can be affected by domain shifts, limited training data, and adversarial modifications to input text.

This research aims to systematically investigate these challenges through a comparative evaluation of selected BERT-family architectures.

**Research Question (Frozen: 26 November 2026)**

How do different BERT-family models perform under domain adaptation, data scarcity, and adversarial conditions in technical question answering?

**Research USP:** A model-wise comparative analysis across three controlled research dimensions: domain adaptation, data scarcity, and adversarial robustness.

See [`docs/final_research_direction.md`](docs/final_research_direction.md) for the finalized research direction.

> **Current status:** Research design and dataset auditing are underway. Model implementation, experiments, evaluation, and paper writing remain in progress. No experimental results are claimed at this stage.

---

## Problem Statement

Transformer-based QA models may perform well on general-domain benchmarks but struggle when applied to specialized technical domains or when training data is limited.

Additionally, minor modifications to question and context wording can affect their ability to identify correct answer spans.

This research investigates these limitations by evaluating different BERT-family models under controlled experimental conditions.

---

## Research Objectives

- Compare extractive QA performance across selected BERT-family models.
- Investigate the impact of technical-domain adaptation.
- Evaluate model performance under different labelled-data budgets.
- Analyze robustness against distractor insertion, word substitution, and paraphrasing.
- Compare model performance using reproducible evaluation metrics.
- Identify performance trade-offs across the three research dimensions.

---

## Research Dimensions

### 1. Domain Adaptation

Investigate how adapting pretrained models to technical-domain text affects their extractive QA performance.

### 2. Data Scarcity

Evaluate model performance using progressively smaller portions of labelled training data to understand their sensitivity to limited supervision.

### 3. Adversarial Robustness

Evaluate model performance against modified inputs, including:

- Distractor insertion
- Word substitution
- Paraphrasing

The modifications will aim to preserve the original QA task wherever possible.

---

## Models Under Comparison

**Primary Models**

| Model | Architecture |
|---|---|
| BERT | Bidirectional Encoder Representations from Transformers |
| RoBERTa | Robustly Optimized BERT Pretraining Approach |
| DeBERTa | Decoding-enhanced BERT with Disentangled Attention |

**Optional Models**

- DistilBERT
- ALBERT

The final model selection will depend on experimental feasibility and available computational resources.

No model is assumed to outperform another before experimentation.

---

## Datasets

Three datasets have been downloaded locally and audited for this research.

| Dataset | Research Role |
|---|---|
| TechQA | Technical-domain question answering and domain adaptation |
| SQuAD 2.0 | General-domain extractive QA and baseline evaluation |
| AdversarialQA | Adversarial robustness evaluation |

### Dataset Details

**1. TechQA**

- Source: IBM Research
- Domain: Technical support and troubleshooting
- Includes technical questions, supporting documents, and answer annotations.
- The associated Technote corpus contains approximately 801,998 documents and supports the planned domain-adaptive pretraining.

Local directory: `data/raw/TechQA/`

**2. SQuAD 2.0**

- General-domain extractive QA benchmark.
- Includes answerable and unanswerable questions.
- Used as a source dataset for baseline evaluation and data-scarcity experiments.

Local directory: `data/raw/squad_v2/`

**3. AdversarialQA**

- Designed to evaluate robustness in extractive question answering.
- Includes multiple configurations:
  - `adversarialQA`
  - `dbert`
  - `dbidaf`
  - `droberta`

Local directory: `data/raw/adversarial_qa/`

For dataset counts, schemas, audit results, and known issues, refer to:

- [`docs/dataset_analysis.md`](docs/dataset_analysis.md)
- [`docs/dataset_audit.md`](docs/dataset_audit.md)

**Note:** Dataset files are stored locally and are not committed to this repository.

---

## Experimental Workflow

The research follows a structured experimental workflow:

1. Literature review and research-question formulation.
2. Dataset selection, downloading, and auditing.
3. Exploratory data analysis and preprocessing.
4. Baseline extractive QA implementation.
5. Technical-domain adaptation experiments.
6. Data-scarcity experiments using different training-data budgets.
7. Adversarial input generation and robustness evaluation.
8. Comparative evaluation across selected models.
9. Metric analysis, visualization, and interpretation.
10. Research documentation and paper preparation.

---

## Evaluation Metrics

The study will use appropriate metrics for extractive question answering and robustness evaluation.

| Metric | Purpose |
|---|---|
| Exact Match (EM) | Measures exact answer-span matching |
| F1 Score | Measures token-level overlap between predicted and reference answers |
| Robustness Retention | Measures performance retained after input modification |
| Performance Degradation | Measures the change in performance between original and modified inputs |

Additional analysis may include model-wise comparisons across data budgets and domain-adaptation conditions.

---

## Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Deep Learning | PyTorch |
| NLP Models | Hugging Face Transformers |
| Dataset Management | Hugging Face Datasets |
| Data Processing | Pandas, NumPy |
| Evaluation | Scikit-learn |
| Visualization | Matplotlib, Seaborn |
| Development | Jupyter Notebook |
| Version Control | Git, GitHub |

---

## Repository Structure

```text
Domain-Adaptive-and-Robustness-Aware-Question-Answering/
│
├── configs/
│   └── Experiment and dataset configurations
│
├── data/
│   ├── raw/
│   │   ├── TechQA/
│   │   ├── squad_v2/
│   │   └── adversarial_qa/
│   └── README.md
│
├── notebooks/
│   └── Exploratory data analysis and experiments
│
├── src/
│   └── Reusable preprocessing, training,
│       modeling, and evaluation modules
│
├── experiments/
│   ├── Domain adaptation
│   ├── Data scarcity
│   └── Adversarial robustness
│
├── results/
│   └── Metrics, plots, and comparisons
│
├── scripts/
│   └── Dataset downloading and auditing scripts
│
├── tests/
│   └── Automated tests
│
├── docs/
│   ├── final_research_direction.md
│   ├── dataset_analysis.md
│   └── dataset_audit.md
│
├── requirements.txt
├── LICENSE
└── README.md
```

Some directories and experiment modules are planned and may not yet contain implemented functionality.

---

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Deepika2222/Domain-Adaptive-and-Robustness-Aware-Question-Answering-.git

cd Domain-Adaptive-and-Robustness-Aware-Question-Answering-
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it:

**macOS / Linux**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip

pip install -r requirements.txt
```

### 4. Verify Installation

```bash
python -c "import torch, transformers, datasets; print('Environment ready')"
```

---

## Project Progress

The project is currently in the research preparation and dataset auditing stage.

- [x] Define research scope and comparison dimensions.
- [x] Finalize the research question.
- [x] Establish repository structure.
- [x] Prepare initial configuration and documentation.
- [x] Select research datasets.
- [x] Download and audit selected datasets.
- [x] Implement preprocessing and tokenization pipeline.
- [ ] Implement baseline QA experiments.
- [ ] Implement domain-adaptation experiments.
- [ ] Implement data-scarcity experiments.
- [ ] Implement adversarial robustness experiments.
- [ ] Perform comparative evaluation.
- [ ] Generate visualizations and analyze findings.
- [ ] Prepare and write the research paper.

---

## Research Contributions

This project is a collaborative research effort by:

| Contributor | GitHub Profile |
|---|---|
| **Vaibhav U Pratap** | [@VaibhavUPratap](https://github.com/VaibhavUPratap) |
| **Deepika M** | [@Deepika2222](https://github.com/Deepika2222) |

Both contributors collaborate on the research process, including research planning, dataset preparation, implementation, experimentation, evaluation, and documentation.

We welcome constructive feedback, technical discussions, and contributions from the research and open-source community.

---

## Contributing

Contributions, suggestions, and discussions are welcome.

If you would like to contribute:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes and test them.
4. Submit a pull request describing your contribution.

Please maintain reproducibility and document any changes affecting the research methodology or experimental setup.

---

## License

This project is licensed under the **MIT License**.

See the [`LICENSE`](LICENSE) file for details.

---

**Research Focus:** Domain Adaptation | Data Scarcity | Adversarial Robustness

**Project:** Domain-Adaptive and Robustness-Aware Question Answering