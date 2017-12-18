class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        #method_
        ret = []
        while matrix:
            ret += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    ret.append(row.pop())
            if matrix:
                ret += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ret.append(row.pop(0))
        return ret 

        #method_mine
        if not matrix:
            return []
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        
        res = []

        m = len(matrix)
        n = len(matrix[0])

        x,y = 0,0
        i = 0
        d = 0

        while i < m*n:
            res.append(matrix[x][y])
            matrix[x][y] = 'a'
            dx,dy = directions[d % 4]

            if -1 < x+dx < m and -1 < y+dy < n and matrix[x+dx][y+dy] != 'a':
                x += dx
                y += dy

            else:
                d += 1
                dx, dy = directions[d % 4]
                x += dx
                y += dy
            i += 1

        return res  
