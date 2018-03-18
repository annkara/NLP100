# 21.カテゴリ名を含む行を抽出
import re

text = 'England.txt'
pattern = 'category'

with open(text) as f:
    for line in f.readlines():
        # パターンにまっちすれば、matchオブジェクト返る。
        # 該当しなければNoneが返る。
        # 大文字、小文字を区別しない。
        if re.search(pattern, line, flags=re.IGNORECASE):
            print(line, end='')
