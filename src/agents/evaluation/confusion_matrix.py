from collections import defaultdict

def build_confusion_matrix(y_true, y_pred):
    labels = sorted(set(y_true + y_pred))
    matrix = defaultdict(lambda: defaultdict(int))

    for t, p in zip(y_true, y_pred):
        matrix[t][p] += 1

    return labels, matrix

def print_confusion_matrix(labels, matrix):
    print("\nConfusion Matrix:\n")

    header = "TRUE \\ PRED".ljust(15)
    for label in labels:
        header += label.ljust(15)
    print(header)

    for true_label in labels:
        row = true_label.ljust(15)
        for pred_label in labels:
            row += str(matrix[true_label][pred_label]).ljust(15)
        print(row)
