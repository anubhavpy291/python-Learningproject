n1 = float(input("Enter the number: "))
op = input("chose oprator (+,-,*,/,%) ")
n2 = float(input("enter the another number: "))

if op == "*":
    print(n1 * n2)
elif op == "+":
    print(n1 + n2)
elif op == "-":
    print(n1 - n2)
elif op == "/":
    print(n1 / n2)
elif op == "%":
    print(n1 % n2)
else:
    print("invalid oprator")