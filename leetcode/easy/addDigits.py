class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num==0:
            return 0
        else:
            if num%9 ==0:
                return 9
            else:
                return num%9

        	
        	


s = Solution()
s.addDigits(9)