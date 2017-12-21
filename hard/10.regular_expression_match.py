class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # p 正则  s--需要匹配的式子
        dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        
        dp[0][0] = True # p and s are both empty string

        # corner case p is not empty string but s is
        # if p[i] 为 *， 那么dp[i+1][0] = dp[i-1][0]
        for i in range(1, len(p)):
            dp[i + 1][0] = dp[i - 1][0] and p[i] == '*'

        for i in range(len(p)):
            for j in range(len(s)):
                if p[i] == '*':
                    # dp[i-1][j+1] --> s[i-1] 不出现
                    # dp[i][j+1] --> s[i-1]出现一次
                    dp[i + 1][j + 1] = dp[i - 1][j + 1] or dp[i][j + 1]
                    if p[i - 1] == s[j] or p[i - 1] == '.':
                        #dp[i+1][j] --> s[i-1]出现多次
                        dp[i + 1][j + 1] |= dp[i + 1][j]
                else:
                    dp[i + 1][j + 1] = dp[i][j] and (p[i] == s[j] or p[i] == '.')
        return dp[-1][-1]

s = Solution()
a = s.isMatch('aaab','a*b')
print(a)
