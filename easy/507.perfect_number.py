import math
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        #mine
        if num <= 1:
            return False
        
        sum_ = num
        i = 1
        while i < math.sqrt(sum_):
            if sum_ % i == 0:
                num -= i
                if i!=1:
                    num -= sum_//i
            i += 1

        return num == 0

        #others
        if num <= 0: return False
        ans, SQRT = 0, int(num ** 0.5)
        ans = sum(i + num//i for i in range(1, SQRT+1) if not num % i)
        if num == SQRT ** 2: ans -= SQRT
        return ans - num == num
        



s = Solution()
a = s.checkPerfectNumber(6)
print(a)
    


        





