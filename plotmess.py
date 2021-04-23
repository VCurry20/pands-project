# Author Veronica Curry
# Student ID: G00074924
# Completed: April 2021

# Outputting the data from the Fisher Iris Dataset to Graphs


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


filename = 'kaggleIrisSet.csv'                      # Import File
df = pd.read_csv(filename)                          # Set variable for file - Pandas - read the CSV file

g = sns.pairplot(df,hue="Species")
plt.show()