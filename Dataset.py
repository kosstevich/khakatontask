import sklearn as skl
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score

class Dataset:
    def getDataSet(self):
        diabetes_X, diabetes_y = skl.datasets.load_diabetes(return_X_y=True)
        diabetes_X_train = diabetes_X[:-42]
        diabetes_X_test = diabetes_X[-42:]
        diabetes_y_train = diabetes_y[:-42]
        diabetes_y_test = diabetes_y[-42:]
        return diabetes_X_train, diabetes_y_train, diabetes_X_test, diabetes_y_test
    
    def getCSV(self):
        data = pd.read_csv('data.csv')
        return data

