import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Setup random seed
np.random.seed(47)

# import data
df = pd.read_csv("data/heart-disease.csv")

# Create X and y
X = df.drop("target", axis=1)
y = df["target"]

# first, split into X_train, X_valid_test, y_train, y_valid_test
# `test_size=0.3` split into 70% and 30%
X_train, X_valid_test, y_train, y_valid_test = train_test_split(X, y, test_size=0.3)

# second, split into X_valid, X_test, y_valid, y_test
# `test_size=0.5` split into 50% and 50%. The original data set is 30%,
# so, it will split into 15% equally.
X_valid, X_test, y_valid, y_test = train_test_split(X_valid_test, y_valid_test, test_size=0.5)

print(len(X_train), len(X_valid), len(X_test))