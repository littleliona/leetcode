class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        #method_fast
        if not matrix:
            return False

        m = len(matrix)
        n = len(matrix[0])
        
        row = 0
        col = n-1
        while row < m and col >= 0:
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                col -= 1
            if matrix[row][col] < target:
                row += 1

        return False
        
        #method_min
        if not matrix or not matrix[0]:
            return False
        
        for row in matrix:
            if row[0] <= target:
                row = set(row)
                if target in row:
                    return True
            else:
                break
        
        return False
            


s = Solution()
a = s.longestValidParentheses(')()())')
print(a)
