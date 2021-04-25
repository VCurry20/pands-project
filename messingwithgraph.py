# Author Veronica Curry
# Student ID: G00074924
# Completed: April 2021

# Outputting the data from the Fisher Iris Dataset to Graphs


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



pairplot1 = sns.pairplot(df,hue="Species")     
# plt.show()

voilinplot = sns.violinplot(x="Species", y=(df['SepalLengthCm'] + df['PetalLengthCm']), data=df)  
#plt.show()

scatterplot = sns.scatterplot(x = "SepalLengthCm", y = "SepalWidthCm", data = df, hue="Species") 
#plt.show() 

scatterplot = sns.scatterplot(x = "PetalLengthCm", y = "PetalWidthCm", data = df, hue="Species", legend=True) 
#plt.show() 

pairplot2 =sns.pairplot( df,hue='Species',palette="muted",height=3,vars=['SepalWidthCm','SepalLengthCm','PetalLengthCm','PetalWidthCm'],kind='scatter') 
#plt.show()

jointplot = sns.jointplot(x='SepalWidthCm', y='SepalLengthCm', data=df, height=4)
#plt.show()

catplot = sns.catplot(x="SepalWidthCm", y="SepalLengthCm",col="Species", data=df, kind="swarm")  
#plt.show()

lmplot1 = sns.lmplot(x="SepalWidthCm", y="SepalLengthCm",col="Species", data=df) 
#plt.show()

distplot1 = sns.displot(df["SepalWidthCm"], bins=16, color="red")
#plt.show()

hisplot1 = sns.histplot(df["SepalWidthCm"], bins=16, color="red")
#plt.show()
