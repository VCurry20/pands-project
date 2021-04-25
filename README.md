# pands-project

Author Veronica Curry

Student ID: G00074924

Completed: April 2021


## Fisher's Iris Data Set

<br/>

![alt text](https://github.com/VCurry20/pands-project/blob/main/johnMuirlaw.1.jpg)
[0]
<br/>

## Overview
The purpose of this project is to research Fisher's Iris Dataset and to show how Python can be used to investigate datasets and output the results to graphs. I will be using Fisher's Dataset as an example of the functionality of Python and to outline ways in which the analysis carried out on this Dataset is transferable.

This is a dataset that examines three species of Iris Plant – Iris Setosa, Iris Virginica, and Iris Versicolor. It outlines their petal width and length and their sepal width and length. There are 50 samples of each of the three species, resulting in a 150 line data set.

This Dataset has been used for pattern analysis, statistics, and more recently for machine learning and for the teaching of data analysis. This use has outweighed its importance as information about the biology of the plants, with botanists now even questioning if Iris plants have a Sepal. [16]

The Dataset is large enough to demonstrate the principles of using a program like python while not so large as to overwhelm a student, it has no missing data, there are 4 attributes covering three different plants and all the data is in the same format and unit type. The data set is now also present as a built-in data set which can be imported directly into Python. [17]


<br/>

In this project I will include the following:

> An overview of the Dataset 

> A guide to python and modules within Python we used to review the Dataset

> Display the results of Python analysis of the Dataset

> Display graphs of the Dataset 


### Fisher's Iris Dataset 
There are approximately 300 types of Iris globally. The name Iris comes from the Greek Goddess Iris, who was the Goddess of the Rainbow or a messenger of the Gods.  [4] [5] The names derives from the fact that Irises can be found in a wide variety of colours. These are a colourful showy plant which grow in the spring or summer and can be found in a diverse range of climates and locations. [3] [7]

<br/>
The Iris Fisher data set examines three different types of Iris:

Iris Virginica


![alt text](https://github.com/VCurry20/pands-project/blob/main/Irisvirginica.wildflowerorg.jpg)
[8]


This an Iris native to North America, is has traditionally been used in Cherokee tribes as a medicinal plant. It can be used as a salve for the skin and as a treatment for liver ailments. [9]

<br/>
Iris Versicolor


![alt text](https://github.com/VCurry20/pands-project/blob/main/irisversicolor.wildflowerorg.jpg)
[10]

This is also known as the Blug Flag Iris. It is also native to North America, and Eastern Canada. It is poisonous, causing illness in humans and animals who have consumed it. It is also said to bring finanical gain to those who carry it. [11]

<br/>
Iris Setosa


![alt text](https://github.com/VCurry20/pands-project/blob/main/Irissetosa.wildflowerorg.jpg)
[12]

This is an Iris which grows in Alaska, Maine, Canada, and parts of Asia. Although it is poisonous it has been used, when cooked, by various Peoples throough out the World for both food and for medicinal reasons. It is currently on a red list of endangered Japanese plants. [13] 


<br/>
Fisher's Iris Dataset

![alt text](https://github.com/VCurry20/pands-project/blob/main/towardsdatascience.jpg)
[14]

This data was compiled by Sir Ronald Aylmer Fisher and Dr Edgar Anderson. It was published in 1936 in a report titled "The use of Multiple Measurements in Taxonimic Problems". While Dr Anderson was a botanist and collected the majority of the measurements, Sir Fisher was a statistician and geneticist. The data listed the sepal and petal length and width as shown in the above diagram.
In this report Fisher "developed and evaluated a linear function to differentiate Iris species based on the morphology of their flowers". The data collected was used to form graphs which outlined the differences between the plants - when plotted the graphs differenciated between the species with little overlap except between the Iris Versicolor and the Iris Virginica. This overlap occurs when the data is used in cluster analysis.  [1] [14] [15]



![alt text](https://github.com/VCurry20/pands-project/blob/main/towardsdatascience2.jpg)
Figure from Fisher's Article [14]

## Python

``` python
print ("Hello World")
```

Python is a fourth-generation programming lanugage created by Guido Van Rossum and released in 1991. This is a high-level multipurpose language that offers an access-point for novice programmers to enter the field. [1] [2] 

Python is an example of object orientated programming, it is easier to read than other languages and can achieve many of its objectives in less lines of code. It is cross – platform and there is a large online community using the language which offers a large and easily accessable database of knowledge for new users.[3] [4]

Python offers a wide range of plug in modules; modules are files "containing a set of functions you want to include in your application". [5] These modules allow us to "plug in" additional capabilities which we can then use to review our data. In this project we will review 4 of these modules.


Uses of Python:

> Automation of Tasks

> Visualisation of Data

> Data Analysis

> Machine Learning

> AI


### Modules Review

The Modules we will be using are:

``` python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

```

NumPy or Numerical Python is a general-purpose numerical module for python, it is the main module for scientific computing in Python. This is a numerical library, which stores data in matrices which are called arrays. The underlying code for NumPy is written in C code or the C language which makes this a very fast module. NumPy can be used for a wide range of operations on arrays including maths, logical operations, sorting, algebra, and statistical operations. NumPy is a core module of Python which Pandas is built upon. [6] [7] [8] [9]

Pandas is an open source module which operates in conjunction with NumPy. It is a Data Analysis module which allows the user to manipulate, clean, slice, index, and merge data. Data is stored in data frames (df). Pandas can read from and output to a wide range of data structures and formats including CSV and Excel.  [10] [11] [12] 



NumPy Vs Pandas

While both modules offer the user a wide range of operations there are differences which should be considered. Pandas operates on tabular data that is structured in rows where NumPy works solely on numerical data stored in arrays. Pandas which is built on NumPy and allows for easier manipulation of data at a higher level and offers easy to use data structures and tools for data analysis. Pandas has a wide range of input / output options. [13] [14]


Matplotlib is a module that offers data visualisation for Python and NumPy, it is open source and can be used to create charts including Line and bar charts. [15] [16]


Seaborn is the next step in Data Visualisation, it offers a variety of visualisation pattern, uses less syntax and is a high-level interface. This module builds on matplotlib and works from Pandas. [17] [18] 


In choosing between these modules it is best to consider the desired output, Matplotlib excels in more basic plotting – the traditional bars, pies, and scatterplots. Seaborn offers an accessible option for data visualisation. [19]

## Analysis


### Dataset
We can use Python to review this dataset using the built in functions and modules. I will outline some of these functions below and have included the output text files with this project.

The Data set was downloaded from [Kaggle](https://www.kaggle.com/uciml/iris) and can be found widely online. I have stored this information in a CSV file titled [kaggleIrisSet.csv](https://github.com/VCurry20/pands-project/blob/main/kaggleIrisSet.csv). The Dataset can be found in various formats and should include a total 150 seets / rows of iris measurements. [1]

It is also included in a list of datasets that can be imported directly into Python. To complete this process the following code is required [2]:

``` python
from sklearn.datasets import load_iris        

iris = load_iris()                            
print(iris)                                    

with open("irisImport.txt", "wt") as f:                                                  
    print("This is the output from the imported inbuilt dataset: \n", iris, file=f)      
```

> Python File - [Iris.py](https://github.com/VCurry20/pands-project/blob/main/Iris.py)

> Output File - [irisImport.txt](https://github.com/VCurry20/pands-project/blob/main/irisImport.txt)

### Review of Dataset

Using python we can break down the Fisher Iris Dataset and then analyise the various components of it. I have included the Python Files as follows:

> Python File - [Analysis.py](https://github.com/VCurry20/pands-project/blob/main/Analysis.py)

> Python File - [Slicedata.py](https://github.com/VCurry20/pands-project/blob/main/Slicedata.py)


In these files we open the NumPy and Pandas modules and use them to review the data in various ways. 
Firstly we open the file containing the Fishers Dataset, from this we set this file as a variable. This allows for us to change the file without having to alter the code, the code therefore can be used on various data files. This process allows for python programs to be written and used muliple times with very few changes needed.

Once this is complete we can start to analyise the data

It should also be noted that although we are using a CSV file format for the Dataset we can change this format or even directly output from the imported data set to a different file type. 

With this code I have created an excel file from the CSV file we have downloaded as an example of this process:

```python 
df.to_excel("Dataprintout.xlsx") 
```

Using Python’s built in functions I have reviewed the Dataset in the following ways:


Describe(): This function allows the user to gain an overview of the Dataset providing the user with stastical information on the entire dataframe:

``` python
The full breakdown is: 
                Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm
count  150.000000     150.000000    150.000000     150.000000    150.000000
mean    75.500000       5.843333      3.054000       3.758667      1.198667
std     43.445368       0.828066      0.433594       1.764420      0.763161
min      1.000000       4.300000      2.000000       1.000000      0.100000
25%     38.250000       5.100000      2.800000       1.600000      0.300000
50%     75.500000       5.800000      3.000000       4.350000      1.300000
75%    112.750000       6.400000      3.300000       5.100000      1.800000
max    150.000000       7.900000      4.400000       6.900000      2.500000

```

This process can also be used to provide stastical information about the individual Iris species:


<table>
<tr>
<th>Sepal Length</th>
<th>Sepal Width</th>
</tr>
<tr>
<td>
<pre>


The Sepal Length Column only is: 
count    150.000000
mean       5.843333
std        0.828066
min        4.300000
25%        5.100000
50%        5.800000
75%        6.400000
max        7.900000
Name: SepalLengthCm, dtype: float64

</pre>
</td>
<td>

``` 
The Sepal Width Column only is: 
count    150.000000
mean       3.054000
std        0.433594
min        2.000000
25%        2.800000
50%        3.000000
75%        3.300000
max        4.400000
Name: SepalWidthCm, dtype: float64

```

</td>
</tr>
</table>



<table>
<tr>
<th>Petal Length</th>
<th>Petal Width</th>
</tr>
<tr>
<td>
<pre>

The Petal Length Column only is: 
count    150.000000
mean       3.758667
std        1.764420
min        1.000000
25%        1.600000
50%        4.350000
75%        5.100000
max        6.900000
Name: PetalLengthCm, dtype: float64

</pre>
</td>
<td>

``` 
The Petal Width Column only is: 
count    150.000000
mean       1.198667
std        0.763161
min        0.100000
25%        0.300000
50%        1.300000
75%        1.800000
max        2.500000
Name: PetalWidthCm, dtype: float64

```

</td>
</tr>
</table>  


This same process can also be used to take either the top or bottom lines of code using df.head() / df.tail(). 


The top lines of the data are as follows: 
``` python
    Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm      Species
0   1            5.1           3.5            1.4           0.2  Iris-setosa
1   2            4.9           3.0            1.4           0.2  Iris-setosa
2   3            4.7           3.2            1.3           0.2  Iris-setosa
3   4            4.6           3.1            1.5           0.2  Iris-setosa
4   5            5.0           3.6            1.4           0.2  Iris-setosa
```

The last lines of the data are as follows: 
``` python
       Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm         Species
145  146            6.7           3.0            5.2           2.3  Iris-virginica
146  147            6.3           2.5            5.0           1.9  Iris-virginica
147  148            6.5           3.0            5.2           2.0  Iris-virginica
148  149            6.2           3.4            5.4           2.3  Iris-virginica
149  150            5.9           3.0            5.1           1.8  Iris-virginica

```

A more targetted approach is also possible - here we use code to print the Dataset grouped by Species and the output lets us know the amount of lines for each:

``` python
irisGroup = df.groupby("Species").size() 
``` 

The output is:
``` python
 Species
Iris-setosa        50
Iris-versicolor    50
Iris-virginica     50
dtype: int64
```

The final overview I have provided is the .info function. This provides "index dtype and columns, non-null values and memory usage" and can offer a snapshot of information prior to working with data [3]:

``` Python
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 150 entries, 0 to 149
Data columns (total 6 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   Id             150 non-null    int64  
 1   SepalLengthCm  150 non-null    float64
 2   SepalWidthCm   150 non-null    float64
 3   PetalLengthCm  150 non-null    float64
 4   PetalWidthCm   150 non-null    float64
 5   Species        150 non-null    object 
dtypes: float64(4), int64(1), object(1)
memory usage: 7.2+ KB
```

Some of these processes can be incorporated into code for programming use or can be used to review data and give an overall picture of a dataset quickly and efficiently - this in turn can be used to evaulate the information provided. 

Depending on file type and the breakout needed of this information I am also including the following review. This shows the output of the slicing the data and from this process we can easily split files - creating new datasets.

> Output File - [Sliceoutput.txt](https://github.com/VCurry20/pands-project/blob/main/Sliceoutput.txt)




<table border="0">
 <tr>
    <td><b style="font-size:30px">Title</b></td>
    <td><b style="font-size:30px">Title 2</b></td>
    <td><b style="font-size:30px">Title 3</b></td>
 </tr>
 <tr>
    <td>Lorem ipsum ...</td>
    <td>Lorem ipsum ...</td>
    <td>Lorem ipsum ...</td>
 </tr>
</table>


