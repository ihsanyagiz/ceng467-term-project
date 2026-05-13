"""
Denoising Autoencoder training for Unsupervised NMT.

Trains a shared encoder-decoder on monolingual data from both languages
using denoising objectives (word dropout, word shuffling, masking).

Usage:
    python src/train_autoencoder.py --config configs/config.yaml
"""

import argparse
import random
import yaml


def load_config(config_path: str) -> dict:
    """Load YAML configuration file."""
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def add_noise(sentence: str, config: dict) -> str:
    """
    Apply denoising noise to a sentence.

    Noise types:
        - Word dropout: randomly remove words
        - Word shuffle: randomly reorder words within a window
        - Word masking: replace words with a mask token
    """
    denoise_cfg = config.get("denoising", {})
    words = sentence.strip().split()

    # Word dropout
    dropout_rate = denoise_cfg.get("word_dropout", 0.1)
    words = [w for w in words if random.random() > dropout_rate]

    # Word shuffle
    shuffle_dist = denoise_cfg.get("word_shuffle", 3)
    if shuffle_dist > 0 and len(words) > 1:
        noise = [i + random.uniform(0, shuffle_dist) for i in range(len(words))]
        words = [w for _, w in sorted(zip(noise, words))]

    # Word masking
    mask_rate = denoise_cfg.get("word_mask", 0.0)
    if mask_rate > 0:
        words = ["<mask>" if random.random() < mask_rate else w for w in words]

    return " ".join(words) if words else sentence


def main():
    parser = argparse.ArgumentParser(
        description="Train denoising autoencoder for UNMT"
    )
    parser.add_argument("--config", type=str, default="configs/config.yaml",
                        help="Path to configuration file")
    args = parser.parse_args()

    config = load_config(args.config)

    print("=" * 60)
    print("Denoising Autoencoder Training")
    print("=" * 60)

    # TODO: Implement the following:
    # 1. Load preprocessed monolingual data for both languages
    # 2. Build shared encoder-decoder model (Transformer)
    # 3. For each epoch:
    #    a. For each batch of monolingual sentences:
    #       - Apply noise to create corrupted input
    #       - Train encoder-decoder to reconstruct original
    #    b. Alternate between Turkish and English batches
    # 4. Save model checkpoint

    print("\n[TODO] Full training loop not yet implemented.")
    print("  Planned components:")
    print("    - Shared Transformer encoder-decoder")
    print(f"    - Encoder layers: {config['model']['encoder_layers']}")
    print(f"    - Decoder layers: {config['model']['decoder_layers']}")
    print(f"    - Hidden size: {config['model']['hidden_size']}")
    print(f"    - Attention heads: {config['model']['num_heads']}")
    print(f"    - Dropout: {config['model']['dropout']}")
    print(f"    - Learning rate: {config['training']['learning_rate']}")
    print(f"    - Batch size: {config['training']['batch_size']}")
    print(f"    - Epochs: {config['training']['epochs']}")
    print(f"    - Seed: {config['training']['seed']}")

    # Demo: noise function
    demo_sentence = "Bu bir test cümlesidir."
    noisy = add_noise(demo_sentence, config)
    print(f"\n  Noise demo:")
    print(f"    Original: {demo_sentence}")
    print(f"    Noisy:    {noisy}")

    print("\n[DONE] Autoencoder training script ready (implementation pending).")


if __name__ == "__main__":
    main()
