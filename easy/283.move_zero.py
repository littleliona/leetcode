class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        #mine
        stack = []
        i = 0
        while i<len(nums):
            if nums[i] == 0:
                stack.append(nums[i])
                nums.pop(i)
            else:
                i+=1
        
        for n in stack:
            nums.append(n)

        #fast
        last0 = 0
        for i in range(0,len(nums)):
            if (nums[i]!=0):
                nums[i],nums[last0] = nums[last0],nums[i]
                last0+=1


s = Solution()
s.moveZeroes([0,0,1])