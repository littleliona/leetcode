class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums))!=len(nums)


s = Solution()
a = s.containsDuplicate([1,2,3,0,0])
print(a)