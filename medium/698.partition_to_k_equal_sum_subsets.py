class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if sum(nums) % k != 0 or len(nums) < k:
            return False
        
        t = [sum(nums) // k] * k
        nums.sort()
        def dfs(i):
            if i<0 : return True
            visited = set()
            for j in range(k):
                if t[j] >= nums[i] and t[j] not in visited:
                    visited.add(t[j])
                    t[j] -= nums[i]
                    if dfs(i-1): return True
                    t[j] += nums[i]

            return False

        return dfs(len(nums)-1)



s = Solution()
a = s.canPartitionKSubsets()
print(a)
