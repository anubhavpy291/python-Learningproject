# set is unoradable and unchangeable and not allowed duplicates 
# its dont have any fixed index value to item each time the index value changes

s = {"hii","how","are","you"}
print(s)

#legth of set
print(len(s))

#duplicates :- 1 and true consider duplicates and - and 0 and false also 
#its suupport any data type 

s1 = {True,1,False,0}
print(s1)

#-----set-construstor---

s2 = set(("wsup","hru"))
print(type(s2))


#--------accesing item in set--------------------------------

#you caan not use index so we have to use loop like for and use in keyword to speficy to find keyword present in set

for x in s2:
    print(f"i found the hreu in s2({x})")

print("hru" in s2) # return true or false

if "hru" in s2:
    print("i found it")

#-----------------adding new item in set--------------------------------

# once we create set we cant edit item in set but we can add new item by add function
s2.add("fin")
s2.add("sus")
print(s2)


#we can add aany irriatable to set like list string disconery etc using update function 
s2.update(s1)
s2.update(s)
print(s2)

#----------------removing item in set-------------------------------------------

#its throw error if item is not in set to dodge this we  have to use dicard fun
s2.remove("fin")

s2.discard("df")

#delete complet set
del s1

#empty the set
s4 = s2.copy()
s4.clear()

#---------loop-set-----------------------------

for x in s2:
    print(f"i found the hreu in s2({x})")

#------------union-set-------------------------------
#union keep only duplicates and return its in new set
s5  = {1,2,3,4,7,7,2,9}
s6 = {1,3,5,4}
s8 = s5.union(s6)
print(s8)

# joining to set

s8 = s5 | s6
print(s8)

# joining multipale set
s8 = s5.union(s,s6,s2)
print(s8)
#this only allow you to joing datta to set tot  set not with other for other use union 
s8 = s5 | s6 | s2 | s4
print(s8)

#update inset item form one set ot another    set and its does not return any set 
s9 = {"hii"}
s9.update(s)
print(s9)

#intersection it return new set that contains item that present in both set

