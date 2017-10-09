class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0]*n for _ in range(n)]
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        d = 0
        y, x = 0, 0
        for i in range(1, n*n+1):
            matrix[x][y] = i
            dx, dy = directions[d % 4]
            if -1 < y+dy < n and -1 < x+dx < n and matrix[x+dx][y+dy] == 0:
                y, x = y+dy, x+dx
            else:
                d += 1
                dx, dy = directions[d % 4]
                y, x = y+dy, x+dx
        return matrix


s = Solution()
a = s.generateMatrix(3)
print(a)