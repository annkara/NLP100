# 20.JSONデータの読み込み
import gzip
import json

text = 'jawiki-country.json.gz'

# gz形式のファイルを開く
with gzip.open(text, mode='rt') as gf:
    articles = []
    # 1行ずつPythonオブジェクトに変換し、リストに追加する。
    for row in gf:
        articles.append(json.loads(row))

with open('England.txt', 'wt') as f:
    # リストから1記事ずつ取得し、titleがイギリスな記事を取得
    for article in articles:
        if 'イギリス' == article['title']:
            print(article['text'], file=f)
            # 見つかったら処理を終える
            # timeコマンドで実行時間みたら、あまり変わらん。
            break
