class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count1, count2, num1, num2 = 0, 0, None, None

        for num in nums:
            if num == num1:
                count1 += 1
            elif num == num2:
                count2 += 1
            elif count1 == 0:
                num1, count1 = num, 1
            elif count2 == 0:
                num2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1


        return [n for n in (num1,num2) if nums.count(n) > len(nums)//3]


s = Solution()
a = s.majorityElement([2,2,3,3,3,4,4])
print(a)
