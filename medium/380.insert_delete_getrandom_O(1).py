import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        #list store number
        #dic trace index
        self.l = []
        self.d = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.d:
            return False
        self.d[val] = len(self.l)
        self.l.append(val)
        return True
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        #to satisfy O(1), swap with the last element
        if val not in self.d:
            return False
        i, newVal = self.d[val], self.l[-1]
        self.l[i], self.d[newVal] = newVal, i
        del self.d[val]
        self.l.pop()
        return True
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.l)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

s = Solution()
a = s.generateMatrix(3)
print(a)