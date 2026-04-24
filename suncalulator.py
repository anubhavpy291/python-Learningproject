
def sum(*args):
    total = 0
    for sums in args:
        total += sums
        return total
    
while True:
    ins = int(input("enter the number q for  quit: "))

print(f"here is your sum {sum(ins)}",end=",")

def sum(**kwgs):
    for key,value in kwgs.items():
        print(f"{key}{value}")