import random
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.L2 = []
        self.L1 = nums
        self.L2[:] = nums

        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.L2
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        random.shuffle(self.L1)
        return self.L1
        


# Your Solution object will be instantiated and called as such:
obj = Solution([1,2,3])
param_1 = obj.reset()
print(param_1)
param_2 = obj.shuffle()
print(param_2)
param_3 = obj.reset()
print(param_3)