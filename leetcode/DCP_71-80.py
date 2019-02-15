#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/2/11'
'''
import unittest, random
from functools import reduce


class Solution1(object):
    '''Two Sigma

    Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability, implement a function rand5() that returns an integer from 1 to 5 (inclusive).
    '''
    def rand5(self):
        x = 6
        while x > 5:
            x = self._rand7()
        return x

    def _rand7(self):
        return random.randint(1, 7)


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


class LinkNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution3(object):
    '''Google*

    Given the head of a singly linked list, reverse it in-place.
    '''
    def reverse1(self, root):
        # auxiliary stack
        stack = []
        cur, head = root, root
        while cur:
            stack.append(cur.val)
            cur = cur.next
        while root:
            root.val = stack.pop()
            root = root.next
        return head

    def reverse2(self, root):
        # recursive
        if not root or not root.next:
            return root
        new_head = self.reverse2(root.next)
        # root.next just reversed, so it refers to last of new_head
        root.next.next = root
        root.next = None
        return new_head

    def reverse3(self, root):
        # iterative
        new_head = None
        while root:
            tmp = root.next
            # point to new_head
            root.next = new_head
            # update new_head
            new_head = root
            root = tmp
        return new_head


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
    '''Microsoft*

    Given an array of numbers, find the length of the longest increasing subsequence in the array. The subsequence does not necessarily have to be contiguous.
    For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.
    '''
    def lis1(self, arr):
        # dp: LIS ending with arr[i]
        n = len(arr)
        dp = [1 for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                if arr[i] > arr[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp) if dp else 0

    def lis2(self, arr):
        # O(nlogk)
        if not arr:
            return 0
        n, res = len(arr), 1
        tails = [0 for _ in range(n)]
        tails[0] = arr[0]
        for i in range(1, n):
            if arr[i] < tails[0]:
                tails[0] = arr[i]
            elif arr[i] > tails[res-1]:
                tails[res] = arr[i]
                res += 1
            else:
                tails[self._find(tails, 0, res-1, arr[i])] = arr[i]
        return res

    def _find(self, A, lo, hi, num):
        # first target >= num
        while lo <= hi:
            mid = (lo+hi) >> 1
            if A[mid] >= num:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo


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
    def merge(self, intervals):
        res = []
        for interval in sorted(intervals, key=lambda item: item[0]):
            if not res:
                res.append(interval)
            else:
                start, end = interval
                head, tail = res[-1]
                if start > tail:
                    res.append(interval)
                else:
                    del res[-1]
                    res.append((head, max(tail, end)))
        return res


class Solution8(object):
    '''Google

    Given k sorted singly linked lists, write a function to merge all the lists into one sorted singly linked list.
    '''
    def merge1(self, lists):
        # iterative: O(nk)
        return reduce(self._merge, lists, None)

    def _merge(self, head1, head2):
        if not head1 or not head2:
            return head1 or head2
        head, pre, cur = None, None, None
        while head1 and head2:
            if head1.val < head2.val:
                cur = head1
                head1 = head1.next
            else:
                cur = head2
                head2 = head2.next
            if pre:
                pre.next = cur
            pre = cur
            if not head:
                head = cur
        pre.next = head1 or head2
        return head

    def merge2(self, lists):
        # PriorityQueue: O(nlogk)
        pass


class Solution9(object):
    '''Facebook*

    Given an array of integers, write a function to determine whether the array could become non-decreasing by modifying at most 1 element.
    For example, given the array [10, 5, 7], you should return true, since we can modify the 10 into a 1 to make the array non-decreasing.
    Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a non-decreasing array.
    '''
    def check(self, arr):
        # greedy: fix monotonic
        count = 0
        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                count += 1
                if i < 2 or arr[i-2] <= arr[i]:
                    # now arr[i-1] is remain_min
                    arr[i-1] = arr[i]
                else:
                    # now arr[i] is front_max
                    arr[i] = arr[i-1]
        return count <= 1


class Solution10(object):
    '''Google

    Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.
        a
       / \
      b   c
     /
    d
    '''
    def deepest(self, root):
        # level order
        height = self._height(root)
        res, queue = None, root and [root]
        while queue:
            if height == 1:
                res = queue.pop(0)
                break
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            height -= 1
        return res

    def _height(self, root):
        if not root:
            return 0
        return 1 + max(self._height(root.left), self._height(root.right))


class TestSolutions(unittest.TestCase):
    def test_solution1(self):
        sol = Solution1()

        n_experiments = 100000
        res_probability = 1 / 5
        res_arr = [0 for _ in range(5)]
        for _ in range(n_experiments):
            tmp = sol.rand5()
            res_arr[tmp-1] += 1
        for res in res_arr:
            self.assertAlmostEqual(res_probability, res / n_experiments, places=2)

    def test_solution3(self):
        sol = Solution3()
        arg = LinkNode(1)
        arg.next = LinkNode(2)
        arg.next.next = LinkNode(3)

        arg = sol.reverse1(arg)
        res1, cur1 = [], arg
        while cur1:
            res1.append(cur1.val)
            cur1 = cur1.next
        self.assertEqual(res1, [3, 2, 1])

        arg = sol.reverse2(arg)
        res2, cur2 = [], arg
        while cur2:
            res2.append(cur2.val)
            cur2 = cur2.next
        self.assertEqual(res2, [1, 2, 3])

        arg = sol.reverse3(arg)
        res3, cur3 = [], arg
        while cur3:
            res3.append(cur3.val)
            cur3 = cur3.next
        self.assertEqual(res3, [3, 2, 1])

    def test_solution5(self):
        sol = Solution5()

        self.assertEqual(sol.lis1([]), 0)
        self.assertEqual(sol.lis1([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]), 6)
        self.assertEqual(sol.lis2([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]), 6)

    def test_solution7(self):
        sol = Solution7()

        self.assertEqual(sol.merge([(1, 3), (5, 8), (4, 10), (20, 25)]), [(1, 3), (4, 10), (20, 25)])
        self.assertEqual(sol.merge([(1, 3), (5, 8), (4, 10), (20, 25), (6, 12)]), [(1, 3), (4, 12), (20, 25)])

    def test_solution9(self):
        sol = Solution9()

        self.assertTrue(sol.check([4, 2, 3]))
        self.assertFalse(sol.check([4, 2, 1]))
        self.assertFalse(sol.check([3, 4, 2, 3]))


if __name__ == '__main__':
    unittest.main()
