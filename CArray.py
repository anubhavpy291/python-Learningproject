import ctypes

class MyArray:
    def __init__(self):
        # mazimun item can store
        self.size = 1
        # current storeed item 
        self.n = 0
        self.A = self.MaArray(self.size)
    def find(self,item):
        for i in range(self.n):
            if(self.A[i] == item):
                return i
            else:
                return "value error"
    def clear(self):
        # mazimun item can store
        self.size = 1
        # current storeed item 
        self.n = 0
    def __delitem__(self, index):
        for i in range(index,self.n-1):
            self.A[i] = self.A[i + 1]
        self.n -= 1
    def insert(self, index, item):
        if self.size == self.n:
            self.__resize(self.size * 2)

        for i in range(self.n,index,-1):
             self.A[i] = self.A[i - 1]
        self.A[index] = item
        self.n += 1

    def pop(self):
        if self.n == 0:
            print("empty array")
        self.n = self.n - 1
    def __getitem__(self, index):
        if index > self.size:
            return 'Index error'
        return self.A[index]
    def __str__(self):
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','
        return '[' + result[:-1] + ']'
    def __len__(self):
        return self.n
    def MaArray(self,size):
        return (size*ctypes.py_object)()
    def append(self,item):
        if self.size == self.n:
            self.__resize(self.size * 2)
        self.A[self.n] = item
        self.n += 1
    def __resize(self,new_size):
        self.size = new_size
        b = self.MaArray(new_size)
        for i in range(self.n):
            b[i] = self.A[i]
        self.A = b
l = MyArray()
l.append("hello")
l.append("hru")
l.append(5)
l.append(7)
print(l)
print(l[2])
print(l.find("hru"))
l.insert(2,"bastard")
print(l)
del l[2]
print(l)