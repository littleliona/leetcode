class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[1 for i in range(n)] for _ in range(m)]

        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i-1 >= 0 and j-1 >= 0:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
                    if i == 0 and j != 0:
                        dp[i][j] = dp[i][j-1]
                    if j == 0 and i != 0:
                        dp[i][j] = dp[i-1][j]
                
        
                
        return dp[-1][-1]


s = Solution()
a = s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
print(a)