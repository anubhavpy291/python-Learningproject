



while True:
    p = float(input("enter the principal amount: "))

    if p <= 0:
        p = float(input("enter the principal amount agin it cant be less then or equal to 0: "))
    else:
        break
while True:
    r = float(input("enter the rate at apply on principal amount: "))

    if r <= 0:
        r = float(input("enter the rate again it cant be less than or equal to zero: "))
    else:
        break
while True:
    t = float(input("enter the time for whcih rate apply: "))

    if t <= 0:
        t = float(input("enter the time agin it cant be less than or equal to zero: "))
    else:
        break

A = p * pow(1 + r / 100,t)

print(f"your final return after {t} at {r} on {p} : {A}")