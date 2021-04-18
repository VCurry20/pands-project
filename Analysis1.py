# Reviewing the Data using Pandas

import pandas as pd 
import numpy as np 

filename = 'kaggleIrisSet.csv'
df = pd.read_csv(filename)


# df.to_excel("Dataprintout.xlsx")                    # Print out to a CSV file - this could also be an excel file etc


#with open(".\Analysis1results.txt", "w") as f:
   #print(df.describe())                                # Breakdown of the csv - outputs a review of the numerical data
    #print(df.describe(include='all'))                   # Outputs all the data
    #print (df.SepalLengthCm.describe())                 # Outputs just the SepalLengthCm Column
    #print(df.SepalWidthCm.describe())                   # Outputs just the SepalWidthCm Column
    #print(df.PetalLengthCm.describe())                  # Outputs just the PetalLengthCm Column
    #print(df.PetalWidthCm.describe())                   # Outputs just the PetalWidthCm Column
# print(df.describe(exclude=[np.Species]))
# print(df.describe()

with open("Analysis1output.txt", "wt") as f:                                                   # Open File "Analysis1out" as a txt file, in write txt mode
    print("\nThe full breakdown is: \n", df.describe(), file=f)                                # Breakdown of the csv - outputs a review of the numerical data
    print("\nThe Sepal Length Column only is: \n", df.SepalLengthCm.describe(), file=f)        # Outputs just the SepalLengthCm Column
    print("\nThe Sepal Width Column only is: \n",df.SepalWidthCm.describe(), file=f)           # Outputs just the SepalWidthCm Column
    print("\nThe Petal Length Column only is: \n",df.PetalLengthCm.describe(), file=f)         # Outputs just the PetalLengthCm Column
    print("\nThe Petal Width Column only is: \n",df.PetalWidthCm.describe(), file=f)           # Outputs just the PetalWidthCm Column
