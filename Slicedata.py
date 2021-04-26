# Author Veronica Curry
# Student ID: G00074924
# Completed: April 2021

# Reviewing the Data using Pandas

print ("Hello World")                                       # Sanity Check

import numpy as np                                          # Import Numpy Module
import pandas as pd                                         # Import Pandas Module
                            

filename = 'kaggleIrisSet.csv'                              # Import File
df = pd.read_csv(filename)                                  # Set variable for file - Pandas - read the CSV file


# print(df[10:21])                                          # Print lines 10 - 20

specific_data=df[["Id", "Species"]]                         # Set variable for specific data
#print (specific_data)                                      # Unhighlight to print in code in VS Code / Terminal

setosa = df.loc[df["Species"] =="Iris-setosa"]              # Set variable for specific data
#print(setosa)                                              # Unhighlight to print in code in VS Code / Terminal

versicolor = df.loc[df["Species"] =="Iris-versicolor"]      # Set variable for specific data
#print(versicolor)                                          # Unhighlight to print in code in VS Code / Terminal

virginica = df.loc[df["Species"] =="Iris-virginica"]        # Set variable for specific data
#print(virginica)                                           # Unhighlight to print in code in VS Code / Terminal


with open("Sliceoutput.txt", "wt") as f:                                                                   # Open File "Sliceoutput.txt" as a txt file, in write txt mode
    print("\nIn this file I will show ways the data can be broken down. \n", file=f)                       # Breakdown of the csv - outputs a review of the numerical data
    print("\nWe can print choosen parts; here I have choosen lines 10-20: \n", df[10:21], file=f)          # Print specific rows
    print("\nIn this case I have choose two columns - 'Id' and 'Species': \n", specific_data, file=f)      # Print Id and Species as choosen in variable
    print("\nWe can then also print just by the particular flower -  Iris Setosa': \n", setosa , file=f)   # Print the file details for the flower Iris Setosa
    print("\nThen the next flower -  Iris Versicolor': \n", versicolor , file=f)                           # Print the file details for the flower Iris Versicolor
    print("\nAnd finally the last remaining flower -  Iris Virginica': \n", virginica , file=f)            # Print the file details for the flower Iris Virginica



