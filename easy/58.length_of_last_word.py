class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        #mine
        return len(s.split()[-1]) if s.split() else 0

        #same idea -- more fast
        v=s.split()
        if len(v)==0:
            return 0
        else:
            return len(v[-1])
        

s = Solution()
a = s.lengthOfLastWord("a ")
print(a)
    


        





