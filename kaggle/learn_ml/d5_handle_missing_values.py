#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2018/12/4'
'''

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

melb_data = pd.read_csv('../datasets/melb_data.csv')
melb_target = melb_data.Price
melb_predictors = melb_data.drop(['Price'], axis=1)
# use only numeric predictors.
melb_numeric_predictors = melb_predictors.select_dtypes(exclude=['object'])
train_X, test_X, train_y, test_y = train_test_split(melb_numeric_predictors, melb_target, random_state=1)


def score_datasets(train_X, test_X, train_y, test_y):
    model = RandomForestRegressor(random_state=1)
    model.fit(train_X, train_y)
    preds = model.predict(test_X)
    return mean_absolute_error(test_y, preds)


# Method 1. Dropping Columns with Missing Values
cols_with_missing = [col for col in train_X.columns
                     if train_X[col].isnull().any()]
reduced_train_X = train_X.drop(cols_with_missing, axis=1)
reduced_test_X = test_X.drop(cols_with_missing, axis=1)
score_method_1 = score_datasets(reduced_train_X, reduced_test_X, train_y, test_y)
print('MAE from dropping columns with Missing Values: {:,.0f}'.format(score_method_1))

# Method 2. Inputation
from sklearn.impute import SimpleImputer
my_imputer = SimpleImputer()
imputed_train_X = my_imputer.fit_transform(train_X)
imputed_test_X = my_imputer.fit_transform(test_X)
score_method_2 = score_datasets(imputed_train_X, imputed_test_X, train_y, test_y)
print('MAE from Imputation: {:,.0f}'.format(score_method_2))

# Method 3. Imputation with Extra Boolean Columns
imputed_train_X_plus = train_X.copy()
imputed_test_X_plus = test_X.copy()
for col in cols_with_missing:
    imputed_train_X_plus[col+'_was_missing'] = imputed_train_X_plus[col].isnull()
    imputed_test_X_plus[col+'_was_missing'] = imputed_test_X_plus[col].isnull()
imputed_train_X_plus = my_imputer.fit_transform(imputed_train_X_plus)
imputed_test_X_plus = my_imputer.fit_transform(imputed_test_X_plus)
score_method_3 = score_datasets(imputed_train_X_plus, imputed_test_X_plus, train_y, test_y)
print('MAE from Imputation with Extra Boolean Columns: {:,.0f}'.format(score_method_3))
