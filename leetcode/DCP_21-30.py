#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2018/12/20'
'''


# Minimum number of rooms required
class Solution1(object):
    def findRoom(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # find maximum number of rooms for lectures at a time
        arr, dep = tuple(zip(*intervals))
        arr = sorted(arr)
        dep = sorted(dep)
        res = cur = 0
        i = j = 0
        # merge process of mergeSort
        while i < len(arr) and j < len(dep):
            if (arr[i] < dep[j]):
                cur, i = cur+1, i+1
                res = max(res, cur)
            else:
                cur, j = cur-1, j+1
        return res
        

# 139. Word Break
class Solution2_1(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # dp: record if current makes it True
        n = len(s)
        if not n: return True
        dp = [False for _ in range(n+1)]
        for i in range(1, n+1):
            if not dp[i] and s[:i] in wordDict:
                dp[i] = True
            if dp[i]:
                for j in range(i+1, n+1):
                    if not dp[j] and s[i:j] in wordDict:
                        dp[j] = True
        return dp[n]
        
    
# 140. Word Break II        
class Solution2_2(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
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


# 63. Unique Paths II
class Solution3(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
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


# Lock a binary tree


# 44. Wildcard Matching
class Solution5_1(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
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

        
# 10. Regular Expression Matching
class Solution5_2(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
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


# Run-length encoding and decoding
class Solution6(object):
    def encode(self, s):
        """
        :input s: 'AAAABBBCCDAA'
        :output encoded_s: '4A3B2C1D2A'
        """
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
            if i == len(s)-1:
                res.append(str(count)+pre)
        return ''.join(res)

    def decode(self, s):
        res = []
        for i in range(0, len(s), 2):
            cur = s[i:i+2]
            count, char = int(cur[0]), cur[1]
            res.append(char * count)
        return ''.join(res)


# 42. Trapping Rain Water
class Solution7(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
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
