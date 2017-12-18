class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        #recursive
        if k == 1:
            return [[x,] for x in range(1, n+1)]
 
        if n == k:
            return [[i for i in range(1, n+1)]]
        return [i + [n] for i in self.combine(n-1,k-1)] + [i for i in self.combine(n-1, k)]

        #backstring
        self.res = []
        L = [i for i in range(1,n+1)]
        self.dfs(L, k, 0, [])

        return self.res

    def dfs(self, n, k, index, path):
        if len(path) == k:
            self.res.append(path)

        if len(path) > k:
            return

        for i,num in enumerate(n[index:]):
            self.dfs(n, k, index+i+1, path + [num])
