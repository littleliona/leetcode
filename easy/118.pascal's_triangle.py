class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        #杨辉三角
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]

        L = [[1],[1,1]]
        L1 = []
        for row in range(1,numRows-1):
            L1.append(1)
            for num in range(1,len(L[row])):
                L1.append(L[row][num-1]+L[row][num])
            L1.append(1)
            L.append(L1)
            L1 = []

        return L




s = Solution()
a = s.generate(5)
print(a)