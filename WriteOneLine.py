__author__ = 'elizajasin'

anjuran = open('anjuran.txt', encoding='utf-8', mode='r')
list_anjuran = anjuran.readlines()
anjuran.close()
kbbi = []
for i in range(len(list_anjuran)):
    kbbi.append(list_anjuran[i].strip('\n'))
s = ''
for i in range(len(kbbi)):
    s = s+kbbi[i]+'|'
print(s)