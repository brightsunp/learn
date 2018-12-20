#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2018/12/20'
'''


# 51. N-Queens
# 52. N-Queens II
'''
This is a classic backtracking problem.

How to translate the problem into programming model?
1. Start row by row, and loop through columns;
2. Check if any queen exists in preceding directions;
3. Find {solutions} or its count.
'''


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.res = []
        self.board = [['.'] * n for _ in range(n)]
        self.dfs(0, n)
        return self.res

    def dfs(self, row, n):
        if row == n:
            self.res.append([''.join(line) for line in self.board])
            return
        for col in range(n):
            if self.check(row, col, n):
                self.board[row][col] = 'Q'
                self.dfs(row + 1, n)
                self.board[row][col] = '.'

    def check(self, row, col, n):
        for i in range(row):
            # upper vertical
            if self.board[i][col] == 'Q':
                return False
            # left upper slash
            if col - 1 - i >= 0 and self.board[row - 1 - i][col - 1 - i] == 'Q':
                return False
            # right upper slash
            if col + 1 + i < n and self.board[row - 1 - i][col + 1 + i] == 'Q':
                return False
        return True
