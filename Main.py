__author__ = 'elizajasin'

import ReadAndWriteFile as RAWfile

# read data from preprocessing
token = RAWfile.readDataPreprocessing("preprocessing_result.xlsx")

# manage data before ANN process
unigram = token
input_train = []
input_norm = RAWfile.readDataInputTrain('clear_prepro_data.xlsx')
for i in range(0,len(input_norm)):
    s = []
    for j in range(0,len(input_norm[i])):
        print(input_norm[i][j])
        if (input_norm[i][j]) == '0':
            s.append(0)
        else:
            s.append(1)
    input_train.append(s)
RAWfile.writeData(input_train,'data_input.xlsx')