import random
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #回溯法
        self.res = []
        self.backtraing(nums, len(nums), [])
        
        return self.res


    def backtraing(self, nums, length, path):
        if length == 0:
            self.res.append(path)

        if length > 0:
            for num in nums:
                if num not in path:
                    self.backtraing(nums, length-1, path+[num])

        

s = Solution()
a = s.permute([1,2,3])
print(a)     

        

