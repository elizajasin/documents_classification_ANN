__author__ = 'elizajasin'

def makeAtribut (data):
    atribut = {}
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] not in atribut.keys():
                atribut[data[i][j]] = []
    return atribut

def sumFE (data, atribut):
    for i in range(len(data)):
        for key in atribut:
            atribut[key].append(0)
        for j in range(len(data[i])):
            if data[i][j] in atribut.keys():
                atribut[data[i][j]][i] += 1
    return atribut