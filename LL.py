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
l = ll([1])
l.append(34)
l.add_after(44,34)
l.add_before(24,34)
l.left_append(14)
l.left_append(14)
l.left_append(14)
l.remove(44)
l.remove(24)
l.repr()