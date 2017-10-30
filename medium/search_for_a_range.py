class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #easy
        start = self.binary_search(nums, target-0.5)
        if not target in nums[start:start+1]:
            return [-1, -1]
        #to get the right position for the edge case
        nums.append(0)
        end = self.binary_search(nums, target+0.5)-1
        return [start, end]

    def binary_search(self, arr, target):
        start, end = 0, len(arr)-1
        while start < end:
            mid = (start+end)//2
            if target < arr[mid]:
                end = mid
            else:
                start = mid+1
        return start


        #mine
        start = 0
        end = 0

        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                start = mid
                end = mid
                while nums[start - 1] == target and start != 0:
                    start -= 1
                while nums[end + 1] == target and end != len(nums) - 1:
                    end += 1
                return [start,end]


            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return [-1,-1]
                
s = Solution()
a = s.searchRange([1, 2, 2, 3, 3, 4, 7], 3)
print(a)