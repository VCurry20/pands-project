# Author Veronica Curry
# Student ID: G00074924
# Completed: April 2021

# Outputting the data from the Fisher Iris Dataset to Graphs - Examples


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl

file = 'kaggleIrisSet.csv'
df = pd.read_csv(file) 

setosa = df.loc[df["Species"] =="Iris-setosa"]              # Set variable for specific Iris - Setosa
versicolor = df.loc[df["Species"] =="Iris-versicolor"]      # Set variable for specific Iris - Versicolor
virginica = df.loc[df["Species"] =="Iris-virginica"]        # Set variable for specific Iris - Virginica


sns.set_style('ticks')
sns.set_palette("pastel")  ## changed this to change color or add in palette variable palette=palette
#epalette = sns.color_palette("rocket")
#sns.color_palette("hls", 10)


# voilinplots
plt.figure(figsize=(10,10))
plt.subplot(2,2,1)
plt.title("Sepal Length")
sns.violinplot(x="Species", y='SepalLengthCm', data=df, palette=("husl"))
plt.subplot(2,2,2)
plt.title("Sepal Width")
sns.violinplot(x="Species", y='SepalWidthCm', data=df, palette=("husl"))
plt.subplot(2,2,3)
plt.title("Petal Length")
sns.violinplot(x="Species", y='PetalLengthCm', data=df, palette=("husl"))
plt.subplot(2,2,4)
plt.title("Petal Width")
sns.violinplot(x="Species", y='PetalWidthCm', data=df, palette=("husl"))
plt.suptitle("Fisher's Iris Dataset", size=20)
plt.tight_layout()
#plt.show()
plt.savefig("Voilinplots.png")  



# Scatterplots
plt.figure(figsize=(10,10))
plt.subplot(2,2,1)
plt.title("Sepal Width Vs Sepal Length")
scatterplot = sns.scatterplot(x = "SepalLengthCm", y = "SepalWidthCm", data = df, hue="Species", legend=True, palette=("husl")) 
plt.subplot(2,2,2)
plt.title("Petal Width Vs Petal Length")
scatterplot = sns.scatterplot(x = "PetalLengthCm", y = "PetalWidthCm", data = df, hue="Species", legend=True, palette=("husl")) 
plt.subplot(2,2,3)
plt.title("Petal Length Vs Sepal Length")
scatterplot = sns.scatterplot(x = "SepalLengthCm", y = "PetalLengthCm", data = df, hue="Species", legend=True, palette=("husl")) 
plt.subplot(2,2,4)
plt.title("Petal Width Vs Sepal Width")
scatterplot = sns.scatterplot(x = "SepalWidthCm", y = "PetalWidthCm", data = df, hue="Species", legend=True, palette=("husl"))
plt.suptitle("Fisher's Iris Dataset", size=20)
plt.tight_layout()
#plt.show()
plt.savefig("Scatterplots.png")  


# Joint Plot
jointplot = sns.jointplot(x='SepalWidthCm', y='SepalLengthCm', data=df, height=4, palette=("husl"))
#plt.show()
plt.savefig("Jointplot.png")  


catplot = sns.catplot(x="SepalWidthCm", y="SepalLengthCm",col="Species", data=df, kind="swarm", palette=("husl"))  
#plt.show()
plt.savefig("catplot.png") 


lmplot1 = sns.lmplot(x="SepalWidthCm", y="SepalLengthCm",col="Species", data=df, palette=("husl")) 
#plt.show()
plt.savefig("Implot.png") 


distplot1 = sns.displot(df["SepalWidthCm"], bins=16, palette=("husl"))
#plt.show()
plt.savefig("Distplot.png") 


hisplot1 = sns.histplot(df["SepalWidthCm"], bins=16, palette=("husl"))
#plt.show()
plt.savefig("Hisplot.png") 



pairplot =sns.pairplot( df,hue='Species',height=3,vars=['SepalWidthCm','SepalLengthCm','PetalLengthCm','PetalWidthCm'],kind='scatter', palette=("husl")) 
#plt.show()
plt.savefig("pairplot.png") 


#pairplot1 = sns.pairplot(df,hue="Species", palette=("husl"), height=1.5, plot_kws={'alpha':0.6})     
#plt.show()