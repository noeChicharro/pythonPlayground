import pandas as pd

data = pd.read_csv('../../data/house.csv')

data.drop(['center_distance', 'metro_distance'], axis=1, inplace=True)
#data.drop(data[data['bedroom_count'] > 3].index, inplace=True)
data.drop(data[data['age'] > 20].index, inplace=True)