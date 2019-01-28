#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/1/24'
'''
import unittest


class Solution1(object):
    '''Google

    Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.
    Do this faster than the naive method of repeated multiplication.
    For example, pow(2, 10) should return 1024.
    '''
    pass


class Solution2(object):
    '''Facebook

    There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of starting at the top-left corner and getting to the bottom-right corner. You can only move right or down.

    Given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:
    - Right, then down
    - Down, then right
    Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.
    '''
    pass


class Solution3(object):
    '''Microsoft*

    Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.

    Given the following matrix:
    [['F', 'A', 'C', 'I'],
     ['O', 'B', 'Q', 'P'],
     ['A', 'N', 'O', 'B'],
     ['M', 'A', 'S', 'S']]
    and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target word 'MASS', you should return true, since it's the last row.
    '''
    def search(self, matrix, word):
        # backtracking
        self.matrix = matrix
        self.word = word
        self.m = len(matrix)
        self.n = len(matrix[0])
        for i in range(self.m):
            for j in range(self.n):
                if self._dfs(i, j, 0, self.matrix[i][j]):
                    return True
        return False

    def _dfs(self, i, j, k, tmp):
        if self.word[k] != tmp[k]:
            return False
        if k == len(self.word) - 1:
            return True
        return ((i < self.m - 1 and self._dfs(i+1, j, k+1, tmp+self.matrix[i+1][j])) or
                (j < self.n - 1 and self._dfs(i, j+1, k+1, tmp+self.matrix[i][j+1])))


class Solution4(object):
    '''Google

    A knight's tour is a sequence of moves by a knight on a chessboard such that all squares are visited once.
    Given N, write a function to return the number of knight's tours on an N by N chessboard.
    '''
    pass


class Solution5(object):
    '''Amazon

    Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

    For example, given the following matrix:
    [[1,  2,  3,  4,  5],
     [6,  7,  8,  9,  10],
     [11, 12, 13, 14, 15],
     [16, 17, 18, 19, 20]]

    You should print out the following:
    [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]
    '''
    def spiral1(self, matrix):
        # brute
        res = []
        row_beg, col_beg, row_end, col_end = 0, 0, len(matrix)-1, len(matrix[0])-1
        while row_beg < row_end and col_beg < col_end:
            for j in range(col_beg, col_end+1):
                res.append(matrix[row_beg][j])
            row_beg += 1
            for i in range(row_beg, row_end+1):
                res.append(matrix[i][col_end])
            col_end -= 1
            for j in range(col_end, col_beg-1, -1):
                res.append(matrix[row_end][j])
            row_end -= 1
            for i in range(row_end, row_beg-1, -1):
                res.append(matrix[i][col_beg])
            col_beg += 1
        return res

    def spiral2(self, matrix):
        # transpose
        if not matrix:
            return []
        row = list(matrix.pop(0))
        t = list(zip(*matrix))[::-1]
        return row + self.spiral2(t)


class TestSolutions(unittest.TestCase):
    def test_solution3(self):
        sol = Solution3()
        arg1 = [['F', 'A', 'C', 'I'],
                ['O', 'B', 'Q', 'P'],
                ['A', 'N', 'O', 'B'],
                ['M', 'A', 'S', 'S']]
        arg21 = 'FOAM'
        arg22 = 'MASS'
        arg23 = 'FBOS'

        self.assertTrue(sol.search(arg1, arg21))
        self.assertTrue(sol.search(arg1, arg22))
        self.assertFalse(sol.search(arg1, arg23))

    def test_solution5(self):
        sol = Solution5()
        arg = [[1,  2,  3,  4,  5],
               [6,  7,  8,  9,  10],
               [11, 12, 13, 14, 15],
               [16, 17, 18, 19, 20]]
        res = [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]

        self.assertEqual(sol.spiral1(arg), res)
        self.assertEqual(sol.spiral2(arg), res)


if __name__ == '__main__':
    unittest.main()
