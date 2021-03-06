# %load q05_lasso/build.py
# Default imports
from sklearn.linear_model import Lasso
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from greyatomlib.advanced_linear_regression.q01_load_data.build import load_data

# We have already loaded the data for you
data_set, X_train, X_test, y_train, y_test = load_data('data/house_prices_multivariate.csv')

np.random.seed(9)

def lasso(alpha = 0.01):
    lasso = Lasso(alpha = 0.01, normalize = True,random_state = 9)
    lasso.fit(X_train,y_train)
    ytrain = lasso.predict(X_train)
    ytest = lasso.predict(X_test)
    rmse_train = mean_squared_error(ytrain,y_train)**0.5
    rmse_test = mean_squared_error(ytest,y_test)**0.5
    return rmse_train, rmse_test
lasso(alpha = 0.01)
# Write your solution here



