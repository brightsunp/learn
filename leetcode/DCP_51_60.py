#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/1/14'
'''

import random


class Solution1(object):
    '''Facebook*

    Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input, write a function that shuffles a deck of cards represented as an array using only swaps.
    It should run in O(N) time.
    Hint: Make sure each one of the 52! permutations of the deck is equally likely.
    https://gaohaoyang.github.io/2016/10/16/shuffle-algorithm/
    '''
    def shuffle(self, cards, k):
        for i in range(52):
            r = i - 1 + self.randK(k) % (52 - i)
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

    def put(self, key, value):
        if len(self.d) == self.cap and key not in self.d:
            least_used = min((v[1], k) for k, v in self.d.items())
            del self.d[least_used[1]]
        self.prior += 1
        self.d[key] = [value, self.prior]


class DllNode(object):
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev, self.next = None, None


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

    def put(self, key, value):
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
    '''Microsoft

    Implement a URL shortener with the following methods:
    - shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
    - restore(short), which expands the shortened string into the original url. If no such shortened string exists, return null.
    Hint: What if we enter the same URL twice?
    '''
    pass
