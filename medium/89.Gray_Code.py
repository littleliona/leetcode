class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        #method_by_definition
        if n == 0:
            return [0]

        res = []
        for i in range(2 ** n):
            res.append(i ^ (i >> 1))
        
        return res
        
        #method by pattern
        if n == 0:
            return [0]
        if n == 1:
            return [0,1]

        res = []
        res = self.grayCode(n-1)
        for num in reversed(res):
            res.append(num + 2 ** (n-1))

        return res
    
        res = [0]
        for i in range(n):
            res += [x + pow(2,i) for x in reversed(res)]
        return res

s = Solution()
a = s.grayCode(3)
print(a)

