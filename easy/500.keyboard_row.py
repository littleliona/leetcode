class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        #mine
        L1 = set('qwertyuiop')
        L2 = set('asdfghjkl')
        L3 = set('zxcvbnm')

        L_r = []

        for n in words:
        	L = set(n.lower())
        	if L.issubset(L1) or L.issubset(L2) or L.issubset(L3):
        		L_r.append(n)

        return L_r

        #easy
        a=set('qwertyuiop')
        b=set('asdfghjkl')
        c=set('zxcvbnm')
        ans=[]
        for word in words:
            t=set(word.lower())
            if a&t==t:
                ans.append(word)
            if b&t==t:
                ans.append(word)
            if c&t==t:
                ans.append(word)
        return ans



s = Solution()
s.findWords(["Hello", "Alaska", "Dad", "Peace"])