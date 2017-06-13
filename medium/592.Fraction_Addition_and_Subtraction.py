import math
import re
class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        #正则表达式'[+-]?\d+'
        #[+-]?表示字符集[+-]中的字符匹配0次或者1次
        #\d+表示数字[0-9]匹配1次或无限次

        ints = map(int, re.findall('[+-]?\d+', expression))
        A, B = 0, 1
        for a in ints:
            b = next(ints)
            A = A * b + a * B
            B *= b
            g = math.gcd(A, B)  #求最大公约数
            A //= g
            B //= g
        return '%d/%d' % (A, B)


     
s = Solution()
a = s.fractionAddition("-1/2+1/2+10/3")
print(a)
        

