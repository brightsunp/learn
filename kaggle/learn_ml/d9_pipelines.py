#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2018/12/7'
'''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Imputer
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline

data = pd.read_csv('../datasets/melb_data.csv')
cols_to_use = ['Rooms', 'Distance', 'Landsize', 'BuildingArea', 'YearBuilt']
X = data[cols_to_use]
y = data.Price
train_X, test_X, train_y, test_y = train_test_split(X, y)

# Pipelines: start with Transformers sequentially, end with a Model
my_pipeline = make_pipeline(Imputer(), RandomForestRegressor(random_state=0))
my_pipeline.fit(train_X, train_y)
preds = my_pipeline.predict(test_X)
print(preds[:10])
# fit arguments like this:
# my_pipeline.fit(train_X, train_y,
#                 xgbregressor__early_stopping_rounds=20,
#                 xgbregressor__eval_set=[(test_X, test_y)],
#                 xgbregressor__verbose=False)


# Same as follows
my_imputer = Imputer()
my_model = RandomForestRegressor(random_state=0)
imputed_train_X = my_imputer.fit_transform(train_X)
imputed_test_X = my_imputer.transform(test_X)
my_model.fit(imputed_train_X, train_y)
same_preds = my_model.predict(imputed_test_X)
print(same_preds[:10])
