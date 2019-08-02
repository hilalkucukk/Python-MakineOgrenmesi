# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 17:52:34 2019

@author: Hilal
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


ulke=veriler.iloc[:,0:1].values
print(ulke)

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
ulke[:,0]=le.fit_transform(ulke[:,0])
print(ulke)

from sklearn.preprocessing import OneHotEncoder
ohe=OneHotEncoder(categorical_features="all")
ulke=ohe.fit_transform(ulke).toarray()
print(ulke)