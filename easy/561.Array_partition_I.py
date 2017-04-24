class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum(nums[::2])

       	

s = Solution()
a = s.arrayPairSum([1,4,3,2])
print(a)