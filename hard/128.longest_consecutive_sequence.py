class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #fast
        #first get the start(check if x-1 in set)
        #then check x+1,x+2...,stop at x+n not in set, find the max length
        nums = set(nums)
        best = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                best = max(best, y - x)
        return best

        #mine
        if not nums:
            return 0
        nums = list(set(nums))
        nums.sort()
        count = 1
        res = 1
        for i in range(len(nums)-1):
            if nums[i] + 1 == nums[i+1]:
                count += 1
            else:
                count = 1
            res = max(res,count)

        return res


s = Solution()
a = s.longestConsecutive([1,2,0,1])
print(a)