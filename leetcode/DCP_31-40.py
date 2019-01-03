#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2018/12/27'
'''


# 295. Find Median from Data Stream
from heapq import heappush, heappushpop

class Solution1_1(object):
    def __init__(self):
        # max_heap: reverse min_heap
        self.small = []
        # min_heap
        self.large = []
        self.even = True

    def addNum(self, num):
        # keep len(self.small) >= len(self.large)
        if len(self.small) == len(self.large):
            heappush(self.small, -heappushpop(self.large, num))
        else:
            heappush(self.large, -heappushpop(self.small, -num))
        self.even = not self.even

    def findMedian(self):
        if self.even:
            return (self.large[0] - self.small[0]) / 2.0
        else:
            return -self.small[0]


# 480. Sliding Window Median
from bisect import bisect_left, insort

class Solution1_2(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        win, res = nums[:k], []
        win.sort()
        odd = k % 2
        res.append(win[(k-1)/2]*1.0 if odd else (win[k/2-1]+win[k/2])/2.0)
        for i in range(k, len(nums)):
            # bisect_left returns exactly the index
            del(win[bisect_left(win, nums[i-k])])
            insort(win, nums[i])
            res.append(win[(k-1)/2]*1.0 if odd else (win[k/2-1]+win[k/2])/2.0)
        return res


# 75. Sort Colors
class Solution2(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # mind blowing from counting-sort
        n0 = n1 = n2 = -1
        for num in nums:
            if num == 0:
                n2, n1, n0 = n2+1, n1+1, n0+1
                nums[n2] = 2
                nums[n1] = 1
                nums[n0] = 0
            elif num == 1:
                n2, n1 = n2+1, n1+1
                nums[n2] = 2
                nums[n1] = 1
            else:
                n2 += 1
                nums[n2] = 2


# 289. Game of Life
class Solution3(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # use 2-bits to store independent states: [cur, pre]
        if not board or len(board) == 0:
            return
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                lives = self.live_neighbors(board, i, j, m, n)
                # 01 -> 11
                if board[i][j] == 1 and lives in [2, 3]:
                    board[i][j] = 3
                # 00 -> 10
                if board[i][j] == 0 and lives == 3:
                    board[i][j] = 2

        for i in range(m):
            for j in range(n):
                # update cur state
                board[i][j] >>= 1

    def live_neighbors(self, board, i, j, m, n):
        lives = 0
        for x in range(max(0, i - 1), min(m, i + 2)):
            for y in range(max(0, j - 1), min(n, j + 2)):
                lives += board[x][y] & 1
        lives -= board[i][j] & 1
        return lives


# 136. Single Number
from functools import reduce

class Solution4_1(object):
    def singleNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        for k, v in d.items():
            if v == 1:
                return k

    def singleNumber2(self, nums):
        # use 1-bit to store num
        return reduce(lambda x, y: x ^ y, nums)


# 137. Single Number II
class Solution4_2(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # use 2-bits to store nums: [a, b]
        a = b = 0
        for num in nums:
            # a stores num, b stores True/False
            a = a ^ num & ~b
            # b stores num, a stores True/False
            b = b ^ num & ~a
        # b == 0 in this problem
        return a


# 260. Single Number III
class Solution4_3(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # two-pass: a != b, so (a ^ b) has at least one '1'
        ans = reduce(lambda x, y: x ^ y, nums)
        # get last '1' set bit
        ans &= -ans
        res = [0, 0]
        for num in nums:
            if num & ans == 0:
                res[0] ^= num
            else:
                res[1] ^= num
        return res
