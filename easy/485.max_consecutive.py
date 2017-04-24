class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        max_a = 0

        for num in range(len(nums)):
        	if nums[num] == 1:
        		count += 1
        	if nums[num] ==0 or num == len(nums)-1:
        		if max_a < count:
        			max_a = count
        			count = 0
        				

        print(max_a)
        		




s = Solution()
s.findMaxConsecutiveOnes([1,1,1,1,1,1,1,1])