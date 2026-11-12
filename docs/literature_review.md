# Literature Review

## Project

**Domain-Adaptive and Robustness-Aware Question Answering: A Comparative Study of Fine-Tuned BERT Variants Under Data-Scarce and Adversarial Conditions**

## 1. Purpose and scope

This review supports a comparative study of **extractive technical-domain question answering**. It is organized around three dimensions:

1. Domain adaptation
2. Data scarcity
3. Adversarial robustness

Architecture papers, QA datasets, evaluation frameworks and recent technical-QA studies provide supporting context.

This document is a research map and synthesis, not a substitute for reading and citing the original papers. Verify bibliographic metadata and detailed experimental claims from the publisher or paper PDF before using them in a formal submission.

## 2. Adversarial robustness and QA evaluation

### Jia and Liang (2017) — Adversarial Examples for Evaluating Reading Comprehension Systems

Introduces adversarial distractor approaches, including sentence insertion, to test whether reading-comprehension systems rely on robust evidence or superficial patterns.

**Relevance:** Motivates testing extractive QA models with distractor sentences and reporting clean-versus-attacked performance.

Source: https://arxiv.org/abs/1707.07328

### Bartolo et al. (2020) — Beat the AI: Investigating Adversarial Human Annotation for Reading Comprehension

Studies human-generated adversarial questions and the AdversarialQA benchmark.

**Relevance:** Shows the value of evaluation examples designed to expose model weaknesses that standard benchmark data may not reveal.

Source: https://arxiv.org/abs/2002.00293

### Jin et al. (2020) — Is BERT Really Robust? A Strong Baseline for Natural Language Attack on Text Classification and Entailment

Introduces TextFooler-style lexical substitution attacks for NLP classification and entailment.

**Relevance:** Provides a possible source of lexical attack ideas. Its original task is not extractive QA, so any adaptation to QA must preserve question meaning, answer evidence and span validity.

Source: https://arxiv.org/abs/1907.11932

### Zhu et al. (2020) — FreeLB: Enhanced Adversarial Training for Natural Language Understanding

Studies multi-step perturbations in embedding space and adversarial training for natural-language understanding.

**Relevance:** Provides an optional defence/training baseline. It should not be confused with an evaluation attack applied to the input text.

Source: https://arxiv.org/abs/1909.11764

### Ribeiro et al. (2020) — Beyond Accuracy: Behavioral Testing of NLP Models with CheckList

Introduces behavioural testing through capability-based test suites.

**Relevance:** Motivates targeted tests for negation, paraphrases, entity changes, answerability and distractors in addition to aggregate EM/F1.

Source: https://arxiv.org/abs/2005.04118

### Tran and Kretchmar (2024) — Towards Robust Extractive Question Answering Models: Rethinking the Training Methodology

Studies a modified training methodology for extractive QA and evaluates in-domain, out-of-domain and adversarial conditions.

**Relevance:** A close QA-specific robustness reference. Compare its training intervention and evaluation protocol with the proposed controlled architecture/data-budget study.

Source: https://aclanthology.org/2024.findings-emnlp.121/

## 3. Domain adaptation

### Gururangan et al. (2020) — Don't Stop Pretraining: Adapt Language Models to Domains and Tasks

Studies continued pretraining on domain and task text before downstream fine-tuning.

**Relevance:** Supports the proposed comparison between an original pretrained checkpoint and one further pretrained on unlabeled technical-domain documents.

Source: https://arxiv.org/abs/2004.10964

### Lee et al. (2020) — BioBERT: a pre-trained biomedical language representation model for biomedical text mining

Demonstrates domain-specific pretraining for biomedical NLP tasks.

**Relevance:** Provides a domain-adaptation precedent. Biomedical language is not the same as technical support/documentation language, so transfer must be tested.

Source: https://arxiv.org/abs/1901.08746

### Recent distributional-robustness studies

Awadalla et al. (2022), *Exploring the Landscape of Distributional Robustness for Question Answering Models*, studies QA behaviour across a broad collection of models and datasets.

**Relevance:** Supports evaluating out-of-distribution behaviour rather than relying only on in-domain benchmark scores.

Source: https://aclanthology.org/2022.findings-emnlp.441/

## 4. Data scarcity and QA augmentation

The collected low-resource QA literature includes several approaches:

- Few-shot fine-tuning and analysis of training instability.
- Combining general-domain and target-domain QA examples.
- Generating synthetic questions and answers from unannotated passages.
- Paraphrasing and selecting additional questions.
- Prompt-based and parameter-efficient adaptation.

Examples to investigate include:

### Fine-tuning Strategies for Domain Specific Question Answering under Low Annotation Budget Constraints

Compares fine-tuning strategies under limited target-domain annotation budgets.

**Relevance:** Motivates controlled comparisons of target-domain-only training and mixed general-/target-domain QA data. Confirm the final publication record and exact experimental details from the official IEEE record.

Source: https://ieeexplore.ieee.org/document/10356566/

### Few-shot Unified Question Answering: Tuning Models or Prompts? (2023)

Compares model tuning and prompt tuning in few-shot QA settings.

**Relevance:** Provides background on parameter-efficient and few-shot approaches. Its unified QA setting is not identical to BERT span prediction.

Source: https://aclanthology.org/2023.findings-emnlp.550/

### Improving Low-resource Question Answering by Augmenting Question Information (2023)

Studies question-information augmentation for low-resource QA and includes technical QA among its evaluated settings.

**Relevance:** Particularly useful when considering whether question generation and filtering could augment a small technical QA training set.

Source: https://aclanthology.org/2023.findings-emnlp.699/

### PPDAC: A Plug-and-Play Data Augmentation Component for Few-shot Extractive Question Answering (2024)

Studies paraphrase generation and selection for few-shot extractive QA.

**Relevance:** A direct source for a possible augmentation baseline, provided paraphrases are checked for answer preservation.

Source: https://aclanthology.org/2024.ccl-1.102/

### Prompting-based Synthetic Data Generation for Few-Shot Question Answering (2024)

Studies prompted synthetic QA data generation for few-shot QA.

**Relevance:** Supports investigating synthetic augmentation, but generated examples must be quality-checked and must not leak test information.

Source: https://aclanthology.org/2024.lrec-main.1153/

### Dealing with Data Scarcity in Spoken Question Answering (2024)

Studies QA generation and data augmentation in a spoken-QA setting.

**Relevance:** Supporting evidence for augmentation under scarce annotations. Spoken QA and ASR noise differ from text-only technical extractive QA.

Source: https://aclanthology.org/2024.lrec-main.397/

## 5. Recent technical-domain QA papers: essential novelty checks

These papers are especially important because they are close to the proposed technical QA setting.

### Sierepeklis and Cole (2025) — Autogenerating a Domain-Specific Question-Answering Data Set from a Thermoelectric Materials Database to Enable High-Performing BERT Models

Reports automatic generation of a thermoelectric-materials QA dataset and BERT fine-tuning comparisons using domain-specific and general-domain QA data.

**Why it matters:** Domain-specific QA data generation and mixing general-domain and domain-specific examples are not new by themselves.

Source: https://doi.org/10.1021/acs.jcim.5c00840

### Kelly and Cole (2026) — Autogenerating a Domain-Specific Question-Answering Data Set to Enable High-Performing Language Models for Magnetic Materials

Reports a magnetic-materials QA dataset and experiments involving BERT, domain-adaptive pretraining, QA-data volume and additional BERT-family models.

**Why it matters:** This is a close prior-work comparator. Do not claim novelty merely from comparing BERT-family models, applying DAPT or varying QA training-data size in a scientific domain.

Source: https://doi.org/10.1021/acs.jcim.6c00136

### Zhang and Cole (2026) — Automatic Generation of a Mechanical Properties Question-Answering Data Set for Language Model Benchmarking: A Comparative Study of BERT, XLNet, and LLaMA Models

Reports MechQA, a large mechanical-properties QA dataset, and a comparison of extractive and generative models.

**Why it matters:** Technical/scientific QA dataset construction and model benchmarking are active areas. The proposed study needs a more specific distinction.

Source: https://doi.org/10.1021/acs.jcim.5c02646

### CATS-RAG (2026) — Contextual Augmented Triplet Synthesis for RAG in Technical QA

Studies generated QA triplets and hard distractors for a retrieval-augmented generation pipeline.

**Why it matters:** It is adjacent technical QA research, but RAG retrieval-plus-generation is not the same task as extractive span prediction.

Source: https://doi.org/10.1016/j.eswa.2026.131491

### Wang et al. (2026) — Toward construction-specialized, small language models: The interplay of domain adaptation, model scale and data volume

Studies domain adaptation, model scale and data volume in construction-specialized language models.

**Why it matters:** Supports the importance of studying interactions between adaptation and data volume in a technical domain. Verify its precise QA task and model setup before treating it as directly comparable.

Source: https://doi.org/10.1016/j.aei.2025.104035

## 6. Model architecture foundations

### Devlin et al. (2019) — BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding

Introduces BERT and its masked-language-model and next-sentence-prediction pretraining objectives.

Source: https://arxiv.org/abs/1810.04805

### Liu et al. (2019) — RoBERTa: A Robustly Optimized BERT Pretraining Approach

Studies changes to BERT pretraining, including data, training duration and optimization.

Source: https://arxiv.org/abs/1907.11692

### He et al. (2021) — DeBERTa: Decoding-enhanced BERT with Disentangled Attention

Introduces disentangled attention and an enhanced mask decoder.

Source: https://arxiv.org/abs/2006.03654

### Lan et al. (2020) — ALBERT: A Lite BERT for Self-supervised Learning of Language Representations

Introduces parameter-reduction techniques including factorized embeddings and cross-layer parameter sharing.

Source: https://arxiv.org/abs/1909.11942

### Sanh et al. (2019) — DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter

Studies knowledge distillation to produce a smaller BERT-like model.

Source: https://arxiv.org/abs/1910.01108

## 7. Dataset and evaluation foundations

- **SQuAD:** Stanford Question Answering Dataset. https://rajpurkar.github.io/SQuAD-explorer/
- **TechQA:** IBM technical question answering dataset and repository. https://github.com/IBM/TechQA
- **MRQA 2019 Shared Task:** A cross-domain reading-comprehension evaluation resource. https://mrqa.github.io/
- **AdversarialQA:** Adversarially collected reading-comprehension questions. https://arxiv.org/abs/2002.00293

Confirm the task format and licensing of every dataset before using it.

## 8. Synthesis and implications for this project

The reviewed work suggests the following:

1. Adversarial examples can reveal weaknesses not visible from clean benchmark performance.
2. Continued pretraining on domain text is an established adaptation approach.
3. Low-resource QA can be approached through fine-tuning choices, data mixing and augmentation.
4. Technical/scientific QA dataset generation and BERT-family comparisons have recent close prior art.
5. Results from different tasks and datasets cannot be directly compared without controlling the experimental setup.

### Implication

The project should focus on a reproducible, matched-protocol investigation of the interaction between model choice, technical-domain adaptation, labelled-data budget and adversarial robustness in a clearly defined extractive QA setting.

## 9. Literature-review limitations and next steps

- This is a curated working review, not an exhaustive systematic review.
- Some adjacent papers use RAG, generative QA, spoken QA or other tasks.
- All detailed numerical claims must be checked against full papers before citation.
- Search for 2025–2026 work that combines low-resource extractive QA, domain adaptation and adversarial evaluation.
- Record search dates, search strings, inclusion criteria and exclusion reasons if the review is to be presented as systematic.
- Update this file when papers are read and verified; do not add papers based on title or abstract alone without marking the evidence level.
