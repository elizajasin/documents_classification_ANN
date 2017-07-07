__author__ = 'elizajasin'

import ReadAndWriteFile as RAWfile
import re
from py2casefold import casefold

# Read Data
hadits = RAWfile.readData('hadits_fix.xlsx')

# Matching Words
words = []
for i in range(len(hadits)):
    match = re.search(r'(\w+lah)', hadits[i])
    if match:
        if (casefold(match.groups()[0]) not in words):
            words.append(casefold(match.groups()[0]))

# Write Classes Result
file = open('lah_results.txt', 'w')
for i in range(len(words)):
	file.write(words[i]+'\n')
file.close()