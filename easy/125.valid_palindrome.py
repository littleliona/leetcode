import string
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        L = list(string.ascii_lowercase)+list('1234567890')
        s = s.lower()
        for char in set(s):
            if char not in L:
                s = s.replace(char,'')

        
        return s[::-1] == s


        
s = Solution()
a = s.isPalindrome("a.")
print(a)



