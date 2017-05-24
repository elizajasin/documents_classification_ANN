__author__ = 'elizajasin'

import ReadAndWriteFile as RAWfile
import Preprocessing as PreP

# Read Data
hadits = RAWfile.readData('hadits_fix.xlsx')

# Preprocessing
remove_punct = PreP.removePunct(hadits)
case_fold = PreP.caseFolding(remove_punct)
stopword_remove = PreP.stopwordsRemoval('id.stopwords.02.01.2016.txt',case_fold)
lemma = PreP.lemmatization(stopword_remove)



print(lemma)