from functools import cmp_to_key 

def f(x, y):
    return int(y + x) - int(x + y)
class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [str(n) for n in nums]
        nums.sort(key=cmp_to_key(f))
        return "".join(nums).lstrip('0') or '0'

