import collections
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        #mine
        dic = {}
        count = 0
        for a in A:
            for b in B:
                if a+b in dic:
                    dic[a+b] += 1
                else:
                    dic[a+b] = 1

        for c in C:
            for d in D:
                if -c-d in dic:
                    count += dic[-c-d]

        return count

        #two-lines
        AB = collections.Counter(a+b for a in A for b in B)
        return sum(AB[-c-d] for c in C for d in D)






s = Solution()
a = s.fourSumCount([1,2],[-2,-1],[-1,2],[0,2])
print(a)     

        

