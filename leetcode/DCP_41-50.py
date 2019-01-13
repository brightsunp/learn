#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/1/7'
'''

import random


class Solution1(object):
    '''Facebook

    Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport, compute the person's itinerary. If no such itinerary exists, return null. If there are multiple possible itineraries, return the lexicographically smallest one. All flights must be used in the itinerary.
    Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. However, the first one is lexicographically smaller.
    '''
    pass


class Solution2(object):
    '''Google*

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
    def __init__(self):
        # each element is a tuple (val, cur_max)
        self.stack = []

    def push(self, val):
        cur_max = self.stack[-1][1] if self.stack else 0
        cur_max = max(cur_max, val)
        self.stack.append((val, cur_max))

    def pop(self):
        return self.stack.pop()[0] if self.stack else None

    def max(self):
        return self.stack[-1][1] if self.stack else None


class Solution4(object):
    '''Google*

    We can determine how "out of order" an array A is by counting the number of inversions it has. Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller element appears after a larger element.
    Given an array, count the number of inversions it has. Do this faster than O(N^2) time. You may assume each element in the array is distinct.
    For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3). The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.
    '''
    def countInversions1(self, nums):
        # O(n^2)
        count = 0
        for i, pre in enumerate(nums):
            for cur in nums[i+1:]:
                count += 1 if pre > cur else 0
        return count
        
    def countInversions2(self, nums):
        # O(nlogn): mergeSort
        pass


class Solution5(object):
    '''Two Sigma

    Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability, implement a function rand7() that returns an integer from 1 to 7 (inclusive).
    '''
    def rand7(self):
        # 1-bit: rand() in [1, N]
        # 2-bits: (rand()-1)*N + rand()
        x = 22
        while x > 21:
            x = (self.rand5()-1)*5 + self.rand5()
        return 1 + x % 7

    def rand5(self):
        return random.randint(1, 5)


class Solution6(object):
    '''Amazon

    Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length, return any one.
    For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of "bananas" is "anana".
    '''
    def longestPalindrome(self, s):
        # O(n^2) time and O(1) space
        max_len = start = 0
        for i in range(len(s)):
            cur_len = max(self.extend(s, i, i), self.extend(s, i-1, i))
            if cur_len > max_len:
                max_len, start = cur_len, i - cur_len//2
        return s[start:start+max_len]

    def extend(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left, right = left-1, right+1
        return right-left-1


class Solution7(object):
    '''Facebook*

    Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.
    For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.
    '''
    def buyOnce(self, prices):
        if len(prices) < 2:
            return 0
        max_profit = max_cur = 0
        for i in range(1, len(prices)):
            # sell to get cur_profit
            max_cur = max(0, max_cur+prices[i]-prices[i-1])
            max_profit = max(max_profit, max_cur)
        return max_profit

    def buyAsMany(self, prices):
        if len(prices) < 2:
            return 0
        profit = 0
        for i in range(1, len(prices)):
            # sell only if price increased
            profit += max(0, prices[i]-prices[i-1])
        return profit

    def buyAtMostK(self, prices, k):
        '''Not so hard to understand.
        https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/discuss/54113/A-Concise-DP-Solution-in-Java/55579
        '''
        n = len(prices)
        # avoid MemoryError
        if k >= (n>>1):
            return self.buyAsMany(prices)
        dp = [[0] * n for _ in range(k+1)]
        for i in range(1, k+1):
            # reduce O(knn) to O(kn)
            tmp = -prices[0]
            for j in range(1, n):
                # sell or not sell
                dp[i][j] = max(dp[i][j-1], prices[j]+tmp)
                tmp = max(tmp, dp[i-1][j-1]-prices[j])
        return dp[k][n-1]


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution8_1(object):
    '''Google*

    Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree. You may assume that duplicates do not exist in the tree.

    For example, given the following preorder traversal:
    [a, b, d, e, c, f, g]
    And the following inorder traversal:
    [d, b, e, a, f, c, g]
    You should return the following tree:
        a
       / \
      b   c
     / \ / \
    d  e f  g
    '''
    def buildTree1(self, preorder, inorder):
        # recursive1 [284ms]
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        pos = inorder.index(preorder[0])
        root.left = self.buildTree1(preorder[1:pos+1], inorder[:pos])
        root.right = self.buildTree1(preorder[pos+1:], inorder[pos+1:])
        return root

    def buildTree2(self, preorder, inorder):
        # recursive2 [48ms]
        self.in_map = {val: i for i, val in enumerate(inorder)}
        self.preorder = preorder
        self.inorder = inorder
        return self.helper(0, len(preorder), 0, len(inorder))

    def helper(self, pre_beg, pre_end, in_beg, in_end):
        if pre_beg >= pre_end:
            return None
        root = TreeNode(self.preorder[pre_beg])
        in_root = self.in_map[root.val]
        offset = in_root - in_beg
        root.left = self.helper(pre_beg+1, pre_beg+offset+1, in_beg, in_root)
        root.right = self.helper(pre_beg+offset+1, pre_end, in_root+1, in_end)
        return root

    def buildTree3(self, preorder, inorder):
        # iterative [48ms]
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        stack = [root]
        i, j = 1, 0
        while i < len(preorder):
            cur = TreeNode(preorder[i])
            mark = None
            # comes to an end of the left node
            while stack and stack[-1].val == inorder[j]:
                mark = stack.pop()
                j += 1
            if mark:
                mark.right = cur
            else:
                stack[-1].left = cur
            stack.append(cur)
            i += 1
        return root


class Solution8_2(object):
    '''
    Construct Binary Tree from Preorder and Postorder Traversal
    '''
    def constructFromPrePost(self, pre, post):
        # iterative
        if not pre:
            return None
        root = TreeNode(pre[0])
        stack = [root]
        i, j = 1, 0
        while i < len(pre):
            cur = TreeNode(pre[i])
            while stack and stack[-1].val == post[j]:
                stack.pop()
                j += 1
            if stack[-1].left:
                stack[-1].right = cur
            else:
                stack[-1].left = cur
            stack.append(cur)
            i += 1
        return root


class Solution9(object):
    '''Amazon

    Given an array of numbers, find the maximum sum of any contiguous subarray of the array. Do this in O(N) time.
    For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.
    Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.
    '''
    def maxSumSubarray(self, nums):
        # f(n) = max(f(n-1)+num, 0)
        res = pre = 0
        for num in nums:
            pre = max(pre+num, 0)
            res = max(res, pre)
        return res


class Solution10(object):
    '''Microsoft*
    
    Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.
    Given the root to such a tree, write a function to evaluate it.
    For example, given the following tree:

        *
       / \
      +    +
     / \  / \
    3  2  4  5
    You should return 45, as it is (3 + 2) * (4 + 5).
    https://blog.csdn.net/mhxy199288/article/details/38025319
    '''
    def evaluate(self, root):
        # Reverse Polish: postorder traverse
        self.vals = []
        self.postorder(root)
        stack = []
        for val in self.vals:
            if isinstance(val, int):
                stack.append(val)
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(self.operate(a, b, val))
        # one element remains in the stack
        return stack[0]
        
    def postorder(self, root):
        if not root:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        self.vals.append(root.val)
        
    def operate(self, a, b, operator):
        d = {'+': a+b, '-': a-b, '*': a*b, '/': a/b}
        return d[operator]


if __name__ == '__main__':
    test2 = Solution2()
    print(test2.combinationSum([12, 1, 61, 5, 9, 2], 24))
    
    test4 = Solution4()
    print(test4.countInversions1([2, 4, 1, 3, 5]))
    print(test4.countInversions2([2, 4, 1, 3, 5]))
    
    test9 = Solution9()
    print(test9.maxSumSubarray([34, -50, 42, 14, -5, 86]))
    print(test9.maxSumSubarray([-5, -1, -8, -9]))
    
    test10 = Solution10()
    node = TreeNode('*')
    node.left = TreeNode('+')
    node.left.left = TreeNode(3)
    node.left.right = TreeNode(2)
    node.right = TreeNode('+')
    node.right.left = TreeNode(4)
    node.right.right = TreeNode(5)
    print(test10.evaluate(node))
