class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #usual way
        if n <= 0:
            return False
        while n%3 ==0:
            n = n//3
            
        return True if n ==1 else False

        #one_line 1162261467--maximum power of three
        return n > 0 and 1162261467 % n == 0


        
    
s = Solution()
a = s.isPowerOfThree(27)
print(a)