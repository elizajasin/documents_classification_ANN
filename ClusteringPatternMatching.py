__author__ = 'elizajasin'

import ReadAndWriteFile as RAWfile
from openpyxl import Workbook
import re

# Read Data
hadits = RAWfile.readData('hadits_fix.xlsx')

# Matching Words
classes = []
for i in range(len(hadits)):
    match1 = re.search(r'jangan|larang|tidak boleh|tinggalkan', hadits[i])
    match2 = re.search(r'bacalah|intailah|tunggulah|hendaklah|permudahlah|sembelihlah|ringankanlah|kenalilah|bertanyalah|berikanlah|hamparkanlah|melemparlah|katakanlah|berbicaralah|hijabilah|minumlah|biarkanlah|buanglah|tetaplah|cucilah|istihadlah|ambillah|sisirlah|ikutlah|pergilah|singkirkanlah|takbirlah|jadikanlah|bangunlah|shalatlah|jagalah|bebaskanlah|tunjukkanlah|lepaskanlah|thawaflah|bawalah|dirikanlah|seimbanglah|tundalah|hapuslah|lakukanlah|sempurnakanlah|bergemberilah|ajaklah|serukanlah|jawablah|kembalilah|iqamatlah|berjalanlah|suruhlah|dahulukanlah|makanlah|teruskanlah|jarilah|rukuklah|taatlah|luruskanlah|bertakbirlah|kembalikanlah|ucapkanlah|ulangilah|pulanglah|berdirilah|berilah|mandilah|izinkanlah|terimalah|diamlah|turunlah|turunkanlah|terjadilah|berdoalah|angkatlah|witirlah|tidurlah|shaumlah|kesinilah|bertahallullah|tanyailah|sederhanakanlah|sebutlah|bertakwalah|bersabarlah|berinfaklah|masukkanlah|tolonglah|datangkanlah|cobalah', hadits[i])

    if match1:
        classes.append(3)
    elif match2:
        classes.append(2)
    else:
        classes.append(1)

# Write Classes Result
wb = Workbook()
ws = wb.active
for i in range(len(classes)):
    ws.cell(row=i+1, column=1).value = classes[i]
wb.save('result_clustering.xlsx')