class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        #space O(m+n) 
        row_num = len(matrix)
        column_num = len(matrix[0])

        L = []
        for row in matrix:
            L += row

        for i,num in enumerate(L):
            if num == 0:
                for column in range(column_num):
                    matrix[i//column_num][column] = 0
                for row in range(row_num):
                    matrix[row][i%column_num] = 0

        return matrix

        #space O(n)
        height = len(matrix)
        if(height ==0): return
        width = len(matrix[0])
        for i in range(height):
            for j in range(width):
                if matrix[i][j] == 0:
                    for tmp in range(height):
                        if matrix[tmp][j] != 0:
                            matrix[tmp][j] = 'a'
                    for tmp in range(width):
                        if matrix[i][tmp] != 0: 
                            matrix[i][tmp] = 'a'

        for i in range(height):
            for j in range(width):
                if matrix[i][j] == 'a':
                    matrix[i][j] = 0


s = Solution()
a = s.setZeroes([[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]])
print(a)