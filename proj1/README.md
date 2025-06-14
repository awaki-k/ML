# 線形回帰モデル作成

## 概要(やったこと)
* 線形回帰の理解
* データ取得・整形と評価・考察

## システム環境
* OS: Windows 11 + Docker Desktop
* Dockerバージョン: 24.0.5
* Docker Compose v2.23.0

## コンテナ環境
* OS: Ubuntu 20.04.6 LTS
* Pythonバージョン: 3.10.13
* cuda: 使ってないです

## 使用したモデルとかデータ
* データ: 地元(愛知県豊田市)の昨日(2025-06-12)から10日間の気温データを1時間ごと取得
* モデル: `sklearn`ライブラリの`LinearRegression`というモデル
* 評価: MAEと標準偏差

## 結果
* MAE: 約0.59℃
* 標準偏差: 約0.256℃
![Image](https://github.com/user-attachments/assets/63c8a456-4d1e-4ada-b6fc-f9627a404551)
![Image](https://github.com/user-attachments/assets/cfc16636-590a-4414-a6be-aac60607bc4e)

## 考察
### 誤差プロット（`prediction_error.png`）
- 大体の予測誤差は ±1℃ に収まった。
- 一部に +2℃ とか -2℃ くらいの外れ値がありそうだが、そこまで多くはない。
- エラーが連続して同じ向きにズレてるところもあって、トレンドを追いきれてない場面がある。
- 気温が急に変化する場面（朝夕とか）に弱い。(線形モデルだから仕方ない)

### 予測 vs 実測（`prediction_vs_actual.png`）
- 全体の波の形はまあまあ合ってる。
- 谷とか山の位置もそこそこ一致してるのは良い。
- ただ、気温のピークのあたり（25〜27℃くらい）では少し低めに出ている。
- 線形回帰の特性で、極端な値を抑え気味にする傾向があるからその影響かも。
- あと、気温が急に上がったり下がったりしてる部分では、予測が少し遅れてる感じがあって、ラグがあるように見える。

### モデルの構造と限界について

- 今回のモデルは、t-2, t-1, t の3時点の気温だけを使って、次の t+1 を予測してる。
- シンプルで軽く動く割に、短期の予測精度はそこそこ出てる。
- 時刻・天気を無視してるから、夜と昼の温度傾向の違いをモデルが知らない。
- 線形モデルなので、非線形な関係（例えば湿度が高いと温度が上がりにくい、みたいなやつ）も再現できない。

### 今後の展望(やらない)
- `hour`, `sin(hour)`, `cos(hour)` 入れれば、24時間周期のパターンを入れられる。
- 移動平均とか、温度変化の速度（微分っぽいやつ）とか、ラグ特徴量もたぶん有効。
- `t - t-1` みたいな差分を使うと、トレンド成分が表に出やすくなるかもしれない。
- XGBoostとかLightGBM使えば、非線形な関係も拾ってくれるし、重要な特徴量も見えてきそう。
- LSTMとかGRUみたいな時系列向けのRNN系使うと、連続した依存関係まで拾ってくれる（ただし重い）。
- SARIMAXやProphetとか、時系列に特化した予測モデルとの比較もしてみる価値あり。
- 今回はMAEだけ使ったけど、RMSEとかMAPE、R²とかも見たほうがいいかも。
- 日中・夜間とかに分けて、それぞれの精度を見るのもあり。

---

とりあえず、今回は線形回帰だけでやってみたけど、思ったより精度が出た。
勉強になりました。


## Reference
* [気象庁サイト](https://www.data.jma.go.jp/gmd/risk/obsdl/index.php)
* [使用モデル詳細](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)
* [MAEの説明](https://e-words.jp/w/%E5%B9%B3%E5%9D%87%E7%B5%B6%E5%AF%BE%E8%AA%A4%E5%B7%AE.html#google_vignette)
* [標準誤差の説明](https://data-viz-lab.com/standarddeviation)

## 実行手順
```bash
docker-compose build
docker-compose up
```
