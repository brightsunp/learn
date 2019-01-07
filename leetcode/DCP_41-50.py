#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/1/7'
'''


class Solution1(object):
    '''Facebook

    Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport, compute the person's itinerary. If no such itinerary exists, return null. If there are multiple possible itineraries, return the lexicographically smallest one. All flights must be used in the itinerary.
    Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. However, the first one is lexicographically smaller.
    '''
    pass


class Solution2(object):
    '''Google

    Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.
    Integers can appear more than once in the list. You may assume all numbers in the list are positive.
    Given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.
    '''
    def combinationSum(self, nums, k):
        # find one solution
        self.res = []
        self.dfs(nums, k, 0)
        return self.res or None

    def dfs(self, nums, k, pos):
        if k < 0:
            return False
        if k == 0:
            return True
        for i in range(pos, len(nums)):
            self.res.append(nums[i])
            if self.dfs(nums, k-nums[i], i+1):
                return True
            else:
                self.res.pop()
        return False


class Solution3(object):
    '''Amazon

    Implement a stack that has the following methods:
    - push(val), which pushes an element onto the stack
    - pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
    - max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.
    Each method should run in constant time.
    '''
    pass


class Solution4(object):
    '''Google

    We can determine how "out of order" an array A is by counting the number of inversions it has. Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller element appears after a larger element.
    Given an array, count the number of inversions it has. Do this faster than O(N^2) time.
    You may assume each element in the array is distinct.
    For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3). The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.
    '''
    pass


if __name__ == '__main__':
    sol = Solution2()
    s = [2,3,6,7]
    k = 7
    print(sol.combinationSum(s, k))
