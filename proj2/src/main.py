# src/main.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# K-NN classifier implementation
class CustomKNNClassifier:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        return np.array([self._predict_one(x) for x in X])

    def _predict_one(self, x):
        distances = [np.linalg.norm(x - x_train) for x_train in self.X_train]
        k_indices = np.argsort(distances)[:self.k]
        k_labels = [self.y_train[i] for i in k_indices]
        return Counter(k_labels).most_common(1)[0][0]

# Load data
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=42
)

# Run K-NN for different K
results = []
for k in [1, 3, 5, 7]:
    model = CustomKNNClassifier(k)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    report = classification_report(y_test, preds, output_dict=True)
    results.append((k, acc, report))

# Format and save results
metrics_rows = []
for k, acc, rep in results:
    for cls_id, cls_name in enumerate(iris.target_names):
        if str(cls_id) in rep:
            m = rep[str(cls_id)]
            metrics_rows.append([
                k, cls_name, m["precision"], m["recall"], m["f1-score"], m["support"]
            ])

df = pd.DataFrame(metrics_rows, columns=["K", "Class", "Precision", "Recall", "F1-Score", "Support"])
# metrics DataFrame の表示と保存
print(df)

# テキストファイルとして保存
with open("../outputs/knn_metrics_output.txt", "w", encoding="utf-8") as f:
    f.write(df.to_string(index=True))