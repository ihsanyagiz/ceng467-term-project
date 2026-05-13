"""
Iterative Back-Translation for Unsupervised NMT.

Implements the iterative back-translation loop:
    1. Use current model to translate monolingual target -> source
    2. Train model on synthetic parallel data
    3. Repeat for N iterations

Usage:
    python src/backtranslate.py --config configs/config.yaml --iterations 5
"""

import argparse
import yaml


def load_config(config_path: str) -> dict:
    """Load YAML configuration file."""
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main():
    parser = argparse.ArgumentParser(
        description="Iterative back-translation for UNMT"
    )
    parser.add_argument("--config", type=str, default="configs/config.yaml")
    parser.add_argument("--iterations", type=int, default=5)
    parser.add_argument("--model_path", type=str, default=None)
    args = parser.parse_args()

    config = load_config(args.config)
    bt_cfg = config.get("backtranslation", {})

    print("=" * 60)
    print("Iterative Back-Translation")
    print("=" * 60)
    print(f"  Planned iterations: {args.iterations}")
    print(f"  Beam size: {bt_cfg.get('beam_size', 5)}")
    print(f"  Batch size: {bt_cfg.get('batch_size', 32)}")

    # TODO: Implement the iterative loop:
    # for i in range(args.iterations):
    #     1. Back-translate EN monolingual -> synthetic TR-EN pairs
    #     2. Train on synthetic TR-EN
    #     3. Back-translate TR monolingual -> synthetic EN-TR pairs
    #     4. Train on synthetic EN-TR
    #     5. Save checkpoint

    print("\n[TODO] Full back-translation loop not yet implemented.")
    print("[DONE] Script ready (implementation pending).")


if __name__ == "__main__":
    main()
