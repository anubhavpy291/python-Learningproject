class huname:
    names = []
    
    @property
    def usr(self):
        return huname.names
    @usr.setter
    def usr(self,new_NoHuname):
        huname.names.append(new_NoHuname)
    @usr.deleter
    def usr(self):
        del huname.names
        print("file is deleted")
h1 = huname()
isruning = True
while isruning:
    ins = input("(a)dd usr / (s)how usr: ")
    if ins == "a" and ins.isalpha():
        instr = str(input("enter the user name: "))
        h1.usr = instr
    elif ins == "s" and ins.isalpha():
        print(h1.usr)
    else:
        print("please enter the valid input")
