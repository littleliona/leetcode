class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        #mine
        count = nums.count(val)
        nums.sort()
        for n in range(count):
            nums.pop(nums.index(val))
        print(nums)
        return len(nums)
        #other
        try:
            while True:
                nums.remove(val)
        except:
            return len(nums)


        
        

s = Solution()
a = s.removeElement([3,2,2,3],3)
print(a)