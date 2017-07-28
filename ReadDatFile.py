__author__ = 'elizajasin'

import pandas as pd

with open('data.dat','rb') as f:
    next(f) # skip first row
    df = pd.DataFrame(l.rstrip().split() for l in f)

print(df)