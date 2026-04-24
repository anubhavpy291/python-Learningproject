questions = ("how is anubhav","age of anubhav","what anubhav do","want anubhav want to become")
options = (("A. Gretest Programmer","B. Time paser","C. Elephant"),("A. 47","B. 5","C. 17"), ("A. working serouly","B. doing nothing","C. pretending working"),("A. gretest programmer", "B. gamer", "c. crickerter"))

anser = ("A","C","A","A")
ansernum = 0 
questionnum = 0
myanser = []
correct = 0
for questio in questions:
    print("-----------------------------------------------------------------")
    print(questio)
    for answers in options[questionnum]:
        print(answers)
    ins = input("enter your anser no: ").upper()
    if anser[questionnum] == ins:
        ansernum += 1
        correct += 1
        print("correct answer, lets go next question")
    else:
        print("incorrect answer,")

        print(f"coreect anser is {options[questionnum][anser.index(anser[questionnum])]}  lets go next question")
    questionnum += 1   

print(f"total  corret: {correct} out of 4")