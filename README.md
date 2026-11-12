# Domain-Adaptive and Robustness-Aware Question Answering

Research project: **Domain-Adaptive and Robustness-Aware Question Answering: A Comparative Study of Fine-Tuned BERT Variants Under Data-Scarce and Adversarial Conditions.**

## Research overview

This project studies extractive Question Answering (QA), where a model identifies an answer span in a supplied context. It compares BERT-family models under three controlled conditions: technical-domain adaptation, limited labelled data, and adversarially modified inputs.

No experimental results are reported at this stage. Dataset selection, implementation, experiments, analysis, and paper writing remain in progress.

## Problem statement

Transformer QA systems can perform well on benchmark data while remaining sensitive to domain shift, limited supervision, and changes to input wording. This study will evaluate these factors systematically and document the conditions under which model performance changes.

## Research objectives

- Compare extractive QA performance across selected BERT-family models.
- Measure the effect of technical-domain adaptation.
- Characterize performance under multiple labelled-data budgets.
- Evaluate robustness to distractor insertion, word substitution, and paraphrasing.
- Produce reproducible metrics, plots, and comparative analyses.

## Research dimensions

1. **Domain adaptation** — Compare models before and after adaptation to technical-domain text.
2. **Data scarcity** — Evaluate training with progressively smaller portions of labelled QA data.
3. **Adversarial robustness** — Test modified inputs while preserving the original QA task where possible.

## Models under comparison

Primary models:

- BERT
- RoBERTa
- DeBERTa

Optional models:

- DistilBERT
- ALBERT

The study does not assume that any model will outperform another.

## Technology stack

Python, PyTorch, Hugging Face Transformers, Hugging Face Datasets, scikit-learn, Pandas, NumPy, Matplotlib, Seaborn, Jupyter Notebook, Git, and GitHub.

## Dataset selection status

Dataset selection is **pending**. Candidate datasets will be assessed for extractive QA format, licensing, domain relevance, answer-span quality, and suitability for domain-adaptation and data-scarcity experiments. Datasets will not be committed to this repository.

## Experimental workflow

1. Review literature and define research questions.
2. Select and document suitable datasets.
3. Explore and preprocess the data.
4. Establish baseline extractive QA experiments.
5. Run domain-adaptation experiments.
6. Repeat evaluations across data budgets.
7. Generate adversarial variants and evaluate robustness.
8. Compare metrics, create visualizations, and document findings.

## Repository structure

```text
configs/              Experiment and dataset configuration
data/                 Local data locations; contents are ignored by Git
notebooks/            Ordered exploratory and analysis notebooks
src/                  Reusable data, model, training, and evaluation code
experiments/          Experiment entry points grouped by research dimension
results/              Generated metrics, plots, and comparisons
tests/                Automated tests for project code
docs/                 Research planning and study documentation
```

See `data/README.md` and the documentation files under `docs/` for more detail.

## Installation

```bash
git clone https://github.com/VaibhavUPratap/Domain-Adaptive-and-Robustness-Aware-Question-Answering.git
cd Domain-Adaptive-and-Robustness-Aware-Question-Answering
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

The repository currently contains structure and planning documentation only. Training, dataset downloads, and experiments are intentionally not implemented.

## Project progress

- [x] Define research scope and comparison dimensions
- [x] Establish repository structure
- [x] Add initial configuration placeholders
- [x] Add research documentation placeholders
- [ ] Select and document datasets
- [ ] Implement preprocessing pipeline
- [ ] Implement baseline QA experiments
- [ ] Implement domain-adaptation experiments
- [ ] Implement data-scarcity experiments
- [ ] Implement adversarial robustness experiments
- [ ] Analyze results and write the research paper

## License

This project is released under the MIT License. See `LICENSE`.

