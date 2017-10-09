class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        
        for i in range(m):
            for j in range(n):
                if i-1 >= 0 and j-1 >= 0: 
                    grid[i][j] += min(grid[i-1][j] , grid[i][j-1])
                if i-1 < 0 and j != 0:
                    grid[i][j] +=  grid[i][j-1]
                if j-1 < 0 and i != 0:
                    grid[i][j] +=  grid[i-1][j]
        
                
        return grid[-1][-1]


s = Solution()
a = s.minPathSum([[1, 2, 3], [4, 5, 6]])
print(a)