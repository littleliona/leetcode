class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #二分查找
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) / 2
            #sorted array
            #如果mid是偶数，xor 1是奇数
            #如果mid是奇数，xor 1是偶数
            if nums[mid] == nums[mid ^ 1]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]



     
s = Solution()
a = s.singleNonDuplicate([1,1,2,2,3])
print(a)
        

