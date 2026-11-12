# Research Questions

## Project

**Domain-Adaptive and Robustness-Aware Question Answering: A Comparative Study of Fine-Tuned BERT Variants Under Data-Scarce and Adversarial Conditions**

## Main research question

**Under a controlled experimental protocol, how do selected BERT-family models differ in technical-domain extractive QA performance when labelled data is scarce, domain-adaptive pretraining is applied, and adversarial perturbations are introduced?**

## Primary research questions

### RQ1 — Baseline model comparison

How do BERT, RoBERTa and DeBERTa compare on the selected technical-domain extractive QA task when trained and evaluated using the same dataset splits and comparable tuning budgets?

**Evidence to collect**
- Exact Match (EM)
- Token-level F1
- Validation performance
- Training time and inference latency
- Parameter count and memory use, where feasible

### RQ2 — Domain adaptation

Does continued masked-language-model pretraining on unlabeled technical-domain documents improve extractive QA performance compared with using the original pretrained checkpoint?

**Comparison**
- Condition A: original pretrained checkpoint → QA fine-tuning
- Condition B: original pretrained checkpoint → technical-domain MLM adaptation → QA fine-tuning

**Evidence to collect**
- Clean in-domain EM and F1
- Held-out-domain results, if a suitable split or dataset is available
- Training cost of the additional adaptation stage
- Changes in performance under adversarial evaluation

### RQ3 — Data scarcity

How does reducing the amount of labelled QA training data affect the performance and sample efficiency of each model?

**Candidate training-data budgets**
- 1%
- 5%
- 10%
- 25%
- 50%
- 100%

These are proposed levels, not fixed requirements. Adjust them after inspecting the dataset size and class/answerability distribution.

**Evidence to collect**
- EM and F1 at each budget
- Learning curves
- Variation across random seeds
- The amount of data required to reach a chosen performance level

### RQ4 — Adversarial robustness

How sensitive are the selected models to controlled adversarial modifications of the question or context?

**Candidate attack categories**
- Distractor-sentence insertion (AddSent-style)
- Meaning-preserving lexical substitution
- Question paraphrasing

**Evidence to collect**
- Clean versus attacked EM and F1
- Absolute and relative performance degradation
- Attack success rate, with its definition stated explicitly
- Validity checks confirming that the answer remains supported and answer spans are correctly updated

### RQ5 — Interaction between the three conditions

Does domain-adaptive pretraining change the way each model responds to reduced labelled-data budgets and adversarial perturbations?

This is the central integrative question. It distinguishes a set of separate experiments from a study of how the conditions interact.

**Evidence to collect**
- Model-by-data-budget comparisons with and without domain adaptation
- Clean and adversarial scores for each condition
- Whether model rankings change across conditions
- Statistical variability across repeated runs

### RQ6 — Practical trade-offs

Which model provides the most suitable balance of answer quality, low-data performance, adversarial robustness and computational cost in the tested technical QA setting?

This question should be answered using measured results, not assumptions about model architecture.

## Hypotheses to test

The following are **testable hypotheses**, not established findings:

- **H1:** Model rankings on the full training set may differ from rankings under very small labelled-data budgets.
- **H2:** Technical-domain continued pretraining may improve technical QA performance, but the benefit may vary by model and data budget.
- **H3:** Adversarial perturbations will reduce performance relative to clean inputs, with the magnitude depending on model and attack type.
- **H4:** Domain adaptation may change the size of the performance drop under adversarial perturbations.
- **H5:** The model with the highest clean EM/F1 may not have the best robustness or efficiency trade-off.

## Important experimental controls

- Use the same train/validation/test split for all model comparisons.
- Keep the test set fixed across data budgets.
- Use model-appropriate tokenizers and document checkpoint versions.
- Use comparable hyperparameter-search budgets.
- Fix and record random seeds; repeat runs where possible.
- Do not use test data for training, model selection or domain-adaptive pretraining.
- Keep natural distribution shifts separate from deliberately generated adversarial examples.
- Report missing or infeasible experiments transparently.

## Decision rule

Do not answer the research questions from intuition or from another paper's results. Answer them only after the corresponding experiments have been run and the results have been checked.
