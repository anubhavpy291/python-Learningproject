def balance():
    print("-----------------------------------------------------------------")
    print(f"your account balance is: {balanced:,}")
    print("-----------------------------------------------------------------")
    return balanced
def withdraw():
    print("-----------------------------------------------------------------")
    inw = int(input("enter the amount for withdraw: "))
    print("-----------------------------------------------------------------")
    if(inw <= 0):
        print("-----------------------------------------------------------------")
        print("enter the corrtarct amount")
        print("-----------------------------------------------------------------")
        return 0
    elif inw > balanced:
        print("-----------------------------------------------------------------")
        print("infecient balance amount")
        print("-----------------------------------------------------------------")
    return inw
def deposite():
     print("-----------------------------------------------------------------")
     inb = int(input("enter the amount for deposite: "))
     print("-----------------------------------------------------------------")
     if(inb <= 0):
        print("-----------------------------------------------------------------")
        print("enter the corrtarct amount")
        print("-----------------------------------------------------------------")
        return 0
     return inb

print("-----------------------------------------------------------------")
print("1. for balance")
print("2. for withraw")
print("3. for deposite")
print("4. for exit")
ins = int(input("enter the number (1-4)"))
isRuning = True
balanced = 500
while isRuning:
    if ins == 1:
        balance()
        print("1. for balance")
        print("2. for withraw")
        print("3. for deposite")
        print("4. for exit")
        ins = int(input("enter the number (1-4)"))
    elif ins == 2:
        balanced -= withdraw()
        print("1. for balance")
        print("2. for withraw")
        print("3. for deposite")
        print("4. for exit")
        ins = int(input("enter the number (1-4)"))
    elif ins == 3:
        balanced += deposite()
        print("1. for balance")
        print("2. for withraw")
        print("3. for deposite")
        print("4. for exit")
        ins = int(input("enter the number (1-4)"))
    elif ins == 4:
        isRuning = False
    else:
        print("enter the valid number plz")
        print("1. for balance")
        print("2. for withraw")
        print("3. for deposite")
        print("4. for exit")
        ins = int(input("enter the number (1-4)"))