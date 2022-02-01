import os
import sys

import pandas as pd
import numpy as np

from xgboost import XGBClassifier

from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = pd.read_csv('parkinsonDetection/parkinsons.data')

# Extract the trainable attributes and their appropriate labels
features = data.loc[:, data.columns != 'status'].values[:, 1:]
labels = data.loc[:, 'status'].values

# print(labels[labels == 1].shape[0], labels[labels == 0].shape[0])

# Normalise the data for the model input
scaleFactor = MinMaxScaler((-1, 1))
x = scaleFactor.fit_transform(features)
y = labels

# Split data for training and testing
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=42)

# Initialise the model
model = XGBClassifier()
model.fit(x_train, y_train)

# Predict using the trained model
prediction = model.predict(x_test)

accuracy = accuracy_score(y_test, prediction)
print(accuracy)
