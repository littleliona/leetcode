from functools import reduce
import operator
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        L = []
        L.append(a)
        L.append(b)

        print(reduce(operator.add,L))

        	
        	


s = Solution()
s.getSum(1,2)