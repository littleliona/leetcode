class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        miss = 1
        cnt = 0
        i = 0

        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss 
                cnt += 1


        return cnt 

if __name__ == '__main__':
    s = Solution()
    a = s.isAdditiveNumber("199100199")
    print(a)
