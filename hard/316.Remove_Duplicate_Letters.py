from collections import Counter
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}
        dic =  Counter(s)
        stack = []
        visited = {c: False for c in dic}
        for c in s:
            dic[c] -= 1
            if not visited[c]:
                while stack and dic[stack[-1]] > 0 and stack[-1] > c:
                    visited[stack[-1]] = False
                    stack.pop()
                
                stack.append(c)
                visited[c] =True 

        return ''.join(stack)

        


if __name__ == '__main__':
    s = Solution()

    a = s.addOperators("105",5)
    print(a)