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
    '''Facebook

    Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0, using only mathematical or bit operations. You can assume b can only be 1 or 0.
    '''
    def choice(self, x, y, b):
        return x*b + y*(1-b)


class Solution6(object):
    '''Google

    Given a string of parentheses, write a function to compute the minimum number of parentheses to be removed to make the string valid (i.e. each open parenthesis is eventually closed).
    For example, given the string "()())()", you should return 1. Given the string ")(", you should return 2, since we must remove all of them.
    '''
    def remove(self, s):
        # auxiliary stack
        stack, count = [], 0
        for char in s:
            if char == '(':
                stack.append(char)
            else:
                if stack:
                    stack.pop()
                else:
                    count += 1
        return count + len(stack)


class NeighbourNode(object):
    def __init__(self, val):
        self.val = val
        # dict.fromkeys(): pointer to SAME object
        self.neighbours = {'N': set(), 'S': set(), 'W': set(), 'E': set()}

    def __hash__(self):
        return hash(self.val)


class Solution7(object):
    '''Uber*

    A rule looks like this:
    A NE B
    This means this means point A is located northeast of point B.
    A SW C
    means that point A is southwest of C.

    Given a list of rules, check if the sum of the rules validate. For example:
    A N B
    B NE C
    C N A
    does not validate, since A cannot be both north and south of C.
    A NW B
    A N B
    is considered valid.
    '''
    def __init__(self):
        self.opposites = {'N': 'S', 'S': 'N', 'W': 'E', 'E': 'W'}

    def is_valid(self, rules):
        nodes = {}
        for rule in rules:
            val1, directions, val2 = tuple(rule.split())
            node1 = nodes.setdefault(val1, NeighbourNode(val1))
            node2 = nodes.setdefault(val2, NeighbourNode(val2))
            if not self._add_rule(node1, directions, node2):
                return False
        return True

    def _add_rule(self, node1, directions, node2):
        # recursive
        for direction in directions:
            if node1 in node2.neighbours[self.opposites[direction]] or node2 in node1.neighbours[direction]:
                return False
            # check node1's transfer dependency
            for node in node1.neighbours[direction]:
                self._add_rule(node, direction, node2)
        for direction in directions:
            node2.neighbours[direction].add(node1)
            node1.neighbours[self.opposites[direction]].add(node2)
        return True


class Solution8(object):
    '''ContextLogic*

    Implement division of two positive integers without using the division, multiplication, or modulus operators. Return the quotient as an integer, ignoring the remainder.
    '''
    def divide(self, dividend, divisor):
        # bit manipulation
        if divisor == 0 or (dividend == -2 ** 31 and divisor == -1):
            return 2 ** 31 - 1

        dvd, dvs = abs(dividend), abs(divisor)
        res = 0
        while dvd >= dvs:
            tmp, mul = dvs, 1
            # divisor doubled to get close to dividend
            while dvd >= (tmp << 1):
                tmp <<= 1
                mul <<= 1
            dvd -= tmp
            res += mul

        sign = (dividend < 0) ^ (divisor < 0)
        return -res if sign else res


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

    def test_solution6(self):
        sol = Solution6()

        self.assertEqual(sol.remove('()())()'), 1)
        self.assertEqual(sol.remove(')('), 2)

    def test_solution7(self):
        sol = Solution7()
        arg1 = ['A N B', 'B NE C', 'C N A']
        arg2 = ['A NW B', 'A N B']

        self.assertFalse(sol.is_valid(arg1))
        self.assertTrue(sol.is_valid(arg2))

    def test_solution8(self):
        sol = Solution8()

        self.assertEqual(sol.divide(10, 0), 2**31-1)
        self.assertEqual(sol.divide(-2**31, -1), 2**31-1)
        self.assertEqual(sol.divide(15, 3), 5)
        self.assertEqual(sol.divide(16, 3), 5)


if __name__ == '__main__':
    unittest.main()
