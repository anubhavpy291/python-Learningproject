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
            self.n  = self.n + 1
            return
        curr = self.head
        while curr.next != None:
            curr = curr.next
        
        curr.next = new_tail
        self.n  = self.n + 1
    def insert_after(self,after,value):
        new_node = node(value)
        curr = self.head
        while curr != None:
            if curr.data == after:
                break
            curr = curr.next
        if curr != None:
            new_node.next = curr.next
            curr.next = new_node
            self.n  = self.n + 1
        else:
            print("invalid after")
    def clear(self):
        self.head =  None
        self.n = 0
    def clear_head(self):
        if self.head == None:
            print("empty ListList")
            return
        new_head = self.head.next
        self.head = None
        self.head = new_head
        self.n  = self.n - 1
    def clear_tail(self):
        if self.head == None:
            return 'empty ll'
        curr = self.head
        if curr.next == None:
            self.clear_head()
            return
        if curr.next.next != None:
            curr = curr.next
        curr.next = None
        self.n  = self.n - 1
    def remove(self,value):
        if self.head == None:
            print("empty ll")
            return
        if self.head.data == value:
            self.clear_head()
            return
        curr = self.head
        while curr != None:
            if curr.next.data == value:
                curr.next = curr.next.next
                self.n = self.n - 1
                break
            curr = curr.next
    def search(self,value):
        pos = 0
        curr = self.head 
        while curr != None:
            if curr.data == value:
                return pos
            curr = curr.next
            pos = pos + 1
        return 'data not found'
    def __getitem__(self, index):
        curr = self.head
        p = 0
        while curr != None:
            if p == index:
                return curr.data
            curr = curr.next
            p = p +1
        return 'index not found'
    def __delitem__(self, key):
        curr = self.head
        p = 0
        while curr != None:
            if p == key:
                self.remove(curr.data)
            curr = curr.next
            p = p + 1
        return 'data not found'
    def replace_max(self,value):
        curr = self.head
        max = curr
        while curr != None:
            if curr.data > max.data:
                max = curr
            curr = curr.next
        max.data = value

    def odd_number_adder(self):
        curr = self.head
        result = 0
        while curr != None:
            if (curr.data % 2) != 0:
                result = result + curr.data
            curr = curr.next
        return result
    def reverse(self):
        prev = None
        curr = self.head
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
l = LinkList()
l.insert_head(5)
l.insert_tail(2)

l.insert_tail(2)
l.insert_tail(3)
l.insert_tail(4)
l.insert_after(2,67)
print(l.odd_number_adder())

del l[3]
l.replace_max(69)
print(l)
print(l[1])
print(l.search(3))

print(len(l))
l.reverse()
print(l)