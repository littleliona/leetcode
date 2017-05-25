class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a1,a2 = int(a[:-1].split('+')[0]),int(a[:-1].split('+')[1])
        b1,b2 = int(b[:-1].split('+')[0]),int(b[:-1].split('+')[1])


        left = str(a1*b1-a2*b2)
        right = str(a1*b2+a2*b1)

        return left+'+'+right+'i'


        

s = Solution()
a = s.complexNumberMultiply("1+-1i", "1+-1i")
print(a)
