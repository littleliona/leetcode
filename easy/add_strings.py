from functools import reduce 
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        #mine
        x1=reduce(lambda x,y:x*10+y,map(lambda x:ord(x)-ord('0'),num1))
        x2=reduce(lambda x,y:x*10+y,map(lambda x:ord(x)-ord('0'),num2))
        return x1+x2
        #easy
        z = itertools.izip_longest(num1[::-1], num2[::-1], fillvalue='0')
        res, carry, zero2 = [], 0, 2*ord('0')
        for i in z:
            cur_sum = ord(i[0]) + ord(i[1]) - zero2 + carry
            res.append(str(cur_sum % 10))
            carry = cur_sum // 10
        return ('1' if carry else '') + ''.join(res[::-1])


s = Solution()
a = s.addStrings("123","456")
print(a)