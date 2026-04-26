
def living(fnc):
    def wrap(*args):
        print("its a living thing")
        fnc(*args)
    return wrap

@living
def gender(name):
    print(name)

gender("male")
