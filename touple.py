# ordeable unchageable duplicate

t = ("zxt","erfd","dsf")
print(t)

#creating with one element

t = ("xyz",)

#crrating with contraint

print(type(t))

t = tuple(("zf","sdf","er"))

#---------------------------access-----------tuple-----------item-----------------------------------------

#indexing
print(t[1]) #its print the second index item of tuple 

#--negative-indexing
print(t[-1]) #its print the fritst index item from last of tuple

#---range of indecing
print(t[:]) # print whole tuple from start to end
print(t[1:3]) # print the item from index 1 to 2 , 1 is inclouded but 3 is not
print(t[:2]) # its print the 0,1 index item 

#--range-of-negative--indexing

print(t[-1:-3]) # print item form last index to 2nd last index -3 is not inclouded 
print(t[:-2]) # its print item from index straring to last sencond index

#check if the item is exit int tuple or not

if "er" in t:
    print("er is already exist in tuple")

#--------------------------updating tuple----------------------------------------------------------

#--converting tuple to list to add and remove and sort tuple by type casting

#adding valuse to tuples

t = list(t)
t.append("dog")
t = tuple(t)
print(t)

#changing valuse in tuple
t = list(t)
t[0] = "cat"
t = tuple(t)
print(t)

#ading item in touple by making new tuple which add to existing tuple and the new tuple must contain addinga data 
tmp = ("gooner",)
t += tmp
print(t)

#when you create tuple and provide data in tuple its called tuple and you  can sign index valuse to vaiable by index

t1 = (45,67,12,34,65)
(age,height,weight,wealth,bodycount) = t1

print(age,height,weight,wealth)