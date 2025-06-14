import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from itertools import product
import os

# ==== JPDT構築 ====
P_X1 = {0: 0.2, 1: 0.8}
P_X2_X1 = {(0,0): 0.8, (0,1): 0.2, (1,0): 0.2, (1,1): 0.8}
P_X3_X1 = {(0,0): 0.8, (0,1): 0.2, (1,0): 0.2, (1,1): 0.8}
P_X4_X2X3 = {
    (0,0,0): 0.8, (0,0,1): 0.2, (0,1,0): 0.4, (0,1,1): 0.6,
    (1,0,0): 0.4, (1,0,1): 0.6, (1,1,0): 0.2, (1,1,1): 0.8
}
P_X5_X3 = {(0,0): 0.8, (0,1): 0.2, (1,0): 0.2, (1,1): 0.8}

jpdt = []
for x1, x2, x3, x4, x5 in product([0, 1], repeat=5):
    p = (
        P_X1[x1] *
        P_X2_X1[(x2, x1)] *
        P_X3_X1[(x3, x1)] *
        P_X4_X2X3[(x4, x2, x3)] *
        P_X5_X3[(x5, x3)]
    )
    jpdt.append(((x1, x2, x3, x4, x5), p))

total_p = sum(p for _, p in jpdt)
jpdt = [(pat, p / total_p) for pat, p in jpdt]

df_jpdt = pd.DataFrame(
    [(x1, x2, x3, x4, x5, p) for (x1, x2, x3, x4, x5), p in jpdt],
    columns=["X1", "X2", "X3", "X4", "X5", "P"]
)
df_jpdt["Cumsum"] = df_jpdt["P"].cumsum()
df_jpdt.to_csv("data/JPDT.csv", index=False)

# ==== サンプル生成 ====
def generate_sample(df, n=100, seed=42):
    np.random.seed(seed)
    r = np.random.rand(n)
    samples = []
    for ri in r:
        row = df[df["Cumsum"] >= ri].iloc[0]
        samples.append([int(row.X1), int(row.X2), int(row.X3), int(row.X4), int(row.X5)])
    return pd.DataFrame(samples, columns=["X1", "X2", "X3", "X4", "X5"])

generated_data = generate_sample(df_jpdt)
generated_data.to_csv("data/generated_data.csv", index=False)

# ==== 分布比較と誤差可視化 ====
empirical = generated_data.value_counts().reset_index(name="count")
empirical["prob_estimated"] = empirical["count"] / len(generated_data)
merged = pd.merge(empirical, df_jpdt.drop(columns="Cumsum"),
                  on=["X1", "X2", "X3", "X4", "X5"], how="right").fillna(0)

merged["pattern"] = merged[["X1","X2","X3","X4","X5"]].astype(str).agg("".join, axis=1)
merged["abs_error"] = abs(merged["P"] - merged["prob_estimated"])

# 分布比較
plt.figure(figsize=(16,6))
bar_width = 0.4
x = range(len(merged))
plt.bar(x, merged["P"], width=bar_width, label="JPDT", alpha=0.7)
plt.bar([i + bar_width for i in x], merged["prob_estimated"], width=bar_width, label="Generated", alpha=0.7)
plt.xticks([i + bar_width/2 for i in x], merged["pattern"], rotation=90)
plt.xlabel("Pattern (X1~X5)")
plt.ylabel("Probability")
plt.title("Probability Distribution: JPDT vs Generated")
plt.legend()
plt.tight_layout()
plt.savefig("outputs/jpdt_vs_generated.png")

# 誤差ヒストグラム
plt.figure(figsize=(8, 5))
sns.histplot(merged["abs_error"], bins=10, kde=True)
plt.xlabel("Absolute Error")
plt.ylabel("Frequency")
plt.title("Histogram of Absolute Errors")
plt.grid(True)
plt.tight_layout()
plt.savefig("outputs/error_histogram.png")

# 誤差 vs 出現頻度
plt.figure(figsize=(10, 6))
sns.scatterplot(data=merged, x="count", y="abs_error", hue="pattern", palette="tab20", legend=False)
plt.xlabel("Sample Count (Generated)")
plt.ylabel("Absolute Error")
plt.title("Error vs Sample Frequency")
plt.tight_layout()
plt.savefig("outputs/error_vs_count.png")
