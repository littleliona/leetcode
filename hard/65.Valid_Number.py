class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        state = [{'blank':0, 'digit':1, 'sign':2, '.':3},
                {'digit':1, 'e':4, '.':5, 'blank':8},
                {'digit':1, '.':3},
                {'digit':5},
                {'digit':6, 'sign':7},
                {'e':4, 'digit':5, 'blank':8},
                {'digit':6, 'blank':8},
                {'digit':6},
                {'blank':8}]
        
        currentState = 0
        for c in s:
            if c >= '0' and c <= '9':
                c = 'digit'
            if c == ' ':
                c = 'blank'
            if c in ['+','-']:
                c = 'sign'

            key_  = state[currentState].keys()
            if c not in key_:
                return False
            
            currentState = state[currentState][c]
            print(currentState)
        
        if currentState not in [1,5,6,8]:
            return False

        return True






s = Solution()
a = s.isNumber(" 005047e+6")
print(a)
