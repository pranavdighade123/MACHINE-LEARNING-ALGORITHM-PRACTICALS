# -*- coding: utf-8 -*-
"""MLA_05_06.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N8jnNhKHoloc09WA_Vka83dJ1mEs-Byo

***MACHINE LEARNING ALGORITHM | PRACTICAL 05 AND 06***

***AIM05:*** Implement Linear Regression using Python.|
***AIM06:*** Implement Logistic Regression using Python.
"""

import pandas as pd
from sklearn import linear_model
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as mpl

data = pd.read_csv(r"C:\Users\Dell\Downloads\Salary_dataset.csv")

regr=linear_model.LinearRegression()
logiRegr=linear_model.LogisticRegression()
x=data['yearsexperience']
y=data['salary']

x=x.values.reshape(len(x),1)
y=y.values.reshape(len(y),1)

regr.fit(x,y)

logiRegr.fit(x,y)

mpl.scatter(x,y)
mpl.plot(x,regr.predict(x),color ='black')

mpl.scatter(x,y)
mpl.plot(x,logiRegr.predict(x),color ='black')

