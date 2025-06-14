# Gaussian Kernel による Iris 分類モデル（最尤推定）

---

## 概要（やったこと）

* Gaussian カーネル密度推定法（KDE）の実装
* 最尤法に基づくクラス分類器の構築
* `sklearn.datasets.load_iris()` を用いた実験
* `h = 0.1, 0.3, 0.5, 0.7, 1.0` のバンド幅ごとの精度評価
* 5分割 Stratified K-Fold による交差検証
* ログ尤度による数値安定な識別の実装
* 結果の可視化（Matplotlib による精度 vs h の誤差付きグラフ）

---

## システム環境

* OS: Windows 11 + Docker Desktop
* Dockerバージョン: 24.0.5
* Docker Compose v2.23.0

---

## コンテナ環境

* OS: Ubuntu 20.04.6 LTS
* Pythonバージョン: 3.10.13
* cuda: 使用していません

---

## 使用したモデル・データ

* **データ**: `sklearn.datasets.load_iris()`（3クラス：Setosa, Versicolor, Virginica）
* **モデル**: Gaussian Kernel による条件付き確率密度推定 + 最尤決定
* **評価指標**: Accuracy（平均 + 標準偏差）, log-likelihood（分類器内部処理）

---

## 実験結果（5-fold CV による各 h の精度）

| Bandwidth $h$ | Fold Accuracies                        | Mean   | Std    |
| ------------- | -------------------------------------- | ------ | ------ |
| 0.1           | 0.9667, 0.9667, 0.9000, 1.0000, 0.9333 | 0.9533 | 0.0340 |
| 0.3           | 1.0000, 0.9667, 0.9000, 1.0000, 0.9000 | 0.9533 | 0.0452 |
| 0.5           | 0.9667, 0.9333, 0.8667, 1.0000, 0.8333 | 0.9200 | 0.0618 |
| 0.7           | 0.9667, 0.9333, 0.8333, 1.0000, 0.8333 | 0.9133 | 0.0686 |
| 1.0           | 0.9333, 0.9000, 0.8000, 0.9667, 0.7667 | 0.8733 | 0.0772 |

---

## グラフ出力（Classification Accuracy vs. Bandwidth h）

![Image](https://github.com/user-attachments/assets/9d759232-f5e8-421b-813f-855594414983)


> グラフは `plt.errorbar()` により、**平均精度 + 標準偏差**をプロット。精度と安定性の両面から最適な h を可視化。

---

## 考察（改訂版）

### h 値による分類性能の影響

| 範囲               | 評価                                                                      |
| ---------------- | ----------------------------------------------------------------------- |
| **h = 0.1, 0.3** | 高精度かつ比較的安定。小さい h はデータのローカル構造を細かく捉える。ノイズに敏感だが Iris データでは過学習は生じていない。      |
| **h = 0.5, 0.7** | 精度がわずかに低下し、ばらつきも増加。クラス間の密接度が増すと境界が曖昧に。                                  |
| **h = 1.0**      | 過度に滑らかすぎる分布推定によりクラス識別力が低下。精度・安定性ともに最も劣る。KDE における典型的な over-smoothing の例。 |

### 精度と再現性のバランス

* **標準偏差の増加**は h 増大に伴って顕著。
* 特に `h=1.0` では再現性が最も悪く、モデルの一般化能力が低い。
* `h=0.1〜0.3` が最も信頼できる分類器を提供。

---

## 今後の展望

* カーネル関数の変更（Epanechnikov, Laplace など）による性能比較
* クラス事前確率 $p(C_i)$ を加味した **Bayes決定則** の導入
* 特徴量次元が増える場合のスケーラビリティ検証
* 他手法（K-NN, SVM, Naïve Bayes）との交差検証による比較研究
* PCAやt-SNEを用いた視覚的クラス境界分析

---

## Refernece
* [カーネル密度](https://pro.arcgis.com/ja/pro-app/latest/tool-reference/spatial-analyst/kernel-density.htm)
* [KDEとは](https://qiita.com/shokishimada/items/f630a20099e8e4bdc2f7)
* [Irisデータセット](https://archive.ics.uci.edu/ml/datasets/iris)
* [scipy.stats.norm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html)
---

## 実行手順
```bash
docker-compose build
docker-compose up
```
