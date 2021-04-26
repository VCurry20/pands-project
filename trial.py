# Author Veronica Curry
# Student ID: G00074924
# Completed: April 2021

# Outputting the data from the Fisher Iris Dataset to Graphs - Examples


import numpy as np                                          # Inport NumPy
import pandas as pd                                         # Import Pandas
import matplotlib.pyplot as plt                             # Import Matplotlib 
import seaborn as sns                                       # Import Seaborn

file = 'kaggleIrisSet.csv'                                  # Set the CSV as a variable                          
df = pd.read_csv(file)                                      # create a dataframe from this file - pandas read CSV

sns.set_style('ticks')                                      # set seaborn background
sns.set_palette("bright")                                   # set seaborn color palette


#sns.displot(df["SepalWidthCm"], bins=16, palette=("husl"))        
#plt.show()
#plt.savefig("Distplot.png") 


# Scatterplots of Variables
plt.figure()                                                                                              # plot figure size
plt.subplot(2,2,1)                                                                                                       # subplot - 2 * 2 - plot 1
sns.displot(df["SepalWidthCm"], bins=8, palette=("husl"))        # Seaborn Scatterplot - ( set X axis / set Y axis ), Data from Iris File, Hue - Species, include a legend, Palette - set color
plt.subplot(2,2,2)                                                                                                       # subplot - 2 * 2 - plot 2
sns.displot(df["SepalWidthCm"], bins=8, palette=("husl"))      # Seaborn Scatterplot - ( set X axis / set Y axis ), Data from Iris File, Hue - Species, include a legend, Palette - set colo
plt.subplot(2,2,3)                                                                                                       # subplot - 2 * 2 - plot 3
sns.displot(df["PetalLengthCm"], bins=8, palette=("husl"))     # Seaborn Scatterplot - ( set X axis / set Y axis ), Data from Iris File, Hue - Species, include a legend, Palette - set colo
plt.subplot(2,2,4)                                                                                                       # subplot - 2 * 2 - plot 4
sns.displot(df["PetalWidthCm"], bins=8, palette=("husl")) # Seaborn Scatterplot - ( set X axis / set Y axis ), Data from Iris File, Hue - Species, include a legend, Palette - set colo
plt.suptitle("Fisher's Iris Dataset", size=20)                                                                           # Set over all plot title - Size 20
plt.tight_layout()                                                                                                       # Crop output
#plt.show()                                                                                                              # Show plot 
plt.savefig("trial.png")                                                                                          # Create file and save to file "Voilinplot"



