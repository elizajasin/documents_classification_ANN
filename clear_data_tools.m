% read data
preprocessing_data = xlsread('feature_extraction_result.xlsx');
preprocessing_data = preprocessing_data';
norm_data = normc(preprocessing_data);
class = xlsread('hadits_fix_2.xlsx','D2:D1297');
data = horzcat(norm_data,class);

% write clear data
xlswrite('clear_prepro_data.xlsx',data,1)