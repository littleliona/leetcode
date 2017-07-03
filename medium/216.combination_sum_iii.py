class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if n >= k*9:
            return []

        
        self.res = []
        for i in range(1, n // 2 + 1):
            self.backtracing(i, k-1, n-i,[]+[i])
            
        return self.res




    def backtracing(self, i, k, remain, path):
        if k == 0 and remain == 0:
            self.res.append(path)
        if k < 0 or remain < 0:
            return 

        for j in range(i+1, 10):
            self.backtracing(j, k-1, remain-j, path + [j])
            
            
            

s = Solution()
a = s.combinationSum3(3,9)
print(a)     

        

