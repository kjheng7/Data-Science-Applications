This notebook uses dataset from Kaggle learn competition (Ames Housing dataset)

Challenge is to predict the final price and achieve the lowest mean absolute error score :

1) Data is split into train test data and preprocessed with pipeline using SimpleImputer and OneHotEncoder for numerical and categorical data. 
2) Categorical data with high unique values are removed
3) RandomForest and XGBoost models are used for training and prediction  