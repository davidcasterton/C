import math
import random

class RandomizedSet:

    def __init__(self):
        self._set = set()

    def insert(self, val: int) -> bool:
        res = True
        if val in self._set:
            res = False
        self._set.add(val)
        return res

    def remove(self, val: int) -> bool:
        res = False
        if val in self._set:
            res = True
            self._set.remove(val)
        return res

    def getRandom(self) -> int:
        index = math.floor(random.random() * len(self._set))
        return 0 if not self._set else list(self._set)[index]




# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
