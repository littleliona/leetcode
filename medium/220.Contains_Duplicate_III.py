import collections
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0: 
            return False
        
        bucket = {}
        w = t + 1
        
        for i in range(len(nums)):
            m = nums[i] / w
            if m in bucket:
                return True
            
            if m - 1 in bucket and abs(nums[i] - bucket[m-1]) <= t:
                return True
            
            if m + 1 in bucket and abs(nums[i] - bucket[m+1]) <= t:
                return True
            
            bucket[m] = nums[i]
            if i >= k: 
                del bucket[nums[i - k] / w]
        return False


s = Solution()
a = s.containsNearbyAlmostDuplicate([0,0],0,0)
print(a)
