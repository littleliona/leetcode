import operator
from functools import reduce 
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """   
        #mine
        if len(s) == len(t):
        	for s_ in set(s):
        		if s.count(s_)!=t.count(s_):
        			return False
        	return True
        else:
        	return False

        #easy
        return sorted(s)==sorted(t)




s = Solution()
a = s.isAnagram("abc","jhg")
print(a)