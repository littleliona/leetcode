import Counter from collections 
class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        #method_1
        count_A = sum(a == b for a,b in zip(secret,guess))
        s = Counter(secret)
        g = Counter(guess)

        return str(count_A)+'A'+str(sum((s & g).values())-count_A) + 'B'


        #method_mine
        count_B = 0
        count_A = sum(a == b for a,b in zip(secret,guess))
    
        dict_A = Counter(secret)
        dict_B = Counter(guess)

        for key,value in dict_A.items():
            if dict_B.get(key,-1) >= value:
                count_B += value
            if dict_B.get(key,-1) < value and dict_B.get(key,-1) != -1:
                count_B += dict_B.get(key,-1)
        count_B -= count_A
        return str(count_A)+'A' + str(count_B)+'B'


s = Solution()
a = s.findClosestElements()
print(a)
