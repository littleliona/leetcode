import numpy as np
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        #mine
        if r*c == len(nums)*len(nums[0]):
            L = []
            nums = sum(nums,[])
            for row in range(r):
                L.append(nums[c*(row+1)-c:c*(row+1)])
            return L

        return nums
        #easy
        flat = sum(nums, [])
        if len(flat) != r * c:
            return nums
        tuples = zip(*([iter(flat)] * c))
        print(tuples)
        return map(list, tuples)
        #numpy
        try:
            return np.reshape(nums, (r, c)).tolist()
        except:
            return nums


s = Solution()
a = s.matrixReshape([[1,2],[3,4]],2,4)
print(a)