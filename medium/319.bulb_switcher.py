import math
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        # bulb is on 如果被执行了奇数次操作
        # 只有平方数，才会被执行奇数次
        # 所以最后变成了找[1,n]中间有几个平方数
        return int(math.sqrt(n))

        


s = Solution()
a = s.bulbSwitch(9)
print(a)


