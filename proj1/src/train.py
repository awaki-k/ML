import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

# === データ取得(気温だけ) ===
df = pd.read_csv('data/data.csv')
df.columns = df.columns.str.strip()
raw = df['temperature'].astype(float).values

# === 時系列データセットを作る ===
X, y, table = [], [], []
for i in range(2, len(raw) - 1):
    X.append([raw[i], raw[i - 1], raw[i - 2]])
    y.append(raw[i + 1])
    table.append([raw[i - 2], raw[i - 1], raw[i], raw[i + 1]])

X = np.array(X)
y = np.array(y)
df_table = pd.DataFrame(table, columns=['t-2', 't-1', 't', 't+1'])

# === データ分割（80/20） ===
n_samples = X.shape[0]
split_index = int(n_samples * 0.8)
X_train, y_train = X[:split_index], y[:split_index]
X_test, y_test = X[split_index:], y[split_index:]

print("学習用データ数:", X_train.shape[0])
print("テスト用データ数:", X_test.shape[0])

# === 全体モデル学習 ===
model = LinearRegression()
model.fit(X_train, y_train)

print("重み（係数）:", model.coef_)
print("切片（バイアス）:", model.intercept_)

# === 予測と評価（全体）===
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print("平均絶対誤差（MAE）:", mae)
errors = y_pred - y_test
std = np.std(errors)
print("誤差の標準偏差:", std)

# === グラフ: 予測 vs 実測 ===
plt.figure(figsize=(10, 4))
plt.plot(y_test, label='Actual', marker='o')
plt.plot(y_pred, label='Prediction', marker='x')
plt.title('Prediction vs Actual (Temperature)')
plt.xlabel('Index')
plt.ylabel('Temperature (℃)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('outputs/prediction_vs_actual.png')
print("予測結果グラフを 'prediction_vs_actual.png' に保存しました。")

# === グラフ: 予測誤差 ===
plt.figure(figsize=(10, 3))
plt.plot(errors, label='Prediction error', color='red', marker='.')
plt.axhline(0, color='black', linestyle='--', linewidth=1)
plt.xlabel('Time-ordered index of test data')
plt.ylabel('Error (℃)')
plt.title('Temperature forecast error (1 hour ahead)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('outputs/prediction_error.png')
print("誤差グラフを 'prediction_error.png' に保存しました。")
