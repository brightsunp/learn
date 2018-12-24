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
wine_counts = pd.read_csv('../datasets/top-five-wine-score-counts.csv', index_col=0)
print(wine_counts.head(5))

# 1. Scatter plot
# show the correlation (overplotting: downsample)
reviews[reviews['price'] < 100].sample(100).plot.scatter(x='price', y='points')
plt.show()

# 2. Hex plot
# aggregate points into hexagons
reviews[reviews['price'] < 100].plot.hexbin(x='price', y='points', gridsize=15)
plt.show()

# 3. Stacked bar chart
wine_counts.plot.bar(stacked=True)
plt.show()

# 4. Bivariate line chart
wine_counts.plot.line()
plt.show()
wine_counts.plot.area()
plt.show()
