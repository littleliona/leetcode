class TrieNode:
    def __init__(self):

        self.children = {}
        self.isWord = False

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode() 
        #method_2
        self.word_dict=collections.defaultdict(list)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root 
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.isWord = True
        #method_2
        self.word_dict[len(word)].append(word)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.find(word, self.root)

        #method_2
        if not word:
            return False
        
        if '.' not in word:
            return word in self.word_dict[len(word)]
        
        for v in self.word_dict[len(word)]:
            for i,ch in enumerate(word):
                if ch!='.' and ch!=v[i]:
                    break
                
            else:
                return True
            
        return False


    def find(self, word, node):
        if word == '':
            return node.isWord

        if word[0] == '.':
            for child in node.children:
                if self.find(word[1:], node.children[child]):
                    return True

        else:
            if word[0] in node.children:
                return self.find(word[1:], node.children[word[0]])

        return False 

s = Solution()
a = s.longestValidParentheses(')()())')
print(a)
