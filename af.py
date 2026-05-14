class disnory:
    def __init__(self,size):
        self.size = size
        self.sloth = [None] * self.size
        self.data = [None] * self.size
    def hash_fun(self,key):
        return abs(hash(key)) % self.size
    def put(self, key, value):
        hash_value = self.hash_fun(key)
        if self.sloth[hash_value] == None:
            self.data[hash_value] = value
            self.sloth[hash_value] = key
        else:
            if self.sloth[hash_value] == key:
                self.data[hash_value] = value
            else:
                new_hash_value = self.reHash_fun(self.hash_value)
                while self.sloth[new_hash_value] != None and self.sloth[new_hash_value] != key:
                    new_hash_value = self.reHash_fun(new_hash_value)
                if self.sloth[new_hash_value] == None:
                    self.data[new_hash_value] = value
                    self.sloth[new_hash_value] = key
                else:
                    self.data[new_hash_value] = value
    def reHash_fun(self,oldHash):
        return (oldHash + 1) % self.size
D = disnory(5)
D.put("python",67)
D.put("csharp",69)
D.put("python",69)
print(D.data)
print(D.sloth)