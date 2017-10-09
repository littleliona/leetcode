class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = p = 1
        cnt = 0
        #每执行完一趟消除后，列表剩余相邻数字之间的差都会加倍。
        #解决问题的关键就是在每一次数字消除操作之后剩余数字的起点
        while n > 1:
            n /= 2
            cnt += 1
            p *= 2
            if cnt % 2:
                a += p / 2 + p * (n - 1)   #an = a1 + (n-1)*d  a1 = a + p/2
            else:
                a -= p / 2 + p * (n - 1)   #a1 = an - (n-1)*d  an = a - p/2 
        return a

        

s = Solution()
a = s.lastRemaining(9)
print(a)     

        

