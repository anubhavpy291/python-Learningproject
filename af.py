class node:
    def __init__(self, value):
        self.data = value
        self.next = None


class stacks:
    def __init__(self):
        self.top = None
        self.n = 0
    def isemoty(self):
        return self.top == None
    def push(self, data):
        nodes = node(data)
        nodes.next = self.top
        self.top = nodes
        self.n += 1
    def pop(self):
        if self.isemoty():
            return 'emoty stake'
        else:
            self.top = self.top.next
            self.n -= 1
    def peak(self):
        if self.isemoty():
            return 'emoty stake'
        else:
            return self.top
    def print(self):
        curr = self.top
        while curr != None:
            data =  curr.data
            curr = curr.next
            print(data)
    def reverse(self):
        
        pre = None
        curr = self.top
        while curr != None:
            next = curr.next
            curr.next = pre 
            pre = curr 
            curr = next
        self.top = pre 
    def reverce_str(self,strs):
        result = ''
        curr = self.top
        for i in strs:
            self.push(i)
        while curr != None:
            result = result + curr.data
            curr = curr.next
        print(result)
s = stacks()
def textEditor(texts,operation):
    u = stacks()
    r = stacks()
    for i in texts:
        u.push(i)
    for i in operation:
        if i == 'u':
            data = u.peak()
            u.pop()
            r.push(data)
            
        elif i == 'r':
            data = r.peak()
            r.pop()
            u.push(data)
            
        else:
            print("invalid opreator")
    res = ""
    curr = u.top
    while curr != None:
        res = str(curr.data) + res
        curr = curr.next
    print(res)
    u.print()
s.reverce_str('hello')
s.print()
print("---------------------")
textEditor("anubhav","uuuur")