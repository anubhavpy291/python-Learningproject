try: 
    ins  = int(input("enter the numbre for input: "))
    print(ins / 3)
except ValueError:
    print("value error")
except TypeError:
    print("type error")
except ZeroDivisionError:
    print("zero division")
finally:
    print("fuck off")