#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/1/24'
'''
import unittest, random
from collections import defaultdict, OrderedDict


class Solution1(object):
    '''Google

    Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.
    Do this faster than the naive method of repeated multiplication.
    For example, pow(2, 10) should return 1024.
    '''
    def pow(self, x, y):
        # divide and conquer
        if y == 0:
            return 1
        if y == -(1 << 31):
            y >>= 1
            x *= x
        if y < 0:
            y = -y
            x = 1 / x
        half = self.pow(x * x, y >> 1)
        return half * x if y & 1 else half


class Solution2(object):
    '''Facebook

    There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of starting at the top-left corner and getting to the bottom-right corner. You can only move right or down.

    Given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:
    - Right, then down
    - Down, then right
    Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.
    '''
    def ways(self, M, N):
        # dp
        dp = [[1 for _ in range(N)] for _ in range(M)]
        for i in range(1, M):
            for j in range(1, N):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]


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
    '''Amazon*

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


class Solution6(object):
    '''Square*

    Assume you have access to a function toss_biased() which returns 0 or 1 with a probability that's not 50-50 (but also not 0-100 or 100-0). You do not know the bias of the coin.
    Write a function to simulate an unbiased coin toss.
    '''
    def toss_unbiased(self):
        n_experiments = 100000
        res_biased = {1: 0, 0: 0}
        res_unbiased = {1: 0, 0: 0}
        for i in range(n_experiments):
            coin = self._toss_biased()
            res_biased[coin] += 1
            coin = not coin if i & 1 else coin
            res_unbiased[coin] += 1
        bias0 = round(res_biased[0] / n_experiments, 1)
        bias1 = round(res_biased[1] / n_experiments, 1)
        unbias0 = round(res_unbiased[0] / n_experiments, 1)
        unbias1 = round(res_unbiased[1] / n_experiments, 1)
        return bias0, bias1, unbias0, unbias1

    def _toss_biased(self):
        return 0 if random.random() < 0.7 else 1


class Solution7(object):
    '''Google*

    Implement an LFU (Least Frequently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:
    - set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the least frequently used item. If there is a tie, then the least recently used key should be removed.
    - get(key): gets the value at key. If no such key exists, return null.
    Each operation should run in O(1) time.
    '''
    def __init__(self, capacity):
        self.remain = capacity
        self.min_freq = 1
        self.d_key = {}
        self.d_freq = defaultdict(OrderedDict)

    def get(self, key):
        if key not in self.d_key:
            return None
        self._update(key)
        return self.d_key[key][0]

    def set(self, key, value):
        if key in self.d_key:
            self._update(key, value)
        else:
            self.d_key[key] = (value, 1)
            self.d_freq[1][key] = (value, 1)
            if self.remain == 0:
                removed = self.d_freq[self.min_freq].popitem(last=False)
                del self.d_key[removed[0]]
            else:
                self.remain -= 1
            self.min_freq = 1

    def _update(self, key, new_val=None):
        value, freq = self.d_key[key]
        if new_val:
            value = new_val
        del self.d_freq[freq][key]
        if len(self.d_freq[self.min_freq]) == 0:
            self.min_freq += 1
        self.d_key[key] = (value, freq+1)
        self.d_freq[freq+1][key] = (value, freq+1)


class Solution8(object):
    '''Google

    On our special chessboard, two bishops attack each other if they share the same diagonal. This includes bishops that have another bishop located between them, i.e. bishops can attack through pieces.
    You are given N bishops, represented as (row, column) tuples on a M by M chessboard. Write a function to count the number of pairs of bishops that attack each other. The ordering of the pair doesn't matter: (1, 2) is considered the same as (2, 1).
    For example, given M = 5 and the list of bishops:
    (0, 0)
    (1, 2)
    (2, 2)
    (4, 0)
    The board would look like this:
    [b 0 0 0 0]
    [0 0 b 0 0]
    [0 0 b 0 0]
    [0 0 0 0 0]
    [b 0 0 0 0]
    You should return 2, since bishops 1 and 3 attack each other, as well as bishops 3 and 4.
    '''
    def attacks(self, M, bishops):
        # traverse diagonals
        res = 0
        for i in range(M):
            res += self._backslash(bishops, M, i, 0)
            res += self._slash(bishops, M, i, 0)
            if i != 0:
                res += self._backslash(bishops, M, 0, i)
                res += self._slash(bishops, M, M-1, i)
        return res

    def _backslash(self, bishops, M, i, j):
        count = 0
        while i < M and j < M:
            if (i, j) in bishops:
                count += 1
            i, j = i+1, j+1
        return (count - 1) * count / 2

    def _slash(self, bishops, M, i, j):
        count = 0
        while i >= 0 and j < M:
            if (i, j) in bishops:
                count += 1
            i, j = i-1, j+1
        return (count - 1) * count / 2


class Solution9(object):
    '''Facebook

    Given a list of integers, return the largest product that can be made by multiplying any three integers.
    For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.
    You can assume the list has at least three integers.
    '''
    def max1(self, nums):
        # backtracking
        self.res = nums[0]*nums[1]*nums[2]
        self._dfs(nums, 0, [])
        return self.res

    def _dfs(self, nums, pos, tmp):
        if len(tmp) == 3:
            self.res = max(self.res, tmp[0]*tmp[1]*tmp[2])
            return
        for i in range(pos, len(nums)):
            self._dfs(nums, i+1, tmp+[nums[i]])

    def max2(self, nums):
        # dp
        res = nums[0]*nums[1]*nums[2]
        two_max = two_min = nums[0]*nums[1]
        for i in range(2, len(nums)):
            res = max(res, two_max*nums[i], two_min*nums[i])
            for j in range(i):
                two_max = max(two_max, nums[j]*nums[i])
                two_min = min(two_min, nums[j]*nums[i])
        return res


class Solution10(object):
    '''Microsoft

    A number is considered perfect if its digits sum up to exactly 10.
    Given a positive integer n, return the n-th perfect number.
    For example, given 1, you should return 19. Given 2, you should return 28.
    '''
    def perfect(self, num):
        tmp = 0
        for char in str(num):
            tmp += int(char)
        return num*10 + (10-tmp)


class TestSolutions(unittest.TestCase):
    def test_solution1(self):
        sol = Solution1()

        self.assertEqual(sol.pow(2, 10), 1024)
        self.assertEqual(sol.pow(2, -2), 0.25)
        self.assertAlmostEqual(sol.pow(2.1, 3), 9.261)

    def test_solution2(self):
        sol = Solution2()

        self.assertEqual(sol.ways(1, 1), 1)
        self.assertEqual(sol.ways(2, 2), 2)
        self.assertEqual(sol.ways(5, 5), 70)

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

    def test_solution6(self):
        sol = Solution6()

        self.assertEqual(sol.toss_unbiased(), (0.7, 0.3, 0.5, 0.5))

    def test_solution8(self):
        sol = Solution8()
        arg1 = 5
        arg21 = [(0, 0), (1, 2), (2, 2), (4, 0)]
        arg22 = [(0, 0), (1, 2), (2, 2)]
        arg23 = [(0, 0), (1, 2), (2, 2), (4, 0), (4, 4)]

        self.assertEqual(sol.attacks(arg1, arg21), 2)
        self.assertEqual(sol.attacks(arg1, arg22), 1)
        self.assertEqual(sol.attacks(arg1, arg23), 4)

    def test_solution9(self):
        sol = Solution9()
        arg = [-10, -10, 5, 2, 3, 4]

        self.assertEqual(sol.max1(arg), 500)
        self.assertEqual(sol.max2(arg), 500)

    def test_solution10(self):
        sol = Solution10()

        self.assertEqual(sol.perfect(1), 19)
        self.assertEqual(sol.perfect(24), 244)
        self.assertEqual(sol.perfect(19), 190)


if __name__ == '__main__':
    unittest.main()
