class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #mine pop take too much time
        i = 0

        while i< len(nums)-1:
            if nums[i+1] == nums[i]:
                nums.pop(i+1)
            else:
                i += 1

        return len(nums)

        #O(n) leave the length beyond
        if not A:
            return 0

        newTail = 0

        for i in range(1, len(A)):
            if A[i] != A[newTail]:
                newTail += 1
                A[newTail] = A[i]

        return newTail + 1


s = Solution()
a = s.removeDuplicates([1,1,2])
print(a)



