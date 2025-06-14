# ベイジアンネットワークによるジョイント確率表の構築とデータ生成（Project 4）

---

## 概要（やったこと）

* 講義資料（Lecture 5）p.25のベイジアンネットワークを対象とした分析
* 条件付き確率に基づく **Joint Probability Distribution Table (JPDT)** の構築（Program 1）
* JPDT を利用した **合成データ（サンプル）生成プログラム** の実装（Program 2）
* 生成されたデータが正しい分布に従っているかの妥当性検証（誤差比較）
* Google Colab 上での完全実行に対応（ファイル入出力、視覚化含む）

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

* **モデル構造**：

  ```
  X1 → {X2, X3}
  X2, X3 → X4
  X3 → X5
  ```

* **定義された条件付き確率**（講義資料より）：

  * P(X1), P(X2|X1), P(X3|X1), P(X4|X2,X3), P(X5|X3)

* **生成データ**：JPDTに従いランダムサンプリングで100件生成

---

## 実験結果（JPDT例）

| X1  | X2  | X3  | X4  | X5  | P(X1,X2,X3,X4,X5) |
| --- | --- | --- | --- | --- | ----------------- |
| 0   | 0   | 0   | 0   | 0   | 0.08192           |
| 0   | 0   | 0   | 0   | 1   | 0.02048           |
| ... | ... | ... | ... | ... | ...               |
| 1   | 1   | 1   | 1   | 1   | 0.32768           |

---

## データ生成結果（サンプル分布 vs JPDT）

* 100サンプルを JPDT に基づいてランダム生成し、確率の一致度を評価
* 統計的に推定した確率と真の確率の **平均絶対誤差 ≒ 0.015〜0.03 程度**
* 小さいサンプルサイズながら高い一致率を確認

---
## 📈 結果①：分布比較グラフ（JPDT vs 生成データ）

![JPDT\_vs\_Generated](/mnt/data/8d3ebf86-b55d-47c4-aab8-1c2273da4acd.png)

* `JPDT`: 理論分布（計算による真値）
* `Generated`: JPDT に基づいて生成された100件のサンプルから推定した経験的分布
* 高確率パターン（例：`11111`, `11110`）の一致度が高い
* 低確率パターンではランダム性により誤差がやや大きくなる

---

## 📉 結果②：誤差のヒストグラム

![Error\_Histogram](/mnt/data/0be92fcf-8024-446c-a542-20bbe92f43f0.png)

* **大多数のパターンで誤差は 0.01 未満**
* 平均絶対誤差（MAE） ≈ 0.012前後
* 明らかに逸脱した外れ値はほぼ存在せず、生成モデルの妥当性を支持

---

## 📌 結果③：誤差 vs サンプル出現頻度（散布図）

![Error\_vs\_Count](/mnt/data/0e5e5b05-6ced-485c-89f7-785c53238a68.png)

* サンプル出現数が**多いパターンほど誤差が小さい**
* サンプル数 1〜2 のレアパターンでは、最大で **0.03 程度の誤差**が発生
* 正しい分布を得るには十分なデータ数が必要なことを視覚的に示す


## 考察

### ジョイント確率生成の妥当性

* 条件付き確率の積により正しい Joint Distribution を構成できることを確認
* 正規化処理も含め、 **全体の確率和 = 1.0** を保証

### サンプルの正確性

* ランダムサンプリングであっても、JPDTが適切に構築されていれば、**分布を正確に再現できる**
* 実際の応用ではこのような手法で疑似データ生成やベイズ学習が行われる

---

## 今後の展望

* MAP推定によるパラメータ学習（Lecture 6 に対応）
* サンプル数を変えての一致率検証（n=1000, 10000など）
* JPDTをCSVに出力して別モデルへの入力に再利用
* 生成データを用いた分類・推論タスクへの応用
* 他のBN構造への一般化（自動グラフ入力など）

---

## Reference

* Lecture 5: Bayesian Network, Prof. Qiangfu Zhao
* [Bayesian Network – Wikipedia](https://en.wikipedia.org/wiki/Bayesian_network)
* [Norsys Netica examples](http://www.norsys.com/networklibrary.html)
* [pandas.DataFrame.cumsum() – pandas docs](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.cumsum.html)

---

## 実行手順
```bash
docker-compose build
docker-compose up
```



















以下は、あなたの最新の実行結果（CSV・可視化グラフ付き）をもとに、Project 4 の成果を反映した `README.md` の更新版です。

---

# Project 4: ベイジアンネットワークによるジョイント確率分布とデータ生成

---

## 📘 概要（やったこと）

* 講義資料 p.25 にあるベイジアンネットワークを元に Joint Probability Distribution Table（JPDT）を作成
* 条件付き確率の積により全 32 通りのパターンに対する **真の確率分布（JPDT）** を構築（Program 1）
* JPDT をもとに **100件のサンプルデータを乱数で生成**（Program 2）
* 生成されたサンプルの分布と元のJPDTを比較し、**誤差の可視化・妥当性評価を実施**

---

## 💻 システム環境

* 実行環境: Google Colab
* OS: Ubuntu 20.04（Colab内）
* Python: 3.10+
* 使用ライブラリ:

  * pandas
  * numpy
  * matplotlib
  * seaborn

---

## 📊 使用モデルと条件付き確率

構造:

```
X1 → {X2, X3}
X2, X3 → X4
X3 → X5
```

条件付き確率（講義資料に基づく）：

* `P(X1)`
* `P(X2 | X1)`
* `P(X3 | X1)`
* `P(X4 | X2, X3)`
* `P(X5 | X3)`

---

## 📈 結果①：分布比較グラフ（JPDT vs 生成データ）

![JPDT\_vs\_Generated](/mnt/data/8d3ebf86-b55d-47c4-aab8-1c2273da4acd.png)

* `JPDT`: 理論分布（計算による真値）
* `Generated`: JPDT に基づいて生成された100件のサンプルから推定した経験的分布
* 高確率パターン（例：`11111`, `11110`）の一致度が高い
* 低確率パターンではランダム性により誤差がやや大きくなる

---

## 📉 結果②：誤差のヒストグラム

![Error\_Histogram](/mnt/data/0be92fcf-8024-446c-a542-20bbe92f43f0.png)

* **大多数のパターンで誤差は 0.01 未満**
* 平均絶対誤差（MAE） ≈ 0.012前後
* 明らかに逸脱した外れ値はほぼ存在せず、生成モデルの妥当性を支持

---

## 📌 結果③：誤差 vs サンプル出現頻度（散布図）

![Error\_vs\_Count](/mnt/data/0e5e5b05-6ced-485c-89f7-785c53238a68.png)

* サンプル出現数が**多いパターンほど誤差が小さい**
* サンプル数 1〜2 のレアパターンでは、最大で **0.03 程度の誤差**が発生
* 正しい分布を得るには十分なデータ数が必要なことを視覚的に示す

---

## 📌 考察（まとめ）

| 項目          | 評価内容                                     |
| ----------- | ---------------------------------------- |
| JPDTの構築精度   | 条件付き確率を掛け合わせることで、理論的に一貫した Joint 分布を正確に生成 |
| データ生成の再現性   | 高頻度パターンでは良好な一致。低頻度パターンではサンプリングのばらつきあり    |
| 可視化による妥当性検証 | 分布比較・誤差ヒストグラム・誤差散布図の3視点から定量的に妥当性を確認      |
| 改善点         | サンプル数を増やすことで、レアケースの分布再現精度がさらに向上する        |

---

## 🔭 今後の展望

* MAP推定を用いた **確率パラメータの再学習（Lecture 6）**
* KLダイバージェンスによる分布類似度の定量評価
* n = 1000, 10000 などでの誤差収束性検証
* 構造学習（BN構造自動構築）の拡張

---

## 📂 入出力ファイル（Colab対応）

| ファイル                 | 内容                     |
| -------------------- | ---------------------- |
| `JPDT.csv`           | 条件付き確率から構築した Joint 分布表 |
| `generated_data.csv` | JPDT に基づき生成したデータ100件   |

---

## ▶️ Google Colab 実行手順

```python
# 必要ライブラリのインストール（初回のみ）
!pip install pandas matplotlib seaborn

# 1. JPDTを生成するコード（Program 1）を実行
# 2. サンプルを生成（Program 2）
# 3. グラフ可視化（比較、ヒストグラム、誤差散布図）
```

---

## 📚 Reference

* Lecture 5: Bayesian Network (Qiangfu Zhao, 2025)
* [Bayesian Network – Wikipedia](https://en.wikipedia.org/wiki/Bayesian_network)
* [pandas.DataFrame.value\_counts() – pandas docs](https://pandas.pydata.org/docs/)
* [seaborn scatterplot](https://seaborn.pydata.org/generated/seaborn.scatterplot.html)

---

ご希望があれば、この `README.md` を Markdown ファイルとして出力します。必要ですか？
