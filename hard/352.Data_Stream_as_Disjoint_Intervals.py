# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

import heapq
class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.interval = []

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        heapq.heappush(self.interval,(val,Interval(val,val)))
        

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        stack = []
        while self.interval:
            val, node = heapq.heappop(self.interval)
            if not stack:
                stack.append((val,node))
            else:
                _,pre = stack[-1]
                if pre.end + 1 >= node.start:
                    pre.end = max(pre.end,node.end)
                else:
                    stack.append((val,node))
        self.interval = stack
        return list(map(lambda x:x[1],stack))

if __name__ == '__main__':
    s = Solution()
    a = s.longestPalindrome("babad")
    print(a)
