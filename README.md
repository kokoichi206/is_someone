# is_someone

## 自作データセット作成
- 基本的には[ここ](https://qiita.com/AlphaMikeNeko/items/9870533f3ab1e11e340f)に則ってやる

### 手順一覧
1. [collectImg.py](https://github.com/kokoichi206/is_someone/blob/main/collectImg.py)で正解・不正解の画像を集めてくる
2. [preprocess.py](https://github.com/kokoichi206/is_someone/blob/main/preprocess.py)で集めた画像を前処理
   1. 大きすぎたらリサイズ
      1. これがないとメモリ食い散らかして死んだ
   2. 顔周辺のみ正方形で切り取り
   3. 画像サイズを一定値（50）にリサイズ
3. [makeDataset.py](https://github.com/kokoichi206/is_someone/blob/main/makeDataset.py)でnpzファイルを生成する（参考のサイト）
