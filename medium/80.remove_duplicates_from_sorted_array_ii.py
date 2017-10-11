from collections import Counter
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #easy compare and in-place replace leave beyond the new length
        i = 0
        for n in nums:
            if i < 2 or n > nums[i-2]:
                nums[i] = n
                i += 1
        return i
        
        #mine compare and pop
        i = 0
        count = 1
        while i < len(nums) - 1:
            if nums[i] == nums[i+1]:
                count += 1
                if count > 2:
                    nums.pop(i+1)
                else:
                    i += 1
            elif nums[i] != nums[i+1]:
                count = 1
                i += 1
            

        
        return len(nums)



s = Solution()
a = s.removeDuplicates([1,1,1,2,2,3])
print(a)