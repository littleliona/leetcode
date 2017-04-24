class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        #mine
        L = list(t)
        if len(set(t)-set(s))==1:
        	print(list(set(t)-set(s))[0])
        else:
        	for s1 in s:
        		if s1 in t:
        			L.pop(t.index(s1))
        	
        	print(L)
        #easy
        return chr(reduce(operator.xor, map(ord, s + t)))

        	
        	


s = Solution()
s.findTheDifference("ae","aea")