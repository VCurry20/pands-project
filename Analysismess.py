# just to ck outputs not for submission

# Reviewing the Data using Pandas

print ("Hello World")

import pandas as pd 
import numpy as np 

filename = 'kaggleIrisSet.csv'
df = pd.read_csv(filename)


#table = pd.pivot_table(df, values=['SepalLengthCm', 'PetalWidthCm'], index='species', columns=['Id'], aggfunc=np.sum, fill_value=0)
#df.to_excel("pivot.xlsx")


###df.to_excel("Dataprintout.xlsx") 