import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score
from scipy.stats import norm
import matplotlib.pyplot as plt
import os

def gaussian_kernel(x, xi, h):
    return norm.pdf((x - xi) / h) / h

def kernel_density_estimation(x, X_train, h):
    return np.mean([gaussian_kernel(x, xi, h) for xi in X_train])

def class_likelihood(x, class_data, h):
    log_likelihood = 0
    for i, xi in enumerate(x):
        density = kernel_density_estimation(xi, class_data[:, i], h)
        log_likelihood += np.log(density + 1e-12)
    return log_likelihood

def classify_with_likelihood(x, class_data, h):
    log_likelihoods = [class_likelihood(x, data, h) for data in class_data]
    return np.argmax(log_likelihoods)

# CSV 読み込み
df = pd.read_csv("data/iris.csv")
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

# 前処理
X = StandardScaler().fit_transform(X)

# 分類・評価
h_values = [0.1, 0.3, 0.5, 0.7, 1.0]
kf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
accuracy_results = {h: [] for h in h_values}

for train_idx, test_idx in kf.split(X, y):
    X_train, X_test = X[train_idx], X[test_idx]
    y_train, y_test = y[train_idx], y[test_idx]
    class_data = [X_train[y_train == c] for c in np.unique(y_train)]
    
    for h in h_values:
        y_pred = [classify_with_likelihood(x, class_data, h) for x in X_test]
        acc = accuracy_score(y_test, y_pred)
        accuracy_results[h].append(acc)

mean_acc = [np.mean(accuracy_results[h]) for h in h_values]
std_acc = [np.std(accuracy_results[h]) for h in h_values]

print("==== Accuracy by Bandwidth (h) ====")
for i, h in enumerate(h_values):
    accs = accuracy_results[h]
    print(f"h = {h:.1f}")
    for j, acc in enumerate(accs):
        print(f"  Fold {j+1}: {acc:.4f}")
    print(f"  Mean: {mean_acc[i]:.4f}, Std: {std_acc[i]:.4f}")
    print("-" * 35)

os.makedirs("outputs", exist_ok=True)
plt.figure(figsize=(8, 5))
plt.errorbar(h_values, mean_acc, yerr=std_acc, fmt='-o', capsize=5)
plt.title("Classification Accuracy vs. Bandwidth (h)")
plt.xlabel("Bandwidth (h)")
plt.ylabel("Accuracy")
plt.grid(True)
plt.savefig("outputs/result.png")
