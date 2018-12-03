#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2018/11/28'
'''

import pandas as pd
pd.set_option('display.max_rows', 5)

# 创建对象
fruit_sales = pd.DataFrame([[35, 21], [41, 34]],
                           index=['2017 Sales', '2018 Sales'],
                           columns=['Apples', 'Bananas'])

ingredients = pd.Series(['4 cups', '1 cup', '2 large', '1 can'],
                        index=['Flour', 'Milk', 'Eggs', 'Spam'],
                        name='Dinner')

# 读写csv
# 第1列作为索引，而不是字段名
reviews = pd.read_csv('../datasets/winemag-data-130k-v2.csv', index_col=0)
reviews.to_csv('../datasets/result.csv')
# Property: reviews.columns/index/values

# 读SQLite数据库
import sqlite3
conn = sqlite3.connect('../datasets/database.sqlite')
music_reviews = pd.read_sql_query('select * from artists;', conn)

# 按行、列选取
desc = reviews.loc[:, 'description']
# desc = reviews.description
first_row = reviews.iloc[0]
sample_reviews = reviews.loc[[1, 2, 3, 5, 8]]
df = reviews.loc[:, ['country', 'variety']].iloc[:100]
# df = reviews.head(100).loc[:, ['country', 'variety']]

# 按条件过滤
italian_wines = reviews[reviews.country == 'Italy']
top_oceania_wines = reviews[
    (reviews.points >= 95)
    & (reviews.country.isin(['Australia', 'New Zealand']))
]
