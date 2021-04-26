# Author Veronica Curry
# Student ID: G00074924
# Completed: April 2021

# This file provides a summary of the information in other files. This is not an exhaustive list, please note the additional files.

# Provide a summary of each variable in a single txt file
# Save a historgram of each variable in a PNG file
# Sets outputs of a scatterplot of each pair of variables


import numpy as np                               # Import Modules  - NumPy
import pandas as pd                              # Import Modules  - Pandas
import matplotlib.pyplot as plt                  # Import Modules  - Matplotlib
import seaborn as sns                            # Import Modules  - Seaborn


filename = 'kaggleIrisSet.csv'                      # Import File
df = pd.read_csv(filename)                          # Set variable for file - Pandas - read the CSV file


setosa = df.loc[df["Species"] =="Iris-setosa"]              # Set variable for specific Iris - Setosa
versicolor = df.loc[df["Species"] =="Iris-versicolor"]      # Set variable for specific Iris - Versicolor
virginica = df.loc[df["Species"] =="Iris-virginica"]        # Set variable for specific Iris - Virginica
