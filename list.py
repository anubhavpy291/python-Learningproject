#shorting
list = [2,45,76,24,12]
list.sort()
print(list)

#sort reverse
list.sort(reverse = True) #use reverse key word in sort function 
print(list)

#coustome-fun
def fun(n):
    return abs(n - 50)


def fun1(n):
    n = str(n)
    m = n[::-1]
    print(n)
    return m
list.sort(key = fun)
print(list)
list.sort(key = fun1)
print(list)

#case sensitive 
#list.sort(key = str.lower())

#list reverse

list.reverse()

#copy--list

#copymethod
list2 = list.copy()

#slice mthod
list2 = list[:]

#new list method
#list2 = list(list)
print(list2)

# joiniing list--

# using plus opeerat
l1 = [1,2,3]
list3 = [4,5,6,7]
l1 = l1 + list3
print(l1)

# loop through each time and append
for x in list3:
    l1.append(x)

#by extend fun
l1.extend(list3)

print(l1)