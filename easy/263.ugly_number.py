class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        #mine -- change
        if num > 0:
            for i in [2,3,5]:
                while num % i == 0:
                    num /= i

        return num == 1

        #easy
        
        for p in 2, 3, 5:
            while num % p == 0<num:
                num /= p
        return num == 1




s = Solution()
a = s.isUgly(14)
print(a)