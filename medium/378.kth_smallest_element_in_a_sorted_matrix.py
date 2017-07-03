import bisect
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        #binary_search
        #从矩阵最小值（左上角）和最大值（右上角）开始
        #首先找到中间值，然后遍历矩阵每一行，找到中间值插入的位置（即比中间值大的第一个数索引－1）
        #求和找到中间值是矩阵第几小的数，与k进行比较
        #如果比k小，说明中间值小，调整下界
        #如果大于等于k，调整上界
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo<hi:
            mid = (lo+hi)//2
            if sum(bisect.bisect_right(row, mid) for row in matrix) < k:
                lo = mid+1
            else:
                hi = mid
        return lo

        #sort
        res = []
        for row in matrix:
            res += row

        res.sort()
        return res[k-1]
    

s = Solution()
a = s.kthSmallest([[ 1, 5, 9],[10, 11, 13],[12, 13, 15]], 8)
print(a)     

        

