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

def normalisasi (atribut):
    norm_atribut = {}
    for key in atribut:
        norm_atribut[key] = []
    for key in atribut:
        sum = 0
        for i in range(len(atribut[key])):
            sum += atribut[key][i]
        for i in range(len(atribut[key])):
            norm = atribut[key][i]/sum
            norm_atribut[key].append(str(round(norm,2)))
    return norm_atribut