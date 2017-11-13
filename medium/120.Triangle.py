class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        #method_1
        #bottom-up
        #从倒数第二层开始，求出每层从某节点出发的最短路径（左、右子节点）
        #自底向上，最后求出从根出发的最短路径
        from copy import deepcopy
        m = len(triangle)
        dp = deepcopy(triangle[-1])
        for i in range(m-2, -1, -1):
            for j in range(i+1):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        return dp[0]

        #method_2
        if not triangle:
            return 
        res = triangle[-1]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                res[j] = min(res[j], res[j+1]) + triangle[i][j]
        return res[0]




s = Solution()
a = s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])
print(a)
