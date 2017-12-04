class Solution:
    def largestRectangleArea(self, height):
        #维持一个非递减height的stack，放入index
        #height最后添0为了弹空stack
        # Before adding a new building pop the building who is taller than the new one. 
        # The building popped out represent the height of a rectangle with the new building as the right boundary 
        # and the current stack top as the left boundary.
        height.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(height)):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
            
        height.pop()
        return ans

                
s = Solution()
a = s.largestRectangleArea([4,5,3])
print(a)
