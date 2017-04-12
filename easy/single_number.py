class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict_ = {}
        for num in nums:
            if num in dict_:
                dict_[num] = 2
            else:
                dict_[num] = 1

        for name, age in dict_.items():
            if age == 1:
                print(name)
        		

s = Solution()
s.singleNumber([1,1,2,2,3])