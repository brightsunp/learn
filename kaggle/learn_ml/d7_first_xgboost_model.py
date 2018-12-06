#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2018/12/6'
'''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Imputer
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error

data = pd.read_csv('../datasets/home-data-for-ml-course/train.csv')
data.dropna(axis=0, subset=['SalePrice'], inplace=True)
X = data.drop(['SalePrice'], axis=1).select_dtypes(exclude=['object'])
y = data.SalePrice
train_X, test_X, train_y, test_y = train_test_split(X.as_matrix(), y.as_matrix(), test_size=0.25)

my_imputer = Imputer()
train_X = my_imputer.fit_transform(train_X)
test_X = my_imputer.transform(test_X)

# default:
my_model = XGBRegressor()
my_model.fit(train_X, train_y, verbose=False)
print(my_model)
print('MAE from XGBoost: {:,.0f}'.format(mean_absolute_error(my_model.predict(test_X), test_y)))

# Model Tuning: building is easy, improving is difficult
# https://www.analyticsvidhya.com/blog/2016/03/complete-guide-parameter-tuning-xgboost-with-codes-python/
# 1. n_estimators & early_stopping_rounds
my_model = XGBRegressor(n_estimators=1000)
my_model.fit(train_X, train_y, early_stopping_rounds=5,
             eval_set=[(test_X, test_y)], verbose=False)
print(my_model)
print('MAE from XGBoost1: {:,.0f}'.format(mean_absolute_error(my_model.predict(test_X), test_y)))

# 2. learning_rate
my_model = XGBRegressor(n_estimators=1000, learning_rate=0.05)
my_model.fit(train_X, train_y, early_stopping_rounds=5,
             eval_set=[(test_X, test_y)], verbose=False)
print(my_model)
print('MAE from XGBoost2: {:,.0f}'.format(mean_absolute_error(my_model.predict(test_X), test_y)))
