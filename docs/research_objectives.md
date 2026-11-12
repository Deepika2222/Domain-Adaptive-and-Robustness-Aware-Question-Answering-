# Research Objectives

## Project title

**Domain-Adaptive and Robustness-Aware Question Answering: A Comparative Study of Fine-Tuned BERT Variants Under Data-Scarce and Adversarial Conditions**

## 1. Project overview

This project investigates the behaviour of pretrained BERT-family encoder models on **extractive technical-domain question answering (QA)**. Given a question and a supporting passage, an extractive QA model predicts the answer as a span of text from that passage. Where the dataset supports it, the model should also identify questions that cannot be answered from the supplied context.

The study focuses on three connected but distinct conditions:

1. **Domain adaptation:** whether exposure to unlabeled technical-domain text before QA fine-tuning improves performance on technical questions.
2. **Data scarcity:** how model performance changes when only a limited proportion of labelled QA examples is available.
3. **Adversarial robustness:** how model performance changes when questions or passages are deliberately modified while preserving, or deliberately challenging, the intended answer.

The project is primarily a **controlled comparative study**, not a proposal to invent a new transformer architecture.

## 2. Overall aim

To systematically compare selected BERT-family models on technical-domain extractive QA under domain-adaptation, limited-labelled-data and adversarial evaluation conditions, using a consistent experimental and evaluation protocol.

## 3. Specific objectives

### Objective 1 — Establish a reproducible baseline

- Select suitable technical-domain and general-domain QA datasets.
- Inspect dataset formats, answer annotations, answerability labels, licensing and train/validation/test splits.
- Fine-tune the selected pretrained models for the same extractive QA task.
- Record baseline Exact Match (EM), token-level F1 and relevant computational measures.

### Objective 2 — Evaluate domain adaptation

- Identify an appropriate collection of **unlabeled technical-domain documents**.
- Compare ordinary pretrained-model QA fine-tuning with a domain-adaptive-pretraining condition.
- Where feasible, continue masked-language-model (MLM) pretraining on technical text before QA fine-tuning.
- Measure whether domain adaptation changes clean QA performance and robustness.

### Objective 3 — Evaluate data scarcity

- Create reproducible subsets of the labelled training data at several data budgets.
- Keep validation and test sets fixed across budgets.
- Compare model performance and learning curves as the amount of labelled data decreases.
- Repeat experiments with multiple random seeds where resources permit.

### Objective 4 — Evaluate adversarial robustness

- Establish clean-input performance before applying attacks.
- Evaluate controlled perturbations, such as distractor-sentence insertion, meaning-preserving word substitutions and question paraphrases.
- Validate that each modified example retains a known answer and valid answer-span annotation.
- Measure performance degradation and attack success using clearly defined metrics.

### Objective 5 — Conduct a comparative analysis

- Compare model rankings across clean, low-data, domain-adapted, shifted and adversarial conditions.
- Investigate interactions between model architecture, domain adaptation and labelled-data budget.
- Include efficiency measures such as parameter count, training time, inference latency and memory use where feasible.
- Identify which model offers the most appropriate trade-off for the tested setting.

### Objective 6 — Produce a reproducible research report

- Document datasets, preprocessing, checkpoints, hyperparameters, random seeds and evaluation procedures.
- Preserve experiment configurations and results.
- Report limitations and avoid claims that extend beyond the tested datasets and conditions.

## 4. Candidate models

Primary comparison:

- BERT-base
- RoBERTa-base
- DeBERTa-v3-base

Optional models, subject to compute and time:

- DistilBERT
- ALBERT

The exact checkpoint identifiers must be recorded in the experiment configuration. Model-specific tokenizers and input conventions must be respected.

## 5. Expected outputs

1. A documented technical extractive-QA dataset selection.
2. A reproducible preprocessing pipeline.
3. Baseline fine-tuned QA checkpoints and evaluation results.
4. Domain-adaptation experiment results.
5. Low-data learning curves.
6. Adversarial robustness evaluation results.
7. A comparative analysis across models and conditions.
8. A research paper describing the methodology, results, limitations and contribution.

## 6. Scope boundaries

- The primary task is extractive QA, not unrestricted generative QA.
- Retrieval-augmented generation (RAG), spoken QA, multilingual QA and multi-hop QA papers may inform the background, but they are not automatically equivalent to the chosen task.
- Natural domain shift and adversarial perturbation must be evaluated as separate conditions.
- No model should be described as best before experiments are completed.
- No numerical result should be entered into the report unless it comes from a reproducible experiment or a clearly cited source.

## 7. Success criteria

The project will be considered successful if it delivers a fair, reproducible comparison; clearly distinguishes the three research conditions; reports performance and uncertainty transparently; and draws conclusions that are supported by the actual experimental evidence.
