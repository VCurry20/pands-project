# Author Veronica Curry
# Student ID: G00074924
# Completed: April 2021

# Reviewing the Data using Pandas

print ("Hello World")

import pandas as pd 
import numpy as np 

filename = 'kaggleIrisSet.csv'
df = pd.read_csv(filename)


df.to_excel("Dataprintout.xlsx")                    # Print out to a CSV file - this could also be an excel file etc


# setting variables for printing below
irisData = pd.read_csv("kaggleIrisSet.csv")    
irisGroup = irisData.groupby("Species").size()
irisCorr = irisData.corr()




with open("Analysis1output.txt", "wt") as f:                                                   # Open File "Analysis1out" as a txt file, in write txt mode
    print("\nThe full breakdown is: \n", df.describe(), file=f)                                # Breakdown of the csv - outputs a review of the numerical data
    print("\nThe Sepal Length Column only is: \n", df.SepalLengthCm.describe(), file=f)        # Outputs just the SepalLengthCm Column
    print("\nThe Sepal Width Column only is: \n",df.SepalWidthCm.describe(), file=f)           # Outputs just the SepalWidthCm Column
    print("\nThe Petal Length Column only is: \n",df.PetalLengthCm.describe(), file=f)         # Outputs just the PetalLengthCm Column
    print("\nThe Petal Width Column only is: \n",df.PetalWidthCm.describe(), file=f)           # Outputs just the PetalWidthCm Column
    print("\nThe top lines of the data are as follows: \n",irisData.head(), file=f)            # Outputs the top rows of the data
    print("\nThe Data grouped by Species is: \n",irisGroup, file=f)                            # Outputs the data grouped by Species
    print("\nThe Pairwise correlation of colums is: \n",irisCorr, file=f)                      # Outputs the data in a 


