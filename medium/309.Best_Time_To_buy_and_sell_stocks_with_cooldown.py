class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        not_hold , hold, not_hold_cooldown = 0, float('-inf'), float('-inf')

        for p in prices:
            not_hold, hold, not_hold_cooldown = max(not_hold,not_hold_cooldown), max(hold, not_hold - p), hold + p


        return max(not_hold, not_hold_cooldown)

if __name__ == '__main__':
    s = Solution()
    a = s.isAdditiveNumber("199100199")
    print(a)
