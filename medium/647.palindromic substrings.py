class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = len(s)
        for i in range(len(s)-1):
        	for j in range(i+2,len(s)+1):
        		s_ = s[i:j]
        		if s_ == s_[::-1]:
        			print(s_)
        			count += 1



        return count

        
        



s = Solution()
a = s.countSubstrings("aaa")
print(a)