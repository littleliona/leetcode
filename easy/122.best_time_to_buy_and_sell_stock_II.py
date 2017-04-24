class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #mine
        if not prices or len(prices)==1:
            return 0
        stack = []
        stack.append(prices[0])
        profit = 0
        for price in prices[1:]:
            if price >= stack[-1]:
                profit += price-stack[-1]
            else:
                stack = []
            stack.append(price)
        return profit

        #easy
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))