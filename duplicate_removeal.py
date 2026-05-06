x = [0,0,0,1,1,1,2,2,3,4,5,6,6,6,7,8,9]
l = len(x)
y =[]
for i in range(l - 1):
    for j in range(i+1,l):
        if x[i] == x[j]:
            
            break
        else:
            y.append(x[i])
            break
x = y
print(x)