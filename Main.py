__author__ = 'elizajasin'

import Preprocessing as PreP

# Preprocessing
hadits = PreP.readData('hadits_fix.xlsx')
remove_punct = PreP.removePunct(hadits)
case_fold = PreP.caseFolding(remove_punct)
stopword_remove = PreP.stopwordsRemoval('id.stopwords.02.01.2016.txt',case_fold)
lemma = PreP.lemmatization(stopword_remove)

print(lemma)