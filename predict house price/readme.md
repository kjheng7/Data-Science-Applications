# Predict House Price
Application Type: Machine Learning (Supervised)<br/>
Application Title: House price prediction<br/>
Application Objective: 
1) To calculate the accuracy of predicted house price using size of house
2) To determine the minimum error value
Model: Linear Regression
Programming Language: Python (jupyter notebook)
Python libraries: numpy, pandas, matplotlib.pyplot, sklearn
Process:
1) Read CSV data
2) Pre-process data (mean normalization: (data – mean) / (max data – min data))
3) Determine the shape of the data, create theta matrix
4) Convert linear equation (theta0 * x0 + theta1 * x1) to matrix equation ( x * theta transpose)
  a) Insert Bias Term (x0)
  b) Separate Bias and Size (x values), Price (y values) and convert to matrix format
5) Compute the error using above matrixes (summation of (x * theta transpose - y) power of 2)/ 2 * number of x rows 
6) Minimizing the error by input learning rate and test iteration number into gradient descent equation and obtain new values of theta
9) Apply new values of theta into matrix equation to get prediction values.
8) check prediction values:
  a) plot predicted data against original and check best fit line (if only have 2 parameters to compare)
  b) plot error vs iterations (error should reduce as iterations increases) 
9) Use mean_absolute_error function in sklearn library to find accuracy of predicted values.
