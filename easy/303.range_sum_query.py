class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        #mine
        self.List = nums

        #fast 初始化的时候就计算出到当前位置的和
        self.accu = [0]
        for num in nums: 
            self.accu += [self.accu[-1] + num]
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        #mine
        return sum(self.List[i:j+1])

        #fast
        return self.accu[j + 1] - self.accu[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)


s = Solution()
a = s.findPairs([1, 1, 2, 2, 5],1)
print(a)
    


        





