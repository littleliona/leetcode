class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        #mine
        if n == 0:
            return 1
        #main idea : 排列组合
        #与位数有关，依次计算出1、2、... n位数的unique digits number数，然后相加
        #e.m.:比如n＝2的时候，第一位有1-9 9种选择，第二位要从0-9中刨出去第一位 也是9种选择
        #所以n＝2的时候有9*9+10种选择
        res = 0
        for num in range(n):
            res += self.count(num+1)

        return res

        #other
        choices = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        ans, product = 1, 1
        
        for i in range(n if n <= 10 else 10):
            product *= choices[i]
            ans += product
            
        return ans

        
    def count(self, n):
        if n == 1:
            return 10
        
        res = 1
        stack = [9,9,8,7,6,5,4,3,2,1]
        for i in range(n):
            res *= stack[i]

        return res

s = Solution()
a = s.countNumbersWithUniqueDigits(4)
print(a)     

        

