# Research Gap

## Project title

**Domain-Adaptive and Robustness-Aware Question Answering: A Comparative Study of Fine-Tuned BERT Variants Under Data-Scarce and Adversarial Conditions**

## 1. Background

Question answering models can perform well on familiar benchmark data but may behave differently when the input domain changes, when only a small amount of labelled training data is available, or when questions and passages are deliberately modified.

The project examines these concerns in the narrower setting of **technical-domain extractive question answering**. The intended comparison is between selected BERT-family models, with and without domain-adaptive pretraining, across multiple labelled-data budgets and adversarial evaluation conditions.

## 2. What the reviewed literature already establishes

The literature collected for this project covers several established directions:

### Adversarial QA and robustness

- Jia and Liang (2017), *Adversarial Examples for Evaluating Reading Comprehension Systems*, introduced adversarial distractor approaches for reading comprehension.
- Bartolo et al. (2020), *Beat the AI: Investigating Adversarial Human Annotation for Reading Comprehension*, introduced adversarially collected QA examples.
- Zhu et al. (2020), *FreeLB: Enhanced Adversarial Training for Natural Language Understanding*, studied embedding-space adversarial training for NLP.
- Tran and Kretchmar (2024), *Towards Robust Extractive Question Answering Models: Rethinking the Training Methodology*, studied training-method changes for robust extractive QA.

### Domain adaptation and technical QA

- Gururangan et al. (2020), *Don't Stop Pretraining: Adapt Language Models to Domains and Tasks*, established continued pretraining as a domain/task adaptation approach.
- Lee et al. (2020), *BioBERT: a pre-trained biomedical language representation model for biomedical text mining*, demonstrated domain-specific pretraining for biomedical NLP.
- Domain-specific QA and synthetic-data studies in the collected literature investigate how technical or specialized QA performance can be improved.

### Data scarcity and QA augmentation

- The collected few-shot QA literature investigates low-resource fine-tuning, synthetic QA generation, question augmentation and parameter-efficient approaches.
- These studies motivate explicit data-budget experiments and careful controls over generated examples.

### Recent technical-domain QA near-neighbours

The following studies are especially important when defining novelty:

1. **Sierepeklis and Cole (2025), thermoelectric-materials QA.** The study reports automatically generated domain-specific QA data and BERT fine-tuning comparisons using domain-only, general-domain and mixed QA data.
2. **Kelly and Cole (2026), magnetic-materials QA (MagQA).** The study reports a large generated domain QA dataset and experiments involving BERT, domain-adaptive pretraining, QA-data volume, and additional BERT-family models.
3. **Zhang and Cole (2026), mechanical-properties QA (MechQA).** The study reports a large technical/scientific QA dataset and comparisons involving extractive and generative models.
4. **Recent adversarial extractive-QA work**, including feature-representation-based adversarial training, is relevant to the robustness component.

These studies mean that the project should **not** claim that technical-domain QA, BERT-family comparisons, domain adaptation, synthetic QA generation or data-volume ablations are individually new.

> **Verification requirement:** Before submitting a formal novelty claim, inspect the complete methods and evaluation sections of these recent papers. Confirm their exact model checkpoints, data budgets, DAPT procedures, attack types and test protocols. Do not claim that a paper omitted an experiment until its full text and supplementary material have been checked.

## 3. Preliminary synthesis

The reviewed work provides evidence for each research dimension, but the studies use different tasks, datasets, model families, adaptation methods and evaluation protocols. Results from biomedical QA, open-domain QA, multilingual QA, spoken QA, RAG and general reading comprehension cannot automatically be treated as results for technical extractive QA.

A useful contribution may therefore come from a **carefully controlled empirical comparison** in a clearly defined technical-documentation setting, rather than from proposing another generic augmentation or adversarial-training method.

## 4. Proposed research gap

**Proposed gap statement**

Recent studies have separately advanced domain-specific QA data generation and adaptation, low-annotation-budget fine-tuning, distribution-shift robustness and adversarially robust extractive QA. Recent materials-science QA studies also make clear that BERT-family model comparisons, domain-adaptive pretraining and QA-data-volume experiments are already established research directions.

A narrower, potentially defensible gap is the need to characterize, under one matched experimental protocol and within a selected technical-documentation extractive-QA setting, **how model architecture and domain-adaptive pretraining interact with reduced labelled-data budgets and adversarial robustness**. In particular, the study can investigate whether model rankings, sample efficiency and robustness degradation change as labelled technical QA data becomes scarce, and whether domain adaptation changes those outcomes.

This is a **preliminary gap hypothesis based on the literature collected so far**, not proof that no prior paper has studied the same combination. A final novelty search is required before publication.

## 5. Proposed research question

Under matched training and tuning budgets, how do selected BERT-family encoders differ in clean answer quality, low-resource sample efficiency and adversarial robustness on a held-out technical-domain extractive QA dataset, and how does continued domain-adaptive pretraining affect these outcomes?

## 6. Sub-questions

1. Which selected encoder achieves the strongest baseline performance on the chosen technical extractive-QA dataset?
2. How does each model's performance change as the amount of labelled QA training data decreases?
3. Does continued MLM pretraining on unlabeled technical documents improve downstream QA performance?
4. Do model rankings change under distractor insertion, lexical substitution or question paraphrasing?
5. Does domain-adaptive pretraining change the size of the performance drop under adversarial perturbations?
6. Which model provides the best measured balance of EM/F1, robustness and computational cost?

## 7. What this project should do differently

| Existing research direction | Proposed project emphasis |
|---|---|
| Domain-specific QA dataset generation | Use a clearly documented technical QA dataset; dataset generation is not claimed as the novelty. |
| Comparing transformer architectures | Compare selected BERT-family encoders under matched conditions, while acknowledging recent comparisons. |
| Domain-adaptive pretraining | Test whether DAPT changes low-data performance and adversarial degradation, not only clean accuracy. |
| Few-shot QA and augmentation | Use fixed labelled-data budgets and reproducible sampling to measure sample efficiency. |
| Adversarial training and attack methods | First measure baseline vulnerability under defined attacks; optionally evaluate a defence as a separate experiment. |
| General distribution-shift evaluation | Include a clearly defined technical-domain held-out evaluation if suitable data are available. |

## 8. Proposed contribution

The planned contribution is an empirical benchmark and analysis comprising:

- A documented technical extractive-QA task and dataset protocol.
- A controlled comparison of BERT, RoBERTa and DeBERTa, with optional efficiency baselines.
- Original-checkpoint versus domain-adapted-checkpoint comparisons.
- Learning curves over multiple labelled-data budgets.
- Clean, held-out-domain and adversarial evaluations.
- Analysis of interactions between model, domain adaptation, data budget and attack type.
- Reproducible metrics and computational-cost reporting.

The project does not need to invent a new model to make a useful contribution. Its value depends on a careful experimental design, reliable annotations, fair comparisons and evidence-based interpretation.

## 9. Threats to the research-gap claim

- A new 2025–2026 paper may already evaluate the same combination of models, data budgets, DAPT and adversarial attacks.
- TechQA may not provide enough directly usable extractive answer-span annotations for the planned experiments.
- Results from a single technical domain may not generalize to all technical domains.
- Different model tokenizers and pretraining corpora may affect fairness and interpretation.
- Synthetic adversarial examples may accidentally change answerability or invalidate answer spans.
- Compute limitations may prevent a complete factorial experiment.

## 10. Next actions to validate the gap

1. Read the full methods, experiments and appendices of the three recent technical/scientific QA papers listed above.
2. Read the complete 2024 robust extractive-QA and 2025 adversarial-robustness papers.
3. Search ACL Anthology, IEEE Xplore, ACM Digital Library, Semantic Scholar, Google Scholar and arXiv for combinations of:
   - extractive QA + low-resource + adversarial robustness
   - technical QA + domain-adaptive pretraining + few-shot
   - BERT variants + domain shift + adversarial QA
   - QA + data budget + robustness evaluation
4. Record whether each closest paper tests all three dimensions together.
5. Refine the gap statement based on the actual methods and experimental coverage found.
6. Only then finalize the novelty claim in the proposal or paper.

## 11. Suggested concise gap for a proposal

Although domain adaptation, few-shot QA and adversarial robustness have each been studied, their combined effects on the low-resource performance and adversarial behaviour of BERT-family models in a controlled technical-domain extractive-QA setting require further empirical investigation. This study will compare selected encoders across labelled-data budgets, with and without technical-domain continued pretraining, and evaluate them under clean and controlled adversarial conditions.
