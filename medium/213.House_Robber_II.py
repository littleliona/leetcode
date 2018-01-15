class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        if len(nums) <= 3:
            return max(nums)
        
        

        return max(self.rob_1(nums[:-1]),self.rob_1(nums[1:]))
    
    def rob_1(self,nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        for i in range(1,len(nums)):
            if i == 1:
                nums[i] = max(nums[i],nums[i-1])
            else:
                nums[i] = max(nums[i-2]+nums[i],nums[i-1])
            

        return nums[-1]

s = Solution()
a = s.rob([2,7,9,3,1])
print(a)