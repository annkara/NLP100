## 03. 円周率

str_Pi = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

# スペースで分割
word_list = str_Pi.split()

# ,.を除外して文字数をカウントする
# 1. stripメソッドを利用してカウントする。
word_hist = []
for word in word_list:
    word_hist.append(len(word.strip(',.')))

print(word_hist)

# 2. 1.のリスト内包表記
print([len(word.strip(',.')) for word in word_list])

