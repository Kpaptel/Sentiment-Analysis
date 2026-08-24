"""
Evaluates the sentiment pipeline used in analysis/views.py against the
SST-2 validation set (Stanford Sentiment Treebank, via GLUE) and reports
accuracy / precision / recall / F1.

Usage:
    python evaluate_sentiment.py [--n N]

    --n N   Only evaluate on the first N examples (default: full validation set, 872 rows)
"""
import argparse
import json
from datetime import datetime, timezone

from datasets import load_dataset
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
from transformers import pipeline

LABEL_MAP = {"NEGATIVE": 0, "POSITIVE": 1}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=None)
    args = parser.parse_args()

    dataset = load_dataset("glue", "sst2", split="validation")
    if args.n:
        dataset = dataset.select(range(args.n))

    sentiment_pipeline = pipeline("sentiment-analysis")

    texts = list(dataset["sentence"])
    y_true = list(dataset["label"])

    predictions = sentiment_pipeline(texts, batch_size=32, truncation=True)
    y_pred = [LABEL_MAP[p["label"]] for p in predictions]

    accuracy = accuracy_score(y_true, y_pred)
    precision, recall, f1, _ = precision_recall_fscore_support(
        y_true, y_pred, average="binary"
    )

    results = {
        "model": sentiment_pipeline.model.config._name_or_path,
        "dataset": "glue/sst2 (validation)",
        "n_examples": len(texts),
        "accuracy": round(accuracy, 4),
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "f1": round(f1, 4),
        "evaluated_at": datetime.now(timezone.utc).isoformat(),
    }

    print(json.dumps(results, indent=2))

    with open("eval_results.json", "w") as f:
        json.dump(results, f, indent=2)


if __name__ == "__main__":
    main()
