#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2018/11/29'
'''

import pandas as pd
pd.set_option('display.max_rows', 5)

# 计算中位数
median_points = reviews.points.median()
# 返回去重列表
countries = reviews.country.unique()
