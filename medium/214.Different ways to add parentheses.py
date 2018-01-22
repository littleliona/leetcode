class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit():
            return [int(input)]
        answer = []
        for i,c in enumerate(input):
            if c in '+-*':
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                for l in left:
                    for r in right:
                        answer.append(self.merge(l, r, c))
        return answer
                
    def merge(self, i, j, sign):
        if sign == '+':
            return i+j
        elif sign == '-':
            return i-j
        else:
            return i*j
        
if __name__ == '__main__':
    s = Solution()
    a = s.wordBreak("leetcode",["leet", "code"])
    print(a)
