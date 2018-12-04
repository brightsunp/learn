#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2018/12/3'
'''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error

iowa_file_path = '../datasets/home-data-for-ml-course/train.csv'
home_data = pd.read_csv(iowa_file_path)

feature_names = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = home_data[feature_names]
y = home_data.SalePrice

# 1. Split Data
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

# 2. Specify and Fit Model
iowa_model = DecisionTreeRegressor(random_state=1)
iowa_model.fit(train_X, train_y)

# 3. Make Predictions
val_predictions = iowa_model.predict(val_X)
# np.ndarray object
print(val_predictions[:10])
print(val_y.head(10))

# 4. Calculate MAE
val_mae = mean_absolute_error(val_predictions, val_y)
print('Validation MAE: {:,.0f}'.format(val_mae))
