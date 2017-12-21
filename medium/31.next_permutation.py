class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        partition = -1

        for i in range(len(nums)-1,-1,-1):
            if nums[i-1] < nums[i]:
                partition = i-1
                break
                
        if partition == -1:
            nums[:] = nums[::-1]
            return
        
        for j in range(len(nums)-1,-1,-1):
            if nums[j] > nums[partition]:
                break

        nums[partition], nums[j] = nums[j], nums[partition]
        nums[partition+1:] = nums[partition+1:][::-1]

s = Solution()
a = s.nextPermutation([1,2,3])
print(a)
