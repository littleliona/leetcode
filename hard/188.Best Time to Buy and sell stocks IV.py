class Solution:
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        res = 0
        if k >= n / 2:
            for i in range(1,n):
                res += max(0, prices[i] - prices[i-1])

            return res

        dp =[[0 for j in range(n)]for i in range(k+1)]
        for i in range(1,k+1):
            maxTemp=-prices[0]
            for j in range(1,n):
                dp[i][j]=max(dp[i][j-1],prices[j] + maxTemp)
                maxTemp =max(maxTemp,dp[i-1][j-1] - prices[j])
        return dp[k][n-1]
                
        
if __name__ == '__main__':
    s = Solution()
    a = s.wordBreak("leetcode",["leet", "code"])
    print(a)
