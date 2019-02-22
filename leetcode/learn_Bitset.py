#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/2/22'
'''
from array import array


class BitSet(object):
    '''
    to be optimized: handle `pos >= self.size()`
    '''
    def __init__(self, capacity):
        self.capacity = capacity
        self.unit_size = 8
        self.unit_count = int(capacity / self.unit_size) + 1
        self.arr = array('B', [0] * self.unit_count)

    def set(self, pos=-1):
        if pos == -1:
            mask = (1 << self.unit_size) - 1
            for i in range(self.unit_count):
                self.arr[i] |= mask
        else:
            idx, offset = self._pair(pos)
            self.arr[idx] |= (1 << offset)

    def get(self, pos):
        idx, offset = self._pair(pos)
        return (self.arr[idx] >> offset) & 1

    def reset(self, pos=-1):
        if pos == -1:
            for i in range(self.unit_count):
                self.arr[i] = 0
        else:
            idx, offset = self._pair(pos)
            self.arr[idx] &= ~(1 << offset)

    def flip(self, pos=-1):
        if pos == -1:
            for i in range(self.unit_count):
                self.arr[i] = ~self.arr[i]
        else:
            idx, offset = self._pair(pos)
            self.arr[idx] ^= (1 << offset)

    def size(self):
        return self.unit_count * self.unit_size

    def show(self):
        print(self.arr)

    def _pair(self, pos):
        idx = int(pos / self.unit_size)
        offset = pos % self.unit_size
        return idx, offset


if __name__ == '__main__':
    test = BitSet(20)

    assert test.size() == 24
    assert test.get(0) == 0
    test.set(0)
    assert test.get(0) == 1
    test.reset(0)
    assert test.get(0) == 0
    test.flip(0)
    assert test.get(0) == 1
    test.flip(0)
    assert test.get(0) == 0
