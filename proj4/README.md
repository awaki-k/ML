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

## グラフ出力（任意）

* 分布の棒グラフ比較（JPDT vs 生成サンプル）
* 誤差のヒストグラムなどに拡張可能

---

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
