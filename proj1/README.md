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

## Reference
* [気象庁サイト](https://www.data.jma.go.jp/gmd/risk/obsdl/index.php)
* [使用モデル詳細](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)
* [MAEの説明](https://e-words.jp/w/%E5%B9%B3%E5%9D%87%E7%B5%B6%E5%AF%BE%E8%AA%A4%E5%B7%AE.html#google_vignette)
* [標準誤差の説明](https://data-viz-lab.com/standarddeviation)
