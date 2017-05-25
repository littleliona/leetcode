from collections import Counter
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #best
        #hash-map
        #without extra space
        res = []
        for x in nums:
            if nums[abs(x)-1] < 0:
                res.append(abs(x))
            else:
                nums[abs(x)-1] *= -1
        return res
        
        #mine
        dic = {}
        res = []
        for num in nums:
            if num in dic:
                res.append(num)
            else:
                dic[num] = 1
        return res
        
        
        


s = Solution()
a = s.findDuplicates([4,3,2,7,8,2,3,1])
print(a)
