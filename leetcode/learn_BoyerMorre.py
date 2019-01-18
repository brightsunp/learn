#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/1/18'
'''


class BoyerMorre(object):
    '''
    1977, Boyer-Morre algorithm

    http://www.cnblogs.com/lanxuezaipiao/p/3452579.html
    '''
    def strStr(self, text, pattern):
        # preprocessing
        bc = self.calcBc(pattern)
        gs = self.calcGs(pattern)
        # searching
        m, n = len(pattern), len(text)
        for i in range(n-m+1):
            j = m-1
            while pattern[j] == text[i+j]:
                j -= 1
            if j < 0:
                print('Find at position {}'.format(i))
                return
            else:
                i += max(bc[ord(text[i+j])]-(m-j-1), gs[j])
        print('Find no one.')

    def calcBc(self, pattern):
        # bad character rule
        n = len(pattern)
        bc = [n for _ in range(256)]
        for i, char in enumerate(pattern):
            bc[ord(char)] = n - i - 1
        return bc

    def calcGs(self, pattern):
        # good suffix rule
        n = len(pattern)
        suffix = [n for _ in range(n)]
        for i in range(n-2, -1, -1):
            j = i
            while j >= 0 and pattern[j] == pattern[j+n-i-1]:
                j -= 1
            suffix[i] = i - j
        gs = [n for _ in range(n)]
        for i in range(n-1, -1, -1):
            if suffix[i] == i+1:
                for j in range(n-i-1):
                    if gs[j] == n:
                        gs[j] = n-i-1
        for i in range(n-1):
            gs[n-suffix[i]-1] = n-i-1
        return gs


if __name__ == '__main__':
    test_text = 'abcdefgfsdaf'
    test_pattern = 'fsd'
    bm = BoyerMorre()
    bm.strStr(test_text, test_pattern)
