#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/1/18'
'''


def findMajority(nums):
    top, count = -1, 0
    for num in nums:
        if not count:
            top = num
            count += 1
        else:
            if num == top:
                count += 1
            else:
                count -= 1
    return top


if __name__ == '__main__':
    print(findMajority([2, 14, 2, 3, 4, 2, 2, 2, 2, 14]))
