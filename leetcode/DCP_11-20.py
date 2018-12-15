#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2018/12/14'
'''


# 340. Longest Substring with At Most K Distinct Characters
class Solution1(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # maintain a valid window
        left = max_len = 0
        counter = {}
        for right in range(len(s)):
            counter[s[right]] = counter.get(s[right], 0) + 1
            while len(counter) > k:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    counter.pop(s[left])
                left += 1
            max_len = max(max_len, right-left+1)
        return max_len


# Monte Carlo method
import random

class Solution2(object):
    def estimatePi(self):
        """
        :rtype: str
        """
        count = 0
        for i in xrange(10**9):
            # random float between [0, 1)
            x = random.random()
            y = random.random()
            if x**2 + y**2 < 1:
                count += 1
        return '{:.3f}'.format(count * 4.0 / 10**9)
            

# Reservoir sampling
import random

class Solution3(object):
    def getRandom(self, stream):
        # uniform probability: 1/(i+1)
        res = None
        for i, e in enumerate(stream):
            if i == 0:
                res = e
            elif random.randint(1, i+1) == 1:
                res = e
        return res

 
# 388. Longest Absolute File Path
class Solution4(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        # dict {depth: cur_len}
        d = {0: 0}
        max_len = 0
        for line in input.split('\n'):
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            if '.' in name:
                max_len = max(max_len, d[depth] + len(name))
            else:
                d[depth+1] = d[depth] + len(name) + 1
        return max_len


# 239. Sliding Window Maximum
class Solution5(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # deque: store useful indexes in num-decreasing order
        res = []
        deque = []
        for i, num in enumerate(nums):
            while deque and num >= nums[deque[-1]]:
                deque.pop()
            deque.append(i)
            # remove indexes out of window
            if deque[0] == i-k:
                deque.pop(0)
            if i >= k-1:
                res.append(nums[deque[0]])
        return res

        
# 265. Paint House II
class Solution6(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not len(costs) or not len(costs[0]):
            return 0
        n, k = len(costs), len(costs[0])
        min1, min2, pre = 0, 0, -1
        for i in range(n):
            # MAX_INT = sys.maxint if Python2 else sys.maxsize
            m1, m2, cur = MAX_INT, MAX_INT, -1
            for j in range(k):
                cur_cost = costs[i][j] + (min2 if j==pre else min1)
                if cur_cost < m1:
                    m1, m2, cur = cur_cost, m1, j
                elif cur_cost < m2:
                    m2 = cur_cost
            # updated when i steps forward
            min1, min2, pre = m1, m2, cur
        return min1               

        
# 160. Intersection of Two Linked Lists
class Solution7(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # no need to calc len's difference
        # if intersect, meet at intersection; else meet at tail-None
        if not (headA and headB):
            return None
        curA, curB = headA, headB
        while curA != curB:
            curA = curA.next if curA else headB
            curB = curB.next if curB else headA
        return curA
        