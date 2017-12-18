class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.res = []

        self.dfs(s, [])
        
        return self.res 

    def dfs(self, s, path):
        if s == '':
            self.res.append(path)
            return

        for i in range(1,len(s)+1):
            if s[:i]== s[:i][::-1]:
                self.dfs(s[i:], path+[s[:i]])

s = Solution()
a = s.partition('aab')
print(a)
