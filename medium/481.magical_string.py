class Solution:
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        S = [1,2,2]
        i = 2
        while len(S) < n:
            S += S[i] * [3 - S[-1]]
            i += 1

        return S[:n].count(1)


s = Solution()
a = s.magicalString(6)
print(a)
