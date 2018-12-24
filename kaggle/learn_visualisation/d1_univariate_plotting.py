#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2018/12/24'
'''

import pandas as pd
import matplotlib.pyplot as plt

reviews = pd.read_csv('../datasets/winemag-data-130k-v2.csv', index_col=0)
print(reviews.head(5))

# 1. Bar chart
# nominal variables
reviews['province'].value_counts().head(10).plot.bar()
# (reviews['province'].value_counts().head(10) / len(reviews)).plot.bar()
plt.show()
# ordinal variables
reviews['points'].value_counts().sort_index().plot.bar()
plt.show()

# 2. Line chart
# used if: 1)many unique values; 2)ordinal variables
reviews['points'].value_counts().sort_index().plot.line()
plt.show()
# Area charts: bottom shaded in
reviews['points'].value_counts().sort_index().plot.area()
plt.show()

# 3. Histogram
# break into even intervals
reviews[reviews['price'] < 200]['price'].plot.hist()
plt.show()
# how to deal with skewed data
reviews['price'].plot.hist()
plt.show()
# ordinal variables
reviews['points'].plot.hist()
plt.show()
