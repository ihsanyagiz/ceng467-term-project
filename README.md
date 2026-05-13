# Unsupervised Neural Machine Translation for Turkish–English

**CENG 467 — Natural Language Understanding and Generation**  
**Term Project — Group 9**

## Team Members

| Name | Student ID |
|---|---|
| Ali Alp Haraç | 290201040 |
| İhsan Yağız Sakızlıoğlu | 300201071 |

## Project Description

This project investigates **Unsupervised Neural Machine Translation (UNMT)** for the **Turkish–English** language pair. The goal is to translate between Turkish and English without using any parallel sentence pairs during training. The system learns cross-lingual mappings solely from monolingual corpora using denoising autoencoding and iterative back-translation.

## Repository Structure

```
unmt-tr-en/
├── README.md
├── requirements.txt
├── .gitignore
├── configs/
│   └── config.yaml
├── src/
│   ├── preprocess.py
│   ├── baseline_word_by_word.py
│   ├── train_autoencoder.py
│   ├── backtranslate.py
│   └── evaluate.py
├── data/
│   ├── raw/
│   └── processed/
└── results/
```

## Setup

```bash
# Clone the repository
git clone https://github.com/ihsanyagiz/unmt-tr-en.git
cd unmt-tr-en

# Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
# Preprocess monolingual corpora
python src/preprocess.py --config configs/config.yaml

# Run word-by-word baseline
python src/baseline_word_by_word.py --config configs/config.yaml

# Train denoising autoencoder
python src/train_autoencoder.py --config configs/config.yaml

# Run iterative back-translation
python src/backtranslate.py --config configs/config.yaml --iterations 5

# Evaluate on test set
python src/evaluate.py --config configs/config.yaml --model_path results/best_model.pt --metrics bleu chrf
```

## Method Overview

1. **Preprocessing**: Text normalization, deduplication, length filtering, SentencePiece/BPE tokenization with shared vocabulary.
2. **Baseline 1 — Word-by-word**: Dictionary/lexicon-based translation as a lower-bound baseline.
3. **Baseline 2 — UNMT**: Denoising autoencoder + iterative back-translation following Lample et al. (2018).
4. **Optional — LLM Zero-shot**: Zero-shot translation using a large language model (resource-dependent).

## Evaluation

- **Metrics**: BLEU, chrF, qualitative error analysis
- **Benchmarks**: FLORES-200 dev/devtest or Tatoeba (Turkish–English)

## Data Sources

- **Training (Monolingual)**: OPUS, Wikipedia dumps, WMT News Crawl
- **Evaluation (Parallel)**: FLORES-200 or Tatoeba (evaluation only — no parallel data used in training)

## References

- Sennrich, R., Haddow, B., & Birch, A. (2016). Improving Neural Machine Translation Models with Monolingual Data. *ACL*.
- Lample, G., Conneau, A., Denoyer, L., & Ranzato, M. (2018). Unsupervised Machine Translation Using Monolingual Corpora Only. *ICLR*.
- Artetxe, M., Labaka, G., Agirre, E., & Cho, K. (2018). Unsupervised Statistical Machine Translation. *EMNLP*.

## License

This project is developed for academic purposes as part of CENG 467 coursework.
