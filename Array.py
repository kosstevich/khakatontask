import numpy as np

class Array:
    def __init__(self):
        pass

    def correctArr(self, weights, Xtrain, Ytrain):
        
        # Ищем максимальные веса и их индексы 

        max = [0,0,0]
        imax = [0,0,0]

        for i in range(0,len(weights)):
            if max[0]<weights[i]:
                max[0] = weights[i]
                imax[0] = i

        for i in range(0,len(weights)):
            if max[1]<weights[i] and weights[i] <= max[0] and imax[0] != i:
                max[1] = weights[i]
                imax[1] = i

        for i in range(0,len(weights)):
            if max[2]<weights[i] and weights[i] <= max[1] and imax[1] != i:
                max[2] = weights[i]
                imax[2] = i


        #Дописать удаление столбца из массива Xtrain и Ytrain


        # dX_finalTrain = Xtrain
        #  dY_finalTrain = Ytrain 

        #  for i in range(0, ):
        #       for j in range(0,10):
        #          if j == imax[0] or j == imax[1] or j == imax[2]: 
        #             dX_finalTrain+=Xtrain[i][j]


        return dX_finalTrain, dY_finalTrain




        


        

            