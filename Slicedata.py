# Author Veronica Curry
# Student ID: G00074924
# Completed: April 2021

# Reviewing the Data using Pandas

print ("Hello World")                               # Sanity Check

import numpy as np                                  # Import Numpy Module
import pandas as pd                                 # Import Pandas Module
                            

filename = 'kaggleIrisSet.csv'                      # Import File
df = pd.read_csv(filename)                          # Set variable for file - Pandas - read the CSV file

# print(df[10:21])

specific_data=df[["Id", "Species"]]
#print (specific_data)

setosa = df.loc[df["Species"] =="Iris-setosa"]
print(setosa)

versicolor = df.loc[df["Species"] =="Iris-versicolor"]
print(versicolor)

virginica = df.loc[df["Species"] =="Iris-virginica"]
print(virginica)