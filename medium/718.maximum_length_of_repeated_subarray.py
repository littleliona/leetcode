class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        if not A or not B:
            return 0


        dp = [[0 for i in range(len(A)+1)] for i in range(len(B)+1)]

        max_length = 0

        for i,num in enumerate(A):
            for j,num_1 in enumerate(B):
                if num == num_1:
                    dp[i+1][j+1] = dp[i][j] + 1
                    max_length = max(max_length, dp[i+1][j+1])


        return max_length




                
s = Solution()
a = s.findLength([1,2,3,2,1],[3,2,1,4,7])
print(a)
