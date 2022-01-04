# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 19:51:47 2022

@author: HP-
"""

import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

 
# create dataframe from file
dataframe = pd.read_csv("creditcard.csv")
 
# show dataframe
print(dataframe)
 
# use corr() method on dataframe to
# make correlation matrix
matrix = dataframe.corr()
 
# print correlation matrix
print("Correlation Matrix is : ")
print(matrix)
sn.heatmap(matrix, annot=True)
plt.show()
