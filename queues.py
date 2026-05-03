class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class queues:
    def __init__(self):    
        self.front = None
        self.rear = None
    def enqueue(self,value):
        node = Node(value)
        if self.rear == None:
            self.front = node
            self.rear = self.front
        else:
            self.rear.next = node
            self.rear = node
    def denqueue(self):
        if self.front == None:
            return 'empty'
        else:
            self.front = self.front.next
    def prints(self):
        curr = self.front
        res = ''
        while curr != None:
            res = res + str(curr.data) + " "
            curr = curr.next
        print(res,)
    def isempty(self):
        return self.front == None
    def rear_data(self):
        if self.rear == None:
            return "empty"
        return self.rear.data
    def front_data(self):
        if self.front == None:
            return "empty"
        return self.front.data
    def size(self):
        curr = self.front
        i = 0
        while curr != None:
            i += 1
            curr = curr.next
        return i
    
q = queues()
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.denqueue()
q.prints()
print(q.rear_data())
print(q.front_data())
print(q.size())