from src.evaluation.error_analysis import analyze_errors, summarize_errors
from src.evaluation.confusion_matrix import build_confusion_matrix, print_confusion_matrix
import json
from src.intent_classifier import classify_intent
from src.evaluation.metrics import calculate_metrics

texts = []
def run_evaluation():
    with open("data/eval_data.json", "r") as f:
        data = json.load(f)

    y_true = []
    y_pred = []

    for item in data:
        text = item["text"]
        true_intent = item["intent"]

        prediction = classify_intent(text)
        predicted_intent = prediction.get("intent", "unknown")

        print(f"\nTEXT: {text}")
        print(f"TRUE: {true_intent}")
        print(f"PRED: {predicted_intent}")

        y_true.append(true_intent)
        y_pred.append(predicted_intent)

    metrics = calculate_metrics(y_true, y_pred)

    print("\nEvaluation Results:")
    for k, v in metrics.items():
        print(f"{k}: {v}")

    labels, matrix = build_confusion_matrix(y_true, y_pred)
    print_confusion_matrix(labels, matrix)

    return y_true, y_pred, metrics

if __name__ == "__main__":
    run_evaluation()