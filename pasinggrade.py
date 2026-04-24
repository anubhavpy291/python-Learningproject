list = []

while True:
    ins = input("Enter the grade and q for quit: ")
    if ins.lower() == "q":
        break
    elif ins.isdigit():
        list.append(ins)
    else:
        print("plz but vaildi number")

nlist = [x for x in list if int(x) >= 32]
print(nlist)