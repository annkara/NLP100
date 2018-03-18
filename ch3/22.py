# 22.カテゴリ名の抽出
'''
    [[Category:カテゴリ名|...]]
'''
import re

text = 'England.txt'
pattern = 'category'

# Category部分のみを抽出
with open(text) as f:
    categories = []
    for line in f.readlines():
        if re.search(pattern, line, flags=re.IGNORECASE):
            categories.append(line)

# stripメソッドを利用して、先頭および末尾から不要文字を削除
for category in categories:
    e = category.strip('[]:Category\n')
    print(e.split('|')[0])

# TODO: 正規表現を利用しての実装
