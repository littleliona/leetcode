class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def dfs(s, part, path, res):
            if part == 4:
                if s == '':
                    res.append(path[:-1])
                return 

            for i in range(1, 4):
                if i <= len(s):
                    if int(s[:i]) <= 255:
                        dfs(s[i:], part+1, path+s[:i]+'.', res)
                    if s[0] == '0':
                        break
        
        res = []
        dfs(s, 0, '',res)
        return res 
