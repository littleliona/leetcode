class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        row = len(board)
        column = len(board[0])
        visited = [[False for _ in range(column)] for _ in range(row)] 
        k = 0
        for i in range(row):
            for j in range(column):
                if board[i][j] == word[k] and visited[i][j] == False:
                    visited[i][j] = True
                    if self.search_neighbor(board, word, k+1, i, j, visited):
                        return True
                    else:
                        k = 0
                        visited[i][j] = False 

        return False
    def search_neighbor(self, board, word, k, x, y, visited):
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        
        if k == len(word):
            return True 


        for dx,dy in directions:
            if 0 <= x+dx < len(board) and 0 <= y+dy< len(board[0]):
                if board[x+dx][y+dy] == word[k] and visited[x+dx][y+dy] == False:
                    visited[x+dx][y+dy] = True 
                    if self.search_neighbor(board, word, k+1, x+dx, y+dy, visited):
                        return True
                    else:
                        visited[x+dx][y+dy] = False 


        return False 





s = Solution()
a = s.exist([["a","a"]],"aaa")
print(a)
