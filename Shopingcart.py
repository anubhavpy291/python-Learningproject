itemss = {"books": "500","pens": "100","copy": "200"}
cart = []
total = 0
for ims in itemss:
    print(ims)
print("---------------------------------------------------------------")
while True:
    inp = input("enter the item name, q for quite: ")
    inpss = inp.lower()
    if  inpss == "q":
        print("thanks for visiting")
        break
    elif itemss.get(inp) is None:
       print("item is not in our list try again")
       continue
    else:
        cart.append(inp)
print(cart)
for ca in cart:
    total += int(itemss.get(ca))
print(f"total cost is: {total}")