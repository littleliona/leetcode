class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #mine
        if x < 0:
            return False

        return str(x)[::-1] == str(x)

        #no extra space
        if x < 0:
            return False

        ranger = 1
        while x / ranger >= 10:
            ranger *= 10

        while x:
            left = x / ranger
            right = x % 10
            if left != right:
                return False
            
            x = (x % ranger) / 10
            ranger /= 100

        return True


s = Solution()
a = s.merge([],0,[1],1)
print(a)



