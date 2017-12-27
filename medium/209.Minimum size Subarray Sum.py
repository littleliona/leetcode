class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        total = left = 0
        min_length = len(nums) + 1
        for right, num in enumerate(nums):
            total += num
            while total >= s:
                min_length = min(min_length, right - left + 1)
                total -= nums[left]
                left += 1

        return min_length





s = Solution()
a = s.longestValidParentheses(')()())')
print(a)
