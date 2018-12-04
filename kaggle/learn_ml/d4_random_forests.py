#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2018/12/4'
'''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

iowa_file_path = '../datasets/home-data-for-ml-course/train.csv'
home_data = pd.read_csv(iowa_file_path)

feature_names = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = home_data[feature_names]
y = home_data.SalePrice
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

# 1. Use a Random Forest
rf_model = RandomForestRegressor(random_state=1)
rf_model.fit(train_X, train_y)
rf_val_mae = mean_absolute_error(rf_model.predict(val_X), val_y)
print('Validation MAE for Random Forest Model: {:,.0f}'.format(rf_val_mae))

# 2. Create a Model for Competition
rf_model_on_full_data = RandomForestRegressor(random_state=1)
rf_model_on_full_data.fit(X, y)

# 3. Predict Using Test Data
test_data_path = '../datasets/home-data-for-ml-course/test.csv'
test_data = pd.read_csv(test_data_path)
test_X = test_data[feature_names]
test_preds = rf_model_on_full_data.predict(test_X)

# 4. Save, Click 'Output' => 'Submit to Competition'
output = pd.DataFrame({'Id': test_data.Id, 'SalePrice': test_preds})
output.to_csv('submission.csv', index=False)
