# Author Veronica Curry
# Student ID: G00074924
# Completed: April 2021

# Import and pring the Fisher Iris Data Set - inbuilt Python Data Set

from sklearn.datasets import load_iris         # Importing the Dataset into Python

iris = load_iris()                             # Setting data set as a variable
print(iris)                                    # Print Data set in Python terminal

with open("irisImport.txt", "wt") as f:                                                  # Open File "irisImport.txt" as a txt file, in write txt mode
    print("This is the output from the imported inbuilt dataset: \n", iris, file=f)      # Prints dataset to this file

# https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html 

