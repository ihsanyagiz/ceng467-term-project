"""
Word-by-word dictionary/lexicon translation baseline.

Translates each source word independently using a bilingual dictionary.
No reordering or morphological processing is applied.
Serves as a lower-bound baseline for evaluation metrics.

Usage:
    python src/baseline_word_by_word.py --config configs/config.yaml
"""

import argparse
import yaml


def load_config(config_path: str) -> dict:
    """Load YAML configuration file."""
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_dictionary(dict_path: str) -> dict:
    """
    Load a bilingual dictionary from a TSV file.
    Expected format: source_word<TAB>target_word (one pair per line).
    """
    dictionary = {}
    # TODO: Implement dictionary loading
    # Options:
    #   - Extract from bilingual word embeddings (MUSE, VecMap)
    #   - Use an existing Turkish-English dictionary file
    #   - Extract from Wiktionary
    print("[TODO] Dictionary loading not yet implemented.")
    return dictionary


def translate_word_by_word(sentence: str, dictionary: dict) -> str:
    """Translate a sentence word-by-word using the bilingual dictionary."""
    words = sentence.strip().split()
    translated = []
    for word in words:
        # Look up word in dictionary; keep original if not found
        translated_word = dictionary.get(word.lower(), word)
        translated.append(translated_word)
    return " ".join(translated)


def main():
    parser = argparse.ArgumentParser(
        description="Word-by-word dictionary translation baseline"
    )
    parser.add_argument("--config", type=str, default="configs/config.yaml",
                        help="Path to configuration file")
    parser.add_argument("--dict_path", type=str, default=None,
                        help="Path to bilingual dictionary TSV file")
    parser.add_argument("--input", type=str, default=None,
                        help="Input file to translate")
    parser.add_argument("--output", type=str, default=None,
                        help="Output file for translations")
    args = parser.parse_args()

    config = load_config(args.config)

    print("=" * 60)
    print("Word-by-Word Dictionary Baseline")
    print("=" * 60)

    # Load dictionary
    dictionary = load_dictionary(args.dict_path or "data/raw/dict_tr_en.tsv")

    if not dictionary:
        print("\n[ERROR] No dictionary loaded. Cannot perform translation.")
        print("  Please provide a bilingual dictionary file.")
        print("  Expected format: source_word<TAB>target_word")
        return

    # Translate input file
    if args.input:
        print(f"\nTranslating: {args.input}")
        with open(args.input, "r", encoding="utf-8") as f:
            sentences = f.readlines()

        translations = [translate_word_by_word(s, dictionary) for s in sentences]
        print(f"  Translated {len(translations)} sentences.")

        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write("\n".join(translations) + "\n")
            print(f"  Saved to: {args.output}")
    else:
        print("\n[INFO] No input file specified. Use --input to translate a file.")

    print("\n[DONE] Word-by-word baseline complete.")


if __name__ == "__main__":
    main()
