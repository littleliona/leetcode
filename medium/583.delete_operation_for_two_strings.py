class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len_1 = len(word1)
        len_2 = len(word2)

        #dp:动态规划，求最长公共子序列lcs
        matrix_c = [[0 for i in range(len_2+1)] for j in range(len_1+1)]
        for i in range(len_1):
            for j in range(len_2):
                if word1[i] == word2[j]:
                    matrix_c[i+1][j+1] = matrix_c[i][j] + 1
                else:
                    matrix_c[i+1][j+1] = max(matrix_c[i+1][j],matrix_c[i][j+1])


        return len_1 + len_2 - 2 * matrix_c[len_1][len_2] 
            
            
            

s = Solution()
a = s.minDistance("sea","")
print(a)     

        

