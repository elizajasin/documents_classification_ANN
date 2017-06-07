__author__ = 'elizajasin'

import ReadAndWriteFile as RAWfile

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