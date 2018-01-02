class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #easy
        if len(nums)<=1:
            return []
        dic = {}
        for i,num in enumerate(nums):
            if num in dic:
                return [dic[num],i]
            else:
                dic[target-num] = i

        #mine
        n1 = []
        n1[:] = nums
        nums.sort()
        left = 0
        right = len(nums)-1
        while left < right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                if nums[left]!=nums[right]
                    return [n1.index(nums[left]),n1.index(nums[right])]
                else:
                    stack = []
                    for i,num in n1:
                        if num == nums[left]:
                            stack.append(i)
                    return stack
        

        
s = Solution()
a = s.twoSum()
print(a)
