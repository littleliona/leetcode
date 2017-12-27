class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = water = min_height = 0
        r = len(height) - 1

        while l < r:
            while l < r and height[l] <= min_height:
                water += min_height - height[l]
                l += 1
            while l < r and height[r] <= min_height:
                water += min_height - height[r]
                r -= 1

            min_height = min(height[l], height[r])

        return water

s = Solution()
a = s.longestValidParentheses(')()())')
print(a)
