class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0

        length = 2
        res = 0
        d = A[1]-A[0]
        for i in range(2,len(A)):
            if A[i]-A[i-1]== d:
                length += 1

            else:
                d = A[i]-A[i-1]
                if length >=3:
                    res += (length-1)*(length-2)/2
                length = 2



        if length >= 3:
            res += (length-1)*(length-2)/2

        return int(res)



s = Solution()
a = s.numberOfArithmeticSlices([1,2,3,4])
print(a)
