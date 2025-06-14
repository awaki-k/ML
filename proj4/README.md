# ベイジアンネットワークによるジョイント確率表の構築とデータ生成（Project 4）

---

## 概要（やったこと）

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
## 結果①：分布比較グラフ（JPDT vs 生成データ）

![Image](https://github.com/user-attachments/assets/85854b73-2303-48c6-9716-74614dc1379a)

* `JPDT`: 理論分布（計算による真値）
* `Generated`: JPDT に基づいて生成された100件のサンプルから推定した経験的分布
* 高確率パターン（例：`11111`, `11110`）の一致度が高い
* 低確率パターンではランダム性により誤差がやや大きくなる

---

## 結果②：誤差のヒストグラム

![Image](https://github.com/user-attachments/assets/5d980fb5-de72-4153-b125-94604285907a)

* **大多数のパターンで誤差は 0.01 未満**
* 平均絶対誤差（MAE） ≈ 0.012前後
* 明らかに逸脱した外れ値はほぼ存在せず、生成モデルの妥当性を支持

---

## 結果③：誤差 vs サンプル出現頻度（散布図）

![Image](https://github.com/user-attachments/assets/0537fd78-762b-41e3-b58c-66d855d5123c)

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

## 今後の展望(やらない)

* MAP推定によるパラメータ学習
* サンプル数を変えての一致率検証（n=1000, 10000など）
* JPDTをCSVに出力して別モデルへの入力に再利用
* 生成データを用いた分類・推論タスクへの応用
* 他のBN構造への一般化（自動グラフ入力など）

---

## Reference
* [Bayesian Network – Wikipedia](https://en.wikipedia.org/wiki/Bayesian_network)
* [Norsys Netica examples](http://www.norsys.com/networklibrary.html)
* [pandas.DataFrame.cumsum() – pandas docs](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.cumsum.html)

---

## 実行手順
```bash
docker-compose build
docker-compose up
```
