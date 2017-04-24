import string
from functools import reduce 
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        #mine
        dict_ = list(string.ascii_uppercase)
        sum_ = 0
        i = 1
        for s_ in s:
            sum_ += (dict_.index(s_)+1) * 26 ** (len(s)-i)
            i+=1
        return sum_
        #easy_1
        s = s[::-1]
        sum = 0
        for exp, char in enumerate(s):
            sum += (ord(char) - 65 + 1) * (26 ** exp)
        return sum

        #easy_2
        return reduce(lambda x,y:x*26+y,map(lambda x:ord(x)-ord('A')+1,s))

s = Solution()
a = s.titleToNumber('AAB')
print(a)