#-*- coding: UTF-8 -*-
from Neuro import Neuro
from Dataset import Dataset
from Array import Array


d = Dataset()
dXTrain, dYTrain, dXTest, dYTest = d.getDataSet()

if __name__ == "__main__":
    neuro = Neuro(dXTrain, dYTrain, dXTest, dYTest)
    neuro.trainFit(neuro.dXTrain, neuro.dYTrain)

	