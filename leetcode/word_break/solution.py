#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2022/8/1'
'''


def load_input(input_file):
    with open(input_file, 'r') as reader:
        return reader.read().strip()


def load_dict():
    res = set()
    for num in file_nums:
        dict_file = '{}{}{}'.format('words-', num, '.txt')
        with open(dict_file, 'r') as reader:
            for line in reader:
                res.add(line.strip())
    return res


def word_break(input_s, input_d):
    dp = [False for _ in range(len(input_s) + 1)]
    dp[0] = True

    for i in range(len(input_s) + 1):
        for j in range(i):
            if dp[j] and input_s[j:i] in input_d:
                dp[i] = True
                break
    
    return dp[len(input_s)]


if __name__ == '__main__':
    file_nums = [10, 20, 35, 40, 50]
    input_string = load_input('novelnospace.txt')
    dictionary = load_dict()

    print(word_break(input_string, dictionary))

    test_s = ['ilikesamsung', 'iiiiiiii', '', 'ilikelikeimangoiii', 'samsungandmango', 'samsungandmangok']
    test_d = [ "mobile", "samsung", "sam", "sung", "man", "mango", "icecream", "and", "go", "i", "like", "ice", "cream" ]
    print(list(word_break(x, test_d) for x in test_s))

