class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        #判断是否被reveal
        visited = [([False] * len(board[0])) for p in range(len(board))]
        #邻居
        neighbor = []


        row,column = click[0],click[1]
        dfs = [(row,column)]

        if board[row][column] == 'M':
            board[row][column] = 'X'

        else:
            #dfs
            for row,column in dfs:
                count = 0
                if row>=1 and column>=1:
                    if board[row-1][column-1] == 'M':
                        count += 1
                    elif board[row-1][column-1] != 'M' and visited[row-1][column-1] == False and (row-1,column-1) not in dfs:
                        neighbor.append((row-1,column-1))
                        
                if column>=1: 
                    if board[row][column-1] == 'M':
                        count += 1
                    elif board[row][column-1] != 'M' and visited[row][column-1] == False and (row,column-1) not in dfs:
                        neighbor.append((row,column-1))

                if row+1<len(board) and column>=1: 
                    if board[row+1][column-1] == 'M':
                        count += 1
                    elif board[row+1][column-1] != 'M' and visited[row+1][column-1] == False and (row+1,column-1) not in dfs:
                        neighbor.append((row+1,column-1))


                if row>=1: 
                    if board[row-1][column] == 'M':
                        count += 1
                    elif board[row-1][column] != 'M' and visited[row-1][column] == False and (row-1,column) not in dfs:
                        neighbor.append((row-1,column))


                if row+1<len(board):
                    if board[row+1][column] == 'M':
                        count += 1
                    elif board[row+1][column] != 'M' and visited[row+1][column] == False and (row+1,column) not in dfs:
                        neighbor.append((row+1,column))


                if row>=1 and column+1<len(board[0]):
                    if board[row-1][column+1] =='M':
                        count +=1
                    elif board[row-1][column+1] != 'M' and visited[row-1][column+1] == False and (row-1,column+1) not in dfs:
                        neighbor.append((row-1,column+1))


                if column+1<len(board[0]):
                    if board[row][column+1] =='M':
                        count += 1
                    elif board[row][column+1] != 'M' and visited[row][column+1] == False and (row,column+1) not in dfs:
                        neighbor.append((row,column+1))


                if row+1<len(board) and column+1<len(board[0]):
                    if board[row+1][column+1] =='M':
                        count +=1
                    elif board[row+1][column+1] != 'M' and visited[row+1][column+1] == False and (row+1,column+1) not in dfs:
                        neighbor.append((row+1,column+1))

                #blank space
                if count == 0:
                    dfs += neighbor
                    board[row][column] = 'B'

                #digit
                else:
                    board[row][column] = str(count)
                
                neighbor = []
                visited[row][column] = True


        return board

            


s = Solution()
a = s.updateBoard([['E', 'E', 'E', 'E', 'E'],['E', 'E', 'M', 'E', 'E'],['E', 'E', 'E', 'E', 'E'],['E', 'E', 'E', 'E', 'E']],[3,0])
print(a)
        

