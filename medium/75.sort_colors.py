class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #
        nums.sort()


        #O(n)time O(1)space
        #trace index
        i = j = 0
        for k in xrange(len(nums)):
            v = nums[k]
            nums[k] = 2
            if v < 2:
                nums[j] = 1
                j += 1
            if v == 0:
                nums[i] = 0
                i += 1

s = Solution()
a = s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
print(a)