class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        Assume we break n into (n / x) x's, then the product will be xn/x, and we want to maximize it.
        Taking its derivative gives us n * xn/x-2 * (1 - ln(x)).
        The derivative is positive when 0 < x < e, and equal to 0 when x = e, then becomes negative when x > e,
        which indicates that the product increases as x increases, then reaches its maximum when x = e, then starts dropping.
        The only potential candidates are 2 and 3 since 2 < e < 3, but we will generally prefer 3 to 2
        '''
        #由导数可知因子为2或3，优先考虑3因为要最大的乘积
        #所以首先计算出有几个3因子，如果此时余数为1，个数要减1，因为要凑2
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        res = 1
        num_3 = n // 3
        if n % 3 == 1:
            num_3 -= 1
        num_2 = (n - 3 * num_3) // 2
        res = (2 ** num_2) * (3 ** num_3)


        return res
        

        
s = Solution()
a = s.integerBreak(8)
print(a)     

        

