以下に、**Gaussian Kernel Density Estimation（KDE）と最尤推定による Iris 分類モデル**の実験を、K-NN モデルのまとめ形式に倣って構成しました。

---

# Gaussian Kernel による Iris 分類モデル

---

## 概要（やったこと）

* Gaussian カーネル密度推定法（KDE）の実装
* 最尤法に基づくクラス分類器の構築
* `sklearn.datasets.load_iris()` を用いた実験
* `h=0.1, 0.3, 0.5, 0.7, 1.0` のバンド幅ごとの性能評価
* 5分割Stratified K-Fold 交差検証による精度評価
* ログ尤度を用いた数値安定な分類
* 結果の視覚化（Matplotlibによる精度 vs h のグラフ）

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

* データ: `sklearn.datasets.load_iris()`（3クラス分類問題）
* モデル: Gaussian Kernel によるクラス条件付き確率密度関数の推定 + 最尤分類
* 評価: Accuracy, log-likelihood, h の比較、交差検証

---

## 実験結果（交差検証5-fold, 各 h に対する Accuracy）

| Bandwidth $h$ | Mean Accuracy | Std (±) |
| ------------- | ------------- | ------- |
| 0.1           | 0.9333        | ±0.0305 |
| 0.3           | 0.9467        | ±0.0337 |
| 0.5           | 0.9600        | ±0.0310 |
| 0.7           | 0.9600        | ±0.0310 |
| 1.0           | 0.9467        | ±0.0337 |

※ すべての精度は 5-fold Stratified K-Fold による平均値。

---

## グラフ出力（精度 vs バンド幅 h）

* 精度は `h=0.5` 〜 `h=0.7` の間で最大
* 小さすぎる h は過学習、h が大きすぎると表現力が落ちる

![Image](https://github.com/user-attachments/assets/9d759232-f5e8-421b-813f-855594414983)
（※ 実行時は matplotlib により自動生成）

---

## 考察

### 精度比較（バンド幅 h による影響）

* `h=0.5, 0.7`：最も安定して高い精度（Accuracy ≈ 0.96）
* `h=0.1`：過剰適合しやすく、局所的なノイズに敏感
* `h=1.0`：なめらかすぎてクラス間の違いを捉えきれない

### 分類手法としての KDE の評価

* クラス分布の形状を仮定せず柔軟にモデル化可能
* 少量データでも Gaussian カーネルにより比較的滑らかに推定可能
* 高次元になると「次元の呪い」に注意が必要（次元削減と併用推奨）

---

## 今後の展望

* 異なるカーネル関数（Epanechnikov, Laplace）での比較
* クラス事前確率 $p(C_i)$ を含めたベイズ決定則への拡張
* PCA / t-SNE などを用いた誤分類分析
* 他モデル（K-NN, SVM, NBCなど）との統一交差検証による比較

---

## Reference

* [Kernel Density Estimation – Wikipedia](https://en.wikipedia.org/wiki/Kernel_density_estimation)
* [scikit-learn iris dataset](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html)
* [Scipy norm.pdf ドキュメント](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html)

---

## 実行手順（Google Colab）

```python
```
