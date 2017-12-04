class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.dict[key] = val
        

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        length = len(prefix)
        value = 0
        for key,value in self.dict.items():
            if key[:length] == prefix:
                sum_ += value


        return sum_




obj = MapSum()
obj.insert(key,val)
param_2 = obj.sum(prefix)
print(param_2)