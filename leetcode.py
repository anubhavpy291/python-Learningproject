##nums1 = []
##m = 0
##nums2 = [1]
##n = 1

##nums1 = [nums1[x] for x in range(m)]
##nums2 = [nums2[x] for x in range(n)]
##nums1 += nums2
##nums1.sort()
##print(nums1)

#nums = [-1,0,0,0,0,3,3]
#l = len(nums)
#a = []
#for i in range(l -1):
#    for j in range(i + 1,l):
#        if nums[i] == nums[j]:
#            a.append(i)
#print(a)
#for i in a:
#    a = nums.index(i)
#    del nums[a]
#print(nums)

#nums = [1,1,2,1,2,6]

#d = {}
#for i in nums:
#    if i not in d:
#        d[i] = 0
#    else:
#        d[i] += 1
#for k,v in d.items():
#    if v == 0:
#        print(k)

#        d = {}
#        for i in nums:
#            if i not in d:
#                d[i] = ""
#            else:
#                del d[i]
#        for i in d.keys():
#            return i

#for k,v in d.items():
#    if v == 0:
#        print(k)
#nums = [1,2,1,3,2,5]
#d = {}
#a = []
#for i in nums:
#    if i not in d:
#        d[i] = 0
#    else:
#        d[i] += 1
#for k,v in d.items():
#    if v == 0:
#        a.append(k)
#print(a)

#nums = [1,3,4,2,2]
#       d = {}
#       for i in nums:
#            if i not in d:
#                d[i] = ""
#            else:
#                return i

prices = [7,1,5,3,6,4]
sell = 0
buy = 8
a = []
a += prices
a.sort()
l = len(a)
b = []
c = []
print(prices)
for i in range(l - 1):
    for j in range(i+1,l):
        if prices.index(a[i]) < prices.index(a[j]):
            b.append(prices[prices.index(a[i])])

b.sort()
buy = b[0]
print(prices.index(buy) + 1)
index = a.index(buy)
for i in reversed(a[index:]):
    if buy <  prices.index(i):
        c.append(prices.index(i))
print(prices.index(prices[c[0]]) + 1)