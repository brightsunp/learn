#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2018/12/4'
'''


class Solution1(object):
    '''Google

    Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
    For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
    '''
    def twoSum(self, nums, k):
        # one-pass
        seen = set()
        for num in nums:
            if k-num in seen:
                return True
            seen.add(num)
        return False


class Solution2(object):
    '''Uber*

    Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i. What if you can't use division?
    For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
    '''
    def productExceptSelf(self, nums):
        # split: left * right
        left, right = [1], [1]
        for num in nums[:-1]:
            left.append(left[-1] * num)
        for num in nums[-1:0:-1]:
            right.append(right[-1] * num)

        res = []
        n = len(nums)
        for i in range(n):
            res.append(left[i] * right[n-1-i])
        return res


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution3(object):
    '''Google*

    Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
    '''
    def serialize(self, root):
        # BFS
        if not root:
            return ''
        queue = [root]
        res = []
        while queue:
            node = queue.pop(0)
            if node:
                res.append(str(node.val) + ' ')
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append('# ')
        return ''.join(res)

    def deserialize(self, data):
        # reverse BFS
        if not data:
            return None
        vals = data.split()
        root = TreeNode(int(vals[0]))
        queue = [root]
        for i in range(1, len(vals), 2):
            parent = queue.pop(0)
            if vals[i] != '#':
                left = TreeNode(int(vals[i]))
                parent.left = left
                queue.append(left)
            if vals[i+1] != '#':
                right = TreeNode(int(vals[i+1]))
                parent.right = right
                queue.append(right)
        return root


class Solution4(object):
    '''Stripe*

    Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well. You can modify the input array in-place.
    For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
    '''
    def firstMissingPositive1(self, nums):
        # hashset
        s = set()
        max_num = 0
        for num in nums:
            if num > 0:
                s.add(num)
                max_num = max(max_num, num)
        for i in range(1, max_num+1):
            if i not in s:
                return i
        return max_num+1

    def firstMissingPositive2(self, nums):
        # swap in-place
        n = len(nums)
        for i in range(n):
            # key point: "while loop"
            while 0 < nums[i] <= n and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n+1


class Solution5(object):
    '''Jane Street

    cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
    For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

    def cons(a, b):
        def pair(f):
            return f(a, b)
        return pair
    Implement car and cdr.
    '''
    def car(self, pair):
        def left(a, b):
            return a
        return pair(left)

    def cdr(self, pair):
        def right(a, b):
            return b
        return pair(right)


class Solution6(object):
    '''Google

    An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node.
    Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.
    '''
    pass


class Solution7(object):
    '''Facebook

    Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
    For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
    '''
    pass


class Solution8(object):
    '''Google

    A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value. Given the root to a binary tree, count the number of unival subtrees.
    For example, the following tree has 5 unival subtrees:
       0
      / \
     1   0
        / \
       1   0
      / \
     1   1
    '''
    pass


class Solution9(object):
    '''Airbnb

    Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
    For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
    '''
    def rob1(self, nums):
        # dp formula: f(n) = max(f(n-2)+num, f(n-1))
        n = len(nums)
        if not n:
            return 0
        dp = [0] * (n + 1)
        dp[1] = nums[0]
        for i in range(2, n + 1):
            dp[i] = max(dp[i - 1], nums[i - 1] + dp[i - 2])
        return dp[n]

    def rob2(self, nums):
        pre = cur = 0
        for num in nums:
            pre, cur = cur, max(pre + num, cur)
        return cur


class Solution10(object):
    '''Apple

    Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
    '''
    pass
