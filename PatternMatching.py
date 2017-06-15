__author__ = 'elizajasin'

import ReadAndWriteFile as RAWfile
import re

# Read Data
hadits = RAWfile.readData('hadits_dist_172.xlsx')

# Matching Words
classes = []
for i in range(len(hadits)):
    match1 = re.search(r'jangan', hadits[i])
    match2 = re.search(r'larang', hadits[i])
    match3 = re.search(r'lah', hadits[i])

    if match1:
        classes.append(3)
    elif match2:
        classes.append(3)
    elif match3:
        classes.append(2)
    else:
        classes.append(1)

# Read Target Classes
target = RAWfile.readDataClass('hadits_dist_172.xlsx')

# Accuracy
nTrue = 0
for i in range(len(classes)):
    if classes[i] == target[i]:
        nTrue += 1
accuracy = nTrue/len(classes)*100

print('Accuracy : ' + str.format('{0:.15f}',accuracy))