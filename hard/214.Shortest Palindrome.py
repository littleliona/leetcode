class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        A=s+"*"+s[::-1]
        cont=[0]
        for i in range(1,len(A)):
            index=cont[i-1]
            while(index>0 and A[index]!=A[i]):
                index=cont[index-1]
            cont.append(index+(1 if A[index]==A[i] else 0))
        
        return s[cont[-1]:][::-1]+s

s = Solution()
a = s.shortestPalindrome('aacecaaa')
print(a)
