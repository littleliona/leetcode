class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0

        forward = [0] * len(prices)
        backward = [0] * len(prices)

        min_buy = prices[0]
        for i in range(1,len(prices)):
            forward[i] = max(forward[i-1], prices[i] - min_buy)
            min_buy = min(prices[i], min_buy)
        
        max_sell = prices[len(prices)-1]
        for i in range(len(prices)-2,-1,-1):
            backward[i] = max(backward[i+1], max_sell - prices[i])
            max_sell = max(max_sell, prices[i])

        res = 0
        for i in range(len(prices)):
            res = max(res, forward[i] + backward[i])

        return res
s = Solution()
a = s.longestValidParentheses(')()())')
print(a)
