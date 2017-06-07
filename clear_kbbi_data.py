from csv import reader
import re

# load csv file
dataset = []
with open('kbbi_data.csv', 'r', encoding='utf8') as file:
	csv_reader = reader(file)
	for row in csv_reader:
		if not row:
			continue
		dataset.append(row)

# cut the words
words = []
for i in range(1,len(dataset)):
    match = re.search(r'\d\s([.\S]+)\s',dataset[i][0])
    words.append(match.groups()[0])

# save words
file = open('words_kbbi.txt', 'w')
for i in range(len(words)):
	file.write(words[i]+'\n')
file.close()