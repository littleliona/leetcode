class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        for token in tokens:
            if token.isdigit():
                stack.append(int(token))
            elif token[0] == '-' and len(token) > 1:
                stack.append(-int(token[1:]))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if token == '*':
                    stack.append(num1 * num2)
                elif token == '/':
                    if num2 % num1 != 0 and num2 // num1 < 0:
                        temp = num2 // num1 + 1
                    else:
                        temp = num2 // num1 
                    stack.append(temp)
                elif token == '+':
                    stack.append(num1 + num2)
                elif token == '-':
                    stack.append(num2 - num1)
        return stack[-1]

s = Solution()
a = s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
print(a)
