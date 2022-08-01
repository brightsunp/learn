#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2022/3/21'
'''
def merge1(nums1, nums2):
    # swap k elements and sort: O(mlogm + nlogn))
    i, j, k = 0, 0, len(nums1) - 1
    while (i <= k and j < len(nums2)):
        if (nums1[i] <= nums2[j]):
            i += 1
        else:
            nums1[k], nums2[j] = nums2[j], nums1[k]
            j += 1
            k -= 1
    nums1.sort()
    nums2.sort()


def merge2(nums1, nums2):
    # insert sort: O(m*n)
    for i in range(len(nums1)):
        if (nums1[i] > nums2[0]):
            nums1[i], nums2[0] = nums2[0], nums1[i]
            j, target = 1, nums2[0]
            while (j < len(nums2) and nums2[j] < target):
                nums2[j-1] = nums2[j]
                j += 1
            nums2[j-1] = target


def merge3(nums1, nums2):
    # leverage Euclidean Division Lemma: O(m+n)
    # (A+B*N)/N = B, (A+B*N)%N = A
    N = max(nums1[-1], nums2[-1]) + 1
    i, j, k, m, n = 0, 0, 0, len(nums1), len(nums2)
    while (i < m and j < n):
        e1, e2 = nums1[i] % N, nums2[j] % N
        if (e1 <= e2):
            if (k < m):
                nums1[k] += e1 * N
            else:
                nums2[k-m] += e1 * N
            i += 1
        else:
            if (k < m):
                nums1[k] += e2 * N
            else:
                nums2[k-m] += e2 * N
            j += 1
        k += 1
    
    while i < m:
        e1 = nums1[i] % N
        if (k < m):
            nums1[k] += e1 * N
        else:
            nums2[k-m] += e1 * N
        i += 1
        k += 1
    while j < n:
        e2 = nums2[j] % N
        if (k < m):
            nums1[k] += e2 * N
        else:
            nums2[k-m] += e2 * N
        j += 1
        k += 1

    for i in range(m):
        nums1[i] //= N
    for i in range(n):
        nums2[i] //= N


if __name__ == '__main__':
    arr1 = [1, 5, 9, 10, 15, 20]
    arr2 = [2, 3, 8, 13]
    arr1_result = [1, 2, 3, 5, 8, 9]
    arr2_result = [10, 13, 15, 20]

    copy1, copy2 = arr1[:], arr2[:]
    merge1(copy1, copy2)
    assert (copy1, copy2) == (arr1_result, arr2_result)

    copy1, copy2 = arr1[:], arr2[:]
    merge2(copy1, copy2)
    assert (copy1, copy2) == (arr1_result, arr2_result)

    copy1, copy2 = arr1[:], arr2[:]
    merge3(copy1, copy2)
    assert (copy1, copy2) == (arr1_result, arr2_result)
