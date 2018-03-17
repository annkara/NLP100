# 10.行数のカウント

text = 'hightemp.txt'

# 1. readlines() -> 各行を要素とするリストを返す。
with open(text) as f:
    lines = f.readlines()
print(len(lines))

# 2. ファイルオブジェクトをイテレートし、カウントする。
with open(text) as f:
    count = 0
    for _ in f:
        count+=1
print(count)
