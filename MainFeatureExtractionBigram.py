__author__ = 'elizajasin'

import ReadAndWriteFile as RAWfile
import FeatureExtraction as FE

# read data from preprocessing
token = RAWfile.readDataPreprocessing("preprocessing_result.xlsx")

# make feature extraction
atribut = FE.makeAtributBigram(token)
FE_result = FE.sumFEBigram(token,atribut)
RAWfile.writeFEResult(FE_result,"feature_extraction_result.xlsx")
# FE_norm = FE.normalisasi(FE_result)
# RAWfile.writeFEResult(FE_norm,"feature_extraction_norm.xlsx")