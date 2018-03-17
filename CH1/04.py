## 元素記号

elements = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

li = [word.strip(',.') for word in elements.split()]

dictionary = {}
for n, v in enumerate(li):
    if n == 0 or (4 <= n <= 8) or (14 <= n <= 15) or n == 18:
        dictionary[n] = v[:1]
    else:
        dictionary[n] = v[:2]

print(dictionary)
