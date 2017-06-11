__author__ = 'elizajasin'

def makeAtribut (data):
    atribut = {}
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] not in atribut.keys():
                atribut[data[i][j]] = []
    return atribut

def makeAtributBigram (data):
    atribut = {}
    for i in range(len(data)):
        for j in range(len(data[i])):
            if (j == 0) and (data[i][j]+'|<s>' not in atribut.keys()):
                atribut[data[i][j]+'|<s>'] = []
            else:
                if data[i][j]+'|'+data[i][j-1] not in atribut.keys():
                    atribut[data[i][j]+'|'+data[i][j-1]] = []
                if (j == len(data[i])) and ('</s>|' + data[i][j] not in atribut.keys()):
                    atribut['</s>|' + data[i][j]] = []
    return atribut

def makeAtributTrigram (data):
    atribut = {}
    for i in range(len(data)):
        for j in range(1,len(data[i])):
            if (j == 1) and (data[i][j]+'|<s>,'+data[i][j-1] not in atribut.keys()):
                atribut[data[i][j]+'|<s>,'+data[i][j-1]] = []
            else:
                if data[i][j]+'|'+data[i][j-2]+','+data[i][j-1] not in atribut.keys():
                    atribut[data[i][j]+'|'+data[i][j-2]+','+data[i][j-1]] = []
                if (j == len(data[i])) and ('</s>|' + data[i][j-1] + ',' + data[i][j] not in atribut.keys()):
                    atribut['</s>|' + data[i][j-1] + ',' + data[i][j]] = []
    return atribut

def sumFE (data, atribut):
    for i in range(len(data)):
        for key in atribut:
            atribut[key].append(0)
        for j in range(len(data[i])):
            if data[i][j] in atribut.keys():
                atribut[data[i][j]][i] += 1
    return atribut

def sumFEBigram (data, atribut):
    for i in range(len(data)):
        for key in atribut:
            atribut[key].append(0)
        for j in range(len(data[i])):
            if (j == 0) and (data[i][j]+'|<s>' in atribut.keys()) and (atribut[data[i][j]+'|<s>'][i] == 0):
                atribut[data[i][j]+'|<s>'][i] = 1
                # atribut[data[i][j] + '|<s>'][i] += 1
            else:
                if (data[i][j]+'|'+data[i][j-1] in atribut.keys()) and (atribut[data[i][j]+'|'+data[i][j-1]][i] == 0):
                    atribut[data[i][j]+'|'+data[i][j-1]][i] = 1
                    # atribut[data[i][j] + '|' + data[i][j - 1]][i] += 1
                if (j == len(data[i])) and ('</s>|' + data[i][j] in atribut.keys()) and (atribut['</s>|' + data[i][j]][i] == 0):
                    atribut['</s>|' + data[i][j]][i] = 1
                    # atribut['</s>|' + data[i][j]][i] += 1
    return atribut

def sumFETrigram (data, atribut):
    for i in range(len(data)):
        for key in atribut:
            atribut[key].append(0)
        for j in range(len(data[i])):
            if (j == 0) and (data[i][j]+'|<s>' in atribut.keys()) and (atribut[data[i][j]+'|<s>'][i] == 0):
                atribut[data[i][j]+'|<s>'][i] = 1
                # atribut[data[i][j] + '|<s>'][i] += 1
            else:
                if (data[i][j]+'|'+data[i][j-1] in atribut.keys()) and (atribut[data[i][j]+'|'+data[i][j-1]][i] == 0):
                    atribut[data[i][j]+'|'+data[i][j-1]][i] = 1
                    # atribut[data[i][j] + '|' + data[i][j - 1]][i] += 1
                if (j == len(data[i])) and ('</s>|' + data[i][j] in atribut.keys()) and (atribut['</s>|' + data[i][j]][i] == 0):
                    atribut['</s>|' + data[i][j]][i] = 1
                    # atribut['</s>|' + data[i][j]][i] += 1
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