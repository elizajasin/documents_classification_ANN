% read data
preprocessing_data = xlsread('feature_extraction_result.xlsx','A1:CV838');
norm_data = normc(preprocessing_data);