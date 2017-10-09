class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #dp
        if not m or not n:
            return 0
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

        #math method
        if not m or not n:
            return 0
        return math.factorial(m+n-2)/(math.factorial(n-1) * math.factorial(m-1))


s = Solution()
a = s.uniquePaths(3,7)
print(a)