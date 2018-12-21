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
class Solution1(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # find all solutions
        self.res = []
        self.board = [['.'] * n for _ in range(n)]
        self.dfs(0, n)
        return self.res

    def dfs(self, row, n):
        if row == n:
            self.res.append([''.join(line) for line in self.board])
            return

        for col in range(n):
            if self.is_valid(row, col, n):
                self.board[row][col] = 'Q'
                self.dfs(row + 1, n)
                self.board[row][col] = '.'

    def is_valid(self, row, col, n):
        # upper vertical
        for i in range(row):
            if self.board[i][col] == 'Q':
                return False

        # left upper diagonal
        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if self.board[i][j] == 'Q':
                return False

        # right upper diagonal
        for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
            if self.board[i][j] == 'Q':
                return False

        return True


# 37. Sudoku Solver
'''
1. Find empty location one by one, if none then solved;
2. Check if same digit exists in violation of rules;
3. Regain current value if not solved.
'''
class Solution2(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # find one solution
        self.board = board
        self.dfs()

    def dfs(self):
        loc = [-1, -1]
        if not self.find_empty_loc(loc):
            return True

        row, col = tuple(loc)
        for num in range(1, 10):
            if self.is_valid(row, col, str(num)):
                self.board[row][col] = str(num)
                if self.dfs():
                    return True
                else:
                    self.board[row][col] = '.'
        return False

    def find_empty_loc(self, loc):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == '.':
                    loc[0] = i
                    loc[1] = j
                    return True
        return False

    def is_valid(self, row, col, digit):
        # used in row
        for i in range(9):
            if self.board[row][i] == digit:
                return False

        # used in col
        for j in range(9):
            if self.board[j][col] == digit:
                return False

        # used in sub-box
        row, col = row - row % 3, col - col % 3
        for i in range(3):
            for j in range(3):
                if self.board[row + i][col + j] == digit:
                    return False

        return True
