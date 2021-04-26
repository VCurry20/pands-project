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


sns.set_palette("bright")                                                 # set seaborn color palette
sns.set_style("ticks", {"xtick.major.size": 8, "ytick.major.size": 8})    # Set background style
sns.color_palette("husl", 9)                                              # Set Color Palette




# Histogram of Variable

# Simple Histogram Output
sns.histplot(df["SepalWidthCm"], bins=16, palette=("husl"))   # Seaborn create histogram - Iris File dataframe variable - "Sepal Width" - 16 bins - Color Palette    
plt.tight_layout()                                            # Crop output
plt.savefig("Hisplot.png")                                    # Create file and save to file "Histplot"
plt.show()                                                    # Show plot


# Varients of Histogram 
sns.histplot( data=df, x="SepalLengthCm", legend=True, kde=True, hue="Species", multiple="stack")   # Seaborn create histogram - Iris File dataframe - Set X axis, add legend, KDE Line, Map species info, stack format  
plt.tight_layout()                                                                                  # Crop output  
plt.savefig("HisplotA.png")                                                                         # Create file and save to file "Histplot A"          
plt.show()                                                                                          # Show plot                       

sns.histplot( data=df, x="SepalWidthCm", legend=True, hue="Species", element="poly")                # Seaborn create histogram - Iris File dataframe - Set X axis, add legend, Map species info, stack format  
plt.tight_layout()                                                                                  # Crop output   
plt.savefig("HisplotB.png")                                                                         # Create file and save to file "Histplot B"    
plt.show()                                                                                          # Show plot    

sns.histplot( data=df, x="PetalLengthCm", legend=True, kde=True, hue="Species", element="step",stat="density", common_norm=False) # Seaborn create histogram - Iris File dataframe - Set X axis, add legend, KDE Line, Map species info, stack format ,normalise 
plt.tight_layout()                                                                                                                # Crop output
plt.savefig("HisplotC.png")                                                                                                       # Create file and save to file "Histplot C"    
plt.show()                                                                                                                        # Show plot    

sns.histplot( data=df, x="PetalWidthCm", y="Species", legend=True, hue="Species")    # Seaborn create histogram - Iris File dataframe - Set X axis, Set Y axis, add legend, Map species info 
plt.tight_layout()                                                                   # Crop output  
plt.savefig("HisplotD.png")                                                          # Create file and save to file "Histplot C"  
plt.show()                                                                           # Show plot




# Scatterplots of Variables
plt.figure(figsize=(10,10))                                                                                              # plot figure size
plt.subplot(2,2,1)                                                                                                       # subplot - 2 * 2 - plot 1
sns.scatterplot(x = "SepalLengthCm", y = "SepalWidthCm", data = df, hue="Species", legend=True, palette=("husl"))        # Seaborn Scatterplot - ( set X axis / set Y axis ), Data from Iris File, Hue - Species, include a legend, Palette - set color
plt.subplot(2,2,2)                                                                                                       # subplot - 2 * 2 - plot 2
sns.scatterplot(x = "PetalLengthCm", y = "PetalWidthCm", data = df, hue="Species", legend=True, palette=("husl"))        # Seaborn Scatterplot - ( set X axis / set Y axis ), Data from Iris File, Hue - Species, include a legend, Palette - set colo
plt.subplot(2,2,3)                                                                                                       # subplot - 2 * 2 - plot 3
sns.scatterplot(x = "SepalLengthCm", y = "PetalLengthCm", data = df, hue="Species", legend=True, palette=("husl"))       # Seaborn Scatterplot - ( set X axis / set Y axis ), Data from Iris File, Hue - Species, include a legend, Palette - set colo
plt.subplot(2,2,4)                                                                                                       # subplot - 2 * 2 - plot 4
sns.scatterplot(x = "SepalWidthCm", y = "PetalWidthCm", data = df, hue="Species", legend=True, palette=("husl"))         # Seaborn Scatterplot - ( set X axis / set Y axis ), Data from Iris File, Hue - Species, include a legend, Palette - set colo
plt.suptitle("Fisher's Iris Dataset", size=20)                                                                           # Set over all plot title - Size 20
plt.tight_layout()                                                                                                       # Crop output
#plt.show()                                                                                                              # Show plot 
plt.savefig("Scatterplots.png")                                                                                          # Create file and save to file "Voilinplot"










