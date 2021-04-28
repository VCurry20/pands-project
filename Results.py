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


with open("review.txt", "wt") as f:                                               # Open File "Analysisout" as a txt file, in write txt mode
    print("\nThe full breakdown is: \n", df.describe(), file=f)                   # Breakdown of the csv - outputs a review of the numerical data
    print("\nThe Iris Setosa breakdown is: \n", setosa.describe(), file=f)        # Outputs just the Setosa variable breakdown data
    print("\nThe Iris Versicolor breakdown is: \n",versicolor.describe(), file=f) # Outputs just the versicolor variable breakdown data
    print("\nThe Iris Virginica is: \n", virginica.describe(), file=f)            # Outputs just the viginica variable breakdown data
    

