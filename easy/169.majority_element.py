class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #mine
        return max(num for num in set(nums) if nums.count(num) >= len(nums)/2 )
        #best
        return sorted(nums)[len(nums)/2]
            
        


s = Solution()
a = s.majorityElement([3,3,2])
print(a)