class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        self.res = []

        self.findNsum(nums, target, 4, [])
        return self.res

    def findNsum(self, nums, target, N, path):

        if len(nums) < N or N < 2 or nums[0]*N > target or nums[-1]*N < target:
            return 

        if N == 2:
            left, right = 0, len(nums) - 1
            while left <  right:
                s = nums[left]+nums[right]
                if s == target:
                    self.res.append(path+[nums[left]]+[nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif s < target:
                    left += 1
                elif s > target:
                    right -= 1

        else:
            for i in range(len(nums) - N + 1):
                if i == 0 or nums[i-1] < nums[i]:
                    self.findNsum(nums[i+1:], target - nums[i], N -1, path+[nums[i]])


s = Solution()
a = s.fourSum([-1,0,1,2,-1,-4],-1)
print(a)
