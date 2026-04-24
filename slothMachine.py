import random
isPlaying = True
de = 2000
ba = 16000
def slothRandom():
    item = ["X","Y","Z"]
    return  [random.choice(item) for _ in range(3)]
def balances():
    return ba
def payout(rands,bet):
    if rands[0] == rands[1] == rands[2]:
        print("-----------------------------------------------------------------")
        print("you win a lottery !!!!!")
        print("''''''''''''''''''''''''''''''''''''''")
        if rands[0] == "X":
            return bet * 3
        elif rands[0] == "Y":
            return bet * 5
        elif rands[0] == "Z":
            return bet * 7
        else:
            return 0
        print(f"here is your update balance: {ba}")
    else:
        return 0

while isPlaying:
    print("-----------------------------------------------------------------")
    print(f"your balance amount: {ba}")
    print(f"the bet amount is {de} per spin: ")
    print("-----------------------------------------------------------------")
    ins = input("do you want to spin (Y/N): ").upper()
    print("-----------------------------------------------------------------")
    if de > ba and ins == "Y":
        print("inficient balance")
        print("_______________________________________________________________")
        isPlaying = False
    elif ins == "Y":
        ba -= de
        rads = slothRandom()
        print("            |            ".join(rads))
        ba += payout(rads,de)
    elif ins == "N":
        print("get the fuck out of here")
        isPlaying = False
    else:
        print("-----------------------------------------------------------------")
        print("enter the valid input:")
        print("-----------------------------------------------------------------")