class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        #mine
        #遍历－－如果左边和上边都不是X，本身是X的count＋1
        count = 0
        for i,m in enumerate(board):
            for j,n in enumerate(m):
                if board[i][j] == 'X' and (i==0 or board[i-1][j]!='X') and (j==0 or board[i][j-1]!='X'):
                    count += 1

        return count


s = Solution()
a = s.countBattleships(["XXX"])
print(a)
