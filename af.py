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
        return -1
    def __getitem__(self, index):
        curr = self.head
        p = 0
        while curr != None:
            if p == index:
                return curr.data
            curr = curr.next
            p = p +1
        return 'index not found'
    def get_node_at_index(self,nodexindex):
        tmp = self.head
        count = 0
        while tmp is not None:
            if count == nodexindex:
                return tmp
            tmp = tmp.next
            count += 1
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
l.add("df",3)
l.add("ghf",4)
l.add("as",5)

print(l)
print(l.get_node_at_index(0).key)
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
    def put(self,key,value):
        bucketIndex = self.hash_function(key)
        node_index = self.get_node_index(bucketIndex,key)
        print(bucketIndex,node_index)
        if node_index == -1:
            self.bucket[node_index].add(key,value)
            self.size += 1

        else:
            node = self.bucket[bucketIndex].get_node_at_index(node_index)
    def get_node_index(self,bucketindex,key):
        node_index = self.bucket[bucketindex].search(key)
        return node_index
    def hash_function(self,key):
        return abs(hash(key)) % self.capicity
    
d = disconry(5)
d.put("ls",23)
d.put("ls",233)
d.put("lds",23)
d.put("las",23)
d.put("lfs",23)