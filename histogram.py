
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
sns.histplot( df, x="SepalLengthCm",  ax=axes[0, 0],kde=True, hue="Species", bins=12)
sns.histplot( df, x="SepalWidthCm", ax=axes[0, 1], kde=True, hue="Species", bins=12)
sns.histplot( df, x="PetalLengthCm", ax=axes[1, 0], kde=True,hue="Species",  bins=12)
sns.histplot( df, x="PetalWidthCm", ax=axes[1, 1], kde=True, hue="Species", bins=12)
#sns.despine(fig=None, ax=None, top=False, right=False, left=False, bottom=False, offset=None, trim=False)
plt.suptitle("Fisher's Iris Dataset", size=20) 
plt.savefig("Histplotextra.png")
plt.show()
