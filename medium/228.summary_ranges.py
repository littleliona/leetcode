class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []

        stack = [nums[0]]
        res = []
        for num in nums[1:]:
            if num == stack[-1] + 1:
                stack.append(num)
            else:
                if len(stack) == 1:
                    res.append(str(stack.pop()))
                else:
                    res.append(str(stack[0])+'->'+str(stack[-1]))
            stack = []

        return res 


s = Solution()
a = s.longestValidParentheses(')()())')
print(a)
