class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        #首先计算出给定的n落在几位数的范围内   一位数：9 两位数：2*90 三位数：3*900
        #first -- 该范围内的起始值   digit -- 位数
        #因为是基于0开始的下标，所以首先对n－1
        #n//digit -- 求出对应的数  n％digit -- 求出对应位置的数
        n -= 1
        for digits in range(1, 11):
            first = 10**(digits - 1)
            if n < 9 * first * digits:
                return int(str(first + n//digits)[n%digits])
            n -= 9 * first * digits
      
        

s = Solution()
a = s.findNthDigit(21)
print(a)
    


        





