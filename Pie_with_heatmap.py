import pandas as pd
from matplotlib import pyplot as plt

base_dir='D://canada//uwo//MEsc//Model_Inversion_Attacks//dataset//'
raw_data = pd.read_csv(base_dir+'Electricity_HPE.csv')
raw_data['datetime'] = pd.to_datetime(raw_data['unix_ts'],unit='s')
raw_data['month'] = raw_data['datetime'].dt.month
raw_data['hour'] = raw_data['datetime'].dt.hour
raw_data['weekday'] = raw_data['datetime'].dt.dayofweek
raw_data['quarter'] = raw_data['datetime'].dt.quarter


group_list = raw_data.groupby('quarter')['P'].mean()
plt.pie(group_list,colors=['#f03b20','#feb24c','#ffeda0','#f03b20'],\
                           labels=['Q1','Q2','Q3','Q4'],autopct='%1.0f%%',\
                           explode=(0.05, 0.05, 0.05, 0.05))

plt.title('Different Power Usage of Heat Pump by Quarters')
plt.ylabel('Watts')
centre_circle = plt.Circle((0,0),0.75,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.tight_layout()
plt.show()
