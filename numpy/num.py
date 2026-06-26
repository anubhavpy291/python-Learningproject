import numpy as np

#array
#0-d arrary

arr = np.array(45)
print(arr)

#1d arrary

arr = np.array([1,2,3,4,5])
print(arr)
print(arr.ndim)

#indexing

print(arr[1])
print(arr[1] + arr[2])
#inndex sclice

print(arr[1:3])

#2d arrary

arr = np.array([[34,45,76],[45,56,78],[45,67,89]])

#indexing
print(arr[1][1])

print(arr[1,1])

#3d array

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

#indxing

print(arr[1,1,1])

print(arr[1][1][1])

#scliding 2d array

arr = np.array([[34,45,76],[45,56,78],[45,67,89]])
print(arr[1,1:3])
print(arr[1:3,1])

print(type(arr))


# data type
arr = np.array([1,2,3,4,5],dtype='S')
print(arr)
print(arr.dtype)


arr1 = np.array([1,2,3,4,5])
new_arr = arr1.astype(str)
print(new_arr)

#copy

arr = np.array([12,43,65,23])
n = arr.copy()
n[1] = 45
print(n)
print(arr)

#view

arr = np.array([12,43,65,23])

m = arr.view()

m[3] = 25
print(m)
print(arr)

#shape
arr = np.array([[34,45,76],[45,56,78],[45,67,89]])
print(arr.shape)

#re-shape 1d to 2d
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
arr1 = arr.reshape(4, 3)
print(arr1)

#re-shaping  1d ro 3d

arr2 = arr.reshape(2,3,2)
print("2",arr2)

#looping through 1d array

arr = np.array([1,2,3,4,5,6])

for i in arr:
	print(i)

#looping though 2d array

arr = np.array([[1, 2, 3], [4, 5, 6]])

for i in arr:
	print(i)

#looping through the one by one

for i in arr:
	for x in i:
		print(x)
#looping through 3d


arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for i in arr:
	print(i)

for i in arr:
	for x in i:
		for y in x:
			print(y)

for i in np.nditer(arr):
	print(i)

#jonining

arr1 = np.array([1,3,4,5])
arr2 = np.array([6,7,8,9])
arr = np.concatenate((arr1,arr2))
print(arr)

#joning 2d array axis = 1

arr1 = np.array([[1,3,4],[6,7,8]])
arr2 = np.array([[11,13,14],[15,16,17]])

arr = np.concatenate((arr1,arr2),axis=1)
print(arr)

#stacking array

arr1 = np.array([1,3,4,5])
arr2 = np.array([6,7,8,9])

arr = np.stack((arr1,arr2),axis=1)
print(arr)

#stacking 2d array

arr1 = np.array([[1,3,4],[6,7,8]])
arr2 = np.array([[11,13,14],[15,16,17]])

arr = np.stack((arr1,arr2),axis=1)
print(arr)

#stacking row

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.hstack((arr1,arr2))
print(arr)

#stacking row 2d

arr1 = np.array([[1,2,3,4],[5,6,7,8]])
arr2 = np.array([[11,12,13,14],[15,16,17,18]])

arr = np.hstack((arr1,arr2))
print(arr)

arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])

arr = np.vstack((arr1,arr2))
print(arr)

#splite array

arr1 = np.array([1,2,3,4,5])
arr = np.array_split(arr1,5)
print(arr)

corr = np.array([1,2,3,4,5])

print(corr.std(axis=0))

# matrix multiplication 

a = np.array([[1,2],[1,2]])
b = np.array([[1,2],[1,2]])

c = a @ b
print(c)

# transposal 

a = np.array([[1,2],[3,4]])
print(a.T)

#dot product

a = np.array([1,2,3,4])
b= np.array([1,2,3,4])
print(np.dot(a,b))