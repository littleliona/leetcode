class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        #回溯法
        self.res = []
        self.backtracing(n-1, n, ['('])

        return self.res

    def backtracing(self, left_, right_, path):
        if left_ == 0 and right_ == 0:
            str_ = ''.join(path)
            self.res.append(str_)

        if left_ < 0 or right_ < 0:
            return
        
        if left_:
            self.backtracing(left_ - 1, right_, path + ['('])
        if left_ < right_:
            self.backtracing(left_, right_ - 1, path + [')'])
        
        
            
            
            

s = Solution()
a = s.generateParenthesis(3)
print(a)     

        

