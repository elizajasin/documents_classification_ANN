__author__ = 'elizajasin'

import ReadAndWriteFile as RAWfile

kelas = RAWfile.readDataClass("hadits_dist_1028.xlsx")
biner_class = []
for i in range(len(kelas)):
    if kelas[i] == 1 :
        temp = [1,0,0]
    elif kelas[i] == 2:
        temp = [0,1,0]
    else:
        temp = [0,0,1]
    biner_class.append(temp)
RAWfile.writeData(biner_class,"data_target_1028.xlsx")