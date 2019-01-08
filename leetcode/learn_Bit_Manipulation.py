#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/1/8'
'''


# 187. Repeated DNA Sequences
# https://leetcode.com/problems/repeated-dna-sequences/discuss/53867/Clean-Java-solution-(hashmap-%2B-bits-manipulation)
class Solution1(object):
    def findRepeatedDnaSequences1(self, s):
        # hashmap
        d = {}
        for i in range(len(s)-9):
            cur = s[i:i+10]
            d[cur] = d.get(cur, 0) + 1
        return [k for k, v in d.items() if v > 1]

    def findRepeatedDnaSequences2(self, s):
        # 2-bits: encode string
        m = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        seen, repeated = set(), set()
        res = []
        for i in range(len(s)-9):
            cur = s[i:i+10]
            v = 0
            for letter in cur:
                v = v << 2 | m[letter]
            if v in seen and v not in repeated:
                res.append(cur)
                repeated.add(v)
            seen.add(v)
        return res


# 201. Bitwise AND of Numbers Range
class Solution2(object):
    def rangeBitwiseAnd1(self, m, n):
        # recursive
        return self.rangeBitwiseAnd1(m >> 1, n >> 1) << 1 if m < n else m

    def rangeBitwiseAnd2(self, m, n):
        # iterative
        count = 0
        while m < n:
            m >>= 1
            n >>= 1
            count += 1
        return m << count


# 318. Maximum Product of Word Lengths
class Solution3(object):
    def maxProduct1(self, words):
        # hashset
        res = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if not (set(words[i]) & set(words[j])):
                    res = max(res, len(words[i]) * len(words[j]))
        return res

    def maxProduct2(self, words):
        # 26-bits: store distinct letters
        values = [0] * len(words)
        res = 0
        for i in range(len(words)):
            for char in words[i]:
                values[i] |= 1 << (ord(char) - ord('a'))
            for j in range(i):
                if values[i] & values[j] == 0:
                    res = max(res, len(words[i]) * len(words[j]))
        return res

