% read data
preprocessing_data = xlsread('feature_extraction_result.xlsx');
% preprocessing_data = preprocessing_data';
% norm_data = normc(preprocessing_data);
% class = xlsread('hadits_dist_172.xlsx','D2:D517');
% data = horzcat(norm_data,class);


% write clear data
% xlswrite('clear_prepro_data.xlsx',data,1)

% manual input ann
data = preprocessing_data';
target = xlsread('data_target.xlsx');
% 
% for i = 1:516
%     for j = 1:6080
%         if data(i,j) ~= 0
%             data(i,j) = 1
%         end
%     end
% end