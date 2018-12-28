#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2018/12/28'
'''


# 5. Longest Palindromic Substring
class Solution1_1(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # O(n^2) time and O(1) space
        max_len = start = 0
        for i in range(len(s)):
            cur_len = max(self.extend(s, i, i), self.extend(s, i - 1, i))
            if cur_len > max_len:
                max_len, start = cur_len, i - cur_len//2
        return s[start:start+max_len]

    def extend(self, s, left, right):
        # calculate length of palindrome
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left, right = left - 1, right + 1
        return right - left - 1


# Manacher's algorithm
'''
The above solution is quite concise. However, nothing can stop us optimizing quadratic approaches to linear ones.

Step 1. transform 'abba' => '^#a#b#b#a#$': avoid even-length-palindromes and bounds
Step 2. calculate each position's LPS: use symmetry to avoid redundant calculation
'''
class Solution1_2(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # O(n) time and O(n) space
        t = '#'.join('^{}$'.format(s))
        res = [0] * len(t)
        center = right = 0
        for i in range(len(t) - 1):
            mirror = 2 * center - i
            if i < right:
                res[i] = min(right - i, res[mirror])
            while t[i + (1 + res[i])] == t[i - (1 + res[i])]:
                res[i] += 1
            if i + res[i] > right:
                center, right = i, i + res[i]
        max_len, center = max((value, i) for i, value in enumerate(res))
        return s[(center - 1 - max_len) / 2:(center - 1 + max_len) / 2]


# 214. Shortest Palindrome
class Solution2_1(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # O(n^2) time: TLE, 119 / 120 test cases passed.
        # find longest palindrome prefix (center <= mid)
        mid = len(s) // 2
        for i in range(mid, -1, -1):
            res = self.extend(s, i, i) or self.extend(s, i - 1, i)
            if res:
                return res
        return ''

    def extend(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left, right = left - 1, right + 1
        if left >= 0:
            return None
        # left reaches front of s
        return s[right:][::-1] + s


class Solution2_2(object):
    def shortestPalindrome(self, s):
        # startswith implemented in C: avoid slow compare loop in Python
        r = s[::-1]
        for i in range(len(s) + 1):
            if s.startswith(r[i:]):
                return r[:i] + s


# Longest common subsequence
class Solution3(object):
    def lcs(self, s1, s2):
        # O(mn) time
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]


# Longest common substring
class Solution4(object):
    def lcs_easy(self, s1, s2):
        # O(mn) time
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = 0
        return dp[m][n]
