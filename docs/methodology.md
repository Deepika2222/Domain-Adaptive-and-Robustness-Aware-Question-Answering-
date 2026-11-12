# Methodology

## 1. Research design

This project uses a **controlled empirical comparative design**. Selected BERT-family models will be evaluated on an extractive technical-domain QA task under baseline, domain-adaptation, data-scarcity and adversarial conditions.

The central experimental factors are:

- Model architecture
- Domain-adaptive pretraining condition
- Amount of labelled QA training data
- Evaluation condition (clean, shifted and adversarial)

The exact experimental matrix will be finalized after dataset inspection and a compute-feasibility check.

## 2. Task definition

Each example contains:

- A context or passage
- A question
- A gold answer, represented by a text span and its character offsets where available
- An answerability label, if supported by the dataset

An extractive QA model predicts start and end token positions for the answer span. For unanswerable examples, the model must follow the dataset/model convention for predicting no answer.

Do not combine datasets with incompatible answer formats without documenting and resolving the differences.

## 3. Candidate datasets

### Primary candidate: TechQA

TechQA is a technical question-answering dataset associated with technical support and documentation. It is a strong candidate for the project's technical-domain focus.

Before adoption, inspect:
- Dataset license and permitted use
- Availability and download requirements
- Number of train, validation and test examples
- Context and question fields
- Answer-span format and answerability
- Whether the examples can be used directly for extractive span prediction
- Dataset-specific preprocessing instructions

Official project repository: https://github.com/IBM/TechQA

**Important:** Do not assume every TechQA example is directly usable as a conventional extractive QA example. Verify the annotations and task formulation first.

### General-domain reference: SQuAD 2.0

SQuAD 2.0 can provide a general-domain reference and includes unanswerable questions.

Dataset page: https://rajpurkar.github.io/SQuAD-explorer/

Use it only in a clearly specified role, such as a general-domain baseline or mixed-domain training condition. Do not silently mix it into the technical training set.

### Other candidates

Natural Questions and other QA resources may be considered only after confirming that their task format, answer annotations and evaluation protocol are compatible with the project's extractive setting.

## 4. Dataset selection and audit

Before model training:

1. Download the candidate dataset from its official source.
2. Read the dataset documentation and license.
3. Inspect raw files and schemas.
4. Count examples in each split.
5. Check missing, duplicated and malformed examples.
6. Inspect answerability and answer-span annotations.
7. Verify that each gold answer occurs in its context where the dataset requires extractive spans.
8. Identify possible leakage between training, validation and test data.
9. Record the dataset version, download date and preprocessing decisions.
10. Decide whether a held-out technical domain or a second dataset is available for out-of-domain evaluation.

Create a dataset report before proceeding.

## 5. Preprocessing

The preprocessing pipeline should:

- Normalize only what is necessary; preserve meaningful technical terms, symbols, identifiers and version numbers.
- Validate answer character offsets before tokenization.
- Tokenize with the tokenizer corresponding to each model checkpoint.
- Map character-level answer offsets to token start and end positions.
- Handle long contexts with a documented truncation or sliding-window strategy.
- Preserve example identifiers so predictions can be traced back to source records.
- Record examples that are skipped and the reason for exclusion.

Do not apply one model's tokenizer to all architectures.

## 6. Models

Primary models:

- BERT-base
- RoBERTa-base
- DeBERTa-v3-base

Optional models:

- DistilBERT
- ALBERT

For each model, record:
- Exact Hugging Face checkpoint identifier
- Model and tokenizer revision
- Number of parameters
- Maximum input length
- QA head configuration
- Training hyperparameters
- Software and hardware environment

The same task formulation and evaluation script should be used across models, while respecting model-specific input conventions.

## 7. Experimental stages

### Stage A — Baseline QA fine-tuning

For each primary model:

1. Start from the original pretrained checkpoint.
2. Fine-tune on the selected QA training set.
3. Select checkpoints using validation data only.
4. Evaluate once on the held-out test set.
5. Record EM, token F1 and computational measures.

This establishes the baseline against which later experiments are compared.

### Stage B — Domain-adaptive pretraining

If a suitable unlabeled technical corpus is available:

1. Collect technical documents that are legally usable.
2. Remove or exclude test-set content to prevent leakage.
3. Apply the model's masked-language-model objective to the technical corpus.
4. Save the domain-adapted checkpoint.
5. Fine-tune that checkpoint on the same labelled QA training data used in Stage A.
6. Compare against the original-checkpoint condition.

The intended comparison is:

- Original pretrained model → QA fine-tuning
- Original pretrained model → technical-domain MLM adaptation → QA fine-tuning

Use comparable downstream training settings. Report the extra compute required for adaptation.

### Stage C — Data-scarcity experiments

Create reproducible subsets of the training split. Candidate proportions are 1%, 5%, 10%, 25%, 50% and 100%, subject to dataset size.

For every budget:

1. Generate the subset using a recorded seed.
2. Preserve the same validation and test sets.
3. Fine-tune each model under the same protocol.
4. Repeat with multiple seeds where feasible.
5. Record EM, F1 and variation.

If the dataset has answerable and unanswerable examples, use a sampling strategy that avoids accidentally changing their proportions without reporting it.

### Stage D — Adversarial robustness

Evaluate models on clean and modified inputs.

Candidate attack families:

**1. Distractor insertion**
- Insert irrelevant or misleading sentences into the context.
- Preserve the original answer-bearing evidence.
- Check whether the model selects the correct answer despite the distractor.

**2. Lexical substitution**
- Replace selected words with meaning-preserving alternatives.
- Ensure technical terms, named entities and answer evidence are not unintentionally changed.
- Verify semantic and answer-span validity.

**3. Question paraphrasing**
- Rephrase the question while preserving its meaning and answer.
- Check that the paraphrase does not introduce ambiguity or change the answer.

For every attack:
- Preserve the original example ID.
- Store the attack type and transformation details.
- Validate that the gold answer remains supported.
- Update answer offsets if the context has changed.
- Record failed or invalid attack generations.
- Evaluate clean and attacked examples using the same scoring implementation.

Do not treat random corruption as automatically adversarial. Explain the threat model and validity criteria.

### Stage E — Combined analysis

Analyze whether the effect of domain adaptation changes across data budgets and attack types.

At minimum, compare:
- Original versus domain-adapted checkpoints
- Full versus reduced labelled-data budgets
- Clean versus adversarial inputs
- All primary architectures

A complete factorial design may be expensive. If compute is limited, prioritize a transparent, pre-declared subset of combinations rather than selectively reporting favourable outcomes.

## 8. Evaluation metrics

### Core QA metrics

- **Exact Match (EM):** whether the normalized predicted answer exactly matches the gold answer.
- **Token-level F1:** overlap between predicted and gold answer tokens.

Use a consistent normalization and scoring implementation.

### Robustness metrics

- **Absolute performance drop:** clean score minus attacked score.
- **Relative performance drop:** performance drop divided by clean score, with zero-score handling documented.
- **Attack success rate:** define precisely what counts as a successful attack before reporting it.

### Efficiency metrics

Where feasible, report:
- Training time
- Inference latency
- Peak memory use
- Parameter count

### Statistical reporting

- Repeat experiments with multiple seeds where resources permit.
- Report mean and standard deviation.
- Include confidence intervals or suitable statistical tests if the sample size and design justify them.
- Do not present tiny score differences as meaningful without considering variation.

## 9. Fair-comparison controls

- Identical dataset splits across model comparisons.
- Fixed test set across data budgets.
- Comparable hyperparameter-search and compute budgets.
- No test-set use for checkpoint selection.
- No test leakage into domain-adaptive pretraining.
- Model-appropriate tokenizers.
- Consistent metric implementation.
- Recorded seeds and software versions.
- Transparent reporting of failed, incomplete or omitted experiments.

## 10. Reproducibility and artifacts

Store:
- Dataset descriptions and split-generation seeds
- Configuration files
- Model checkpoint identifiers
- Training logs
- Evaluation predictions
- Metric summaries
- Attack-generation records
- Plots and comparison tables

Do not commit large datasets, private documents, credentials or model checkpoints to Git unless licensing and repository policy explicitly permit it. Use `.gitignore` and document how data can be obtained.

## 11. Proposed implementation order

1. Dataset audit and feasibility report.
2. Preprocessing and answer-span validation.
3. One baseline model end-to-end.
4. Remaining baseline models.
5. Baseline comparison.
6. Domain-adaptation experiment.
7. Data-scarcity experiments.
8. Adversarial dataset generation and validation.
9. Adversarial evaluation.
10. Combined analysis and research-paper writing.

This order is intended to reduce risk: validate the dataset and one complete training/evaluation pipeline before expanding to the full experiment matrix.
