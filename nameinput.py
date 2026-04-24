name  = input("Enter your name: ")

if len(name) > 12:
    print("your name is under 12 chaacter only")
elif not name.isalpha():
    print("name does not contain spaces and number and special charcater")
else:
    print(f"welcome sir {name}")