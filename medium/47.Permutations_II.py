class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #method_fast
        self.res = []
        nums.sort()        
        self.find_path(nums, [], len(nums))

        return self.res 


        #method_general
        self.res = []
        
        length = len(nums)
        nums.sort()
        used = [False] * len(nums)
        self.dfs(nums, [], length, used)

        return self.res


    def find_path(self, nums, path, length):
        if len(path) == length:
            self.res.append(path)
            return 

        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue

            cur = nums[i]


    def dfs(self, nums, path, length, used):
    
        if len(path) == length:
            self.res.append(path)
            return
        
        if len(path) < length:
            for i,num in enumerate(nums):
                if used[i]:
                    continue
                if i > 0 and used[i-1] == False and nums[i-1] == nums[i]:
                    continue

                used[i] = True
                self.dfs(nums, path+[num], length, used)
                used[i] = False 


s = Solution()
a = s.partition('aab')
print(a)
