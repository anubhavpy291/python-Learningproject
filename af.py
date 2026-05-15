class node:
    def __init__(self,key,value):
        self.data = value
        self.key = key
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
            result += str(curr.key)+":"+str(curr.data)+"->"
            curr = curr.next 
        return result[:-2]
    def __len__(self):
        return self.n
    def clear_head(self):
        if self.head == None:
            print("empty ListList")
            return
        new_head = self.head.next
        self.head = None
        self.head = new_head
        self.n  = self.n - 1
    def add(self,key,value):
        new_tail = node(key,value)
        if self.head == None:
            self.head = new_tail
            self.n  = self.n + 1
            return
        curr = self.head
        while curr.next != None:
            curr = curr.next
        
        curr.next = new_tail
        self.n  = self.n + 1
    
    def clear(self):
        self.head =  None
        self.n = 0
    def remove(self,key):
        if self.head == None:
            print("empty ll")
            return
        if self.head.key == key:
            self.clear_head()
            return
        curr = self.head
        while curr != None:
            if curr.next.key == key:
                curr.next = curr.next.next
                self.n = self.n - 1
                break
            curr = curr.next
    def search(self,key):
        pos = 0
        curr = self.head 
        while curr != None:
            if curr.key == key:
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

l = LinkList()
l.add("hii",45)
l.add("hii",45)
l.add("hii",45)
l.add("hii",45)
print(l)

class disconry:
    def __init__(self,capicity):
        self.capicity = capicity
        self.size = 0
        self.bucket = self.make_Array(self.capicity)
    def make_Array(self,capicity):
        l = []
        for i in range(capicity):
            l.append(LinkList())
        return l