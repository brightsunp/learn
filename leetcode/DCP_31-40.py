#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2018/12/27'
'''

from heapq import heappush, heappushpop
from bisect import bisect_left, insort


class Solution1(object):
    '''Google

    The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other.
    For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.
    Given two strings, compute the edit distance between them.
    '''
    pass


class Solution2(object):
    '''Jane Street

    Suppose you are given a table of currency exchange rates, represented as a 2D array. Determine whether there is a possible arbitrage: that is, whether there is some sequence of trades you can make, starting with some amount A of any currency, so that you can end up with some amount greater than A of that currency.
    There are no transaction costs and you can trade fractional quantities.
    '''
    pass


class Solution3_1(object):
    '''Microsoft*

    Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.
    Recall that the median of an even-numbered list is the average of the two middle numbers.
    '''
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


class Solution3_2(object):
    '''
    Sliding Window Median
    '''
    def medianSlidingWindow(self, nums, k):
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


class Solution4(object):
    '''Quora

    Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).
    For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome). As another example, given the string "google", you should return "elgoogle".
    '''
    pass


class Solution5(object):
    '''Google*

    Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array. Do this in linear time and in-place.
    For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
    '''
    def sortColors(self, nums):
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


class Solution6(object):
    '''Dropbox

    Given the root to a binary search tree, find the second largest node in the tree.
    '''
    pass


class Solution7(object):
    '''Google

    The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.
    For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.
    '''
    pass


class Solution8(object):
    '''Microsoft

    You have an N by N board. Write a function that, given N, returns the number of possible arrangements of the board where N queens can be placed on the board without threatening each other, i.e. no two queens share the same row, column, or diagonal.
    '''
    pass


class Solution9(object):
    '''Dropbox

    Conway's Game of Life
    '''
    def gameOfLife(self, board):
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
    '''Google

    Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.
    '''
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
