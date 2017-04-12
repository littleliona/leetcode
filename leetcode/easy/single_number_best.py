class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print(2*sum(set(nums))-sum(nums))
        		

s = Solution()
s.singleNumber([1,1,2,2,3])