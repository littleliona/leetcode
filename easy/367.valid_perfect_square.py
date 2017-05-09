class Solution(object):
    def isPerfectSquare(self, x):
        """
        :type num: int
        :rtype: bool
        """
        #mine
        return num % (num ** 0.5) == 0
        
        #python2
        r = x
        while r*r > x:
            r = (r + x/r) / 2
        return r*r == x



s = Solution()
a = s.isPerfectSquare(14)
print(a)