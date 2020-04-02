import matplotlib.pyplot as plt
import sklearn.datasets as dsets
import sklearn.linear_model as slm
from sklearn.metrics import mean_squared_error, r2_score
from Array import Array

a = Array()

class Neuro:
    def __init__(self, dXTrain, dYTrain, dXTest, dYTest):     
        self.dXTrain = dXTrain
        self.dYTrain = dYTrain
        self.dXTest = dXTest
        self.dYTest = dYTest

    def trainFit(self, inputX, inputY):
        regr = slm.LinearRegression()
        regr.fit(inputX, inputY)
        dYPred = regr.predict(self.dXTest)
        
        print('Coefficients: \n', regr.coef_)
        print('Mean squared error: %.2f' % mean_squared_error(self.dYTest, dYPred))
        print('Coefficient of determination: %.2f' % r2_score(self.dYTest, dYPred))
        
        #Получаем изменённые параметры X,Y
        dX_finalTrain, dY_finalTrain = a.correctArr(regr.coef_, inputX, inputY) 

        #Насколько я понял тут я тренирую и тестирую модель на новых значениях
        regr.fit(dX_finalTrain, dY_finalTrain)
        dYPred_final = regr.predict(self.dXTest)

        print('Final coefficients: \n', regr.coef_)
        print('Final mean squared error: %.2f' % mean_squared_error(self.dYTest, dYPred))
        print('Final coefficient of determination: %.2f' % r2_score(self.dYTest, dYPred))

        #Нужно реализовать предсказание для для новых файлов

