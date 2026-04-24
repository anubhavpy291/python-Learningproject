import random
options = ("rock", "paper", "sisor")
player = None

pscore = 0
cscore = 0


while True:
    if player != "rock" or player != "paper" or player != "sisor":
        computer = random.choice(options)
        player = input("pick one of them (rock, paper, sisor) plz: ")
        if computer == player:
            print("its a tie")
        elif computer == "paper" and player == "rock":
            print("computer win")
            cscore += 1
        elif computer == "paper" and player == "sisor":
            print("player win")
            pscore += 1
        elif computer == "rock" and player == "sisor":
            print("computer win")
            cscore += 1
        elif computer == "rock" and player == "paper":
            print("player win")
            pscore += 1
        elif computer == "sisor" and player == "rock":
            print("player win")
            pscore += 1
        elif computer == "sisor" and player == "paper":
            print("computer win")
            cscore += 1

            
if pscore > cscore:
    print("player win")
else:
    print("computer win")