__author__ = 'elizajasin'

from string import punctuation
import re
from py2casefold import casefold
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

def lemmatization (hadits):
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    for i in range(len(hadits)):
        for j in range(len(hadits[i])):
            hadits[i][j] = stemmer.stem(hadits[i][j])
    return hadits

def removePunct (hadits):
    punct = list(punctuation)
    punct.remove("-")
    punct = ''.join(punct)
    no_punctional = []
    for i in range (len(hadits)):
        remove_punct = re.compile('[%s]' % re.escape(punctuation)).sub('',hadits[i])
        remove_punct = re.split(r'\s',remove_punct)
        no_punctional.append(remove_punct)
    return no_punctional

def stopwordsRemoval (filename,hadits):
    stopword_remove = []
    stopword = open (filename, encoding='utf-8', mode='r')
    sw = stopword.readlines()
    stopword.close()
    sw = [word.strip() for word in sw]
    sw = set(sw)
    for i in range (len(hadits)):
        stop_remove = [i for i in hadits[i] if i not in sw]
        stopword_remove.append(stop_remove)
    return stopword_remove

def caseFolding (hadits):
    for i in range (len(hadits)):
        for j in range(len(hadits[i])):
            hadits[i][j] = casefold(hadits[i][j])
    return hadits