__author__ = 'elizajasin'

import os
import openpyxl
from  openpyxl import Workbook

def readData (filename):
    os.getcwd
    wb = openpyxl.load_workbook(filename)
    ws = wb.active
    hadits = []
    for i in range (2,102):
        hadits.append(str(ws.cell(row=i,column=3).value))
    return hadits

def writeData (data, filename):
    wb = Workbook()
    ws = wb.active
    for i in range(len(data)):
        ws.append(data[i])
    wb.save(filename)

def readDataPreprocessing (filename):
    os.getcwd
    wb = openpyxl.load_workbook(filename)
    ws = wb.active
    hadits = []
    for i in range (1,101):
        s = []
        for j in range(1,ws.max_column):
            s.append(str(ws.cell(row=i,column=j).value))
        hadits.append(s)
    for i in range(len(hadits)):
        while 'None' in hadits[i]:
            hadits[i].remove('None')
    return hadits