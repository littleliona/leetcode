class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #O(nlogn) binary search
        dp = []

        for num in nums:
            low, high = 0, len(dp) - 1
            while low <= high: 
                mid = low + (high - low) // 2
                if dp[mid] >= num:
                    high = mid - 1 
                else:
                    low = mid + 1

            if low >= len(dp):
                dp.append(num)
            else:
                dp[low] = num

        return len(dp)
        

        #O(n ^ 2)
        if not nums:
            return 0

        dp = [1] * len(nums)
        
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)

s = Solution()
a = s.lengthOfLIS()
print(a)
