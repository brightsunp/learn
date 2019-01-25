#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/1/25'
'''


def search_eq(arr, x):
    # find element == x
    lo, hi = 0, len(arr)-1
    while lo <= hi:
        mid = (lo + hi) >> 1
        if x == arr[mid]:
            return mid
        elif x < arr[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1


def search_ge(arr, x):
    # find first element >= x
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) >> 1
        if x <= arr[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return lo


def search_gt(arr, x):
    # find first element > x
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) >> 1
        if x < arr[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return lo


if __name__ == '__main__':
    A = [2, 4, 5, 6, 9]
    B = [2, 4, 4, 5, 5, 5, 6, 9]

    assert search_eq(A, 4) == 1
    assert search_eq(A, 3) == -1

    assert search_ge(B, 4) == 1
    assert search_ge(B, 7) == 7

    assert search_gt(B, 4) == 3
    assert search_gt(B, 5) == 6
