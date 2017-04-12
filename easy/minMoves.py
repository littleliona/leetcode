class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums)-len(nums)*min(nums)

s = Solution()
a = s.minMoves([1,3,5])
print(a)
