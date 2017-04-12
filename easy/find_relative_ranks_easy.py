class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        sort = sorted(nums)[::-1]
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + map(str, range(4, len(nums) + 1))
        return map(dict(zip(sort, rank)).get, nums)



s = Solution()
print(s.findRelativeRanks([7,2,4,8,5,9]))