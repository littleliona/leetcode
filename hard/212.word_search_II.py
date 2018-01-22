from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_word(self,words):
        current = self.root
        for letter in words:
            current = current.children[letter]

        current.is_word = True

    def search_word(self, words):
        current = self.root
        for letter in words:
            if letter not in current.children:
                return False
            else:
                current = current.children[letter]

        return current.is_word


class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board or not words:
            return []

        trie_tree = Trie()

        for word in words:
            trie_tree.insert_word(word)

        visited = [[False] * len(board[0]) for _ in range(len(board))]
        res = set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.find_valid(res, board, trie_tree.root, visited, i, j, '')

        return list(res)

    def find_valid(self, res, board, node, visited, i, j, path):
        if node.is_word:
            res.add(path)

        if i < 0 or i >= len(board) or j< 0 or j >= len(board[0]):
            return

        if not visited[i][j] and node.children.get(board[i][j]):
            visited[i][j] = True
            for x,y in [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]:
                self.find_valid(res, board, node.children[board[i][j]], visited, x, y, path + board[i][j])

            visited[i][j] = False