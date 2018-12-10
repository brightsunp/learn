#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2018/12/6'
'''

import pandas as pd
from sklearn.preprocessing import Imputer
from sklearn.ensemble import GradientBoostingRegressor, GradientBoostingClassifier
from sklearn.ensemble.partial_dependence import plot_partial_dependence
import matplotlib.pyplot as plt

# Example 1
data = pd.read_csv('../datasets/melb_data.csv')
y = data.Price
cols_to_use = ['Distance', 'Landsize', 'BuildingArea']
X = data[cols_to_use]
my_imputer = Imputer()
imputed_X = my_imputer.fit_transform(X)
# make the plot
my_model = GradientBoostingRegressor()
my_model.fit(imputed_X, y)
my_plots = plot_partial_dependence(my_model, features=[0, 2], X=imputed_X,
                                   feature_names=cols_to_use, grid_resolution=10)
plt.show()

# Example 2
titanic_data = pd.read_csv('../datasets/titanic/train.csv')
titanic_y = titanic_data.Survived
titanic_X_colns = ['PassengerId', 'Age', 'Fare']
titanic_X = titanic_data[titanic_X_colns]
my_imputer = Imputer()
imputed_titanic_X = my_imputer.fit_transform(titanic_X)
# make the plot
clf = GradientBoostingClassifier()
clf.fit(imputed_titanic_X, titanic_y)
titanic_plots = plot_partial_dependence(clf, features=[1, 2], X=imputed_titanic_X,
                                        feature_names=titanic_X_colns, grid_resolution=8)
plt.show()
