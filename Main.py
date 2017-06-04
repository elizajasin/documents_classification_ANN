__author__ = 'elizajasin'

import ReadAndWriteFile as RAWfile
import FeatureExtraction as FE
import NeuralNetwork as NN
import numpy as np
import time

#read data from preprocessing
token = RAWfile.readDataPreprocessing("preprocessing_result.xlsx")

#make feature extraction
atribut = FE.makeAtribut(token)
FE_result = FE.sumFE(token,atribut)
# # RAWfile.writeFEResult(FE_result,"feature_extraction_result.xlsx")
# FE_norm = FE.normalisasi(FE_result)
# RAWfile.writeFEResult(FE_norm,"feature_extraction_norm.xlsx")

# manage data before ANN process
unigram = token
input_train = []
input_norm = RAWfile.readDataInputTrain('clear_prepro_data.xlsx')
for i in range(0,len(input_norm)):
    s = []
    for j in range(0,len(input_norm[i])):
        if (input_norm[i][j]) == '0':
            s.append(0)
        else:
            s.append(1)
    input_train.append(s)
class_train = []
classes = RAWfile.readDataClass('hadits_fix.xlsx')
for i in range(0,len(classes)):
    if classes[i] == 1:
        class_train.append([1,0,0])
    elif classes[i] == 2:
        class_train.append([0,1,0])
    else:
        class_train.append([0,0,1])
RAWfile.writeData(class_train,'data_target.xlsx')
RAWfile.writeData(input_train,'data_input.xlsx')

# try ANN

