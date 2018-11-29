#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2018/11/29'
'''

import pandas as pd
pd.set_option('display.max_rows', 5)

reviews = pd.read_csv('../datasets/winemag-data-130k-v2.csv', index_col=0)
# 中位数
median_points = reviews.points.median()
# 去重后的字段列表
countries = reviews.country.unique()
# 各字段的频率
reviews_per_country = reviews.country.value_counts()
# series 可以直接减 mean_value
centered_price = reviews.price - reviews.price.mean()
# idxmax/argmax 找到某最大值的索引值/位置
bargain_idx = (reviews.points / reviews.price).idxmax()
bargain_wine = reviews.loc[bargain_idx, 'title']
# 某个词在 series 中出现的频率
n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum()
n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
descriptor_counts = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'])
# apply 对行元素进行统计
def stars(row):
    if row.country == 'Canada':
        return 3
    elif row.points >= 95:
        return 3
    elif row.points >= 85:
        return 2
    else:
        return 1

star_ratings = reviews.apply(stars, axis='columns')
