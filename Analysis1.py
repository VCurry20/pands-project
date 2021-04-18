# Reviewing the Data using Pandas

import pandas as pd 
import numpy as np 

filename = 'kaggleIrisSet.csv'
df = pd.read_csv(filename)


#df.to_csv("Dataprintout.csv")                        # Print out to a CSV file - this could also be an excel file etc

# print(df.describe())                                # Breakdown of the csv - outputs a review of the numerical data
# print(df.describe(include='all'))                   # Outputs all the data
# print (df.SepalLengthCm.describe())                 # Outputs just the SepalLengthCm Column
# print(df.SepalWidthCm.describe())                   # Outputs just the SepalWidthCm Column
# print(df.PetalLengthCm.describe())                  # Outputs just the PetalLengthCm Column
# print(df.PetalWidthCm.describe())                   # Outputs just the PetalWidthCm Column
print(df.describe(exclude=[np.Species]))
# print(df.describe()