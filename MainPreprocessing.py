__author__ = 'elizajasin'

import ReadAndWriteFile as RAWfile
import Preprocessing as PreP

# Read Data
hadits = RAWfile.readData('hadits_merge_fix.xlsx')

# Preprocessing
remove_punct = PreP.removePunct(hadits)
case_fold = PreP.caseFolding(remove_punct)
stopword_remove = PreP.stopwordsRemoval('id.stopwords.02.01.2016.txt',case_fold)
lemma = PreP.lemmatization(stopword_remove)
remove_kbbi = PreP.stopword_kbbi(lemma)

#Write preprocessing result
RAWfile.writeData(remove_kbbi,"preprocessing_result_merge_fix.xlsx")