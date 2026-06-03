import array
a = array.array('d',[45.23])
print(a[0])

a.append(45.6)
a.extend([34.34,45.5])
a.insert(0,34.2)

for i in a:
    print(i)

a.remove(45.6)
a.pop()

print(a[0:2])
