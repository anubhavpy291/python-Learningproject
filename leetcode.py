h = "sedbutswd"
n = "sad"
a = 0
l = len(h)
b = len(n)
A = 0
while a < l:
    print(h[a:b])
    c = h[a:b]
    if c == n:
        A = a
        break
    else:
        A = -1
    b += 1
    a += 1
print(A)