class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        matrix_row = len(matrix)
        matrix_column = len(matrix[0]) if matrix else 0

        #同一连线上的点，坐标x+y都相等
        #偶数次沿右上方向运动，奇数次沿左下方向运动
        #循环的次数等于矩阵的row＋column－1
        for i in range(matrix_row+matrix_column):
            if i%2 == 0:
                row = i if i < matrix_row else matrix_row-1
                column = i - row
                while row >=0 and column < matrix_column:
                    res.append(matrix[row][column])
                    row -= 1
                    column += 1

            else:
                column = i if i < matrix_column else matrix_column-1
                row = i - column
                while column >= 0 and row < matrix_row:
                    res.append(matrix[row][column])
                    column -= 1
                    row += 1

        return res

s = Solution()
a = s.findDiagonalOrder([[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]])
print(a)     

        

