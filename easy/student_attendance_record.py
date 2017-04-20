class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if not (s.count('A')>1 or "LLL" in s):
            return True
        else:
            return False

s = Solution()
a = s.checkRecord("PPALLL")
print(a)