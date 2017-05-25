class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        #faster
        #遇到2的指数次幂时，前一半跟后一半相比位数加1，1的个数也加1
        res=[0]
        while len(res)<=num:
            res+=[i+1 for i in res]
        return res[:num+1]

        
        #mine
        L = []
        for i in range(num+1):
            a = bin(i).count('1')
            L.append(a)

        return L



s = Solution()
a = s.countBits(10)
print(a)
