class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) <= 1:
            return 0

        pre = 0
        for i in range(len(A)):
            pre += i * A[i]

        max_value = pre
        for i in range(len(A)-1,-1,-1):
            res = pre - (len(A)-1) * A[i] + sum(A) - A[i]
            max_value = max(max_value,res)
            pre = res


        return max_value

        

if __name__ == '__main__':
    s = Solution()
    a = s.maxRotateFunction([4,3,2,6])
    print(a)
