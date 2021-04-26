
# Provide a summary of each variable in a single txt file
# Save a historgram of each variable in a PNG file
# Sets outputs of a scatterplot of each pair of variables


import numpy as np                               # Import Modules  - NumPy
import pandas as pd                              # Import Modules  - Pandas
import matplotlib.pyplot as plt                  # Import Modules  - Matplotlib
import seaborn as sns                            # Import Modules  - Seaborn


filename = 'kaggleIrisSet.csv'                      # Import File
df = pd.read_csv(filename)                          # Set variable for file - Pandas - read the CSV file


sns.set_style('ticks')                                      # set seaborn background
sns.set_palette("bright")                                   # set seaborn color palette
sns.color_palette("husl", 9)


f, axes = plt.subplots(2, 2, figsize=(7, 7), sharex=True)
plt.title("Fisher's Iris Dataset", size=20) 
sns.histplot( df["SepalLengthCm"] , ax=axes[0, 0], legend=True, kde=True,bins=10 )
sns.histplot( df["SepalWidthCm"] ,  ax=axes[0, 1], legend=True, kde=True, bins=8)
sns.histplot( df["PetalLengthCm"] ,  ax=axes[1, 0], legend=True, kde=True)
sns.histplot( df["PetalWidthCm"] ,  ax=axes[1, 1], legend=True, kde=True)
plt.show()




#isplot1 = sns.histplot(df["SepalWidthCm"], bins=16, palette=("husl"))
#plt.show()
#plt.savefig("Hisplot2.png") 