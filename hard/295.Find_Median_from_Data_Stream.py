from heapq import * 
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.large = []  # min heap
        self.small = []  # max heap
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if len(self.large) == len(self.small):
            heappush(self.large, -heappushpop(self.small, -num))

        else:
            heappush(self.small, -heappushpop(self.large, num))
        

    def findMedian(self):
        """
        :rtype: float
        """

        if len(self.large) == len(self.small):
            return float(self.large[0] - self.small[0]) / 2
        else:
            return float(self.large[0])


        


if __name__ == '__main__':
    s = Solution()

    a = s.addOperators("105",5)
    print(a)