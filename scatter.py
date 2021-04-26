
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl

file = 'kaggleIrisSet.csv'
df = pd.read_csv(file) 

sns.set_style('ticks')
sns.set_palette("pastel")  ## changed this to change color or add in palette variable palette=palette
#palette = sns.color_palette("rocket")
sns.color_palette("hls", 10)


#scattersepal = sns.FacetGrid(df, col="Species", col_wrap=4, height=2, ylim=(0, 6))
#scattersepal.map(sns.scatterplot, "SepalLengthCm", "SepalWidthCm", ci=None)

plt.figure(figsize=(10,10))
plt.subplot(2,2,1)
scatterpetal = sns.FacetGrid(df, col="Species", col_wrap=4, height=2, ylim=(0, 4), legend_out=False, col_order=None)
scatterpetal.map(sns.scatterplot, "PetalLengthCm", "PetalWidthCm", ci=None)
plt.subplot(2,2,2)
scatterpetal = sns.FacetGrid(df, col="Species", col_wrap=4, height=2, ylim=(0, 4), legend_out=False, col_order=None)
scatterpetal.map(sns.scatterplot, "SepalLengthCm", "SepalWidthCm", ci=None, color='r')
plt.show()
# plt.savefig("Fingerscrossd.png")
#plt.suptitle("Fisher's Iris Dataset")
#plt.tight_layout()
#plt.savefig("Voilinplots.png")  
