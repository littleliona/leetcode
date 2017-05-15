class Solution(object):
    def reverse(self, x):
        #-2147483648～2147483647
        """
        :type x: int
        :rtype: int
        """
        #mine
        if x >=0 :
            y = int(str(x)[::-1])
        else:
            y = -int(str(abs(x))[::-1])
            
        if y <= 2147483647 and y >= -2147483648:
            return y
        else:
            return 0


        
s = Solution()
a = s.reverse(2147483648)
print(a)



