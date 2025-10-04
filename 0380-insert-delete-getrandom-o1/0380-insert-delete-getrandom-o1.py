class RandomizedSet:

    def __init__(self):
        self.store = set()
        

    def insert(self, val: int) -> bool:
        if val not in self.store:
            self.store.add(val)
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.store:
            self.store.remove(val)
            return True
        return False

            
        

    def getRandom(self) -> int:
        return random.choice(list(self.store))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()