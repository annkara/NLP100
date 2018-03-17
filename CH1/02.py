## 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」

str1 = 'パトカー'
str2 = 'タクシー'

# zip関数とアンパック、リスト内包表記
li = [c1+c2 for c1, c2 in zip(str1, str2)]
for e in li:
    print(e, end='')

print()

# joinメソッド
print(''.join(li))

