import math
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        #等差数列求和公式，然后一元二次解方程
        return int((-1+math.sqrt(1+4*2*n))/2)


s = Solution()
a = s.arrangeCoins(10)
print(a)