class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        #mine
        if not matrix or not matrix[0]:
            return False
        column = len(matrix[0])
        for row in matrix:
            if target == row[0] or target == row[column-1]:
                return True
            if target > row[0] and target < row[column-1]:
                if target in row:
                    return True



        return False

        #binary search
        if not matrix or target is None:
            return False

        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1
        
        while low <= high:
            mid = (low + high) / 2
            num = matrix[mid / cols][mid % cols]

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False




s = Solution()
a = s.searchMatrix([[1, 3, 5, 7],[10, 11, 16, 20],[23, 30, 34, 50]], 3)
print(a)