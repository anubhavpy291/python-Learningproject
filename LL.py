class node:
    def __init__(self,value):
        self.next = None
        self.data = value

class ll:
    def __init__(self,l=list):
        self.head = None
        for i in l:
            self.append(i)
    def append(self,value):
        new_node = node(value)
        curr = self.head
        if curr == None:
            self.head = new_node
            return
        
        while curr.next != None:
            curr = curr.next
        curr.next = new_node
    def left_append(self,value):
        new_node = node(value)
        curr = self.head
        if curr == None:
            self.head = new_node
            return
        new_node.next = curr
        self.head = new_node
        
    def repr(self):
        curr = self.head
        while curr != None:
            print(curr.data,"->",end="")
            curr = curr.next
    def add_after(self,data,after):
        new_node = node(data)
        curr = self.head
        while curr != None:
            if curr.data == after:
                break
            curr = curr.next
        if curr != None:
            new_node.next = curr.next
            curr.next = new_node
        else:
            print("invalid after")
    def add_before(self,value,before):
        new_node = node(value)
        curr = self.head
        while curr != None:
            if curr.next.data == before:
                
                break
            curr = curr.next    
        if curr != None:
            new_node.next = curr.next
            curr.next = new_node
        else:
            print("before not found")
    def remove(self,data):
        curr = self.head
        while curr.next != None:
            if curr.next.data == data:
                break
            curr = curr.next
        if curr != None:
            curr.next = curr.next.next  
        else:
            print("node not found") 
    def reverse(self):
        curr = self.head
        prev = None
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev


def sortndmerge(ll1,ll2):
    curr = node(0)
    l1 = ll1.head
    l2 = ll2.head
    while l1 != None or l2 != None:
        
        if l1.data <= l2.data:
            curr.data = l1.data
            new_node = node(0)
            curr.next = new_node
            new_node.data = l2.data 
            print(curr.data)
            curr = curr.next
            
            
        l1 = l1.next
        l2  = l2.next
    
l = ll([1])
L = ll([2,3,4])
l.append(34)
l.add_after(44,34)
l.add_before(24,34)
l.left_append(14)
l.left_append(14)
l.left_append(14)
l.remove(44)
l.remove(24)
l.reverse()
l.repr()