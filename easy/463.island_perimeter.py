class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        for m in range(0,len(grid)):
            for n in range(0,len(grid[m])):
                if grid[m][n] == 1:
                    res += 4
                    if m>0 and grid[m-1][n]==1:
                        res -= 2 
                    if n>0 and grid[m][n-1]==1:
                        res -= 2
                        

        print(res)







s = Solution()
s.islandPerimeter([[1],[0]])