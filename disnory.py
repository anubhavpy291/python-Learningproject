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
                new_hash_value = self.reHash_fun(hash_value)
                while self.sloth[new_hash_value] != None and self.sloth[new_hash_value] != key:
                    new_hash_value = self.reHash_fun(new_hash_value)
                if self.sloth[new_hash_value] == None:
                    self.data[new_hash_value] = value
                    self.sloth[new_hash_value] = key
                else:
                    self.data[new_hash_value] = value
    def __setitem__(self, key, value):
        self.put(key,value)
    def reHash_fun(self,oldHash):
        return (oldHash + 1) % self.size
    def get(self,key):
        starting_hash = self.hash_fun(key)
        current_hash = starting_hash
        while self.sloth[current_hash] != None:
            if self.sloth[current_hash] == key:
                print(self.data[current_hash])
                break
            current_hash = self.reHash_fun(current_hash)
            if current_hash == starting_hash:
                break
    def __str__(self):
        for i in range(len(self.sloth)):
            if self.sloth[i] != None:
                print(self.sloth[i],":",self.data[i],end=", ")

        return ""
D = disnory(5)
D.put("python",67)
D.put("csharp",69)
D.put("python",69)
D["js"] = 55
print(D.data)
print(D.sloth)
D.get("js")
print(D)