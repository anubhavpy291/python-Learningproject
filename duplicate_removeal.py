x = [0,0,1,1,1,2,2,3,3,4]
l = len(x)
y = ""
z = None
for i in range(l - 1):
    for j in range(i+1,l):
        if x[i] == x[j]:
            x.pop(i)
            break
        else:
            y += str(x[i])
            z = str(x[j])
            break
y += z
print(int(y))
print(x)