__author__ = 'elizajasin'

import ReadAndWriteFile as RAWfile
import FeatureExtraction as FE

# read data from preprocessing
token = RAWfile.readDataPreprocessing("preprocessing_result_merge_fix.xlsx")

# make feature extraction
atribut = FE.makeAtribut(token)
FE_result = FE.sumFE(token,atribut)
RAWfile.writeFEResultWithTxt(FE_result,"feature_extraction_result_merge_fix.txt")
# FE_norm = FE.normalisasi(FE_result)
# RAWfile.writeFEResult(FE_norm,"feature_extraction_norm.xlsx")