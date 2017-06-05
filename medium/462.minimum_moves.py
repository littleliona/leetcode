class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #找到list中的众数
        #众数一定在排好序的数组的中部
        #小于众数的算＋1，大于众数的算-1
        count = 0
        nums.sort()
        most_num = nums[len(nums)//2]
        for num in nums:
            if num < most_num:
                count += most_num-num
            if num > most_num:
                count += num - most_num

        return count


        
s = Solution()
a = s.minMoves2([1,2,2,3,3,3,4])
print(a)



