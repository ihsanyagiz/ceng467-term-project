"""
Preprocessing pipeline for monolingual corpora.

Steps:
    1. Text normalization (Unicode NFC, whitespace)
    2. Empty line removal
    3. Duplicate removal
    4. Sentence length filtering
    5. Punctuation normalization
    6. Optional lowercasing
    7. SentencePiece/BPE tokenization
    8. Shared vocabulary construction

Usage:
    python src/preprocess.py --config configs/config.yaml
"""

import argparse
import unicodedata
import yaml
from pathlib import Path


def load_config(config_path: str) -> dict:
    """Load YAML configuration file."""
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def normalize_text(text: str) -> str:
    """Apply Unicode NFC normalization and whitespace standardization."""
    text = unicodedata.normalize("NFC", text)
    text = " ".join(text.split())
    return text.strip()


def normalize_punctuation(text: str) -> str:
    """Normalize common punctuation variants."""
    replacements = {
        "\u2018": "'", "\u2019": "'",  # smart single quotes
        "\u201C": '"', "\u201D": '"',  # smart double quotes
        "\u2013": "-", "\u2014": "-",  # en/em dash
        "\u2026": "...",               # ellipsis
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def filter_by_length(sentences: list, min_len: int, max_len: int) -> list:
    """Filter sentences by word count."""
    return [s for s in sentences if min_len <= len(s.split()) <= max_len]


def remove_duplicates(sentences: list) -> list:
    """Remove duplicate sentences while preserving order."""
    seen = set()
    result = []
    for s in sentences:
        if s not in seen:
            seen.add(s)
            result.append(s)
    return result


def preprocess_corpus(filepath: str, config: dict) -> list:
    """Run full preprocessing pipeline on a monolingual corpus."""
    prep_cfg = config["preprocessing"]

    # Read raw text
    with open(filepath, "r", encoding="utf-8") as f:
        sentences = f.readlines()

    # Step 1: Normalize text
    sentences = [normalize_text(s) for s in sentences]

    # Step 2: Remove empty lines
    sentences = [s for s in sentences if len(s) > 0]

    # Step 3: Punctuation normalization
    if prep_cfg.get("normalize_punctuation", True):
        sentences = [normalize_punctuation(s) for s in sentences]

    # Step 4: Optional lowercasing
    if prep_cfg.get("lowercase", False):
        sentences = [s.lower() for s in sentences]

    # Step 5: Remove duplicates
    if prep_cfg.get("remove_duplicates", True):
        sentences = remove_duplicates(sentences)

    # Step 6: Length filtering
    min_len = prep_cfg.get("min_sentence_length", 3)
    max_len = prep_cfg.get("max_sentence_length", 100)
    sentences = filter_by_length(sentences, min_len, max_len)

    return sentences


def train_sentencepiece(input_files: list, config: dict):
    """Train a shared SentencePiece model on concatenated corpora."""
    # TODO: Implement SentencePiece training
    # import sentencepiece as spm
    # spm.SentencePieceTrainer.train(
    #     input=",".join(input_files),
    #     model_prefix=config["tokenization"]["model_prefix"],
    #     vocab_size=config["tokenization"]["vocab_size"],
    #     model_type="bpe",
    #     character_coverage=1.0,
    # )
    print("[TODO] SentencePiece training not yet implemented.")


def main():
    parser = argparse.ArgumentParser(description="Preprocess monolingual corpora")
    parser.add_argument("--config", type=str, default="configs/config.yaml",
                        help="Path to configuration file")
    args = parser.parse_args()

    config = load_config(args.config)

    print("=" * 60)
    print("UNMT Preprocessing Pipeline")
    print("=" * 60)

    # Process each language
    for lang_key in ["src_mono", "tgt_mono"]:
        filepath = config["data"].get(lang_key)
        if filepath and Path(filepath).exists():
            print(f"\nProcessing: {filepath}")
            sentences = preprocess_corpus(filepath, config)
            print(f"  Sentences after preprocessing: {len(sentences)}")

            # Save processed output
            out_dir = Path(config["data"]["processed_dir"])
            out_dir.mkdir(parents=True, exist_ok=True)
            out_path = out_dir / Path(filepath).name
            with open(out_path, "w", encoding="utf-8") as f:
                f.write("\n".join(sentences) + "\n")
            print(f"  Saved to: {out_path}")
        else:
            print(f"\n[SKIP] File not found: {filepath}")
            print("  Please download monolingual data first.")

    # Train tokenizer
    print("\n--- Tokenizer Training ---")
    train_sentencepiece([], config)

    print("\n[DONE] Preprocessing pipeline complete.")


if __name__ == "__main__":
    main()
