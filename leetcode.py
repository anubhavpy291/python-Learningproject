l1 = [2,4,3]
l2 = [5,6,4]

l1 = reversed(l1)
l2 = reversed(l2)
a = ""
b = ""
for i in l1:
    a += str(i)
for i in l2:
    b += str(i)

c = int(a) + int(b)
d = []

for i in reversed(str(c)):
    d.append(int(i))

print(d)