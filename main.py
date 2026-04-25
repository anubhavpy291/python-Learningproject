import math
import random


name = "blad1e river"
age = 2
height = 5.8
print(f"hello my name is the {name} my age is {age}")


# typecast
name = bool(name)
height = int(height)
print(type(height))
print(name)
print(height)

#input
name = str(input("Enter your name:"))
print(name)

#logical oprator

age += 1
age -= 1

age **= 2
print(age)
age %= 2
print(age)
age = 2
age /= 2
print(age)

#math

height = 5.8
height = round(height)
print(height)
age = -40
age = abs(age)
print(age)
bodycount = 2
bodycount = pow(bodycount,2)
print(bodycount)
bodycount = min(height,age)
print(bodycount)
bodycount = max(height,age)
print(bodycount)

print(math.pi)
print(math.e)
print(math.sqrt(4))
print(math.ceil(4.1))
print(math.floor(9.1))

#state
alive = True
age = int(input("enter you age: "))

if age >= 32:
    print("do in real life")
elif age >= 18:
    print("can enter")
elif age <= 0:
    print("give valid age")
else:
    print("go and brush your teeth")

if alive:
    print("sleep on bed")
else:
    print("sleep under coffine")

disable = True

if alive and disable:
    print("become steven hawking")
elif alive and not disable:
    print("become nikola tesla")
elif alive or disable:
    print("idk")
else:
    print("enjoy the heven i guess")

# string opration

lengthofstring = len(name)
print(lengthofstring)
name = name.capitalize()
print(name)
m = name.find("A")
print(m)
o = name.rfind("a")
print(o)
p = name.index("v")
print(p)

print(name.isalpha())
name = name.upper()
print(name)
name = name.replace("A","a")
print(name)
name = name.lower()
print(name)
q = name.count("a")
print(q)

#INDEXING

print(name[0])
print(name[:5])
print(name[::2])
print(name[::-1])
print(name[-1:-4])
print(name[::1])
print(name[2::2])

#formate specific 

height = 5000.837928
age = 3
bodycount = -10.9383
print(f"height is {height:.5f}")
print(f"height is {height:,}")
print(f"height is {age:08}")
print(f"height is {age:<05}")
print(f"height is {age:>05}")
print(f"height is {age:^05}")
print(f"height is {bodycount:+}")
print(f"height is {bodycount:+,.2f}")


#while loop

rate = int(input("ENter your rate: "))

while rate <= 0:
    if rate < 0:
        rate = int(input("enter valide rate: "))
    elif rate == 0:
        rate = int(input("Enter rate that give profit: "))
    else:
        break

print(f"thanks for that {rate}")

#--------------------for--------loop-------------------------#

for x in range(1,100):
    print(x)
for y in reversed(range(1,100)):
    print(y)
for z in range (1,10,2):
    print(z)

for i in name:
    print(i)
    if i == "a":
        continue
    elif i == "v":
        break

#------ted loop

row = int(input("enter the no of row: "))
colum = int(input("enter the no of colum: "))
symbols = input("enter the symbol")

for x in range(row):
    for y in range(colum):
        print(symbols, end="")
    print()

#-----list -----[]-----orderabl and can chnage 
asset = ["car","house","laptop","helicoptor","bmw","bmw"]
asset.append("earbud")
asset.remove("house")
asset.sort()
print(asset)

asset.reverse()
print(asset)
asset.insert(3,"anubhav")
print(asset.index("anubhav"))

print(asset.count("bmw"))
print(asset)
print(len(asset))
asset.clear()
print(asset)
print(asset[::-1])

for x in asset:
    print(x)
print("car" in asset)
#--------------set----{}----------unorderable but can change by add and remove

libality = {"car","work","family members","parents"}
libality.add(".com")
libality.remove("parents")
libality.remove("family members")
libality.pop()
print(libality)

#------------touple----()---orderable but notchangable

hobby = ("playing game", "programing", "reading book", "learning new stff")
print(hobby)

#-----2d---list------

food = ["pizza","saurma","burger","pasty","cake"]
drnk = ["coca","pepsi","starbugs","fenta"]
menu = [food,drnk]
print(menu)
x = int(input("enter the catgrie "))
y = int(input("enter the item: "))

print(f"you want to buy this: {menu[x][y]}")

for f in food:
    for d in drnk:
        print(f,d)

#-----------------distnory-----------

dis = {"usa": "idk","in": "idks","china": "idkss"}
print(dis.get("usa"))
ins = input("enter the country name: ")
if dis.get(ins) is  None:
    print("its not in my mind ")
dis.update({"usa": "ik"})
dis.update({"brazil": "idk"})
print(dis.get("brazil"))
print(dis.keys())
print(dis.values())

#------------random------------

print(random.randint(1,10))
print(random.random())
print(random.shuffle(asset))
print(random.choice(hobby))

#-------function-------

def function_name(agrumesnt, defaultagrument=3):
    print(agrumesnt)
    return defaultagrument
function_name("hi11")
function_name(agrumesnt="hellow ")
print(function_name("anv"))

 
def sum(*args):
    total = 0
    for sums in args:
        total += sums
        return total
    
#while True:
#    ins = int(input("enter the number q for  quit: "))

#    print(f"here is your sum {sum(ins)}",end=",")

#    def sum(**kwgs):
 #       for key,value in kwgs.items():
#            print(f"{key}{value}")


#----------------iritable---------

item = ["gun","food","home"]
itemss = {"food": "anubhav","home": "lone"}
for items in item:
    print(items)
for key,value in itemss.items():
    print(f"{key}{value}")

#----------------membership opratror--------------

inputss = input("enter the ite name: ")
itemr = ["anubhav","sing","user"]

if inputss in  itemr:
    print("yes")
else:
    print("not")

#-----list comprihencen ------------------

double = []
for x in  range(1,10):
    double.append(x * 2)
print(double)
ls = [y *2 for y in range(1,10)]

#------match-case-----

day = input("enter the day")
day.lower()
match day:
    case "monday" | "tuesday" | "wednesday" :
        print("its a boring day")
    case "thursday" | "friday" | "saturday" | "sunday":
        print("its a good day")
    case _:
        print("enter the valid day plz")


#---moudls-------
from math import e
import areacal as a
a.hel()
print(e)
import math

#---variable scope





#-----oop---------------------------------------------------------------------
class car:
    def __init__(self,speed,milaze,engine):
        self.speed = speed
        self.milaze = milaze
        self.engine = engine
    def start(self):
        print(f"start {self.speed}")
    def stop(self):
        print(f"stop {self.milaze}")

bmw1 = car(300,5,"v5")
bmw1.start()
#calss variable
class std:
    numstd = 0
    def __init__(self,name,age,clas):
        self.name = name
        self.age = age
        self.clas = clas
        std.numstd += 1
x = std("x",34,34)
y = std("Y",23,12)
print(std.numstd)

#------------inheritance--------------

class shape:
    def __init__(self,name,area):
        self.name = name
        self.area = area
    def dec(self):
        print(f"thw name is {self.name}")
        print(f"the area is {self.area}")
class triangle(shape):
    pass
class circle(shape):
    pass
cir = circle("circ",50)
cir.dec()
tra = triangle("tri",500)
tra.dec()

#--------------multiinheritance---------------------

class shape:
    def __init__(self,name,x,y):
        self.name = name
        self.x = x
        self.y = y

    def dec(self):
        print(f"thw name is {self.name}")
        print(f"the area is {self.x} {self.y}")
class rombus(shape):
    pass

class square(rombus):
    pass

squar = square("square",45,70)
squar.dec()

#-----super()--------------
class shape:
    X = "dff"
    def __init__(self,name,x,y):
        self.name = name
        self.x = x
        self.y = y

    def dec(self):
        print(f"thw name is {self.name}")
        print(f"the area is {self.x} {self.y}")

    def area(self):
        return self.x * self.y
class square(shape):
    X = "4545"
    def dec(self):
        print(f"the square of area is alwwsys same")
        super().dec()

squar = square("square",45,70)
squar.dec()
print(squar.X)

#------polymorphesis---------------

class car:
    def __init__(self,speed,hp,engine,name):
        self.speed = speed
        self.hp = hp
        self.engine = engine 
        self.name = name
    def start(self):
        print(f"the {self.name} is starting")
class bmw(car):
    pass
class mustange(car):
    pass
class nissan(car):
    pass


cars = [bmw(300,1200,"v8","bmw m4 cs"),mustange(259,1000,"v4","mustange gt 28"),nissan(280,1100,"v6","nissan gtr")]

for c in cars:
    print(c.name)
    print("-------------------------------------------------")
    print(c.speed)
    print(c.hp)
    print(c.engine)
    print("-------------------------------------------------")

#---------------duct---type---------------------------

class human:
    def idk(self):
        print("idk")
    def __init__(self,name):
        self.name = name
        print(self.name)
class male(human):
    pass
class female:
    def idk(self):
        print("idk")

h = [male("hi"),female()]

for j in h:
    j.idk()

#-----------static--methood--------------

class pc:
    
    @staticmethod
    def info(namee):
        spec = {"dell inspiration 3537": (6,"i5 4200u",720,"itnel hd 4400")}
        if spec.get(namee):
            print(namee)
            print("----------------------------------------")
            print(f"ram: {spec.get(namee)[0]}")
            print(f"cpu: {spec.get(namee)[1]}")
            print(f"storage: {spec.get(namee)[2]}")
            print(f"gpu: {spec.get(namee)[3]}")
            print("--------------------------------------")
        else:
            print("data is unavaliable")
pc.info("dell inspiration 3537")


#------class---method------

class st:
    sts = {}
    totalgpa = 0
    totalstd = 0
    def __init__(self,gpa,name):
        st.sts.update({name: gpa})
        st.totalgpa += gpa
        st.totalstd += 1
    def hi(self):
        pass
    @classmethod
    def stinfo(cls):
        print(f"the average gpa is {(cls.totalgpa / cls.totalstd):.2f}")
   
    @classmethod
    def stfullinfo(cls):
        print("name: gpa")
        print("------------------------------------")
        for key, iva in cls.sts.items():
            
            print(f"{key}: {iva}")
        print("------------------------------------")
        st.stinfo()
        print("------------------------------------")
s = st(3,"gacky")
s = st(3,"robin")
s = st(3,"idk")
st.stfullinfo()
s.hi()

#----------magic--method

class liberary:
    def __init__(self,name,author,price):
        self.name = name
        self.author = author
        self.price = price
    def __call__(self):
        print("hiii")
    def __add__(self, other):
        print(f"the total is {self.price + other.price}")
    def __eq__(self, other):
        print("eq")
        return self.price == other.price 
    def __lt__(self, other):
        print("lt")
        return self.price < other.price
    def __gt__(self, other):
        print("gt")
        return self.price > other.price
    def __contains__(self, item):
        return item in self.name 
    
hi = liberary("yoo","idk",343)
hl = liberary("yoo","idk",33)
hi()
hi + hl
print(hi == hl)
print(hi < hl)
print(hi > hl)
print("oo" in hi)

#--------------propertyieses-------

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
h1.usr = "anubhsdasv"
h1.usr = "anubhdfaav"
h1.usr = "anubhdfsav"
h1.usr = "anubhdfav"
h1.usr = "anubsdfhav"
h1.usr = "anudfbhav"
print(h1.usr)
del h1.usr

#-------decoration

def living(fnc):
    def wrap(*args):
        print("its a living thing")
        fnc(*args)
    return wrap

@living
def gender(name):
    print(name)

gender("male")

#------expection----editing-------

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

#------file-handiling------
