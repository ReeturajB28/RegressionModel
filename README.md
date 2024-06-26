# RegressionModel

This is a multiple linear regression model created on Algerian Forest Fire dataset. The objective is to predict based on certain weather variables for two resgions within Algeria, we need to predict what will be the fire weather index(propensity of a fire in the forest).

We have done Feature Engineering(removing null values, treating outliers, scaling the data), Feature Selection( through correlation) and trained the model after splitting the data into train and test set.
We have used the normal Linear Regression model as well applied regularization techniques- Lasso,Ridge, Elastic net. We have achived the highest R2 score with Ridge Rigression and have converted the same into a pickle file for model deployment and prediction.
