class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
       
        res = 0
        nums = self.radixsort(nums)
        for i in range(1,len(nums)):
            res = max(res, nums[i] - nums[i-1])
        
        return res

    def radixsort(self,nums):
        for k in range(10):
            s = [[] for _ in range(10)]
            for num in nums:
                s[num/(10**k)%10].append(num)

            nums = [a for b in s for a in b]

        return nums

