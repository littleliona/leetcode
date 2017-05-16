class Solution(object):
    def wordPattern(self, pattern, str_):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        L = str_.split()
        if len(L) != len(pattern):
            return False
        return len(set(zip(pattern,L))) == len(set(pattern)) == len(set(L))

s = Solution()
a = s.wordPattern('syys','a abc abc a')
print(a)
    


        





