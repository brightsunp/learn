#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2018/12/3'
'''

import pandas as pd
pd.set_option('display.max_rows', 5)

reviews = pd.read_csv('../datasets/winemag-data-130k-v2.csv', index_col=0)

# 显示类型
points_dtype = reviews['points'].dtype
# 修改类型
point_strings = reviews['points'].astype(str)
# point_strings = reviews['points'].astype('float64')
# 空值的个数：isnull 等价于 isna
n_missing_prices = reviews['price'].isnull().sum()
# n_missing_prices = pd.isnull(reviews['price']).sum()
# 降序排列：常见的链式处理
reviews_per_region = reviews['region_1'].fillna('Unknown').value_counts().sort_values(ascending=False)
# 两种重命名方法
renamed = reviews.rename(columns={'region_1': 'region', 'region_2': 'locale'})
reindexed = reviews.rename_axis('wines', axis='index')

powerlifting_meets = pd.read_csv("../datasets/powerlifting_meets.csv")
powerlifting_competitors = pd.read_csv("../datasets/openpowerlifting.csv")

# 最简单的联接
simple_combined = powerlifting_meets.append(powerlifting_competitors)
# simple_combined = pd.concat([powerlifting_meets, powerlifting_competitors])
# 根据外键联接
powerlifting_combined = powerlifting_meets.set_index("MeetID").join(powerlifting_competitors.set_index("MeetID"))
