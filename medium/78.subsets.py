class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #easy iterate
        res = [[]]
        for num in sorted(nums):
            res += [item+[num] for item in res]
        return res

        #mine backtracing
        self.res = []
        if not nums:
            return self.res

        self.backtracing(nums, [], len(nums), 0)
        return self.res

    def backtracing(self, nums, sets, length, index):
        if len(sets) > length:
            return 

        if len(sets) <= length and sets not in self.res:
            self.res.append(sets)

        if index < len(nums):
            self.backtracing(nums, sets + [nums[index]], length, index+1)
            self.backtracing(nums, sets, length, index+1)




s = Solution()
a = s.subsets([1, 2, 3])
print(a)