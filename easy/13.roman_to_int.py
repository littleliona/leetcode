class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_ = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        z = 0
        for i in range(len(s)-1):
        	if dict_[s[i]]< dict_[s[i+1]]:
        		z -= dict_[s[i]]
        	else:
        		z += dict_[s[i]]
        z+=dict_[s[-1]]
        return z

       	

s = Solution()
a = s.arrayPairSum([1,4,3,2])
print(a)