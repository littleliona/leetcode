class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        #mine
        self.Dict = set()

        #
        for i in xrange(len(word)):
            yield word[:i] + '*' + word[i+1:]
        

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        #mine
        for word in dict:
        	self.Dict.add(word)


        #
        self.words = set(words)
        self.near = collections.Counter(cand for word in words
                                        for cand in self._candidates(word))

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        #mine
        for w in self.Dict:
        	if len(w) == len(word):
        		count = 0
        		i = 0
        		while i < len(word):
        			if word[i] != w[i]:
        				count += 1
        			i += 1
        		if count = 1:
        			return True

        return False

        #
        return any(self.near[cand] > 1 or 
                   self.near[cand] == 1 and word not in self.words
                   for cand in self._candidates(word))

        


# Your MagicDictionary object will be instantiated and called as such:
obj = MagicDictionary()
obj.buildDict(["hello", "leetcode"])
param_2 = obj.search('hhllo')
print(param_2)