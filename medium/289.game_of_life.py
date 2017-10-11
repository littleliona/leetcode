class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        directions = [(-1,-1),(-1,0),(-1,1),(0,1),(0,-1),(1,-1),(1,0),(1,1)]
        index_live = []
        index_die = []
        row = len(board)
        column = len(board[0])
        
        for m in range(row):
            for n in range(column):
                if board[m][n] == 0:
                    count = sum(board[m + r][n + c] == 1 for r,c in directions if 0 <= m + r < row and 0 <= n + c < column)
                    if count == 3:
                        index_live.append((m,n))
                        
                else:
                    count = sum(board[m + r][n + c] == 1 for r,c in directions if 0 <= m + r < row and 0 <= n + c < column)
                    if count < 2 or count > 3:
                        index_die.append((m,n))

        for m,n in index_live:
            board[m][n] = 1

        for m,n in index_die:
            board[m][n] = 0


s = Solution()
a = s.gameOfLife([[0,0,0,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,0,0,0]])
print(a)