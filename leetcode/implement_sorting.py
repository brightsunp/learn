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
    return merge(merge_sort(nums[:mid]), merge_sort(nums[mid:]))


def merge(left, right):
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:] + right[j:])
    return res


def quick_sort(nums, left, right):
    # swap
    if left < right:
        pivot_idx = partition(nums, left, right)
        quick_sort(nums, left, pivot_idx-1)
        quick_sort(nums, pivot_idx+1, right)


def partition(nums, left, right):
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
    pass


def build_heap(nums):

    pass


def heapify(nums, i):
    left, right, min_idx = i*2+1, i*2+2, i
    if left < len(nums) and nums[left] < nums[min_idx]:
        min_idx = left
    if right < len(nums) and nums[right] < nums[min_idx]:
        min_idx = right
    while min_idx != i:
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
        heapify(nums, min_idx)


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
    # compare keywords
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

    copy1 = test[:]
    print('Merge sort of', test, ':\n', merge_sort(copy1))

    copy2 = test[:]
    quick_sort(copy2, 0, 6)
    print('Quick sort of', test, ':\n', copy2)

    copy3 = test[:]
    print('Counting sort of', test, ':\n', counting_sort(copy3, -8, 9))
