# ML
* 大学のMLの授業の課題を張り付けるだけ。

## プロジェクトのリスト

### [Project 1: 線形回帰による気温予測](https://github.com/awaki-k/ML/tree/main/proj1) (2025-06-13)
- 時系列の気温データを使って、1時間後の気温を線形回帰モデルで予測。
- 特徴量として過去3時点の気温を用い、scikit-learn の `LinearRegression` を使用。
- MAEや標準偏差による評価、予測誤差の可視化グラフあり。

---

### [Project 2: K最近傍法（K-NNC）のアルゴリズム設計と実装](https://github.com/awaki-k/ML/tree/main/proj2) (2025-06-17)
- K-NNC（K-Nearest Neighbor Classifier）を自作実装。
- Irisデータセットを用いて、分類性能の評価を実施。

---

### [Project 3: ガウスカーネルによる確率密度推定と最尤決定法の実装](https://github.com/awaki-k/ML/tree/main/proj3) (2025-06-20)
- ガウスカーネルを用いた確率密度推定器を構築。
- Irisデータセットを用いて、K-NN法との比較を行う。

---

### Project 4: ベイジアンネットワークの結合確率分布生成とデータサンプリング (2025-06-24)
- 与えられたベイジアンネットワーク構造に基づいて JPDT（Joint Probability Distribution Table）を計算。
- サンプリングの結果と理論値の一致性を確認。

---

### Project 5: アンサンブル学習法の解説と実装・評価 (2025-06-27)
- Bagging, AdaBoost, Random Forest, LightGBM などの手法を簡潔にまとめ実装。
- 決定木との比較により、アンサンブルの利点を分析。

---

### Project 6: バックプロパゲーション（BP）アルゴリズムの設計・実装と性能評価 (2025-07-04)
- BPアルゴリズムの手順を整理し、自作ニューラルネットワークで Iris / MNIST を学習。
- アンサンブル決定木との性能比較も含む。

---

### Project 7: CNNモデルの構造解説と転移学習の実践 (2025-07-08)
- VGG-16 や ResNet-50 の構造を整理し、MNISTを対象とした転移学習を実装。
- 層の凍結パターンごとの性能を比較。

---

### Project 8: CNN性能向上のための最新手法の調査・解説 (2025-07-11)
- EfficientNet、SAM（Sharpness-Aware Minimization）、Meta Pseudo Labels などの手法を調査。
- 各手法の概要・工夫点・導入メリットを簡潔にまとめる。

---

### Project 9: コントラスト・ダイバージェンス（CD）アルゴリズムの理解と実装 (2025-07-15)
- Restricted Boltzmann Machine（RBM）へのCDアルゴリズムの適用。
- MNIST等での性能評価とAuto-Encoderとの比較を実施。

---

### Project 10: GANアルゴリズムの理解・実装とAutoEncoder/RBMとの比較 (2025-07-18)
- GANの基本アルゴリズムを整理し、MNISTやCIFAR-10で実装・学習。
- AE・RBMとの生成性能や構造的違いを整理。

---

### Project 11: Vision Transformer（ViT）アルゴリズムの解説・実装とCNN比較 (2025-07-22)
- ViTのパイプラインを理解・実装し、CIFAR-10を使ってCNNと性能比較。
- 特にResNet-50との比較で、ViTの長所と短所を議論。
