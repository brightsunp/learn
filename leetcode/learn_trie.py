#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2018/12/8'
'''


# 208. Implement Trie (Prefix Tree)
class TrieNode(object):
    def __init__(self):
        self.isLeaf = False
        # defaultdict: {char: TrieNode}
        self.children = {}
        

class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for char in word:
            cur = cur.children.setdefault(char, TrieNode())
        cur.isLeaf = True
        
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for char in word:
            cur = cur.children.get(char)
            if not cur:
                return False
        return cur.isLeaf

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for char in prefix:
            cur = cur.children.get(char)
            if not cur:
                return False
        return True

        
# 79. Word Search
class Solution1(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # backtracking: find a solution
        if not board: return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word, 0):
                    return True
        return False
        
    def dfs(self, board, i, j, word, idx):
        if idx == len(word):
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j] != word[idx]:
            return False
        tmp, board[i][j] = board[i][j], '#'
        res = (self.dfs(board, i-1, j, word, idx+1) or self.dfs(board, i+1, j, word, idx+1)
              or self.dfs(board, i, j-1, word, idx+1) or self.dfs(board, i, j+1, word, idx+1))
        # regain original board
        board[i][j] = tmp
        return res

        
# 212. Word Search II
class Solution2_1(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        # Backtracking + Trie
        self.trie = Trie()
        for word in words:
            self.trie.insert(word)
        self.res = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, board[i][j])
        return list(self.res)
        
    def dfs(self, board, i, j, tmp):
        if not self.trie.startsWith(tmp):
            return
        if self.trie.search(tmp):
            self.res.add(tmp)
        c, board[i][j] = board[i][j], '#'
        if i>0: self.dfs(board, i-1, j, tmp+board[i-1][j])
        if i<len(board)-1: self.dfs(board, i+1, j, tmp+board[i+1][j])
        if j>0: self.dfs(board, i, j-1, tmp+board[i][j-1])
        if j<len(board[0])-1: self.dfs(board, i, j+1, tmp+board[i][j+1])
        board[i][j] = c

        
class Solution2_2(object):
    def findWords(self, board, words):
        # Backtracking + Trie
        trie = self.buildTrie(words)
        self.res = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, trie)
        return self.res
    
    def dfs(self, board, i, j, trie):
        # found one
        if trie.get('word'):
            self.res.append(trie['word'])
            # de-duplicate
            trie['word'] = None
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j] not in trie:
            return
        c, board[i][j] = board[i][j], '#'
        self.dfs(board, i-1, j, trie[c])
        self.dfs(board, i+1, j, trie[c])
        self.dfs(board, i, j-1, trie[c])
        self.dfs(board, i, j+1, trie[c])
        board[i][j] = c
    
    def buildTrie(self, words):
        trie = {}
        for word in words:
            cur = trie
            for char in word:
                cur = cur.setdefault(char, {})
            cur['word'] = word
        return trie
    