strs = ["flower","flow","flight"]
l = len(strs)
a = strs[0]
o = ""
b = ""
for i in range(l - 1):
    if i < l - 1:
        b = strs[i + 1]
    for j in range(len(a)):
        if j < len(b) and a[j] == b[j]:
            o = o + a[j]
        else:
            break
    a = o
    o = ""
print(a)