import time
ins = int(input("enter the nuber in second: "))
def countdown(max,min=0):
    for n in reversed(range(min,max)):
        print(n)
        time.sleep(1)
    print("time up")
countdown(max=ins)