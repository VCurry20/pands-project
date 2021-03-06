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


# voilinplots
plt.figure(figsize=(10,10))                                                          # plot figure size
plt.subplot(2,2,1)                                                                   # subplot - 2 * 2 - plot 1
plt.title("Sepal Length")                                                            # set plot title - Sepal Length
sns.violinplot(x="Species", y='SepalLengthCm', data=df, palette=("husl"))            # Seaborn Voilin plot - ( set X axis / set Y axis ), Data from Iris File, Plot Color          
plt.subplot(2,2,2)                                                                   # subplot - 2 * 2 - plot 2
plt.title("Sepal Width")                                                             # set plot title - Sepal Width
sns.violinplot(x="Species", y='SepalWidthCm', data=df, palette=("husl"))             # Seaborn Voilin plot - ( set X axis / set Y axis ), Data from Iris File, Plot Color 
plt.subplot(2,2,3)                                                                   # subplot - 2 * 2 - plot 3
plt.title("Petal Length")                                                            # set plot title - Petal Length
sns.violinplot(x="Species", y='PetalLengthCm', data=df, palette=("husl"))            # Seaborn Voilin plot - ( set X axis / set Y axis ), Data from Iris File, Plot Color
plt.subplot(2,2,4)                                                                   # subplot - 2 * 2 - plot 4
plt.title("Petal Width")                                                             # set plot title - Petal Width
sns.violinplot(x="Species", y='PetalWidthCm', data=df, palette=("husl"))             # Seaborn Voilin plot - ( set X axis / set Y axis ), Data from Iris File, Plot Color
plt.suptitle("Fisher's Iris Dataset", size=20)                                       # Set over all plot title - Size 20
plt.tight_layout()                                                                   # Crop output
#plt.show()                                                                          # Show plot 
plt.savefig("Voilinplots.png")                                                       # Create file and save to file "Voilinplot"




# Joint Plots
sns.jointplot(x='PetalWidthCm', y='SepalWidthCm', data=df, height=6, palette=("husl"), kind="reg")    # Seaborn - jointplot ( set X axis / set Y axis ), Data from Iris File, height = 6, Palette (color code), kind - regular
#plt.show()                                                                                           # Show plot 
plt.savefig("Jointplot.png")                                                                          # Create file and save to file "Jointplot"


sns.jointplot(x='PetalLengthCm', y='SepalLengthCm', data=df, height=6, palette=("husl"), kind="reg")  # Seaborn - jointplot ( set X axis / set Y axis ), Data from Iris File, height = 6, Palette (color code), kind - regular
#plt.show()                                                                                           # Show plot 
plt.savefig("Jointplot2.png")                                                                         # Create file and save to file "Jointplot"




# Cat plot                                                              
sns.catplot(x="SepalWidthCm", y="SepalLengthCm",col="Species", data=df, kind="swarm", palette=("husl"))  # Seaborn - jointplot ( set X axis / set Y axis ), Data from Iris File, Palette (color code), kind - swarp data points
plt.tight_layout()                                                                                       # Crop output
#  plt.show()                                                                                            # Show plot 
plt.savefig("catplot.png")                                                                               # Create file and save to file "Catplot"
plt.show() 


# Implot
sns.lmplot(x="SepalWidthCm", y="SepalLengthCm",col="Species", data=df, palette=("husl"))   # Seaborn - jointplot ( set X axis / set Y axis ), Data from Iris File, Palette (color code)
plt.legend()
#plt.show()                                                                                # Show plot 
plt.savefig("Implot.png")                                                                  # Create file and save to file "implot"
 

sns.lmplot(x="PetalWidthCm", y="PetalLengthCm",col="Species", data=df, palette=("husl"))   # Seaborn - jointplot ( set X axis / set Y axis ), Data from Iris File, Palette (color code)
plt.legend()
#plt.show()                                                                                # Show plot 
plt.savefig("Implot2.png")                                                                 # Create file and save to file "implot2"




# Distrubtion chart
sns.displot(data=df, x="SepalLengthCm", hue="Species", bins=16, palette=("husl"))    # Seaborn - distrubution plot ( choose one variable, 16 bins along the axis, color palette)              
#plt.show()                                                                          # Show plot 
plt.savefig("Distplot.png")                                                          # Create file and save to file "Distplot"

#sns.displot(data=df, x="SepalWidthCm", hue="Species", bins=10, rug=True, palette=("husl"))
#sns.displot(data=df, x="PetalLengthCm", hue="Species", bins=16, kde=True,  palette=("husl"))
#sns.displot(data=df, x="PetalWidthCm", hue="Species", bins=8, kde_kws={"shade": True}, palette=("husl")) 

# Pairplots
sns.pairplot( df,hue='Species',height=3,vars=['SepalWidthCm','SepalLengthCm','PetalLengthCm','PetalWidthCm'],kind='scatter', palette=("husl")) # Seaborn - distrubution plot ( choose one variable, 16 bins along the axis, color palette) 
plt.legend()
#plt.show()                                                                                                                                    # Show plot
plt.savefig("pairplot.png")                                                                                                                    # Create file and save to file "Pairplot"



# Boxplot

plt.figure(figsize=(10,10))                                                    # Plt Figure - Size
plt.subplot(2,2,1)                                                             # Plot Subplots - 2 * 2 - Number 1
sns.boxplot(x=("Species"), y=("SepalLengthCm"), data=df, palette=("husl"))     # Seaborn - Boxplot - x = Sepcies /  Y = Sepal Length, Data = Fisher Iris, Palette Color
plt.subplot(2,2,2)                                                             # Plot Subplots - 2 * 2 - Number 2
sns.boxplot(x=("Species"), y=("SepalWidthCm"), data=df, palette=("husl"))      # Seaborn - Boxplot - x = Sepcies /  Y = Sepal Width, Data = Fisher Iris, Palette Color
plt.subplot(2,2,3)                                                             # Plot Subplots - 2 * 2 - Number 3
sns.boxplot(x=("Species"), y=("PetalLengthCm"), data=df, palette=("husl"))     # Seaborn - Boxplot - x = Sepcies /  Y = Petal Length, Data = Fisher Iris, Palette Color
plt.subplot(2,2,4)                                                             # Plot Subplots - 2 * 2 - Number 4
sns.boxplot(x=("Species"), y=("PetalWidthCm"), data=df, palette=("husl"))      # Seaborn - Boxplot - x = Sepcies /  Y = Petal Width, Data = Fisher Iris, Palette Color
plt.suptitle("Fisher's Iris Dataset", size=20)                                 # Plot Title - Fisher's Iris Dataset
plt.tight_layout()                                                             # Crop plots                                        
#plt.show()                                                                    # Plot Show 
plt.savefig("boxs.png")                                                        # Plot Save "boxes.png"