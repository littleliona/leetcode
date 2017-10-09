class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums, count, n = sorted(nums, reverse=1), 0, len(nums)
        print(nums)
        for i in range(n):
            j, k = i + 1, n - 1
            while j < k:
                # any value x between j...k will satisfy nums[j] + nums[x] > nums[i]
                # and because nums[i] > nums[j] > nums[x] >= 0, they will always satisfy
                # nums[i] + nums[x] > nums[j] and nums[i] + nums[j] > nums[x]
                if nums[j] + nums[k] > nums[i]:
                    count += k - j
                    j += 1
                else:
                    k -= 1
        return count




s = Solution()
a = s.triangleNumber([24,3,82,22,35,84,19])
print(a)