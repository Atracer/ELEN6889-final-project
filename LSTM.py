import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import date
from dateutil.relativedelta import relativedelta
from datetime import datetime
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import LSTM, Dropout, Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

training_dataset = pd.read_csv("APPL_final.csv")

df = training_dataset[['Open', 'Close', 'Volume', 'Sentiment']]
df['Open'] = df['Open'].shift(-1)
df.drop(df.tail(1).index, inplace=True)

X = df[['Close', 'Volume', 'Sentiment']]
sc = MinMaxScaler(feature_range=(0, 1))
X = sc.fit_transform(X)

y = df['Open'].values
sc2 = MinMaxScaler(feature_range=(0, 1))
y = y.reshape(-1, 1)
y = sc2.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False, stratify=None)

# Build the LSTM model
model = Sequential()
model.add(LSTM(128, return_sequences=True, input_shape=(X_train.shape[1], 1)))
model.add(LSTM(64, return_sequences=False))
model.add(Dense(25))
model.add(Dense(1))

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mean_absolute_error'])

# Train the model
model.fit(X_train, y_train, batch_size=1, epochs=15)

y_pred = model.predict(X_test)
y_pred = sc2.inverse_transform(y_pred)
y_true = sc2.inverse_transform(y_test)

from sklearn.metrics import mean_squared_error

mean_squared_error(y_true, y_pred, squared=False)

y_pred = model.predict(X_test)
y_pred = sc2.inverse_transform(y_pred)
y_true = sc2.inverse_transform(y_test)
# Visualize the data

plt.figure(figsize=(16, 6))
plt.plot(y_true)
plt.plot(y_pred)
plt.xlabel('Time')
plt.ylabel('Stock price')
plt.legend(['real', 'prediction'])
plt.title('prediction for Amazon stock price using LSTM')
plt.show()
