#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2018/12/4'
'''


class Solution1(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # split: left * right
        # no need to calc: ProductOfEntireNums
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


class Solution2(object):
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # BFS
        res = ''
        if not root: return res
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                res += str(node.val) + ' '
                queue.append(node.left)
                queue.append(node.right)
            else:
                res += '# '
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # reverse BFS
        if not data: return None
        vals = data.split()
        root = TreeNode(int(vals[0]))
        queue = [root]
        i = 1
        while i < len(vals):
            parent = queue.pop(0)
            if vals[i] != '#':
                left = TreeNode(int(vals[i]))
                parent.left = left
                queue.append(left)
            i += 1
            if vals[i] != '#':
                right = TreeNode(int(vals[i]))
                parent.right = right
                queue.append(right)
            i += 1
        return root


class Solution3(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
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

        # use set
        # s = set()
        # max_num = 0
        # for num in nums:
        #     if num > 0:
        #         s.add(num)
        #         max_num = max(max_num, num)
        # for i in range(1, max_num+1):
        #     if i not in s:
        #         return i
        # return max_num+1


class Solution4(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp formula: f(n) = max(f(n-2)+nums[n-1], f(n-1))
        pre = cur = 0
        for num in nums:
            pre, cur = cur, max(pre + num, cur)
        return cur

        # n = len(nums)
        # if not n:
        #     return 0
        # dp = [0] * (n+1)
        # dp[1] = nums[0]
        # for i in range(2, n+1):
        #     dp[i] = max(dp[i-1], nums[i-1]+dp[i-2])
        # return dp[n]
