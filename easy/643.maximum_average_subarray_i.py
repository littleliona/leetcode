class Solution(object):
    def findMaxAverage(self, A, K):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        P = [0]
        for x in A:
            P.append(P[-1] + x)

        ma = max(P[i+K] - P[i] for i in xrange(len(A) - K + 1))
    
        return ma / float(K)



s = Solution()
a = s.findMaxAverage([1,12,-5,-6,50,3], 4)
print(a)