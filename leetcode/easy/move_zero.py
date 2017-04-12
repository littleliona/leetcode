class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        

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

        print(nums)


s = Solution()
s.moveZeroes([0,0,1])