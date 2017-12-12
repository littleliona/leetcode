from collections import defaultdict
class Solution:
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        
        words = defaultdict(set)
        
        # build a graph from pairs
        for w1,w2 in pairs:
            words[w1].add(w2)
            words[w2].add(w1)
        
        # find root word of each word
        similar_words = {}
        def dfs(word, root_word):
            if word in similar_words:
                return
            similar_words[word] = root_word
            [dfs(synonym, root_word) for synonym in words[word]]


        [dfs(word,word) for word in words]
        
        #compare words: if all words have same root word, then similar
        return all(similar_words.get(w1,w1) == similar_words.get(w2,w2) for w1,w2 in zip(words1,words2))

s = Solution()
a = s.areSentencesSimilarTwo(["great", "acting", "skills"],["fine", "drama", "talent"],[["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]])
print(a)
