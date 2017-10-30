class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums:
            return 0
        ###math problem, each number can be positive or negtive
        ### sum(nums) = P(positive) + P(negtive)
        ### P(positive) - P(negtive) = Target
        ### P(positive) + P(negtive) + P(positive) - P(negtive) = Target + sum(nums)
        ### 2P(positive) = Target + sum(nums)
        allsum = sum(nums)
        if allsum < abs(S) or (allsum - S) % 2 == 1:
            return 0
        subset_target = (allsum + S) // 2
        
        dp = [0 for i in range(subset_target + 1)]
        dp[0] = 1
        for n in nums:
            for i in range(subset_target, n - 1, -1):
                dp[i] += dp[i - n]
        
        return dp[subset_target]



s = Solution()
a = s.findTargetSumWays([1, 1, 1, 1, 1], 3)
print(a)
