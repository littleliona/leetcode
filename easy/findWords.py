class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        L1 = set('qwertyuiop')
        L2 = set('asdfghjkl')
        L3 = set('zxcvbnm')

        L_r = []

        for n in words:
        	L = set(n.lower())
        	if L.issubset(L1) or L.issubset(L2) or L.issubset(L3):
        		L_r.append(n)

        return L_r



s = Solution()
s.findWords(["Hello", "Alaska", "Dad", "Peace"])