#!/usr/bin/python

import numpy as np
#np.set_printoptions(threshold=np.nan)
from DataLib import DataLib
from NeuralNet import NeuralNet
from NNLib import NNLib

def main():
    data = DataLib.csvToArray("../heart_disease_dataset.csv")
    
    dataNorm = DataLib.normalizeData(data,np.array([0,3,4,7,9,11]))
    
    # Firsy
    nn = NeuralNet(dataNorm,1,2)

    nn.train(100)


if __name__ == "__main__":
    main()

