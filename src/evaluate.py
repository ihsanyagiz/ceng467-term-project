"""
Evaluation script for UNMT models.

Computes BLEU and chrF metrics on parallel test data.

Usage:
    python src/evaluate.py --config configs/config.yaml --model_path results/best_model.pt --metrics bleu chrf
"""

import argparse
import yaml


def load_config(config_path: str) -> dict:
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def compute_bleu(hypotheses: list, references: list) -> float:
    """Compute corpus-level BLEU score using sacrebleu."""
    # TODO: import sacrebleu and compute
    # import sacrebleu
    # bleu = sacrebleu.corpus_bleu(hypotheses, [references])
    # return bleu.score
    print("[TODO] BLEU computation not yet implemented.")
    return 0.0


def compute_chrf(hypotheses: list, references: list) -> float:
    """Compute corpus-level chrF score using sacrebleu."""
    # TODO: import sacrebleu and compute
    # import sacrebleu
    # chrf = sacrebleu.corpus_chrf(hypotheses, [references])
    # return chrf.score
    print("[TODO] chrF computation not yet implemented.")
    return 0.0


def main():
    parser = argparse.ArgumentParser(description="Evaluate UNMT model")
    parser.add_argument("--config", type=str, default="configs/config.yaml")
    parser.add_argument("--model_path", type=str, default=None)
    parser.add_argument("--metrics", nargs="+", default=["bleu", "chrf"])
    parser.add_argument("--src_file", type=str, default=None)
    parser.add_argument("--ref_file", type=str, default=None)
    args = parser.parse_args()

    config = load_config(args.config)

    print("=" * 60)
    print("UNMT Evaluation")
    print("=" * 60)
    print(f"  Model: {args.model_path or 'Not specified'}")
    print(f"  Metrics: {args.metrics}")
    print("\n[TODO] Full evaluation pipeline not yet implemented.")
    print("[DONE] Evaluation script ready (implementation pending).")


if __name__ == "__main__":
    main()
