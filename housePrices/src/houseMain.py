import pandas as pd
from sklearn.model_selection import train_test_split #pip3 install scikit-learn
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error


# load dataset
data = pd.read_csv('../data/house.csv')

# clean dataset
data.drop(['center_distance', 'metro_distance'], axis=1, inplace=True)
data.drop(data[data['bedroom_count'] > 3].index, inplace=True)

#print(data.head)
#print(data.info)

# divide dataset
X = data.drop('price', axis=1)
y = data['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# train model
model = LinearRegression()
model.fit(X_train, y_train)

# make prodiction
predictions = model.predict(X_test)
comparison = pd.DataFrame({'Actual':  y_test, 'Prediction': predictions})
print(comparison.head())

mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)

print(f'MAE: {mae}, MSE: {mse}')

