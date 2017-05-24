__author__ = 'elizajasin'

import ReadAndWriteFile as RAWfile
import FeatureExtraction as FE

#read data from preprocessing
token = RAWfile.readDataPreprocessing("preprocessing_result.xlsx")

#make feature extraction
atribut = FE.makeAtribut(token)

print(atribut)
print(len(atribut))