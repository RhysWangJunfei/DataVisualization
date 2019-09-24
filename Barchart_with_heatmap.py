import pandas as pd
from matplotlib import pyplot as plt

base_dir='D://canada//uwo//MEsc//Model_Inversion_Attacks//dataset//'
raw_data = pd.read_csv(base_dir+'Electricity_CWE.csv')
raw_data['datetime'] = pd.to_datetime(raw_data['unix_ts'],unit='s')
raw_data['month'] = raw_data['datetime'].dt.month
raw_data['hour'] = raw_data['datetime'].dt.hour
raw_data['weekday'] = raw_data['datetime'].dt.dayofweek
raw_data['quarter'] = raw_data['datetime'].dt.quarter
group_list = raw_data.groupby('hour')['P'].mean()

for i in range(0,24):
    value = group_list[i]
    my_color = '#ffffb2'
    if value>10:
        my_color='#e31a1c'
    elif value>6.5:
        my_color='#fd8d3c'
    elif value>2:
        my_color='#fecc5c'
    plt.bar(i,value,color=my_color)
plt.xlabel('Hour in a Day')
plt.ylabel('Power Consumption per Minute')
plt.title('Hourly Average Power Usage of Dryer')
plt.margins(0)
plt.show()
#http://colorbrewer2.org/#type=sequential&scheme=YlOrRd&n=4
