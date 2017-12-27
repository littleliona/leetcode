class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        n, remainder = divmod(abs(numerator), abs(denominator))
        sign = '-' if denominator * numerator < 0 else ''
        if remainder == 0:
            return sign + str(n)
        
        res = [sign+str(n),'.']
        stack = []

        while remainder not in stack:
            stack.append(remainder)
            n, remainder = divmod(remainder * 10, abs(denominator))
            res.append(str(n))

        index = stack.index(remainder)
        res.insert(index+2, '(')
        res.append(')')

        return ''.join(res).replace('(0)','')

        
s = Solution()
a = s.longestValidParentheses(')()())')
print(a)
