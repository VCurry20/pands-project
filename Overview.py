# Author Veronica Curry
# Student ID: G00074924
# Completed: April 2021

# Reviewing the Data using Pandas

print ("Hello World")                               # Sanity Check

import numpy as np                                  # Import Numpy Module
import pandas as pd                                 # Import Pandas Module
                            

filename = 'kaggleIrisSet.csv'                      # Import File
df = pd.read_csv(filename)                          # Set variable for file - Pandas - read the CSV file


df.to_excel("Dataprintout.xlsx")                    # Print out to a CSV file - this could also be an excel file etc


# Alternative Methods

irisGroup = df.groupby("Species").size()            # Set requirement to group by species and give the file output for each - print below



# Open file and print the following:
# Some lines include more code / some print variables set above 
# The following will print the output with new lines between results \n

with open("Analysisoutput.txt", "wt") as f:                                                   # Open File "Analysisout" as a txt file, in write txt mode
    print("\nThe full breakdown is: \n", df.describe(), file=f)                                # Breakdown of the csv - outputs a review of the numerical data
    print("\nThe Sepal Length Column only is: \n", df.SepalLengthCm.describe(), file=f)        # Outputs just the SepalLengthCm Column
    print("\nThe Sepal Width Column only is: \n",df.SepalWidthCm.describe(), file=f)           # Outputs just the SepalWidthCm Column
    print("\nThe Petal Length Column only is: \n",df.PetalLengthCm.describe(), file=f)         # Outputs just the PetalLengthCm Column
    print("\nThe Petal Width Column only is: \n",df.PetalWidthCm.describe(), file=f)           # Outputs just the PetalWidthCm Column
    print("\nThe top lines of the data are as follows: \n", df.head(), file=f)                 # Outputs the top rows of the data
    print("\nThe last lines of the data are as follows: \n", df.tail(), file=f)                # Outputs the last rows of the data
    print("\nThe Data grouped by Species is: \n \n",irisGroup, file=f)                         # Outputs the data grouped by Species



import io                                                                       # Code found on Stackoverflow - allows File info to be printed to Another TXT file
buffer = io.StringIO()
df.info(buf=buffer)
i = buffer.getvalue()
with open("Analysisoutput.txt", "a") as f:
    f.write("\nThis is an overview of the file information: \n{}".format(i))

# https://stackoverflow.com/questions/64067424/how-to-convert-df-info-into-data-frame-df-info
    
