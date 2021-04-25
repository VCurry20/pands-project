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
    <td><b style="font-size:10px">Iris Setosa</b></td>
    <td><b style="font-size:10px">Iris Versicolor</b></td>
    <td><b style="font-size:10px">Iris Virginica</b></td>
 </tr>
 <tr>
    <td>     Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm      Species
0    1            5.1           3.5            1.4           0.2  Iris-setosa
1    2            4.9           3.0            1.4           0.2  Iris-setosa
2    3            4.7           3.2            1.3           0.2  Iris-setosa
3    4            4.6           3.1            1.5           0.2  Iris-setosa
4    5            5.0           3.6            1.4           0.2  Iris-setosa
5    6            5.4           3.9            1.7           0.4  Iris-setosa
6    7            4.6           3.4            1.4           0.3  Iris-setosa
7    8            5.0           3.4            1.5           0.2  Iris-setosa
8    9            4.4           2.9            1.4           0.2  Iris-setosa
9   10            4.9           3.1            1.5           0.1  Iris-setosa
10  11            5.4           3.7            1.5           0.2  Iris-setosa
11  12            4.8           3.4            1.6           0.2  Iris-setosa
12  13            4.8           3.0            1.4           0.1  Iris-setosa
13  14            4.3           3.0            1.1           0.1  Iris-setosa
14  15            5.8           4.0            1.2           0.2  Iris-setosa
15  16            5.7           4.4            1.5           0.4  Iris-setosa
16  17            5.4           3.9            1.3           0.4  Iris-setosa
17  18            5.1           3.5            1.4           0.3  Iris-setosa
18  19            5.7           3.8            1.7           0.3  Iris-setosa
19  20            5.1           3.8            1.5           0.3  Iris-setosa
20  21            5.4           3.4            1.7           0.2  Iris-setosa
21  22            5.1           3.7            1.5           0.4  Iris-setosa
22  23            4.6           3.6            1.0           0.2  Iris-setosa
23  24            5.1           3.3            1.7           0.5  Iris-setosa
24  25            4.8           3.4            1.9           0.2  Iris-setosa
25  26            5.0           3.0            1.6           0.2  Iris-setosa
26  27            5.0           3.4            1.6           0.4  Iris-setosa
27  28            5.2           3.5            1.5           0.2  Iris-setosa
28  29            5.2           3.4            1.4           0.2  Iris-setosa
29  30            4.7           3.2            1.6           0.2  Iris-setosa
30  31            4.8           3.1            1.6           0.2  Iris-setosa
31  32            5.4           3.4            1.5           0.4  Iris-setosa
32  33            5.2           4.1            1.5           0.1  Iris-setosa
33  34            5.5           4.2            1.4           0.2  Iris-setosa
34  35            4.9           3.1            1.5           0.1  Iris-setosa
35  36            5.0           3.2            1.2           0.2  Iris-setosa
36  37            5.5           3.5            1.3           0.2  Iris-setosa
37  38            4.9           3.1            1.5           0.1  Iris-setosa
38  39            4.4           3.0            1.3           0.2  Iris-setosa
39  40            5.1           3.4            1.5           0.2  Iris-setosa
40  41            5.0           3.5            1.3           0.3  Iris-setosa
41  42            4.5           2.3            1.3           0.3  Iris-setosa
42  43            4.4           3.2            1.3           0.2  Iris-setosa
43  44            5.0           3.5            1.6           0.6  Iris-setosa
44  45            5.1           3.8            1.9           0.4  Iris-setosa
45  46            4.8           3.0            1.4           0.3  Iris-setosa
46  47            5.1           3.8            1.6           0.2  Iris-setosa
47  48            4.6           3.2            1.4           0.2  Iris-setosa
48  49            5.3           3.7            1.5           0.2  Iris-setosa
49  50            5.0           3.3            1.4           0.2  Iris-setosa</td>
    <td>      Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm          Species
50   51            7.0           3.2            4.7           1.4  Iris-versicolor
51   52            6.4           3.2            4.5           1.5  Iris-versicolor
52   53            6.9           3.1            4.9           1.5  Iris-versicolor
53   54            5.5           2.3            4.0           1.3  Iris-versicolor
54   55            6.5           2.8            4.6           1.5  Iris-versicolor
55   56            5.7           2.8            4.5           1.3  Iris-versicolor
56   57            6.3           3.3            4.7           1.6  Iris-versicolor
57   58            4.9           2.4            3.3           1.0  Iris-versicolor
58   59            6.6           2.9            4.6           1.3  Iris-versicolor
59   60            5.2           2.7            3.9           1.4  Iris-versicolor
60   61            5.0           2.0            3.5           1.0  Iris-versicolor
61   62            5.9           3.0            4.2           1.5  Iris-versicolor
62   63            6.0           2.2            4.0           1.0  Iris-versicolor
63   64            6.1           2.9            4.7           1.4  Iris-versicolor
64   65            5.6           2.9            3.6           1.3  Iris-versicolor
65   66            6.7           3.1            4.4           1.4  Iris-versicolor
66   67            5.6           3.0            4.5           1.5  Iris-versicolor
67   68            5.8           2.7            4.1           1.0  Iris-versicolor
68   69            6.2           2.2            4.5           1.5  Iris-versicolor
69   70            5.6           2.5            3.9           1.1  Iris-versicolor
70   71            5.9           3.2            4.8           1.8  Iris-versicolor
71   72            6.1           2.8            4.0           1.3  Iris-versicolor
72   73            6.3           2.5            4.9           1.5  Iris-versicolor
73   74            6.1           2.8            4.7           1.2  Iris-versicolor
74   75            6.4           2.9            4.3           1.3  Iris-versicolor
75   76            6.6           3.0            4.4           1.4  Iris-versicolor
76   77            6.8           2.8            4.8           1.4  Iris-versicolor
77   78            6.7           3.0            5.0           1.7  Iris-versicolor
78   79            6.0           2.9            4.5           1.5  Iris-versicolor
79   80            5.7           2.6            3.5           1.0  Iris-versicolor
80   81            5.5           2.4            3.8           1.1  Iris-versicolor
81   82            5.5           2.4            3.7           1.0  Iris-versicolor
82   83            5.8           2.7            3.9           1.2  Iris-versicolor
83   84            6.0           2.7            5.1           1.6  Iris-versicolor
84   85            5.4           3.0            4.5           1.5  Iris-versicolor
85   86            6.0           3.4            4.5           1.6  Iris-versicolor
86   87            6.7           3.1            4.7           1.5  Iris-versicolor
87   88            6.3           2.3            4.4           1.3  Iris-versicolor
88   89            5.6           3.0            4.1           1.3  Iris-versicolor
89   90            5.5           2.5            4.0           1.3  Iris-versicolor
90   91            5.5           2.6            4.4           1.2  Iris-versicolor
91   92            6.1           3.0            4.6           1.4  Iris-versicolor
92   93            5.8           2.6            4.0           1.2  Iris-versicolor
93   94            5.0           2.3            3.3           1.0  Iris-versicolor
94   95            5.6           2.7            4.2           1.3  Iris-versicolor
95   96            5.7           3.0            4.2           1.2  Iris-versicolor
96   97            5.7           2.9            4.2           1.3  Iris-versicolor
97   98            6.2           2.9            4.3           1.3  Iris-versicolor
98   99            5.1           2.5            3.0           1.1  Iris-versicolor
99  100            5.7           2.8            4.1           1.3  Iris-versicolor</td>
    <td>       Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm         Species
100  101            6.3           3.3            6.0           2.5  Iris-virginica
101  102            5.8           2.7            5.1           1.9  Iris-virginica
102  103            7.1           3.0            5.9           2.1  Iris-virginica
103  104            6.3           2.9            5.6           1.8  Iris-virginica
104  105            6.5           3.0            5.8           2.2  Iris-virginica
105  106            7.6           3.0            6.6           2.1  Iris-virginica
106  107            4.9           2.5            4.5           1.7  Iris-virginica
107  108            7.3           2.9            6.3           1.8  Iris-virginica
108  109            6.7           2.5            5.8           1.8  Iris-virginica
109  110            7.2           3.6            6.1           2.5  Iris-virginica
110  111            6.5           3.2            5.1           2.0  Iris-virginica
111  112            6.4           2.7            5.3           1.9  Iris-virginica
112  113            6.8           3.0            5.5           2.1  Iris-virginica
113  114            5.7           2.5            5.0           2.0  Iris-virginica
114  115            5.8           2.8            5.1           2.4  Iris-virginica
115  116            6.4           3.2            5.3           2.3  Iris-virginica
116  117            6.5           3.0            5.5           1.8  Iris-virginica
117  118            7.7           3.8            6.7           2.2  Iris-virginica
118  119            7.7           2.6            6.9           2.3  Iris-virginica
119  120            6.0           2.2            5.0           1.5  Iris-virginica
120  121            6.9           3.2            5.7           2.3  Iris-virginica
121  122            5.6           2.8            4.9           2.0  Iris-virginica
122  123            7.7           2.8            6.7           2.0  Iris-virginica
123  124            6.3           2.7            4.9           1.8  Iris-virginica
124  125            6.7           3.3            5.7           2.1  Iris-virginica
125  126            7.2           3.2            6.0           1.8  Iris-virginica
126  127            6.2           2.8            4.8           1.8  Iris-virginica
127  128            6.1           3.0            4.9           1.8  Iris-virginica
128  129            6.4           2.8            5.6           2.1  Iris-virginica
129  130            7.2           3.0            5.8           1.6  Iris-virginica
130  131            7.4           2.8            6.1           1.9  Iris-virginica
131  132            7.9           3.8            6.4           2.0  Iris-virginica
132  133            6.4           2.8            5.6           2.2  Iris-virginica
133  134            6.3           2.8            5.1           1.5  Iris-virginica
134  135            6.1           2.6            5.6           1.4  Iris-virginica
135  136            7.7           3.0            6.1           2.3  Iris-virginica
136  137            6.3           3.4            5.6           2.4  Iris-virginica
137  138            6.4           3.1            5.5           1.8  Iris-virginica
138  139            6.0           3.0            4.8           1.8  Iris-virginica
139  140            6.9           3.1            5.4           2.1  Iris-virginica
140  141            6.7           3.1            5.6           2.4  Iris-virginica
141  142            6.9           3.1            5.1           2.3  Iris-virginica
142  143            5.8           2.7            5.1           1.9  Iris-virginica
143  144            6.8           3.2            5.9           2.3  Iris-virginica
144  145            6.7           3.3            5.7           2.5  Iris-virginica
145  146            6.7           3.0            5.2           2.3  Iris-virginica
146  147            6.3           2.5            5.0           1.9  Iris-virginica
147  148            6.5           3.0            5.2           2.0  Iris-virginica
148  149            6.2           3.4            5.4           2.3  Iris-virginica
149  150            5.9           3.0            5.1           1.8  Iris-virginica</td>
 </tr>
</table>


