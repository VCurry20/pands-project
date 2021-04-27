
import numpy as np                                          # Inport NumPy
import pandas as pd                                         # Import Pandas
import matplotlib.pyplot as plt                             # Import Matplotlib 
import seaborn as sns                                       # Import Seaborn

file = 'kaggleIrisSet.csv'                                  # Set the CSV as a variable                          
df = pd.read_csv(file)                                      # create a dataframe from this file - pandas read CSV


sns.set_style('ticks')                                      # set seaborn background
sns.set_palette("bright")                                   # set seaborn color palette


# Implot
sns.lmplot(x="SepalWidthCm", y="SepalLengthCm",col="Species", data=df, palette=("husl"))   # Seaborn - jointplot ( set X axis / set Y axis ), Data from Iris File, Palette (color code)
#plt.subplots()
ax.legend()
plt.show()                                                                                # Show plot 




