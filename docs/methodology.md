# Methodology

- **Task**: Extractive Question Answering (span prediction).
- **Models**: BERT, RoBERTa, DeBERTa (optional: DistilBERT, ALBERT).
- **Phases**:
  1. Baseline fine-tuning on selected QA benchmark.
  2. Domain-adaptation experiments on technical corpus.
  3. Data-scarcity experiments via controlled subsampling.
  4. Adversarial robustness evaluation with transformed inputs.
- **Evaluation**: Exact Match (EM), F1, and robustness drop analyses.
