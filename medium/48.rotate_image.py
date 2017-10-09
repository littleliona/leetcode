class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        #zip [::-1] upside down and zip to rotate
        A[:] = zip(*A[::-1])

        #by means of L trace the index
        L = []
        row_num = len(matrix)
        col_num = row_num

        for row in matrix:
            L += row


        for i,num in enumerate(L):
            col = col_num - 1 - (i // row_num)
            matrix[i%row_num][col] = num


        return matrix


s = Solution()
a = s.rotate([[1,2,3],[4,5,6],[7,8,9]])
print(a)