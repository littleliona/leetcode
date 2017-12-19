class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start = sums = 0
        for x in range(len(gas)):
            sums += gas[x] - cost[x]
            if sums < 0:
                start, sums = x + 1, 0
        return start if sum(gas) >= sum(cost) else -1

            
s = Solution()
a = s.canCompleteCircuit([1,2],[2,1])
print(a)
