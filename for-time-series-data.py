import pandas as pd
import numpy as np

# setup random seed
np.random.seed(47)

# read the data
# `parse_dates` is for easy to use date time column
df = pd.read_csv("data/netflix-stock-price-prediction.csv", parse_dates=True)

# sort the dataframe by `Date`
# `Date` is the column name in the csv file
df = df.sort_values(by="Date", ascending=True)

# Create X and y
X = df.drop("Volume", axis=1)
y = df["Volume"]

"""
The original data set has 1009 values and 
We sorted the dataframe from top to bottom with `ascending=True`

In this case, real time data set cannot be same like this, 
this is just an example
"""

# Indexing for training set
X_train, y_train = X[:800], y[:800]
# Indexing for validation set
X_valid, y_valid = X[801:901], y[801:901]
# Indexing for testing set
X_test, y_valid = X[902:], y[9002:]

print(len(X_train), len(X_valid), len(X_test))
