class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        nums.sort()
        

        dp = [[]for i in range(len(nums))]

        for i in range(len(nums)):
            dp[i] = [nums[i]]


        for i in range(1, len(nums)):
            stack = []
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    stack += [dp[j]]

            dp[i] += max(stack,key = len) if stack else []

       
        return max(dp,key = len)



if __name__ == '__main__':
    s = Solution()
    a = s.largestDivisibleSubset([4,8,10,240])
    print(a)
