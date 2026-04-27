class node:
    def __init__(self,value):
        self.data = value
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None
        #no of linkedlist
        self.n = 0
    def __str__(self):
        curr = self.head
        result = ""
        while curr != None:
            result = result + str(curr.data) + "->"
            curr = curr.next 
        return result[:-2]
    def __len__(self):
        return self.n
    def insert_head(self,value):
        new_head = node(value)
        new_head.next = self.head
        self.head = new_head

        self.n += 1 
    def insert_tail(self,value):
        new_tail = node(value)
        if self.head == None:
            self.head = new_tail
            self.n += 1

        curr = self.head
        while curr.next != None:
            curr = curr.next
        
        curr.next = new_tail
        self.n += 1
    def insert(self,index,value):
        curr = self.head
        for i in range(self.n,index,-1):
            
l = LinkList()
l.insert_head(34)
l.insert_head(34)
l.insert_tail(69)
l.insert_head(34)
l.insert_head(34)
print(l)
print(len(l))