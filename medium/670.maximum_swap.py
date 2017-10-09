class Solution:
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        #brute-force
        #swap each two num, find the max one
        #O(n^2)
        A = list(str(num))
        ans = A[:]
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                A[i], A[j] = A[j], A[i]
                if A > ans: ans = A[:]
                A[i], A[j] = A[j], A[i]

        return int("".join(ans))
        
        #O(n)
        #find the max num after current index and swap them
        A = map(int, str(num))
        last = {x: i for i, x in enumerate(A)}
        for i, x in enumerate(A):
            for d in xrange(9, x, -1):
                if last.get(d, None) > i:
                    A[i], A[last[d]] = A[last[d]], A[i]
                    return int("".join(map(str, A)))
        return num



s = Solution()
a = s.findMaxAverage([1,12,-5,-6,50,3], 4)
print(a)