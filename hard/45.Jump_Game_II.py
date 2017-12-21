class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = end = 0
        max_index = 0
        step = 0
        while end < len(nums) - 1:
            
            for i in range(start, end+1):
                max_index = max(max_index, i+nums[i])

            start = end + 1
            end = max_index
            step += 1

        return step 

s = Solution()
a = s.partition('aab')
print(a)
