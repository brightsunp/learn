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


if __name__ == '__main__':
    unittest.main()
