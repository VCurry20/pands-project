import numpy as np                                          # Inport NumPy
import pandas as pd                                         # Import Pandas
import matplotlib.pyplot as plt                             # Import Matplotlib 
import seaborn as sns                                       # Import Seaborn

file = 'kaggleIrisSet.csv'                                  # Set the CSV as a variable                          
df = pd.read_csv(file)                                      # create a dataframe from this file - pandas read CSV


sns.set_style('ticks')                                      # set seaborn background
sns.set_palette("bright")                                   # set seaborn color palette


# Distrubtion chart
sns.displot(df["SepalWidthCm"], bins=16, palette=("husl"))             # Seaborn - distrubution plot ( choose one variable, 16 bins along the axis, color palette)              
#plt.show()                                                            # Show plot 
plt.savefig("Distplot.png")                                            # Create file and save to file "Distplot"
