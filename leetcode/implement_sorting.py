#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/1/14'
'''

import math, random


def bubble_sort(nums):
    # swap
    n = len(nums)
    for i in range(n-1):
        for j in range(n-1-i):
            if nums[j+1] < nums[j]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


def select_sort(nums):
    # selection
    n = len(nums)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums


def insert_sort(nums):
    # insertion
    for i in range(1, len(nums)):
        pre_idx, cur = i-1, nums[i]
        while pre_idx >= 0 and cur < nums[pre_idx]:
            nums[pre_idx+1] = nums[pre_idx]
            pre_idx -= 1
        nums[pre_idx+1] = cur
    return nums


def merge_sort(nums):
    # divide and conquer
    n = len(nums)
    if n < 2:
        return nums
    mid = n >> 1
    return _merge(merge_sort(nums[:mid]), merge_sort(nums[mid:]))


def _merge(nums1, nums2):
    res = []
    i = j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            res.append(nums1[i])
            i += 1
        else:
            res.append(nums2[j])
            j += 1
    res.extend(nums1[i:] + nums2[j:])
    return res


def quick_sort(nums, left, right):
    # swap
    if left < right:
        pivot_idx = _partition(nums, left, right)
        quick_sort(nums, left, pivot_idx-1)
        quick_sort(nums, pivot_idx+1, right)


def _partition(nums, left, right):
    # random selection
    pivot = random.randint(left, right)
    nums[pivot], nums[right] = nums[right], nums[pivot]
    idx = left
    for i in range(left, right):
        if nums[i] <= nums[right]:
            nums[i], nums[idx] = nums[idx], nums[i]
            idx += 1
    nums[right], nums[idx] = nums[idx], nums[right]
    return idx


def heap_sort(nums):
    # heap
    min_heap = _build_heap(nums)
    for i in range(len(nums)):
        nums[i] = min_heap.pop(0)
        _heapify(min_heap, 0)


def _build_heap(nums):
    res = nums[:]
    for i in range(len(res)>>1 + 1):
        _heapify(res, i)
    return res


def _heapify(nums, i):
    left, right, min_idx = i*2+1, i*2+2, i
    if left < len(nums) and nums[left] < nums[min_idx]:
        min_idx = left
    if right < len(nums) and nums[right] < nums[min_idx]:
        min_idx = right
    if min_idx != i:
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
        _heapify(nums, min_idx)


def counting_sort(nums, min_num, max_num):
    n, size = len(nums), max_num-min_num+1
    counts = [0 for _ in range(size)]
    for num in nums:
        counts[num-min_num] += 1
    accs = []
    for count in counts:
        accs.append(count+(accs[-1] if accs else 0))
    # use accumulation info collected
    res = [0 for _ in range(n)]
    for num in nums:
        idx = num - min_num
        accs[idx] -= 1
        res[accs[idx]] = num
    return res


def bucket_sort(nums, min_num, max_num, capacity=3):
    n, size = len(nums), (max_num-min_num)/capacity + 1
    buckets = [[] for _ in range(size)]
    for num in nums:
        buckets[(num-min_num)//capacity].append(num)
    return [num for bucket in buckets for num in insert_sort(bucket)]


def radix_sort(nums, capacity=10):
    k = int(math.ceil(math.log(max(nums)+1, capacity)))
    for i in range(k):
        buckets = [[] for _ in range(capacity)]
        for num in nums:
            idx = num / capacity**i % 10
            buckets[idx].append(num)
        del nums[:]
        nums = [num for bucket in buckets for num in bucket]
    return nums


if __name__ == '__main__':
    test = [6, -2, -8, 9, 3, 3, 3]
    result = [-8, -2, 3, 3, 3, 6, 9]

    copy1 = test[:]
    assert merge_sort(copy1) == result

    copy2 = test[:]
    quick_sort(copy2, 0, 6)
    assert copy2 == result

    copy3 = test[:]
    heap_sort(copy3)
    assert copy3 == result

    copy4 = test[:]
    assert counting_sort(copy4, -8, 9) == result
