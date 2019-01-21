#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/1/17'

How to solve a hard question:
Find the naive solution, then optimize it.
'''


class Solution1(object):
    '''
    Largest Rectangle in Histogram

    Naive: for each bar, find left and right where height is lower, then calculate max_area containing this bar.
    '''
    def largestRectangleArea(self, heights):
        # increment stack
        res, stack = 0, []
        heights.append(0)
        for i, height in enumerate(heights):
            while stack and heights[stack[-1]] >= height:
                left = stack.pop()
                res = max(res, heights[left] * (i-(stack[-1] if stack else -1)-1))
            stack.append(i)
        return res


class Solution2_1(object):
    '''
    Longest Increasing Subsequence
    '''
    def lengthOfLIS(self, nums):
        # dp: f(i) = max(f(j where nums[j] < nums[i]) + 1, j: 0->i-1)
        dp = [1 for _ in range(len(nums))]
        max_len = 0
        for i, cur in enumerate(nums):
            for j in range(i):
                if nums[j] < cur:
                    dp[i] = max(dp[i], dp[j] + 1)
            max_len = max(max_len, dp[i])
        return max_len


class Solution2_2(object):
    '''
    Number of Longest Increasing Subsequence
    '''
    def findNumberOfLIS(self, nums):
        if not nums:
            return 0
        dp = [[1, 1] for _ in range(len(nums))]
        max_len = 1
        for i, cur in enumerate(nums):
            for j in range(i):
                if nums[j] < cur:
                    tmp = dp[j][0] + 1
                    if tmp > dp[i][0]:
                        dp[i] = [tmp, dp[j][1]]
                    elif tmp == dp[i][0]:
                        dp[i][1] += dp[j][1]
            max_len = max(max_len, dp[i][0])
        return sum(res[1] for res in dp if res[0] == max_len)
