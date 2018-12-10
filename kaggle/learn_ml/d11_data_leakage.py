#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2018/12/7'
'''

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import cross_val_score

data = pd.read_csv('../datasets/AER_credit_card_data.csv',
                   true_values=['yes'],
                   false_values=['no'])
y = data.card
X = data.drop(['card'], axis=1)

# How to prevent data leakage: requires data, case-specific inspection and common sense
print(data.head())
# Use pipeline as best practice
modeling_pipeline = make_pipeline(RandomForestClassifier())
cv_scores = cross_val_score(modeling_pipeline, X, y, scoring='accuracy')
print("Cross-val accuracy: {:.2%}".format(cv_scores.mean()))

# Data comparision
expenditures_cardholders = data.expenditure[data.card]
expenditures_noncardholders = data.expenditure[~data.card]
print('Fraction of those who owned a card with no expenditures: {:.0%}'
      .format((expenditures_cardholders == 0).mean()))
print('Fraction of those who owned no card with no expenditures: {:.0%}'
      .format((expenditures_noncardholders == 0).mean()))

# Drop potential leaks
potential_leaks = ['expenditure', 'share', 'active', 'majorcards']
X2 = X.drop(potential_leaks, axis=1)
cv_scores = cross_val_score(modeling_pipeline, X2, y, scoring='accuracy')
print("Cross-val accuracy without data leakage: {:.2%}".format(cv_scores.mean()))
