#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2018/11/29'
'''

import pandas as pd
pd.set_option('display.max_rows', 5)

reviews = pd.read_csv('../datasets/winemag-data-130k-v2.csv', index_col=0)

# 以taster_twitter_handle为索引，以其对应的组大小为值
reviews_written = reviews.groupby('taster_twitter_handle').size()
# 以price为索引，以其对应的max(points)为值
best_rating_per_price = reviews.groupby('price')['points'].max().sort_index()
# aggregate聚合：以variety为索引，以其对应的min(price)和max(price)为值
price_extremes = reviews.groupby('variety')['price'].agg([min, max])
# 降序排列：min(price)和max(price)的列表
sorted_varieties = price_extremes.sort_values(by=['min', 'max'], ascending=False)
# 以taster_name为索引，以其对应的mean(points)为值
reviewer_mean_ratings = reviews.groupby('taster_name')['points'].mean()
# 以(country, variety)为索引，以其对应的组大小为值
country_variety_counts = reviews.groupby(['country', 'variety']).size().sort_values(ascending=False)
