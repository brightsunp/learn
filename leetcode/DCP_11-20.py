#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2018/12/14'
'''
import random, sys


class Solution1(object):
    '''Twitter*

    Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.
    For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
    Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
    '''
    def autoComplete(self, words, prefix):
        trie = self.build_trie(words)
        # startsWith
        cur = trie
        for char in prefix:
            cur = cur.get(char)
            if not cur:
                return []
        res, stack = [], [cur]
        while stack:
            to_search = stack.pop()
            for k, v in to_search.items():
                if k == 'word':
                    res.append(v)
                else:
                    stack.append(v)
        return res

    def build_trie(self, words):
        trie = {}
        for word in words:
            # insert
            cur = trie
            for char in word:
                cur = cur.setdefault(char, {})
            # isLeaf & search
            cur['word'] = word
        return trie


class Solution2(object):
    '''Amazon

    There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.
    For example, if N is 4, then there are 5 unique ways:

    1, 1, 1, 1
    2, 1, 1
    1, 2, 1
    1, 1, 2
    2, 2
    What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
    '''
    def climb(self, n):
        pass


class Solution3(object):
    '''Amazon*

    Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
    For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
    '''
    def longestSubstringKDistinct(self, s, k):
        # maintain a valid window
        max_len = max_left = left = 0
        counter = {}
        for right in range(len(s)):
            counter[s[right]] = counter.get(s[right], 0) + 1
            while len(counter) > k:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    counter.pop(s[left])
                left += 1
            if right-left+1 > max_len:
                max_len, max_left = right-left+1, left
        return s[max_left:max_left+max_len]


class Solution4(object):
    '''Google*

    The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.
    Hint: The basic equation of a circle is x^2 + y^2 = r^2.
    '''
    def estimatePi(self):
        # Process [estimatePi] completed: 579.40 secs.
        count = 0
        for i in range(10**9):
            x = random.random()
            y = random.random()
            if x**2 + y**2 < 1:
                count += 1
        return '{:.4f}'.format(count * 4.0 / 10**9)


class Solution5(object):
    '''Facebook*

    Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
    '''
    def getRandom(self, stream, n):
        # uniform probability: 1/(i+1), i=n-1 => 1/n
        res = None
        for i in range(n):
            if random.randrange(i+1) == 0:
                res = stream[i]
        return res

    def getRandomK(self, stream, n, k):
        # Reservoir sampling
        res = []
        for i in range(k):
            res.append(stream[i])
        for i in range(k, n):
            j = random.randrange(i+1)
            if j < k:
                res[j] = stream[i]
        return res


class Solution6(object):
    '''Twitter

    You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:
    - record(order_id): adds the order_id to the log
    - get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
    '''
    pass


class Solution7(object):
    '''Google*

    Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.
    In the string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext", the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).
    '''
    def lengthLongestPath(self, input):
        # hashmap {depth: cur_len}
        d = {0: 0}
        max_len = 0
        for line in input.split('\n'):
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            if '.' in name:
                max_len = max(max_len, d[depth] + len(name))
            else:
                d[depth+1] = d[depth] + len(name) + 1
        return max_len



class Solution8(object):
    '''Google*

    Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.
    For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:
    Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.
    '''
    def maxSlidingWindow(self, nums, k):
        # deque: store useful indexes in num-decreasing order
        res = []
        deque = []
        for i, num in enumerate(nums):
            while deque and num >= nums[deque[-1]]:
                deque.pop()
            deque.append(i)
            # remove indexes out of window
            if deque[0] == i-k:
                deque.pop(0)
            if i >= k-1:
                res.append(nums[deque[0]])
        return res


class Solution9(object):
    '''Facebook*

    A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.
    Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.
    '''
    def minCost(self, costs):
        if not len(costs) or not len(costs[0]):
            return 0
        n, k = len(costs), len(costs[0])
        min1, min2, pre = 0, 0, -1
        for i in range(n):
            # MAX_INT = sys.maxint if Python2 else sys.maxsize
            m1, m2, cur = sys.maxsize, sys.maxsize, -1
            for j in range(k):
                cur_cost = costs[i][j] + (min2 if j==pre else min1)
                if cur_cost < m1:
                    m1, m2, cur = cur_cost, m1, j
                elif cur_cost < m2:
                    m2 = cur_cost
            # updated when i steps forward
            min1, min2, pre = m1, m2, cur
        return min1               


class Solution10(object):
    '''Google

    Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.
    For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.
    Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
    '''
    def getIntersectionNode(self, headA, headB):
        # no need to calc len's difference
        # if intersect, meet at intersection; else meet at tail[None]
        if not (headA and headB):
            return None
        curA, curB = headA, headB
        while curA != curB:
            curA = curA.next if curA else headB
            curB = curB.next if curB else headA
        return curA


if __name__ == '__main__':
    test1 = Solution1()
    print(test1.autoComplete(['dog', 'deer', 'deal'], 'de'))

    test4 = Solution4()
    print(test4.estimatePi())
