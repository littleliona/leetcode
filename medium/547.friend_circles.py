class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        #dfs 
        #调用dfs的次数即为circle数
        #利用递归dfs，也可以使用stack
        self.visited = [False] * len(M)
        count = 0
        for i in range(len(M)):
            if self.visited[i] == False:
                self.dfs(i,M)
                count += 1

        return count 


    def dfs(self, i, M):
        self.visited[i] = True
        for j,student in enumerate(M[i]):
            if student == 1 and i!=j and self.visited[j] == False:
                self.dfs(j,M)
             

s = Solution()
a = s.findCircleNum([[1,1,0],[1,1,1],[0,1,1]])
print(a)
        

