class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #binary search
        left = 0
        right = len(nums)-1

        while left < right:
            mid = (left+right)/2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid

            if nums[mid] < nums[mid+1]:
                left = mid+1
            else:
                right = mid-1

        return left

        #O(n)
        for i,num in enumerate(nums):
            if i == 0:
                if num > nums[i+1]:
                    return i
            if i == len(nums) - 1:
                if num > nums[i-1]:
                    return i
            else:
                if num > nums[i-1] and num > nums[i+1]:
                    return i




s = Solution()
a = s.findPeakElement([1,2,3,1])
print(a)