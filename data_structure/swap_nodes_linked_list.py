#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2022/3/23'

Given a linked list and two keys in it, swap nodes for two given keys. Nodes should be swapped by changing links.
(Swapping data of nodes may be expensive in many situations when data contains many fields.)
It may be assumed that all keys in the linked list are distinct.

Examples:
Input : 10->15->12->13->20->14,  x = 12, y = 20
Output: 10->15->20->13->12->14

Notes:
1. x and y may or may not be adjacent.
2. Either x or y may be the head node.
3. Either x or y may be the last node.
4. x and/or y may not be present in the linked list.
'''
class Node(object):
    def __init__(self, val):
        self.next = None
        self.value = val


def node2list(head):
    res, cur = [], head
    while cur:
        res.append(cur.value)
        cur = cur.next
    return res


def list2node(arr):
    if not arr: return None
    head = Node(arr[0])
    res = head
    for ele in arr[1:]:
        head.next = Node(ele)
        head = head.next
    return res


def swapNodes(head, x, y):
    # nothing to do if x equals y
    if x == y:
        return head
    prevX, currX, prevY, currY = None, head, None, head
    while (currX and currX.value != x):
        prevX = currX
        currX = currX.next
    while (currY and currY.value != y):
        prevY = currY
        currY = currY.next
    # nothing to do if x or y is not present
    if (not currX or not currY):
        return head
    
    # swap current needs consider head node
    if not prevX:
        head = currY
    else:
        prevX.next = currY
    if not prevY:
        head = currX
    else:
        prevY.next = currX
    # swap next
    tmp = currX.next
    currX.next = currY.next
    currY.next = tmp
    return head


if __name__ == '__main__':
    arr1 = [10, 15, 12, 13, 20, 14]
    
    copy1 = swapNodes(list2node(arr1), 12, 13)
    assert node2list(copy1) == [10, 15, 13, 12, 20, 14]

    copy2 = swapNodes(list2node(arr1), 10, 14)
    assert node2list(copy2) == [14, 15, 12, 13, 20, 10]

    copy3 = swapNodes(list2node(arr1), 10, 18)
    assert node2list(copy3) == arr1

    copy4 = swapNodes(list2node(arr1), 12, 12)
    assert node2list(copy4) == arr1

    print("All test cases passed!")
