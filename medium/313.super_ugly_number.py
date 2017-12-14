from collections import defaultdict
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        prime_index = [-1] * len(primes)
        prime_list = [1] * len(primes)
        q = []
        while len(q) < n:
            m = min(prime_list)
            q += m,
            for i in range(len(prime_list)):
                if prime_list[i] == m:
                    prime_index[i] += 1
                    prime_list[i] = q[prime_index[i]] * primes[i]
        

        return q[-1]

s = Solution()
a = s.nthSuperUglyNumber(12,[2,7,13,19])
print(a)
