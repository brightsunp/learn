#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/1/14'
'''
import hashlib
import random


class Solution1(object):
    '''Facebook*

    Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input, write a function that shuffles a deck of cards represented as an array using only swaps.
    It should run in O(N) time.
    Hint: Make sure each one of the 52! permutations of the deck is equally likely.
    '''
    def shuffle(self):
        cards = [i for i in range(1, 53)]
        for i in range(52):
            r = i - 1 + self.randK(52 - i)
            cards[i], cards[r] = cards[r], cards[i]
        return cards

    def randK(self, k):
        return random.randint(1, k)


class Solution2_1(object):
    '''Google*

    Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:
    - set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the least recently used item.
    - get(key): gets the value at key. If no such key exists, return null.
    Each operation should run in O(1) time.
    '''
    def __init__(self, capacity):
        # {key: [value, prior]}
        self.cap = capacity
        self.d = {}
        self.prior = 0

    def get(self, key):
        if key in self.d:
            self.prior += 1
            self.d[key][1] = self.prior
            return self.d[key][0]
        return -1

    def set(self, key, value):
        if len(self.d) == self.cap and key not in self.d:
            least_used = min((v[1], k) for k, v in self.d.items())
            del self.d[least_used[1]]
        self.prior += 1
        self.d[key] = [value, self.prior]


class DllNode(object):
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None


class Solution2_2(object):
    def __init__(self, capacity):
        self.cap = capacity
        self.d = {}
        self.head, self.tail = DllNode(0, 0), DllNode(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key):
        if key in self.d:
            node = self.d[key]
            self._remove(node)
            self._add(node)
            return node.val
        return -1

    def set(self, key, value):
        if key in self.d:
            self._remove(self.d[key])
        node = DllNode(key, value)
        self._add(node)
        self.d[key] = node
        if len(self.d) > self.cap:
            h = self.head.next
            self._remove(h)
            del self.d[h.key]

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node):
        t = self.tail.prev
        t.next = node
        self.tail.prev = node
        node.prev = t
        node.next = self.tail


class Solution3_1(object):
    '''Apple*

    Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods:
    - enqueue, which inserts an element into the queue.
    - dequeue, which removes it.
    '''
    def __init__(self):
        self.store = []
        self.buffer = []

    def enqueue(self, x):
        self.store.append(x)

    def dequeue(self):
        if self.buffer:
            return self.buffer.pop()
        while self.store:
            self.buffer.append(self.store.pop())
        return self.buffer.pop()


class Solution3_2(object):
    '''
    Implement Stack using Queues
    '''
    def __init__(self):
        self.queue = []

    def push(self, x):
        # convert queue to stack
        self.queue.append(x)
        for _ in range(1, len(self.queue)):
            self.queue.append(self.queue.pop(0))

    def pop(self):
        return self.queue.pop(0)

    def top(self):
        return self.queue[0]

    def empty(self):
        return not self.queue


class Solution4(object):
    '''Dropbox

    Sudoku is a puzzle where you're given a partially-filled 9 by 9 grid with digits. The objective is to fill the grid with the constraint that every row, column, and box (3 by 3 subgrid) must contain all of the digits from 1 to 9. Implement an efficient sudoku solver.
    '''
    pass


class Solution5(object):
    '''Microsoft*

    Implement a URL shortener with the following methods:
    - shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
    - restore(short), which expands the shortened string into the original url. If no such shortened string exists, return null.
    Hint: What if we enter the same URL twice?
    '''
    def __init__(self):
        self.d = {}
        self.m = hashlib.sha256

    def shorten(self, url):
        sha_sign = self.m(url.encode()).hexdigest()
        short_hash = sha_sign[:6]
        self.d[short_hash] = url
        return short_hash

    def restore(self, short):
        return self.d.get(short, None)


class Solution6(object):
    '''Google

    Given an undirected graph represented as an adjacency matrix and an integer k, write a function to determine whether each vertex in the graph can be colored such that no two adjacent vertices share the same color using at most k colors.
    '''
    pass


class Solution7(object):
    '''Amazon

    Given a string s and an integer k, break up the string into multiple texts such that each text has a length of k or less. You must break it up so that words don't break across lines. If there's no way to break the text up, then return null.
    You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.
    Given the string "the quick brown fox jumps over the lazy dog", k = 10 => ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No string in the list has a length of more than 10.
    '''
    def text_break(self, text):
        pass


class Solution8(object):
    '''Amazon*

    An sorted array of integers was rotated an unknown number of times. Given such an array, find the index of the element in the array in faster than linear time. If the element doesn't exist in the array, return null.
    Given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array). You can assume all the integers in the array are unique.
    '''
    def find_num(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                return mid
            elif nums[mid] < nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1


class Solution9(object):
    '''Google*

    Implement a file syncing algorithm for two computers over a low-bandwidth network. What if we know the files in the two computers are mostly the same?
    https://ianhowson.com/blog/file-synchronisation-algorithms/
    https://unterwaditzer.net/2016/sync-algorithm.html
    '''
    pass


class Solution10(object):
    '''Facebook

    Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.
    {15, 5, 20, 10, 35, 15, 10} => true: since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.
    {15, 5, 20, 10, 35} => false: since we can't split it up into two subsets that add up to the same sum.
    '''
    def is_split(self, nums):
        target = sum(nums)
        if target & 1 == 1:
            return False
        target >>= 1
        # convert to combination-sum (Problem #42)
        return self.dfs(nums, target, 0)

    def dfs(self, nums, target, pos):
        if target < 0:
            return False
        if target == 0:
            return True
        for i in range(pos, len(nums)):
            if self.dfs(nums, target-nums[i], i+1):
                return True
        return False


if __name__ == '__main__':
    test1 = Solution1()
    for _ in range(10):
        assert all(x in test1.shuffle() for x in range(1, 53))

    test5 = Solution5()
    long_url = 'https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/0013868328251266d86585fc9514536a638f06b41908d44000'
    assert len(test5.shorten(long_url)) == 6
    assert test5.restore(test5.shorten(long_url)) == long_url

    test8 = Solution8()
    assert test8.find_num([13, 18, 25, 2, 8, 10], 8) == 4
    assert test8.find_num([25, 2, 8, 10, 13, 18], 8) == 2
    assert test8.find_num([8, 10, 13, 18, 25, 2], 7) == -1

    test10 = Solution10()
    assert test10.is_split([15, 5, 20, 10, 35, 15, 10])
    assert not test10.is_split([15, 5, 20, 10, 35])
