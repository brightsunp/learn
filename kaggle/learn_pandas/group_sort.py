#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2018/11/29'
'''

import pandas as pd
pd.set_option('display.max_rows', 5)
pd.set_option('display.max_columns', 10)

reviews = pd.read_csv('../datasets/winemag-data-130k-v2.csv', index_col=0)
print(reviews)
# 各字段的频率（无序）
reviews_written = reviews.groupby('taster_twitter_handle').size()


