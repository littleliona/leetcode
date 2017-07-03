class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #鸽巢原理
        #二分查找，在1～n之间，找到mid，然后计算<=mid的数量，如果数量大于mid，说明在low～mid中有重复的数
        #如果小于等于mid，说明在mid～high中有重复的数
        low = 1
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            cnt = sum([1 for num in nums if num <= mid])
 
            if cnt <= mid:
                low = mid + 1
            else:
                high = mid - 1
        
        return low




s = Solution()
a = s.findDuplicate([1,3,3,3])
print(a)     

        

