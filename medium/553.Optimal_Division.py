#coding=utf-8
class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        #在不添加任何括号的情况下：
        #a / b / c / d / ... = a / (b * c * d * ...)
        #但无论括号的位置如何，a一定是被除数的一部分，b一定是除数的一部分
        #原式添加括号方案的最大值，等价于求除数的最小值
        #因此最优添加括号方案为：
        #a / (b / c / d / ...) = a * c * d * ... / b
        A = map(str, nums)
        if len(A) <= 2:
            return '/'.join(A)
        return A[0] + '/(' + '/'.join(A[1:]) + ')'



     
s = Solution()
a = s.fractionAddition("-1/2+1/2+10/3")
print(a)
        

