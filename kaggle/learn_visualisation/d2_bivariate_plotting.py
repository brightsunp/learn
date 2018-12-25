#!/usr/bin/env python
# coding: utf-8

# In[11]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd


# In[12]:


reviews = pd.read_csv('../datasets/winemag-data-130k-v2.csv', index_col=0)
reviews.head()


# In[17]:


# 1. Scatter plot
# overplotting
reviews[reviews.price < 100].plot.scatter(x='price', y='points')


# In[16]:


# downsample: show the correlation
reviews[reviews.price < 100].sample(100).plot.scatter(x='price', y='points')


# In[18]:


# 2. Hex plot
# aggregate points into hexagons
reviews[reviews.price < 100].plot.hexbin(x='price', y='points', gridsize=15)


# In[19]:


wine_counts = pd.read_csv('../datasets/top-five-wine-score-counts.csv', index_col=0)
wine_counts.head()


# In[21]:


# 3. Stacked bar chart
wine_counts.plot.bar(stacked=True)


# In[22]:


# 4. Bivariate line chart
wine_counts.plot.line()
wine_counts.plot.area()


# In[ ]:




