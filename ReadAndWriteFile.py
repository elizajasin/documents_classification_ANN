__author__ = 'elizajasin'

import os
import openpyxl
from  openpyxl import Workbook

def readData (filename):
    os.getcwd
    wb = openpyxl.load_workbook(filename)
    sheet = wb.active
    hadits = []
    for i in range (2,102):
        hadits.append(str(sheet.cell(row=i,column=3).value))
    return hadits

def writeData (data, filename):
    wb = Workbook()
    ws = wb.active
    for i in range(len(data)):
        ws.append(data[i])
    wb.save(filename)