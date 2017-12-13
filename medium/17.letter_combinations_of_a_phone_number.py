class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        dic = {'2':['a','b','c'],
               '3':['d','e','f'],
               '4':['g','h','i'],
               '5':['j','k','l'],
               '6':['m','n','o'],
               '7':['p','q','r','s'],
               '8':['t','u','v'],
               '9':['w','x','y','z']}
       
        self.result = []
        self.dfs(digits,dic,"",0)
        return self.result 

    def dfs(self,digits,dic,s,index):
        if index == len(digits):
            self.result.append(s)
            return 
        for letter in dic[digits[index]]:
            self.dfs(digits, dic, s+letter, index+1)

s = Solution()
a = s.findClosestElements()
print(a)
