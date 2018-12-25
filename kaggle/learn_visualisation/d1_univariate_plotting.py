#!/usr/bin/env python
# coding: utf-8

# In[1]:


# set environments
get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd


# In[2]:


# read data
reviews = pd.read_csv('../datasets/winemag-data-130k-v2.csv', index_col=0)
reviews.head()


# In[3]:


# 1. Bat chart
# nominal variables
reviews.province.value_counts().head(10).plot.bar()


# In[4]:


# ordinal variables
reviews.points.value_counts().sort_index().plot.bar()


# In[5]:


# 2. Line chart
# if many unique values
reviews.points.value_counts().sort_index().plot.line()


# In[6]:


# Area chart: with bottom shaded in
reviews.points.value_counts().sort_index().plot.area()


# In[7]:


# 3. Histogram
# break into even intervals
reviews[reviews.price < 200].price.plot.hist()


# In[8]:


# skewed data
reviews.price.plot.hist()


# In[9]:


# compare to line chart
reviews.points.plot.hist()

