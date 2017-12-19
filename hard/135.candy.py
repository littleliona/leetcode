class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        res = [1] * len(ratings)
        
        lbase = rbase = 1
        for i in range(1,len(ratings)):
            lbase = lbase + 1 if ratings[i] > ratings[i-1] else 1
            res[i] = lbase

        for i in range(len(ratings)-2, -1, -1):
            rbase = rbase + 1 if ratings[i] > ratings[i+1] else 1
            res[i] = max(rbase,res[i])

        return sum(res)
s = Solution()
a = s.partition('aab')
print(a)
