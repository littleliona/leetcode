class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #mine
        if not prices:
            return 0
        stack = [prices[0]]   
        profit = 0
        for price in prices[1:]:
            if price > stack[-1]:      #维护一个递增栈
                stack.append(price)
            elif price < stack[0]:     #min_price
                stack = [price]
            profit = max(profit,stack[-1]-stack[0])
        return profit
        #easy
        max_profit, min_price = 0, float('inf')  #最大值－infinite
        for price in prices:
            min_price = min(min_price, price)    #更新最小值
            profit = price - min_price           #更新profit
            max_profit = max(max_profit, profit)
        return max_profit


s = Solution()
a = s.maxProfit([7, 1, 5, 3, 6, 4])
print(a)