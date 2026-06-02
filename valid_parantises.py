s = "()"
ins = []
a = False
b = None
for i in s:
    
    
    if len(ins) != 0:
        b = ins[-1]
    if i == "(" or i == "{" or i == "[":
        ins.append(i)
        b = i
    elif (i == ")" and b == "(")  or (i == "}" and b == "{") or (i == "]" and b == "["):
        print(ins)
        print(b,i)
        del ins[-1]
        b = None
        
if len(ins) == 0:
    a = True
else:
    a = False
print(a)