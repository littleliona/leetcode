class Solution:
    def replaceWords(self, roots, sentence):
        """
        :type roots: List[str]
        :type sentence: str
        :rtype: str
        """
        rootset = set(roots)

    	def replace(word):
        	for i in xrange(1, len(word)):
            	if word[:i] in rootset:
                	return word[:i]
        	return word

    	return " ".join(map(replace, sentence.split()))



s = Solution()
a = s.replaceWords(["a", "aa", "aaa", "aaaa"],"a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa")
print(a)