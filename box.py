
import numpy as np                                          # Inport NumPy
import pandas as pd                                         # Import Pandas
import matplotlib.pyplot as plt                             # Import Matplotlib 
import seaborn as sns                                       # Import Seaborn

file = 'kaggleIrisSet.csv'                                  # Set the CSV as a variable                          
df = pd.read_csv(file)                                      # create a dataframe from this file - pandas read CSV


sns.set_style('ticks')                                      # set seaborn background
sns.set_palette("bright")                                   # set seaborn color palette



plt.figure(figsize=(10,10))
plt.subplot(2,2,1) 
sns.boxplot(x=("Species"), y=("SepalLengthCm"), data=df, palette=("husl"))
plt.subplot(2,2,2) 
sns.boxplot(x=("Species"), y=("SepalWidthCm"), data=df, palette=("husl"))
plt.subplot(2,2,3) 
sns.boxplot(x=("Species"), y=("PetalLengthCm"), data=df, palette=("husl"))
plt.subplot(2,2,4) 
sns.boxplot(x=("Species"), y=("PetalWidthCm"), data=df, palette=("husl"))
plt.suptitle("Fisher's Iris Dataset", size=20)                                                                           # Set over all plot title - Size 20
plt.tight_layout()                                                                                                       # Crop output
#plt.show()                                                                                                              # Show plot 
plt.savefig("boxs.png")  

