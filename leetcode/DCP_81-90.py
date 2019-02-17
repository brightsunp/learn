#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/2/13'
'''
import unittest
from functools import reduce


class Solution1(object):
    '''Yelp

    Given a mapping of digits to letters (as in a phone number), and a digit string, return all possible letters the number could represent. You can assume each valid number in the mapping is a single digit.
    For example if {2: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} then “23” should return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].
    '''
    def __init__(self):
        self.d = dict(zip([2, 3, 4, 5, 6, 7, 8, 9],
                          [list(s) for s in ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']]))

    def combination(self, s):
        # iterative
        return reduce(lambda x, y: [e1+e2 for e1 in x for e2 in self.d[int(y)]], s, [''])


class Solution2(object):
    '''Microsoft*

    Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.
    For example, given a file with the content “Hello world”, three read7() returns “Hello w”, “orld” and then “”.

    Notes: `read` process should be cached.
    '''
    def __init__(self, content):
        self.content = content
        # cache _read7()
        self.offset = 0
        # cache readN(n)
        self.buffer = ''

    def readN(self, n):
        while len(self.buffer) < n:
            piece = self._read7()
            if not piece:
                break
            self.buffer += piece
        n_chars = self.buffer[:n]
        self.buffer = self.buffer[n:]
        return n_chars

    def _read7(self):
        start = self.offset
        end = min(self.offset+7, len(self.content))
        self.offset = end
        return self.content[start:end]


class Solution3(object):
    '''Google

    Invert a binary tree.
    For example, given the following tree:
        a
       / \
      b   c
     / \  /
    d   e f
    should become:
      a
     / \
     c  b
     \  / \
      f e  d
    '''
    def invert1(self, root):
        # recursive
        if not root:
            return None
        root.left, root.right = self.invert1(root.right), self.invert1(root.left)
        return root

    def invert2(self, root):
        # stack
        stack = root and [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root


class Solution4(object):
    '''Amazon

    Given a matrix of 1s and 0s, return the number of "islands" in the matrix. A 1 represents land and 0 represents water, so an island is a group of 1s that are neighboring whose perimeter is surrounded by water.
    For example, this matrix has 4 islands.
    1 0 0 0 0
    0 0 1 1 0
    0 1 1 0 0
    0 0 0 0 0
    1 1 0 0 1
    1 1 0 0 1
    '''
    def islands(self, matrix):
        # backtracking
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if self._dfs(matrix, i, j):
                    res += 1
        return res

    def _dfs(self, matrix, i, j):
        if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] == 0:
            return False
        if matrix[i][j] == 1:
            matrix[i][j] = 0
            self._dfs(matrix, i, j-1)
            self._dfs(matrix, i, j+1)
            self._dfs(matrix, i-1, j)
            self._dfs(matrix, i+1, j)
            return True


class Solution5(object):
    '''Facebook*

    Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0, using only mathematical or bit operations. You can assume b can only be 1 or 0.
    '''
    def choice(self, x, y, b):
        return x*b + y*(1-b)


class TestSolutions(unittest.TestCase):
    def test_solution1(self):
        sol = Solution1()

        self.assertEqual(sol.combination(''), [''])
        self.assertEqual(sol.combination('2'), ['a', 'b', 'c'])
        self.assertEqual(sol.combination('23'), ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'])

    def test_solution2(self):
        test1 = Solution2('Hello world')
        self.assertEqual(test1.readN(8), 'Hello wo')
        self.assertEqual(test1.readN(8), 'rld')
        self.assertEqual(test1.readN(8), '')

        test2 = Solution2('Hello world')
        self.assertEqual(test2.readN(4), 'Hell')
        self.assertEqual(test2.readN(4), 'o wo')
        self.assertEqual(test2.readN(4), 'rld')
        self.assertEqual(test2.readN(4), '')

    def test_solution4(self):
        sol = Solution4()
        arg = [[1, 0, 0, 0, 0],
               [0, 0, 1, 1, 0],
               [0, 1, 1, 0, 0],
               [0, 0, 0, 0, 0],
               [1, 1, 0, 0, 1],
               [1, 1, 0, 0, 1]]

        self.assertEqual(sol.islands(arg), 4)

    def test_solution5(self):
        sol = Solution5()

        self.assertEqual(sol.choice(3, 4, 1), 3)
        self.assertEqual(sol.choice(3, 4, 0), 4)


if __name__ == '__main__':
    unittest.main()
