class Solution:
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        row = len(dungeon)
        column = len(dungeon[0])

        dp = [[0 for _ in range(column)] for _ in range(row)]
        
        dp[-1][-1] = max(1, 1-dungeon[-1][-1])

        for i in range(row-2,-1,-1):
            dp[i][column-1] = max(1, dp[i+1][column-1] - dungeon[i][column-1])

        for j in range(column-2,-1,-1):
            dp[row-1][j] = max(1, dp[row-1][j+1] - dungeon[row-1][j])

        for i in range(row-2,-1,-1):
            for j in range(column-2,-1,-1):
                dp[i][j] = max(1, min(dp[i+1][j],dp[i][j+1]) - dungeon[i][j])

        return dp[0][0]

        
if __name__ == '__main__':
    s = Solution()
    a = s.wordBreak("leetcode",["leet", "code"])
    print(a)
