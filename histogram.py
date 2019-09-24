import pandas as pd
#import numpy as np
#from sklearn.preprocessing import OneHotEncoder
#import tensorflow as tf
#from sklearn.model_selection import train_test_split 
from matplotlib import pyplot as plt
import seaborn as sns

base_dir='D://canada//uwo//MEsc//Model_Inversion_Attacks//dataset//'
cde=pd.read_csv(base_dir+'Electricity_CDE.csv')['P'].values
plt.hist(cde,bins=500)
plt.yscale('log')
plt.title("Histogram of Dryer's Power Usage")
plt.xlabel("Watts")
plt.ylabel("Number of points")
plt.margins(0.01)
plt.show()

ax = sns.distplot(cde,bins=500,kde=False)
plt.yscale('log')
plt.show()
