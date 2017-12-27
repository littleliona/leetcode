class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len_1 = len(word1)+1
        len_2 = len(word2)+1

        dp = [[0 for _ in range(len_2)] for _ in range(len_1)]

        for i in range(len_1):
            dp[i][0] = i

        for j in range(len_2):
            dp[0][j] = j

        for i in range(1, len_1):
            for j in range(1, len_2):
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+(word1[i-1]!=word2[j-1]))

        return dp[-1][-1]


s = Solution()
a = s.longestValidParentheses(')()())')
print(a)
