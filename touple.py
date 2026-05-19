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

#when you create tuple and provide data in tuple its called tuple packing and when  sign variable to index value its called tuple unpacking

t1 = (45,67,12,34,65)
(age,height,weight,wealth,bodycount) = t1

print(age,height,weight,wealth)

#when unpaking tuple , the variable is less than the index in tuple so remaining index apply to aastrik * variable as the list

(a,b,*c) = t1
print(c)

#===================loop through tuple

#for loop
for x in t1:
    print(x)

#loop throgh index and using range and len function 
for x in range(len(t1)):
    print(t1[x])

#loop using while loop 
x = 0
while x < len(t1):
    print(t1[x])
    x += 1

#adding or joining tuples
t2 = (1,2,3,4,5)
t3 = (6,7,8,9)
t4 = t2 + t3
print(t4)

#multiplying tuple

t2 = t2 * 2
print(t2)

#---------------------------tuple method

#
t2.count() # give number of item in tuple
t2.index(3) # give the value of index or position in tuple

