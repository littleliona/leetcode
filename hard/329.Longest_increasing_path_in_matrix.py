class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        def dfs(i,j):
            if not dp[i][j]:
                val = matrix[i][j]
                dp[i][j] = 1 + max(
                        dfs(i-1, j) if i and val > matrix[i-1][j] else 0,
                        dfs(i, j-1) if j and val > matrix[i][j-1] else 0,
                        dfs(i+1, j) if i+1 < M and val > matrix[i+1][j] else 0,
                        dfs(i, j+1) if j+1 < N and val > matrix[i][j+1] else 0)

            return dp[i][j]

        if not matrix or not matrix[0]:
            return 0

        M = len(matrix)
        N = len(matrix[0])

        dp = [[0 for _ in range(N)] for _ in range(M)]

        return max(dfs(i,j) for i in range(M) for j in range(N)) 
if __name__ == '__main__':
    s = Solution()
    a = s.longestPalindrome("babad")
    print(a)
