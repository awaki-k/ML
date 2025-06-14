# K-NNによるIris分類モデル

## 概要（やったこと）
* K-Nearest Neighbors (K-NNC) の理解と手実装
* `sklearn.datasets.load_iris()` を用いた実験
* `K=1, 3, 5, 7` での精度評価（Accuracy、混同行列、F1スコアなど）
* 結果の視覚化（PNG形式で出力）

## システム環境
* OS: Windows 11 + Docker Desktop
* Dockerバージョン: 24.0.5
* Docker Compose v2.23.0

## コンテナ環境
* OS: Ubuntu 20.04.6 LTS
* Pythonバージョン: 3.10.13
* cuda: 使用していません

## 使用したモデル・データ
* データ: `sklearn.datasets.load_iris()` （アヤメの花の分類用データセット）
* モデル: 自作K-NN分類器（`K=1,3,5,7`）
* 評価: Accuracy, Confusion Matrix, Precision, Recall, F1スコア（クラス別）

## 結果
* K=1, 3, 5 のときは **Accuracy = 1.000**
* K=7 のときは **Accuracy = 0.967**（一部誤分類）
* クラス別評価指標は以下の通り：

## K-NNC クラス別評価指標（Precision / Recall / F1 / Support）

| K | Class       | Precision | Recall   | F1-Score | Support |
|---|-------------|-----------|----------|----------|---------|
| 1 | setosa      | 1.000000  | 1.000000 | 1.000000 | 10.0    |
| 1 | versicolor  | 1.000000  | 1.000000 | 1.000000 | 9.0     |
| 1 | virginica   | 1.000000  | 1.000000 | 1.000000 | 11.0    |
| 3 | setosa      | 1.000000  | 1.000000 | 1.000000 | 10.0    |
| 3 | versicolor  | 1.000000  | 1.000000 | 1.000000 | 9.0     |
| 3 | virginica   | 1.000000  | 1.000000 | 1.000000 | 11.0    |
| 5 | setosa      | 1.000000  | 1.000000 | 1.000000 | 10.0    |
| 5 | versicolor  | 1.000000  | 1.000000 | 1.000000 | 9.0     |
| 5 | virginica   | 1.000000  | 1.000000 | 1.000000 | 11.0    |
| 7 | setosa      | 1.000000  | 1.000000 | 1.000000 | 10.0    |
| 7 | versicolor  | 1.000000  | 0.888889 | 0.941176 | 9.0     |
| 7 | virginica   | 0.916667  | 1.000000 | 0.956522 | 11.0    |

## 考察

### 精度比較
- K=1〜5：すべて完全分類。特徴の分離が明確で、近傍が同一クラスに偏っている。
- K=7：VersicolorのRecallが0.889まで低下。境界付近のサンプルがVirginicaに分類された。

### クラスごとの挙動
- **Setosa**：全Kで完全分類。明確に分離された簡単なクラス。
- **Versicolor**：K=7で一部誤分類あり。Virginicaとの境界付近で混同が発生。
- **Virginica**：K=7では他クラスの混入によりPrecision低下。ただしRecallは1.0。

### Kの選び方
- 小さいKは過学習しやすく、ノイズに敏感。
- 大きいKは滑らかな境界を生成し、一般化性能が向上するが、誤分類のリスクも増える。
- 奇数のKを使うことで、投票の同数を回避可能。
- 現実的にはクロスバリデーションで最適なKを選定するのが理想。

### K-NNCモデルの限界
- 計算量がデータ数に比例するため、大規模データセットには不向き。
- 特徴量が高次元になると「次元の呪い」により距離尺度が機能しにくくなる。

## 今後の展望（やらない）
- 重み付きK-NNや局所適応K-NNによる改善
- 特徴空間の可視化（PCA, t-SNE等）で誤分類点を分析
- 距離関数の工夫（マンハッタン距離やコサイン類似度などの導入）
- 他の分類器（SVM, 決定木, ランダムフォレスト等）との比較
- 精度以外の指標（ROC曲線、AUC、kappaなど）も併用した評価

---

シンプルな実装ながら、K-NNCの特性を深く理解できる良い演習になった。

## Reference
* [scikit-learn KNeighborsClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)
* [Irisデータセットについて](https://archive.ics.uci.edu/ml/datasets/iris)
* [F1スコアの解説](https://note.com/noa813/n/nef0692042cdf)
* [混同行列の解説](https://qiita.com/TsutomuNakamura/items/a1a6a02cb9bb0dcbb37f)
