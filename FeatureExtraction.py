__author__ = 'elizajasin'

def makeAtribut (data):
    atribut = {}
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] not in atribut.keys():
                atribut[data[i][j]] = 0
    return atribut