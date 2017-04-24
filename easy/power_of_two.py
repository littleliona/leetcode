class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #usual way
        if n <= 0:
            return False
        while n%2 ==0:
            n = n//2
            
        return True if n ==1 else False

        #one_line 
        return n > 0 and not (n & n-1)
