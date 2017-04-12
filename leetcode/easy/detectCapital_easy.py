class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        print(word.isupper() or word.islower() or word.istitle())
		

s = Solution()
s.detectCapitalUse("Fasdasd")