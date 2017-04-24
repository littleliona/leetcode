class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #mine:
        if target in nums:
            return nums.index(target)
        else:
            for num in nums:
                if target<num:
                    return nums.index(num)
            return len(nums)
        
        #binary_search:
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        
        return self.binary_search(nums,0,len(nums)-1,target)

    def binary_search(self, nums, start, end, target):
        if start > end:
            return start
        mid = start + (end - start)//2
        if nums[mid] == target:
            return mid
        else: 
            if nums[mid] > target:
                return self.binary_search(nums,start,mid-1,target)
            else:
                return self.binary_search(nums,mid+1,end,target)



s = Solution()
a = s.searchInsert([1,3,5,6],0)
print(a)