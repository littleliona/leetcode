class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo, hi = 0, len(nums) - 1
        
        while lo <= hi:   
            mid = (lo + hi) / 2
            if nums[mid] == target:
                return mid
            
            if nums[0] <= nums[mid]:
                # left doesn't include the part rotated, which is sorted
                if target >= nums[lo] and target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                # right is completely the part rotated, which is sorted
                if target <= nums[hi] and target > nums[mid]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        
        return -1

        #mine
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            if nums[low] == target:
                return low
            if nums[low] > target:
                low = low + 1
            else:
                if nums[mid] < target and nums[high] < target:
                    low = low + 1
                elif nums[mid] < target and nums[high] >= target:
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid - 1


        if low < len(nums) and nums[low] == target:
            return low

        return -1

        
s = Solution()
a = s.search([8,9,2,3,4], 9)
print(a)