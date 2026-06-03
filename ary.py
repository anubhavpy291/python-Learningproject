class stacks:
    def __init__(self,size):
        self.top = -1
        self.size = size
        self.stacks = [None] * size
    def push(self,data):
        if self.top == self.size -1:
            print("overflow ep 1 uncon")
        else:
            self.top += 1
            self.stacks[self.top] = data
    def pop(self):
        if self.top == -1:
            print("emotty")
        else:
            self.top -= 1
    def prints(self):
        for i in range(self.top + 1):
            print(self.stacks[i],end=' ')   
s = stacks(5)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.pop()
s.pop()
s.prints()