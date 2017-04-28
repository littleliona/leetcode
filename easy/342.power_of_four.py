class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        #mine
        if num > 0:
            L = list(bin(num))
            L.pop(0)
            if L[1] == '1' and L.count('0')%2 == 0 and L.count('1') == 1:
                return True

        return False


        #one-line 
        #1010101010101010101010101010101 (1431655765)
        #num &(num-1) == 0 make sure it is the power of two
        
        return num > 0 and num &(num-1) == 0 and num & 1431655765== num




s = Solution()
a = s.isPowerOfFour(1)
print(a)