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


class Solution2(object):
    '''Google

    Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:
    - set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the least recently used item.
    - get(key): gets the value at key. If no such key exists, return null.
    Each operation should run in O(1) time.
    '''
    pass


class Solution3(object):
    '''Apple

    Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods:
    - enqueue, which inserts an element into the queue.
    - dequeue, which removes it.
    '''
    pass
