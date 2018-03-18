# ファイルをN分割する
import sys

text = 'hightemp.txt'

# ファイルの分割数
n = int(sys.argv[1])

with open(text, 'rt') as f:
    lines = f.readlines()

# 1ファイル当たりの出力行数
unit = len(lines) // n

for row in lines[0:12]:
    print(row, end='')

# TODO: 分割してファイル出力する処理を実装する。
