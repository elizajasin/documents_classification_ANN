__author__ = 'elizajasin'

import ReadAndWriteFile as RAWfile
import FeatureExtraction as FE

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
for key in FE_result:
    input_train.append(FE_result[key])
# class_train = []
class_train = RAWfile.readDataClass('hadits_fix.xlsx')