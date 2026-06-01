#Dictionaries are use to store key value pair data it is oradable . changeable but do not allow   duplicates 

d = {"name":"bladeriver","age":18,"height":5.8}
print(d)

#oradable mean they have defined oradable but the oder do not change
#unoradable mean they not have any defined orade you cannot use index

#changeable mean you can add or remove item after Dictionaries is created 

#------------------Dictionaries---len--------------

print(len(d))

#---------------data-type the value can be in any data type-------------
d2 = {"name":"bladeriver","age":18,"height":5.8,"alive":True}

#-------type=----
#dictionary is a object in a data type of dict
print(type(d2))

#dictinoay can be created using countructor dict

d2 = dict(name = "anubhav",age = 42,alive = True)


#--------------------accesing item in dictionry

#you can access item in dictionry by p;uting key in sqyare braket

print(d2["name"])

#you can also use method called get() to see the same result

print(d2.get("name"))

#key function return all key in list 
x = d2.keys()
print(x)
print(d2.keys())


#adding new key 

d2["class"] = 12
print(d2.keys())


#values return list of value present in discnoery

print(d2.values())

#item function return all keya and value in tuple list 
print(d2.items())

#checking if key exist in dictonri or not 

if "name" in d2:
    print("yes its exixts ")

#changing value in item by refring key

d2["alive"] = False

# the update fun update the dicitonary by refring key and its value in {} braket

d2.update({"alive":True})

# update fun also add key and value if key does not exixts 
d2.update({"class":11})

#same with []
d2["look"] = 6

#removing dictionary item by pop method

