class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #tricky part
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return True
            while l < mid and nums[l] == nums[mid]: # tricky part
                l += 1
            # the first half is ordered
            if nums[l] <= nums[mid]:
                # target is in the first half
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # the second half is ordered
            else:
                # target is in the second half
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False

        #mine
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return True
            if nums[low] == target:
                return True
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
            return True

        return False

        

        
s = Solution()
a = s.search([1, 3], 0)
print(a)