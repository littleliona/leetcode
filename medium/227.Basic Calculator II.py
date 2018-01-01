class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return "0"

        stack, seq, sign = [], '', "+"
        for i in xrange(len(s)):
            if s[i].isdigit():
                seq += s[i]
            if (not s[i].isdigit() and not s[i].isspace()) or i == len(s)-1:
                num = int(seq)
                if sign == "-":
                    stack.append(-num)
                elif sign == "+":
                    stack.append(num)
                elif sign == "*":
                    stack.append(stack.pop()*num)
                else:
                    tmp = stack.pop()
                    if tmp//num < 0 and tmp%num != 0:
                        stack.append(tmp//num+1)
                    else:
                        stack.append(tmp//num)
                sign = s[i]
                seq = ''
        return sum(stack)

s = Solution()
a = s.calculate('  30')
print(a)
