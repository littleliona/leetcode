class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #mine
        res = [[]]
        for num in sorted(nums):
            res += [item+[num] for item in res if item+[num] not in res] 
        return res
        
        #fast
        if not nums:
            return [tuple()]
        nums=sorted(nums)
        tmp=self.subsetsWithDup(nums[1:])
        result=list(set(tmp+[(nums[0],)+i for i in tmp]))
        return result



s = Solution()
a = s.subsetsWithDup([1,2,2])
print(a)