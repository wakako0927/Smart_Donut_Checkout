<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8" />
</head>
<body>

<header>
  <h1>ドーナツ自動会計システム</h1>
  <p class="muted">
    本プログラムは、写真に写ったドーナツを検出し、<br>
    種類ごとの個数と合計金額を自動で計算する Python アプリケーションです。<br>
    YOLOv8 による物体検出を用いて、最大30%の重なりがある場合でも識別可能。<br>
    実店舗での会計処理を想定したシステムを構築しました。
  </p>
</header>

<section>
  <h2>特徴</h2>
  <ul>
    <li><strong>物体検出:</strong> YOLOv8 により 6 種類のドーナツを検出</li>
    <li><strong>価格計算:</strong> 検出ラベルと価格表を照合し、個数・小計・合計を自動算出</li>
    <li><strong>二段階推論:</strong> 全体検出 → 切り出し再推論で精度向上</li>
    <li><strong>Web UI:</strong> 画像アップロード → 即時に検出結果と会計明細を表示</li>
  </ul>
</section>

<section>
  <h2>ディレクトリ構成</h2>
  <pre><code>donut_checkout_system/
├─ app.py                 # Flaskアプリ
├─ utils/
│   └─ donut_detector.py  # 検出・価格計算
├─ templates/
│   ├─ index.html         # アップロード画面
│   └─ result.html        # 結果表示画面
├─ static/
│   └─ uploads/       
└─ models/
    └─ yolov8_donut.pt    # 学習済みYOLOモデル

</code></pre>
</section>

<section>
  <h2>セットアップ</h2>

  <h3>1) 環境</h3>
  <ul>
    <li>Python 3.10–3.12</li>
    <li>Windows / Linux（GPU は任意）</li>
  </ul>

  <h3>2) 依存関係</h3>
  <pre><code>pip install flask ultralytics opencv-python</code></pre>

  <h3>3) 学習済みモデル</h3>
  <p><code>models/yolov8_donut.pt</code> を同梱しています。</p>
</section>

<section>
  <h2>使い方</h2>

  <h3>Webアプリ（Flask）</h3>
  <pre><code>python app.py
# ブラウザで http://127.0.0.1:5000</code></pre>

  <ol>
    <li>トップページで画像をアップロード</li>
    <li>YOLOv8 によるドーナツ検出が実行</li>
    <li>検出結果と会計明細（種類・単価・個数・合計金額）が表示</li>
  </ol>

  <h4>出力例</h4>
  <p><img src="https://raw.githubusercontent.com/wakako0927/subtrans/refs/heads/main/SubTrans/images/sumple_image.JPEG" alt="例" width="700"></p>
</code></pre>
</section>

<section>
  <h2>モデル（YOLOv8）について</h2>
  <p><code>models/yolov8_donut.pt</code>（約 6 MB）を同梱しています。</p>

  <h3>学習データ</h3>
  <ul>
    <li>ドーナツ写真の自作収集</li>
    <li>クラス: 各種類ごと</li>
    <li>train 1400 / valid 130</li>
  </ul>

  <h3>学習条件</h3>
  <ul>
    <li>モデル: YOLOv8n</li>
    <li>画像サイズ: 640×640</li>
    <li>バッチサイズ: 16</li>
    <li>エポック: 約 100</li>
  </ul>
</section>

<section>
  <h2>ライセンス</h2>
  <p>MIT</p>
</section>

</body>
</html>
