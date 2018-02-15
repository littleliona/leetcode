class Solution(object):
    def isSelfCrossing(self,L):
        """
        :type x: List[int]
        :rtype: bool
        """
        b = c = d = e = 0
        for a in x:
            print(a,b,c,d)
            if d >= b > 0 and (a >= c or (a >= c-e >= 0 and f >= d-b)):
                return True
            b, c, d, e, f = a, b, c, d, e
            
        return False
if __name__ == '__main__':
    s = Solution()
    a = s.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])
    print(a)
