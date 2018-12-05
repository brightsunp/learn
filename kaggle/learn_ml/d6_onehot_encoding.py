#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2018/12/5'
'''

import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor

train_data = pd.read_csv('../datasets/home-data-for-ml-course/train.csv')
test_data = pd.read_csv('../datasets/home-data-for-ml-course/test.csv')
# Drop houses where the target is missing
train_data.dropna(axis=0, subset=['SalePrice'], inplace=True)
target = train_data.SalePrice

cols_with_missing = [col for col in train_data.columns
                                 if train_data[col].isnull().any()]
candidate_train_predictors = train_data.drop(['Id', 'SalePrice'] + cols_with_missing, axis=1)
candidate_test_predictors = test_data.drop(['Id'] + cols_with_missing, axis=1)

# One-Hot Encoding: no more than 15 unique values in a column
low_cardinality_cols = [cname for cname in candidate_train_predictors.columns if
                                candidate_train_predictors[cname].nunique() < 10 and
                                candidate_train_predictors[cname].dtype == "object"]
numeric_cols = [cname for cname in candidate_train_predictors.columns if
                                candidate_train_predictors[cname].dtype in ['int64', 'float64']]
my_cols = low_cardinality_cols + numeric_cols
train_predictors = candidate_train_predictors[my_cols]
test_predictors = candidate_test_predictors[my_cols]
# print(train_predictors.dtypes.sample(10))
one_hot_encoded_training_predictors = pd.get_dummies(train_predictors)


def get_mae(X, y):
    return -1 * cross_val_score(RandomForestRegressor(n_estimators=50), X, y,
                                scoring='neg_mean_absolute_error').mean()


predictors_without_categoricals = train_predictors.select_dtypes(exclude=['object'])
mae_without_categoricals = get_mae(predictors_without_categoricals, target)
mae_one_hot_encoded = get_mae(one_hot_encoded_training_predictors, target)

print('Mean Absolute Error when Dropping Categoricals: {:,.0f}'.format(mae_without_categoricals))
print('Mean Abslute Error with One-Hot Encoding: {:,.0f}'.format(mae_one_hot_encoded))

one_hot_encoded_test_predictors = pd.get_dummies(test_predictors)
# SQL's left join
final_train, final_test = one_hot_encoded_training_predictors.align(
    one_hot_encoded_test_predictors, join='left', axis=1)
