class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = [0] * (len(num1) + len(num2))

        pos = len(res) - 1

        for num_1 in reversed(num1):
            temp_pos = pos
            for num_2 in reversed(num2):
                res[temp_pos] += int(num_1) * int(num_2)
                res[temp_pos - 1] += res[temp_pos] // 10
                res[temp_pos] %= 10
                temp_pos -= 1
            pos -= 1

        p = 0
        while p < len(res)-1 and res[p] == 0:
            p += 1

        return ''.join(map(str,res[p:]))

s = Solution() 
a = s.multiply([-1,0,1,2,-1,-4])
print(a)

