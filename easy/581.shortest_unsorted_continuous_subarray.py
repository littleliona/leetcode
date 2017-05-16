class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #mine
        nums1 = []
        nums1[:]= nums
        nums.sort()

        if nums == nums1:
            return 0

        left = len(nums)-1
        right = 0
        for i in range(len(nums)):
            if nums[i]!=nums1[i]:
                left = min(left,i)
                right = max(right,i)

        
        return right-left+1

        #concise
        B = sorted(A)
        if A == B: return 0
        for i in xrange(len(A)):
            if A[i] != B[i]: break
        for j in xrange(len(A)-1, -1, -1):
            if A[j] != B[j]: break
        return j - i + 1



s = Solution()
a = s.findUnsortedSubarray([4,3,2,1])
print(a)
    


        





