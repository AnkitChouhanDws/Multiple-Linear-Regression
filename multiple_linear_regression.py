# Multiple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Path to database')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

# Encoding categorical data
# Dummy Encoding(To don't let computer compare between categories)
# Encoding is necessary because we can't perform numerical operartions on it
# Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 3] = labelencoder_X.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()

# Avoiding the dummy variable trap
# Although some libraries takes care of it
X= X[:,1:]


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Fitting Multiple Linear Regression to the training set 
from sklearn.linear_model import LinearRegression
# Create the linearregressor object
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Now the model that we fitted is not the optimal model.
# Since, we have included all the independent variables, some are there which not affect or very
# less affect the dependent variables(i.e. non statistically significant variables )
# So we need to remove them through our model.

# Building the optimal solution using Backward elimination
import statsmodels.formula.api as sm
# This statsmodels library doesn't take intercept on y-axis(B0) into account.
# So we take the independent variable associated with it as 1.(X0=1)
X = np.append(arr = np.ones((50,1)).astype(int), values = X ,  axis = 1)

# Let's create the optimal matrix of features
# 1. Add all independent variables to the opt_matrix
X_opt= X[:, [0,1,2,3,4,5]] 
regressor_OLS = sm.OLS(endog=y, exog= X_opt).fit()
regressor_OLS.summary()

# By executing above 3 lines in ipython terminal, we have observed that 
# 2nd column has highest p-value(as compared to significance level= 0.5).
# So, let's remove this variable

X_opt= X[:, [0,1,3,4,5]] 
regressor_OLS = sm.OLS(endog=y, exog= X_opt).fit()
regressor_OLS.summary()
# To know how these variables are removed, run these above 3 lines and remove the variable with highest P-Value
# Until all variables contains P-value less than our significance level.

X_opt= X[:, [0,3,4,5]] 
regressor_OLS = sm.OLS(endog=y, exog= X_opt).fit()
regressor_OLS.summary()

X_opt= X[:, [0,3,5]] 
regressor_OLS = sm.OLS(endog=y, exog= X_opt).fit()
regressor_OLS.summary()

X_opt= X[:, [0,3]] 
regressor_OLS = sm.OLS(endog=y, exog= X_opt).fit()
regressor_OLS.summary()





