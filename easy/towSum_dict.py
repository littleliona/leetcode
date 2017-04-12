class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i,num in enumerate(numbers):
            if target-num in dic:
                return [dic[target-num]+1,i+1]
            dic[num] = i



s = Solution()
print(s.twoSum([2, 7, 11, 15],9))