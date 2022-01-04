# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 19:40:56 2022

@author: HP-
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
fruits=pd.read_table('fruit_data_with_colors.txt')
fruits.head()
fruits.shape

X=fruits[['mass','width','height']]
y=fruits['fruit_label']

X_train, X_test, y_train, y_test=train_test_split(X,y, random_state=0)