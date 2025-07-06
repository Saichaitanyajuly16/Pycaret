# importing nessessary libraries
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('diabetes.csv')
df.head()

df.columns

# check missing data
df.isnull().sum()

#EDA
df.info()

df.describe()

df.duplicated().sum()

# Glucose	BloodPressure	SkinThickness	Insulin	BMI
print("Mean :", df['Glucose'].mean())
print("median:",df['Glucose'].median())

df['Glucose']=np.where(df['Glucose']==0, df['Glucose'].mean(), df['Glucose'])
df['BloodPressure']=np.where(df['BloodPressure']==0, df['BloodPressure'].mean(), df['BloodPressure'])
df['SkinThickness']=np.where(df['SkinThickness']==0, df['SkinThickness'].mean(), df['SkinThickness'])
df['Insulin']=np.where(df['Insulin']==0, df['Insulin'].mean(), df['Insulin'])
df['BMI']=np.where(df['BMI']==0, df['BMI'].mean(), df['BMI'])

df.describe()

#!pip install dtale

import dtale
dtale.show(df)









