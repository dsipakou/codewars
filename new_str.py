class RandomizedSet:

    def __init__(self):
        self.size = 0
        self.l = []
        self.d = {}
        

    def insert(self, val: int) -> bool:
        if val not in self.d:
            self.d[val] = len(self.l)
            self.l.append(val)
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.d:
            el = self.l[-1]
            index = self.d[val]
            self.l[index], self.d[el] = el, index
            self.l.pop()
            del self.d[val]
            return True
        return False
        

    def getRandom(self) -> int:
        return random.choice(self.l)
        
