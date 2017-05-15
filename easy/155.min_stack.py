class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.L = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        #use tuple to push--easy to get the min value
        #(a1,a2) -- a1 - value a2 - min value
        min_ = self.getMin()
        if min_== None or x< min_:
            min_ = x
        self.L.append((x,min_))
        

    def pop(self):
        """
        :rtype: void
        """
        return self.L.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if self.L:
            return self.L[-1][0]
        return None
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.L:
            return self.L[-1][1]
        return None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()