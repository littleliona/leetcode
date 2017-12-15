class Solution:
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        ls = list(s.strip())
        if len(s) == 0:
            return 0

        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['+','-']:
            del ls[0]

        res = 0
        i = 0 

        while i < len(ls) and ls[i].isdigit():
            res = res * 10 + ord(ls[i]) - ord('0')
            i += 1

        return max(-2 ** 31 , min(res * sign, 2**31-1))
        
s = Solution()
a = s.longestPalindrome('pwwkew')
print(a)
