## 06.集合

def n_gram(n, sequence):

    result = []
    for i in range(len(sequence)-n+1):
        result.append(sequence[i:i+n])

    return result

str1 = "paraparaparadise"
str2 = "paragraph"

X = set(n_gram(2, str1))
Y = set(n_gram(2, str2))

# 和集合
# print(X or Y)
print(X | Y)
print(X.union(Y))


# 積集合
# print(X and Y)
print(X & Y)
print(X.intersection(Y))

# 差集合
print(X - Y)
print(X.difference(Y))

# 'se'の検査
print('se' in X.union(Y))
