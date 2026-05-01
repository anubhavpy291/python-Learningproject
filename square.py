raw = int(input("Enter a raw: "))
colm = 4

data = []
for i in range(raw):
    r = []
    print("-----------")
    for f in range(colm):
        d = int(input("data: "))
        r.append(d)
    data.append(r)
print(data)
for i in range(raw):
    if data[i][0] == data[i][1] == data[i][2] == data[i][3]:
        print("win")
    else:
        print("lose")