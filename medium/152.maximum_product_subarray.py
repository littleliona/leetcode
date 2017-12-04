class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #每次更新最大值（正数）最小值（负数）
        #如果当前元素大于连续乘积，更新起点
        maximum=big=small=nums[0]
        for n in nums[1:]:
            big, small=max(n, n*big, n*small), min(n, n*big, n*small)
            maximum=max(maximum, big)
        return maximum


                
s = Solution()
a = s.maxProduct([2,3,-2,4])
print(a)
