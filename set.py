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
#union keep only unduplicates and return its in new set
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
s11 = {"hii","how","are"}
s12 = s11.intersection(s9)
print(s12)

#you can use & operator to use instedof intersection give same result as intersection you can use only set ot set its does not support other data type like intersection
s12 = s11 & s9
print(s12)

#direct intersection
s11.intersection_update(s9)
print(s11)

#difference remove same item present in both set1 and 2 from set set 1 
a = {2,4,56}
b = {2,56,673,3445}
c = a.difference(b) # remove the same item present in botht from a 
print(c)

#direct remove from set 1 

#a.difference_update(b)
print(a)

# yoou  can direct use the - operator to see the sane result but you can inly use set tot set not other like differenece 

c = a - b
print(c)

# semmartic  differnece keep only ittem that are not present in both 
c = a.symmetric_difference(b) 
print(c)

# direct symmetric  differnece 

a.symmetric_difference_update(b)
print(a)

# you   can also use ^ to get same result 

c = a ^ b
print(c)

#frgenset 
a = frozenset({1, 2})
b = frozenset({3, 4})
c = frozenset({2, 3})
print(a.isdisjoint(b))
print(a.isdisjoint(c))

#subsert
a = frozenset({1, 2})
b = frozenset({1, 2, 3})
print(a.issubset(b))
print(a <= b)
print(a < b)

#superset
a = frozenset({1, 2, 3})
b = frozenset({1, 2})
print(a.issuperset(b))
print(a >= b)
print(a > b)

