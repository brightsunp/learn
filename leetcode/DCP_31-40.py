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
