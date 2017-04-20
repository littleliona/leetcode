class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #mine
        return sum(list(range(len(nums)+1)))-sum(nums)
        ### 利用首项加末项 ＊ 项数／2
        n = len(nums)
        return n * (n+1) / 2 - sum(nums)


s = Solution()
a = s.missingNumber([0,1,2])
print(a)