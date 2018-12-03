#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2018/12/3'
'''

import pandas as pd
from sklearn.tree import DecisionTreeRegressor

iowa_file_path = '../datasets/home-data-for-ml-course/train.csv'
home_data = pd.read_csv(iowa_file_path)

# 1. Specify prediction target
print(home_data.columns)
# dot notation
y = home_data.SalePrice

# 2. Create X
feature_names = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
# X = home_data.loc[:, feature_names]
X = home_data[feature_names]
# review data
print(X.describe())
print(X.head())

# 3. Specify and Fit Model
iowa_model = DecisionTreeRegressor(random_state=1)
iowa_model.fit(X, y)

# 4. Make Predictions
predictions = iowa_model.predict(X)
# same values to y
print(predictions)
