__author__ = 'elizajasin'

import Preprocessing as PreP

# Preprocessing
hadits = PreP.readData('hadits_eliza.xlsx')
# lemma = PreP.lemmatization(hadits)
remove_punct = PreP.removePunct(hadits)
stopword_remove = PreP.stopwordsRemoval('id.stopwords.02.01.2016.txt',remove_punct)
case_fold = PreP.caseFolding(stopword_remove)

print(case_fold[0][0])