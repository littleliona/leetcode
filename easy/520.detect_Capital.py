class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        #mine
        set_apl = set('QWERTYUIOPASDFGHJKLZXCVBNM')
        set_word = set(list(word))
        
        if set_word.issubset(set_apl) or set_word.isdisjoint(set_apl):
        	print(True)
        elif word[0] in set_apl and set(list(word[1:])).isdisjoint(set_apl):
        	print(True)
        else:
        	print(False)

        #easy

        print(word.isupper() or word.islower() or word.istitle())
		

s = Solution()
s.detectCapitalUse("FFFFFFFf")