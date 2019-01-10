#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2018/12/20'
'''


class Solution1(object):
    '''Snapchat*

    Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.
    For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
    '''
    def findRoom(self, intervals):
        # find maximum number of lectures at a time
        arr, dep = tuple(zip(*intervals))
        arr, dep = sorted(arr), sorted(dep)
        i = j = cur = res = 0
        # merge process of mergeSort
        while i < len(arr) and j < len(dep):
            if arr[i] < dep[j]:
                cur, i = cur+1, i+1
                res = max(res, cur)
            else:
                cur, j = cur-1, j+1
        return res
        

class Solution2_1(object):
    '''Microsoft*

    Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.
    For example, given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
    '''
    def wordBreak(self, s, wordDict):
        # dp: record if current makes it True
        n = len(s)
        if not n:
            return True
        dp = [False for _ in range(n+1)]
        for i in range(1, n+1):
            if not dp[i] and s[:i] in wordDict:
                dp[i] = True
            if dp[i]:
                for j in range(i+1, n+1):
                    if not dp[j] and s[i:j] in wordDict:
                        dp[j] = True
        return dp[n]
        

class Solution2_2(object):
    '''
    Word Break II
    '''
    def wordBreak(self, s, wordDict):
        # find all solutions
        return self.dfs(s, wordDict, {})
    
    def dfs(self, s, wordDict, memory):
        # dfs returns all break results of s.
        if not s:
            return ['']
        if s in memory:
            return memory[s]
        res = []
        for word in wordDict:
            if s.startswith(word):
                results = self.dfs(s[len(word):], wordDict, memory)
                for result in results:
                    res.append(word + (' ' + result if result else ''))
        memory[s] = res
        return res


class Solution3(object):
    '''Google

    You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on. Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.

    For example, given the following board:
    [[f, f, f, f],
    [t, t, f, t],
    [f, f, f, f],
    [f, f, f, f]]
    and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.
    '''
    def uniquePathsWithObstacles(self, obstacleGrid):
        # some difference from UniquePaths
        # first row or column: if i obstacle, i+next all 0
        # other rows: if i&j obstacle, just dp[i][j] = 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                break
            dp[0][i] = 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]


class Solution4(object):
    '''Google*

    Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.

    - is_locked, which returns whether the node is locked
    - lock, which attempts to lock the node. If it cannot be locked, then it should return false. Otherwise, it should lock it and return true.
    - unlock, which unlocks the node. If it cannot be unlocked, then it should return false. Otherwise, it should unlock it and return true.
    You may augment the node to add parent pointers or any other property you would like. You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes. Each method should run in O(h), where h is the height of the tree.
    '''
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        
        self._is_locked = False
        self.locked_descendants_count = 0

    def _can_lock_or_unlock(self):
        if self.locked_descendants_count > 0:
            return False
        cur = self.parent
        while cur:
            if cur._is_locked:
                return False
            cur = cur.parent
        return True

    def is_locked(self):
        return self._is_locked

    def lock(self):
        if self._can_lock_or_unlock():
            # increment count in all ancestors
            self._is_locked = True
            cur = self.parent
            while cur:
                cur.locked_descendants_count += 1
                cur = cur.parent
            return True
        return False

    def unlock(self):
        if self._can_lock_or_unlock():
            # decrement count in all ancestors
            self._is_locked = False
            cur = self.parent
            while cur:
                cur.locked_descendants_count -= 1
                cur = cur.parent
            return True
        return False


class Solution5_1(object):
    '''
    Wildcard Matching
    '''
    def isMatch(self, s, p):
        # dp[i][j]: if s[:i] matches p[:j]
        m, n = len(s), len(p)
        dp = [[False for _ in range(n+1)] for _ in range(m+1)]
        dp[0][0] = True
        for j in range(1, n+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-1]
                
        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] == '*':
                    # key point: j forward or i forward
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                elif p[j-1] == '?' or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
        return dp[m][n]


class Solution5_2(object):
    '''Facebook*

    Implement regular expression matching with the following special characters:

    . (period) which matches any single character
    * (asterisk) which matches zero or more of the preceding element
    That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.
    '''
    def isMatch(self, s, p):
        # dp[i][j]: if s[:i] matches p[:j]
        m, n = len(s), len(p)
        dp = [[False for _ in range(n+1)] for _ in range(m+1)]
        dp[0][0] = True
        
        for i in range(m+1):
            for j in range(1, n+1):
                if j > 1 and p[j-1] == '*':
                    # preceding pattern repeats 0 or more times
                    dp[i][j] = dp[i][j-2]
                    if i > 0 and (p[j-2] == '.' or p[j-2] == s[i-1]):
                        dp[i][j] = dp[i][j] or dp[i-1][j]
                elif i > 0 and (p[j-1] == '.' or p[j-1] == s[i-1]):
                    dp[i][j] = dp[i-1][j-1]
        return dp[m][n]


class Solution6(object):
    '''Google

    Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.
    The list is very long, so making more than one pass is prohibitively expensive. Do this in constant space and in one pass.
    '''
    pass


class Solution7(object):
    '''Facebook

    Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).
    For example, given the string "([])[]({})", you should return true.
    Given the string "([)]" or "((()", you should return false.
    '''
    pass


class Solution8(object):
    '''Palantir

    Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of strings which represents each line, fully justified.
    More specifically, you should have as many words as possible in each line. There should be at least one space between each word. Pad extra spaces when necessary so that each line has exactly length k. Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.
    If you can only fit one word on a line, then you should pad the right-hand side with spaces.
    Each word is guaranteed not to be longer than k.

    For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the following:
    ["the  quick brown", # 1 extra space on the left
    "fox  jumps  over", # 2 extra spaces distributed evenly
    "the   lazy   dog"] # 4 extra spaces distributed evenly
    '''
    pass


class Solution9(object):
    '''Amazon

    Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
    Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.
    '''
    def encode(self, s):
        res = []
        count, pre = 0, '#'
        for i, char in enumerate(s):
            if char == pre:
                count += 1
            else:
                # find switch pos
                if pre != '#':
                    res.append(str(count)+pre)
                count, pre = 1, char
        res.append(str(count)+pre)
        return ''.join(res)

    def decode(self, s):
        res = []
        for i in range(0, len(s), 2):
            cur = s[i:i+2]
            count, char = int(cur[0]), cur[1]
            res.append(char * count)
        return ''.join(res)


class Solution10(object):
    '''Facebook

    You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.
    Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.
Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.
    '''
    def trap(self, height):
        # cur_holder = max(min(left_max_height, right_max_height)-cur_height, 0)
        # two pointers: just avoid those two-step comparision
        res, left_max, right_max, lo, hi = 0, 0, 0, 0, len(height) - 1
        while lo <= hi:
            if height[lo] < height[hi]:
                if height[lo] > left_max:
                    left_max = height[lo]
                else:
                    res += left_max - height[lo]
                lo += 1
            else:
                if height[hi] > right_max:
                    right_max = height[hi]
                else:
                    res += right_max - height[hi]
                hi -= 1
        return res
