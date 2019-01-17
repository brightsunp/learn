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
