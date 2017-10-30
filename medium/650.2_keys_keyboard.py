class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        #method_1
        d = 2
        operation = 0
        while (1):
            if n % d == 0:
                operation += d
                n = n / d
            else:
                d += 1
            if n == 1:
                break

                
        return operation
        
        #method_2
        def factors(n):
            d = 2
            while d * d <= n:
                while n % d == 0:
                    n /= d
                    yield d
                d += 1
            if n > 1:
                yield n

        return sum(factors(n))



s = Solution()
a = s.minSteps(8)
print(a)
