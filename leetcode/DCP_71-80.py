#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/2/11'
'''


class Solution1(object):
    '''Two Sigma

    Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability, implement a function rand5() that returns an integer from 1 to 5 (inclusive).
    '''
    pass


class Solution2(object):
    '''Google

    In a directed graph, each node is assigned an uppercase letter. We define a path's value as the number of most frequently-occurring letter along that path. For example, if a path in the graph goes through "ABACA", the value of the path is 3, since there are 3 occurrences of 'A' on the path.
    Given a graph with n nodes and m directed edges, return the largest value path of the graph. If the largest value is infinite, then return null.
    The graph is represented with a string and an edge list. The i-th character represents the uppercase letter of the i-th node. Each tuple in the edge list (i, j) means there is a directed edge from the i-th node to the j-th node. Self-edges are possible, as well as multi-edges.

    For example, the following input graph:
    ABACA
    [(0, 1),
     (0, 2),
     (2, 3),
     (3, 4)]
    Would have maximum value 3 using the path of vertices [0, 2, 3, 4], (A, A, C, A).
    The following input graph:
    A
    [(0, 0)]
    Should return null, since we have an infinite loop.
    '''
    pass


class Solution3(object):
    '''Google

    Given the head of a singly linked list, reverse it in-place.
    '''
    pass


class Solution4(object):
    '''Apple

    Suppose you have a multiplication table that is N by N. That is, a 2D array where the value at the i-th row and j-th column is (i + 1) * (j + 1) (if 0-indexed) or i * j (if 1-indexed).
    Given integers N and X, write a function that returns the number of times X appears as a value in an N by N multiplication table.

    For example, given N = 6 and X = 12, you should return 4, since the multiplication table looks like this:
    | 1 | 2 | 3 | 4 | 5 | 6 |
    | 2 | 4 | 6 | 8 | 10 | 12 |
    | 3 | 6 | 9 | 12 | 15 | 18 |
    | 4 | 8 | 12 | 16 | 20 | 24 |
    | 5 | 10 | 15 | 20 | 25 | 30 |
    | 6 | 12 | 18 | 24 | 30 | 36 |
    And there are 4 12's in the table.
    '''
    pass


class Solution5(object):
    '''Microsoft

    Given an array of numbers, find the length of the longest increasing subsequence in the array. The subsequence does not necessarily have to be contiguous.
    For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.
    '''
    pass


class Solution6(object):
    '''Google

    You are given an N by M 2D matrix of lowercase letters. Determine the minimum number of columns that can be removed to ensure that each row is ordered from top to bottom lexicographically. That is, the letter at each column is lexicographically later as you go down each row. It does not matter whether each row itself is ordered lexicographically.

    For example, given the following table:
    cba
    daf
    ghi
    This is not ordered because of the a in the center. We can remove the second column to make it ordered:
    ca
    df
    gi
    So your function should return 1, since we only needed to remove 1 column.

    As another example, given the following table:
    abcdef
    Your function should return 0, since the rows are already ordered (there's only one row).

    As another example, given the following table:
    zyx
    wvu
    tsr
    Your function should return 3, since we would need to remove all the columns to order it.
    '''
    pass


class Solution7(object):
    '''Snapchat

    Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.
    The input list is not necessarily ordered in any way.
    For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].
    '''
    pass


class Solution8(object):
    '''Google

    Given k sorted singly linked lists, write a function to merge all the lists into one sorted singly linked list.
    '''
    pass


class Solution9(object):
    '''Facebook

    Given an array of integers, write a function to determine whether the array could become non-decreasing by modifying at most 1 element.
    For example, given the array [10, 5, 7], you should return true, since we can modify the 10 into a 1 to make the array non-decreasing.
    Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a non-decreasing array.
    '''
    pass
