class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = 0
        b = len(numbers)-1

        while(True):
            if numbers[a] + numbers[b] < target:
                a+=1
            elif numbers[a] + numbers[b] > target:
                b-=1
            elif numbers[a] + numbers[b] == target:
                return [a+1,b+1]


s = Solution()
print(s.twoSum([2, 7, 11, 15],9))