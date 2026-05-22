import random

print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100.")
print("You have 5 chances to guess the correct number.")

print("Please select the difficulty level:")
print("1. Easy (10 chances)")
print("2. Medium (5 chances)")
print("3. Hard (3 chances)")

randomss = random.randint(1, 101)
inputs = int(input("Enter your choice: "))
attempt = 0
if inputs == 1:
    print("Great! You have selected the Easy difficulty level.")
    print("Let's start the game!")
    attempt = 10
elif inputs == 2:
    attempt = 5
    print("Great! You have selected the Medium difficulty level.")
    print("Let's start the game!")
    attempt = 5
elif inputs == 3:
    attempt = 3
    print("Great! You have selected the Hard difficulty level.")
    print("Let's start the game!")

print(inputs)
print(attempt)
while attempt != 0:
    guess = int(input("Enter your guess: "))
    if not 0 <= guess < 101:
        print("enter valid input")
        continue
    if randomss < guess and random != guess:
        print(f"Incorrect! The number is less than {guess}.")
        attempt -= 1
        continue
    elif randomss > guess and randomss != guess:
        print(f"Incorrect! The number is greater than {guess}.")
        attempt -= 1
        continue
    if randomss == guess:
        print(f"Congratulations! You guessed the correct number in {attempt} attempts.") 
        continue
