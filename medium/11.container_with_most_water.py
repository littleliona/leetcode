class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left ,right = 0, len(height)-1
        
        max_area = 0 
        while left < right:
            area = min(height[left],height[right]) * (right - left)
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


s = Solution()
a = s.fourSum([-1,0,1,2,-1,-4],-1)
print(a)
