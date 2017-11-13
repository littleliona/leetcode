class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0 for i in range(target+1)]
        dp[0] = 1
        for v in range(1,target+1):
            for i in range(len(nums)):
                if v >= nums[i]:
                    dp[v] += dp[v-nums[i]]


        return dp[target]



s = Solution()
a = s.combinationSum4([1, 2, 3], 4)
print(a)
