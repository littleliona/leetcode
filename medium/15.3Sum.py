class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        s = 0
        for i in range(len(nums)-2):
            if i == 0 or nums[i-1] < nums[i]:
                l, r = i + 1, len(nums) - 1
                while l < r:        
                    s = nums[i]  + nums[l] + nums[r]
                    if s == 0:
                        res.append([nums[i],nums[l],nums[r]])
                        while l < r and nums[l] == nums[l+1]: l += 1
                        while l < r and nums[r] == nums[r-1]: r -= 1
                        l += 1; r -= 1
                    elif s < 0:
                        l += 1
                    elif s > 0:
                        r -= 1
        return res

s = Solution()
a = s.threeSum([-1,0,1,2,-1,-4])
print(a)
