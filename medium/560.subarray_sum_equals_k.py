from collections import Counter
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = sums = 0
        cnt = Counter()
        #cnt 前n项和出现的个数
        for num in nums:
            cnt[sums] += 1
            sums += num
            ans += cnt[sums - k]

        return ans


s = Solution()
a = s.subarraySum([1,1,1],2)
print(a)