
# Provide a summary of each variable in a single txt file
# Save a historgram of each variable in a PNG file
# Sets outputs of a scatterplot of each pair of variables


import numpy as np                               # Import Modules  - NumPy
import pandas as pd                              # Import Modules  - Pandas
import matplotlib.pyplot as plt                  # Import Modules  - Matplotlib
import seaborn as sns                            # Import Modules  - Seaborn


filename = 'kaggleIrisSet.csv'                      # Import File
df = pd.read_csv(filename)                          # Set variable for file - Pandas - read the CSV file



sns.FacetGrid(df, hue="type", height=3).map(sns.distplot,"PetalLengthCm").add_legend()
sns.FacetGrid(df, hue="type", height=3).map(sns.distplot,"PetalWidthCm").add_legend()
sns.FacetGrid(df, hue="type", height=3).map(sns.distplot,"SepalLengthCm").add_legend()
sns.FacetGrid(df, hue="type", height=3).map(sns.distplot,"SepalWidthCm").add_legend()
plt.show()





#isplot1 = sns.histplot(df["SepalWidthCm"], bins=16, palette=("husl"))
#plt.show()
#plt.savefig("Hisplot2.png") 