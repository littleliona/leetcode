
class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        
        row = len(matrix)
        column = len(matrix[0])

        dp = [[0 for _ in range(column)] for _ in range(row)]
        res = 0
        for i in range(row):
            for j in range(column):
                dp[i][j] = int(matrix[i][j])
                if i and j and dp[i][j]:
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]) + 1
                res = max(dp[i][j],res)

        return res * res
