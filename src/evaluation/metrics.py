from collections import Counter

def accuracy(y_true, y_pred):
    correct = sum(1 for t, p in zip(y_true, y_pred) if t == p)
    return correct / len(y_true)

def precision_recall_f1(y_true, y_pred):
    labels = set(y_true)
    tp = Counter()
    fp = Counter()
    fn = Counter()

    for t, p in zip(y_true, y_pred):
        if t == p:
            tp[t] += 1
        else:
            fp[p] += 1
            fn[t] += 1

    precision_list = []
    recall_list = []
    f1_list = []

    for label in labels:
        precision = tp[label] / (tp[label] + fp[label]) if (tp[label] + fp[label]) > 0 else 0
        recall = tp[label] / (tp[label] + fn[label]) if (tp[label] + fn[label]) > 0 else 0
        f1 = (
            2 * precision * recall / (precision + recall)
            if (precision + recall) > 0 else 0
        )

        precision_list.append(precision)
        recall_list.append(recall)
        f1_list.append(f1)

    return {
        "precision": sum(precision_list) / len(labels),
        "recall": sum(recall_list) / len(labels),
        "f1": sum(f1_list) / len(labels)
    }

def calculate_metrics(y_true, y_pred):
    acc = accuracy(y_true, y_pred)
    prf = precision_recall_f1(y_true, y_pred)

    return {
        "accuracy": round(acc, 3),
        "precision": round(prf["precision"], 3),
        "recall": round(prf["recall"], 3),
        "f1": round(prf["f1"], 3)
    }
