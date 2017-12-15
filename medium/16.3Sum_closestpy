class Solution:
    def threeSumClosest(self, num, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """  
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        s = 0
        for i in range(len(nums)-2):
            if i == 0 or nums[i-1] < nums[i]:
                l, r = i + 1, len(nums) - 1
                while l < r:        
                    s = nums[i]  + nums[l] + nums[r]
                    if s == target:
                        return s
                
                    if abs(s - target) < abs(res - target):
                        res = s
                    
                    if s > target:
                        r -= 1
                    if s < target:
                        l +=1
        return res

s = Solution()
a = s.threeSum([-1,0,1,2,-1,-4])
print(a)
