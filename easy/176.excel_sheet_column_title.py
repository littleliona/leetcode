import string
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        L = list(string.ascii_uppercase)
        s = ""
        while n > 26:
            s += L[n%26-1]
            if n%26 == 0:
                n = (n-26)//26
            else:
                n = n//26

        s += L[n%26-1]
        return s[::-1]


        
s = Solution()
a = s.convertToTitle(52)
print(a)



