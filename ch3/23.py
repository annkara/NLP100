# 23.セクション構造

import re

text = 'England.txt'

with open(text, 'rt') as f:
    for line in f.readlines():
        # "== word" にマッチする...はず
        # 後方部分はある前提にしてしまっているのでよくないかも
        match = re.match(r'(=+)\s*(\w+)', line)
        if match:
            print(len(match.group(1))-1, ' ', match.group(2))

