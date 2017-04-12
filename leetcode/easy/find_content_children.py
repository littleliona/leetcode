class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        
        g.sort()
        s.sort()
        i = 0
        j = 0

        while(i<len(g) and j<len(s)):
            if g[i] <= s[j]:
                i+=1
            j+=1

        return i

s = Solution()
a = s.findContentChildren([10,9,8,7],[5,6,7,8])
print(a)