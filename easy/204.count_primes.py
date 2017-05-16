class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        #埃拉托斯特尼筛法
        #给出要筛数值的范围n，找出sqrt(n)以内的素数p1,p2,p3,p4...
        #先用2去筛，即把2留下，把2的倍数剔除掉；
        #再用下一个素数，也就是3筛，把3留下，把3的倍数剔除掉；
        #接下去用下一个素数5筛，把5留下，把5的倍数剔除掉；不断重复下去......
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: : i] = [False] * len(primes[i * i: : i])
        return sum(primes)

s = Solution()
a = s.countPrimes(10)
print(a)
    


        





