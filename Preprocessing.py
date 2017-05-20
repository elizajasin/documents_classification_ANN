__author__ = 'elizajasin'

import os
import openpyxl
from string import punctuation
import re
from py2casefold import casefold
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

def readData (filename):
    os.getcwd
    wb = openpyxl.load_workbook(filename)
    sheet = wb.active
    hadits = []
    for i in range (2,302):
        hadits.append(str(sheet.cell(row=i,column=7).value))
    return hadits

def lemmatization (hadits):
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    for i in range (0,300):
        hadits[i] = stemmer.stem(hadits[i])
    return hadits

def removePunct (hadits):
    punct = list(punctuation)
    punct.remove("-")
    punct = ''.join(punct)
    no_punctional = []
    for i in range (0,300):
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
    for i in range (0,300):
        stop_remove = [i for i in hadits[i] if i not in sw]
        stopword_remove.append(stop_remove)
    return stopword_remove

def caseFolding (hadits):
    for i in range (0,300):
        for j in range(len(hadits[i])):
            hadits[i][j] = casefold(hadits[i][j])
    return hadits