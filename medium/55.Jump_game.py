class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_index = 0

        for i,num in enumerate(nums):
            if i > max_index:
                return False
            
            max_index = max(max_index, i+num)

        return True

