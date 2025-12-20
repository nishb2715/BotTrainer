def analyze_errors(texts, y_true, y_pred):
    errors = []

    for text, true, pred in zip(texts, y_true, y_pred):
        if true != pred:
            errors.append({
                "text": text,
                "true_intent": true,
                "predicted_intent": pred
            })

    return errors


def summarize_errors(errors):
    summary = {}

    for err in errors:
        key = f"{err['true_intent']} → {err['predicted_intent']}"
        summary[key] = summary.get(key, 0) + 1

    return summary
