# Author Veronica Curry
# Student ID: G00074924
# Completed: April 2021

# This file provides a summary of the information in other files. This is not an exhaustive list, please note the additional files.

# Provide a summary of each variable in a single txt file
# Save a historgram of each variable in a PNG file
# Sets outputs of a scatterplot of each pair of variables


import numpy as np                               # Import Modules  - NumPy
import pandas as pd                              # Import Modules  - Pandas
import matplotlib.pyplot as plt                  # Import Modules  - Matplotlib
import seaborn as sns                            # Import Modules  - Seaborn


filename = 'kaggleIrisSet.csv'                      # Import File
df = pd.read_csv(filename)                          # Set variable for file - Pandas - read the CSV file


setosa = df.loc[df["Species"] =="Iris-setosa"]              # Set variable for specific Iris - Setosa
versicolor = df.loc[df["Species"] =="Iris-versicolor"]      # Set variable for specific Iris - Versicolor
virginica = df.loc[df["Species"] =="Iris-virginica"]        # Set variable for specific Iris - Virginica


with open("analysisOutout.txt", "wt") as f:                                                  # Open File "Analysisout" as a txt file, in write txt mode
    print("\nThe fileover view is: \n", df.describe(), file=f)                               # Outputs the datafile Column 
    print("\nThe Sepal Length Column only is: \n", df.SepalLengthCm.describe(), file=f)      # Outputs the SepalLengthCm Column
    print("\nThe Sepal Width Column only is: \n",df.SepalWidthCm.describe(), file=f)         # Outputs the SepalWidthCm Column
    print("\nThe Petal Length Column only is: \n",df.PetalLengthCm.describe(), file=f)       # Outputs the PetalLengthCm Column
    print("\nThe Petal Width Column only is: \n",df.PetalWidthCm.describe(), file=f)         # Outputs the PetalWidthCm Column
    print("\nThe Species details are: \n",df.Species.describe(), file=f)                     # Outputs the Species Column
    print("\nThe Data grouped by Species is: \n \n",df.groupby("Species").size(), file=f)    # Outputs the data grouped by Species


# 










# Scatterplots
plt.figure(figsize=(10,10))
plt.subplot(2,2,1)
scatterplot = sns.scatterplot(x = "SepalLengthCm", y = "SepalWidthCm", data = df, hue="Species", legend=True, palette=("husl")) 
plt.subplot(2,2,2)
scatterplot = sns.scatterplot(x = "PetalLengthCm", y = "PetalWidthCm", data = df, hue="Species", legend=True, palette=("husl")) 
plt.subplot(2,2,3)
scatterplot = sns.scatterplot(x = "SepalLengthCm", y = "PetalLengthCm", data = df, hue="Species", legend=True, palette=("husl")) 
plt.subplot(2,2,4)
scatterplot = sns.scatterplot(x = "SepalWidthCm", y = "PetalWidthCm", data = df, hue="Species", legend=True, palette=("husl"))
plt.suptitle("Fisher's Iris Dataset", size=20)
plt.tight_layout()
#plt.show()
plt.savefig("Scatterplots.png") 










