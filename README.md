# pands-project

Author Veronica Curry

Student ID: G00074924

Completed: April 2021


## Fisher's Iris Data Set

<br/>

![alt text](https://github.com/VCurry20/pands-project/blob/main/Images/johnMuirlaw.1.jpg)
[0]
<br/>

## Overview
The purpose of this project is to research Fisher's Iris Dataset and to show how Python can be used to investigate datasets and output the results to graphs. I will be using Fisher's Dataset as an example of the functionality of Python and to outline ways in which the analysis carried out on this Dataset is transferable. I have included in this Respository the datasets, outputs and also the code used.

The Fisher Iris Dataset examines three species of Iris Plant – Iris Setosa, Iris Virginica, and Iris Versicolor. It outlines their petal width and length, and their sepal width and length. There are 50 samples of each of the three species, resulting in a 150 line data set.

This Dataset has been used for pattern analysis, statistics, and more recently for machine learning and for the teaching of data analysis. This use has far outweighed its importance as information about the biology of the plants, with botanists now even questioning if Iris plants have a Sepal. [16]

The Dataset is large enough to demonstrate the principles of using a program like python while not so large as to overwhelm a student, it has no missing data, there are 4 attributes covering three different plants and all the data is in the same format and unit type. The data set is now also present as a built-in data set which can be imported directly into Python. [17]


<br/>

In this project I will include the following:

> An overview of the Dataset 

> A guide to python and modules within Python we used to review the Dataset

> Display the results of Python analysis of the Dataset

> Display graphs of the Dataset 

<br/>

### Fisher's Iris Dataset 
There are approximately 300 types of Iris globally. The name Iris comes from the Greek Goddess Iris, who was the Goddess of the Rainbow or a messenger of the Gods.  [4] [5] The names derives from the fact that Irises can be found in a wide variety of colours. These are a colourful showy plant which grow in the spring or summer and can be found in a diverse range of climates and locations. [3] [7]

<br/>
The Iris Fisher data set examines three different types of Iris:

Iris Virginica


![alt text](https://github.com/VCurry20/pands-project/blob/main/Images/Irisvirginica.wildflowerorg.jpg)
[8]


This an Iris native to North America, is has traditionally been used in Cherokee tribes as a medicinal plant. It can be used as a salve for the skin and as a treatment for liver ailments. [9]

<br/>
Iris Versicolor


![alt text](https://github.com/VCurry20/pands-project/blob/main/Images/irisversicolor.wildflowerorg.jpg)
[10]

This is also known as the Blug Flag Iris. It is also native to North America, and Eastern Canada. It is poisonous, causing illness in humans and animals who have consumed it. It is also said to bring finanical gain to those who carry it. [11]

<br/>
Iris Setosa


![alt text](https://github.com/VCurry20/pands-project/blob/main/Images/Irissetosa.wildflowerorg.jpg)
[12]

This is an Iris which grows in Alaska, Maine, Canada, and parts of Asia. Although it is poisonous it has been used, when cooked, by various Peoples throough out the World for both food and for medicinal reasons. It is currently on a red list of endangered Japanese plants. [13] 


<br/>
Fisher's Iris Dataset

![alt text](https://github.com/VCurry20/pands-project/blob/main/Images/towardsdatascience.jpg)
[14]

This data was compiled by Sir Ronald Aylmer Fisher and Dr Edgar Anderson. It was published in 1936 in a report titled "The use of Multiple Measurements in Taxonimic Problems". While Dr Anderson was a botanist and collected the majority of the measurements, Sir Fisher was a statistician and geneticist. The data listed the sepal and petal length and width as shown in the above diagram.
In this report Fisher "developed and evaluated a linear function to differentiate Iris species based on the morphology of their flowers". The data collected was used to form graphs which outlined the differences between the plants - when plotted the graphs differenciated between the species with little overlap except between the Iris Versicolor and the Iris Virginica. This overlap occurs when the data is used in cluster analysis.  [1] [14] [15]



![alt text](https://github.com/VCurry20/pands-project/blob/main/Images/towardsdatascience2.jpg)
Figure from Fisher's Article [14]

## Python

``` python
print ("Hello World")
```

Python is a fourth-generation programming lanugage created by Guido Van Rossum and released in 1991. This is a high-level multipurpose language that offers an access-point for novice programmers to enter the field. [1] [2] 

Python is an example of object orientated programming, it is easier to read than other languages and can achieve many of its objectives in less lines of code. It is cross – platform and there is a large online community using the language which offers a large and easily accessable database of knowledge for new users.[3] [4]

Python offers a wide range of plug in modules; modules are files "containing a set of functions you want to include in your application". [5] These modules allow us to "plug in" additional capabilities which we can then use to review our data. 

In this project we will review 4 of these modules, running python via VScode and will upload all relevant data to this Github account.


Common uses of Python:

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

Analytical Modules

NumPy or Numerical Python is a general-purpose numerical module for python, it is the main module for scientific computing in Python. This is a numerical library, which stores data in matrices which are called arrays. The underlying code for NumPy is written in C code or the C language which makes this a very fast module. NumPy can be used for a wide range of operations on arrays including maths, logical operations, sorting, algebra, and statistical operations. NumPy is a core module of Python which Pandas is built upon. [6] [7] [8] [9]

Pandas is an open source module which operates in conjunction with NumPy. It is a Data Analysis module which allows the user to manipulate, clean, slice, index, and merge data. Data is stored in data frames (df). Pandas can read from and output to a wide range of data structures and formats including CSV and Excel.  [10] [11] [12] 



NumPy Vs Pandas

While both modules offer the user a wide range of operations there are differences which should be considered. Pandas operates on tabular data that is structured in rows where NumPy works solely on numerical data stored in arrays. Pandas which is built on NumPy and allows for easier manipulation of data at a higher level and offers easy to use data structures and tools for data analysis. Pandas has a wide range of input / output options. [13] [14]


Graphing Modules

Matplotlib is a module that offers data visualisation for Python and NumPy, it is open source and can be used to create charts including Line and bar charts. [15] [16]


Seaborn is the next step in Data Visualisation, it offers a variety of visualisation pattern, uses less syntax and is a high-level interface. This module builds on matplotlib and works from Pandas. [17] [18] 


In choosing between these modules it is best to consider the desired output, Matplotlib excels in more basic plotting – the traditional bars, pies, and scatterplots. Seaborn offers an accessible option for data visualisation. [19]

## Analysis


### Dataset
We can use Python to review this dataset using the built in functions and modules. I will outline some of these functions below and have included the output text files with this project.

The Fisher's Iris Dataset was downloaded from [Kaggle](https://www.kaggle.com/uciml/iris) and can be found widely online. I have stored this information in a CSV file titled [kaggleIrisSet.csv](https://github.com/VCurry20/pands-project/blob/main/kaggleIrisSet.csv). The Dataset can be found in various formats and should include a total of 150 sets / rows of iris measurements. [1]

It is also included in a list of datasets that can be imported directly into Python. To complete this process the following is an example of the code required [2]:
(Note that I have included the code for printing for viewing in VScode and also for creating a file and printing to this file)

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

> Python File - [Overview.py](https://github.com/VCurry20/pands-project/blob/main/Overview.py)

> Python File - [Slicedata.py](https://github.com/VCurry20/pands-project/blob/main/Slicedata.py)


In these files we open the NumPy and Pandas modules and use them to review the data in various ways. 
Firstly we open the file containing the Fishers Dataset, from this we set this file as a variable. This allows for us to change the file without having to alter the code, the code therefore can be used on various data files. This process allows for python programs to be written and used muliple times with very few changes needed.

Once this is complete we can start to analyise the data.

It should also be noted that although we are using a CSV file format for the Dataset we can change this format or even directly output from the imported data set to a different file type. 

With this code I have created an excel file from the CSV file we have downloaded as an example of this process:

```python 
df.to_excel("Dataprintout.xlsx") 
```

<br/>
Using Python’s built in functions I have reviewed the Dataset in the following ways:
<br/>

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

This code can also be used to provide stastical information about the individual Iris species:


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


This same syntax can also be used to take either the top or bottom lines of code using df.head() / df.tail(). 


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

Some of these processes can be incorporated into code for programming use or can be used individually to review data and give an overall picture of a dataset quickly and efficiently - this in turn can be used to evaulate the information provided and take further steps. 

Program uses for this could be to review documents / files / datasets for missing data and with if statements allow the user to continue or allow for the document to continue to the next stage for processing. Null values could result in the document / user being declined and further actions being needed.

Depending on file type and the breakout needed from this information I am also including the following Python program output file. This shows the output of slicing the data and how from this process we can easily split files - creating new datasets or saving the information to variables. This file includes a print of specific rows, specific colums and also the data per Iris type. I have outputted some of these results by setting variables for each flower species.

> Output File - [Sliceoutput.txt](https://github.com/VCurry20/pands-project/blob/main/Sliceoutput.txt)

File creation and print code:
``` Python
with open("Sliceoutput.txt", "wt") as f:                                                                   # Open File "Sliceoutput.txt" as a txt file, in write txt mode
    print("\nIn this file I will show ways the data can be broken down. \n", file=f)                       # Breakdown of the csv - outputs a review of the numerical data
    print("\nWe can print choosen parts; here I have choosen lines 10-20: \n", df[10:21], file=f)          # Print specific rows
    print("\nIn this case I have choose two columns - 'Id' and 'Species': \n", specific_data, file=f)      # Print Id and Species as choosen in variable
    print("\nWe can then also print just by the particular flower -  Iris Setosa': \n", setosa , file=f)   # Print the file details for the flower Iris Setosa
    print("\nThen the next flower -  Iris Versicolor': \n", versicolor , file=f)                           # Print the file details for the flower Iris Versicolor
    print("\nAnd finally the last remaining flower -  Iris Virginica': \n", virginica , file=f)            # Print the file details for the flower Iris Virginica

```

This is not an exhaustive list of the potential of Python and the ways it can be used for file manipulation. The important factors are that Python offers us the chance to review information quickly and efficiently, it also offers us the chance to write programs which can be used on different datasets.


## Graphing

Matplotlib and Seaborn will now be used in conjunction with NumPy and Pandas to plot and print graphs of the Dataset, this offers visualisation of the data and can be used for Presentations.

For an overview of the possibilities of this process please review the following: [Plotting Gallery](https://seaborn.pydata.org/examples/index.html)

Although there is a large number of graph options available, in this project we will review the following:

> Histrogram

> Scatterplot


<br/>



![alt text](https://github.com/VCurry20/pands-project/blob/main/Hisplot.png)

<br/>

<p float="centre">
  <img src="https://github.com/VCurry20/pands-project/blob/main/HisplotA.png" width="400" />
  <img src="https://github.com/VCurry20/pands-project/blob/main/HisplotB.png" width="400" /> 
  </p>

<p float="centre">
  <img src="https://github.com/VCurry20/pands-project/blob/main/HisplotC.png" width="400" />
  <img src="https://github.com/VCurry20/pands-project/blob/main/HisplotD.png" width="400" /> 
  </p>




<br/>
<br/>

![alt text](https://github.com/VCurry20/pands-project/blob/main/Scatterplots.png)












<br/>
<br/>

I have also provided a Sample of the following graphs for you to view which used the Fisher's Iris Dataset:


> Voilin Plots     - [Voilinplots.png](https://github.com/VCurry20/pands-project/blob/main/Voilinplots.png)

> Joint Plots      - [Jointplot.png](https://github.com/VCurry20/pands-project/blob/main/Jointplot.png)

> Joint Plot 2     - [Jointplot2.png](https://github.com/VCurry20/pands-project/blob/main/Jointplot2.png)

> Catagorical Plot - [catplot.png](https://github.com/VCurry20/pands-project/blob/main/catplot.png)

> Implot           - [implot.pgn](https://github.com/VCurry20/pands-project/blob/main/Implot.png)

> Implot 2         - [implot2.png](https://github.com/VCurry20/pands-project/blob/main/Implot2.png)

> Distribution Plot  - [distplot.txt](https://github.com/VCurry20/pands-project/blob/main/Distplot.png)

> Pair Plot  - [pairplot.txt](https://github.com/VCurry20/pands-project/blob/main/pairplot.png)





## References:
All references were accessed and correct as of April 2021

### Overview:
[0] John Muirlaws, How to draw an Irish: part 2 (No Date) https://johnmuirlaws.com/how-to-draw-an-iris-part-2/  
[1] Research Gate, What Should we know about the famous Iris Data? (March 2013) https://www.researchgate.net/publication/237010807_What_should_we_know_about_the_famous_Iris_data 
[2] Towards Data Science, Exploring Classifiers with Python Scikit-learn – Iris Dataset (July 13 1020) https://towardsdatascience.com/exploring-classifiers-with-python-scikit-learn-iris-dataset-2bcb490d2e1b
[3] Wikipedia, Irish Flower Data Set,  (September 14th 2018) - https://en.wikipedia.org/wiki/Iris_flower_data_set 
[4] U.S forest Service, The Iris Flower, (No Date) https://www.fs.fed.us/wildflowers/beauty/iris/flower.shtml 
[5] The Spruce, 9 Top Types of Iris for the Flower Garden, ( February 3rd, 2021) https://www.thespruce.com/irises-for-flower-garden-1315808  
[6] The Old Farmer’s Alamac, Growing Irises, (No Date) https://www.almanac.com/plant/irises
[7] Wikipedia, Iris (Mythology), (February 2nd,2019) https://en.wikipedia.org/wiki/Iris_(mythology) 
[8] Grow Irises for easy elegance in your garden, (September 12th, 2018)
https://www.gardendesign.com/flowers/iris.html 
[9] Lady Bird Johnston Wildflower Centre, Iris Virginica (No Date) https://www.wildflower.org/gallery/result.php?id_image=43626 
[10] Wikipedia, Iris Virginica, (first created February 4th , 2011) https://en.wikipedia.org/wiki/Iris_virginica 
[11] Lady Bird Johnston Wildflower Centre, Iris Versicolor (No Date) https://www.wildflower.org/gallery/result.php?id_image=1894 
[12] Wikipedia, Iris Versicolor, (first created April 12th 2016) https://en.wikipedia.org/wiki/Iris_versicolor 
[13] Lady Bird Johnston Wildflower Centre, Iris Setosa (No Date) https://www.wildflower.org/plants/result.php?id_plant=irse  
[14] Wikipedia, Iris Setosa, (first created October 26th2017) https://en.wikipedia.org/wiki/Iris_versicolor 
[15] Towards data science, The Iris Dataset – A little bit of History and Biology (April 25th 2020) https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5 
[16] Centre for machine learning and intelligent systems, Iris Data set (No Date for webpage) http://archive.ics.uci.edu/ml/datasets/Iris/ 
 

### Python:
[1] W3 Schools, What is Python (1999 -2021) https://www.w3schools.com/python/python_intro.asp 
[2] Computer Hope, Generation Languages (June 30th 2019) https://www.computerhope.com/jargon/num/1gl.htm#:~:text=The%20fourth%2Dgeneration%20languages%2C%20or,Python%2C%20Ruby%2C%20and%20SQL. 
[3] Wikipedia, Python (Programming Language) (October 29th, 2001) https://en.wikipedia.org/wiki/Python_(programming_language 
[4] YouTube, What is python? Why Python is so helpful? (Oct 23rd, 2018) https://www.youtube.com/watch?v=Y8Tko2YC5hA 
[5] Python Modules, What is a Module? (1999 -2021)  https://www.w3schools.com/python/python_modules.asp 
[6] Youtube, What is Numpy? (June 6th 2016) https://www.youtube.com/watch?v=Tkv45wgxlEU 
[7] NumPy Org, What is NumPy? (Last Updated Jan 31st 2021) https://numpy.org/doc/stable/user/whatisnumpy.html 
[8] NumPy Org, Why is NumPy so fast? (Last Updated Jan 31st 2021)  https://numpy.org/doc/stable/user/whatisnumpy.html#why-is-numpy-fast 
[9] Towards Data Science, Top Python Libraries: NumPy and Pandas ( November 16, 2019) https://towardsdatascience.com/top-python-libraries-numpy-pandas-8299b567d955
[10] Pandas Org, About Pandas (No Date) https://pandas.pydata.org/about/index.html
[11] Active State, What is Pandas in Python? Everything you need to know  (No Date) https://www.activestate.com/resources/quick-reads/what-is-pandas-in-python-everything-you-need-to-know/ 
[12] Educative, What is Pandas in Python? (No Date) https://www.educative.io/edpresso/what-is-pandas-in-python
[13] Java T Point, Pandas Vs NumPy (2011 – 2018) https://www.javatpoint.com/pandas-vs-numpy#:~:text=The%20Pandas%20module%20mainly%20works,works%20with%20the%20numerical%20data.&text=NumPy%20library%20provides%20objects%20for,memory%20as%20compared%20to%20Pandas. 
[14] Geeks for Geeks, Difference between Pandas vs NumPy (Oct 24th 2020) https://www.geeksforgeeks.org/difference-between-pandas-vs-numpy/ 
[15] Matplotlib org, Introductory page (2012-2021) https://matplotlib.org/ 
[16] Active State, What is Matplotlib in Python (No Date) https://www.activestate.com/resources/quick-reads/what-is-matplotlib-in-python-how-to-use-it-for-plotting/ 
[17] Analytics India Magazine, Comparing Python Data Visualization Tools: Matplotlib Vs Seaborn, (July 2nd 2019) https://analyticsindiamag.com/comparing-python-data-visualization-tools-matplotlib-vs-seaborn/ 
[18] Seaborn Org, Seaborn: Statistical Data Visualisation (2012 – 2021) https://seaborn.pydata.org/#:~:text=Seaborn%20is%20a%20Python%20data,attractive%20and%20informative%20statistical%20graphics. 
[19] Seaborn Org, An introduction to Seaborn (2021 – 2021) https://seaborn.pydata.org/introduction.html#:~:text=Seaborn%20is%20a%20library%20for%20making%20statistical%20graphics%20in%20Python.&text=Seaborn%20helps%20you%20explore%20and,aggregation%20to%20produce%20informative%20plots. 

### Analysis:
[1] Kaggle, Iris Species, classify iris plants into three species in this classic dataset (2016) https://www.kaggle.com/uciml/iris 
[2] Scikit Learn, Sklearn.datasets.load_iris (2007-2020) https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html 

Code Review Links:
(Please note that I reviewed a large number of sites for code – this is a list of sites which I accessed)
[3] Pandas Org, pandas.Dataframe.info, (2008 -2021)  https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html 
[4] Geeks for Geeks, Python Basics of Pandas using Iris Dataset, (May 17th,2020) https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/ 
[4] Pandas Org, pandas.DataFrame.describe, (2008 -2021) https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html
[6] Pandas Org, pandas.DataFrame.groupby, (2008 -2021) https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html 
[7] Pandas Org, pandas.DataFrame.head, (2008 -2021) https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html 
[8] Pandas Org, pandas.DataFrame.tail, (2008 -2021) https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.tail.html 
[9] Stack Overflow, how to convert df.info() into data frame. df.info(), (2020) https://stackoverflow.com/questions/64067424/how-to-convert-df-info-into-data-frame-df-info 
[10] Python for Beginners, Reading and Writing Files in Python, (February 5th, 2021) https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python 
[11] Kaggle, Iris Flower Data EDA, (April 2021) https://www.kaggle.com/doreamon11122000/iris-flower-dataset-eda 
[12] Kaggle, Iris_Dataset_EDA_N, (April 2021) https://www.kaggle.com/necibecan/iris-dataset-eda-n 
[13] Medium, Exploratory Data Analysis of IRIS Data set using Python, (May 13th 2019) https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d 
[14] YouTube, Pairwise Comparison Charts 2: setting up and running them (August 7th, 2014) https://www.youtube.com/watch?v=orrQFHKlocs 
[15] Pandas Org, Indexing and selecting Data, (2008 -2021)  https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html 
[16] Data Carpentry, Indexing, Slicing and Subsetting DataFrames in Python ( 2018-2021) https://datacarpentry.org/python-ecology-lesson/03-index-slice-subset/index.html 
[17] Pandas Org, pandas.DataFrame.corr , (2008 -2021)  https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.corr.html 
[18] Pandas Org, pandas.DataFrame.loc , (2008 -2021)  https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html 
[19] Geeks for Geeks, Pandas Dataframe.loc[], (Feb 20th, 2019) https://www.geeksforgeeks.org/python-pandas-dataframe-loc/ 


### Graphing:
[1] Seaborn, Example Gallery, (2012 - 2021) https://seaborn.pydata.org/examples/index.html 
[2] Amazon Aws, Using Seaborn Styles, (No date) https://s3.amazonaws.com/assets.datacamp.com/production/course_6919/slides/chapter2.pdf 
[3] Geeks for Geeks, Plotting graph For IRIS Dataset Using Seaborn And Matplotlib, (March 4th, 2021) https://www.geeksforgeeks.org/plotting-graph-for-iris-dataset-using-seaborn-and-matplotlib/ 
[4] Stack Overflow, create a scatter plot from a csv file with categories, (2020)    https://stackoverflow.com/questions/61668759/create-a-scatter-plot-from-a-csv-file-with-categories 
[5] Stack Overflow, Use different colors in scatterplot for Iris dataset, (2018), https://stackoverflow.com/questions/45862223/use-different-colors-in-scatterplot-for-iris-dataset 
[6] Kaggle, Seaborn visualization on iris data set, (2016) , https://www.kaggle.com/noelano/seaborn-visualization-on-iris-data-set 
[7] Jake VDP, Visualisation with Seaborn, (No Date), https://jakevdp.github.io/PythonDataScienceHandbook/04.14-visualization-with-seaborn.html 
[8] Kaggle, Iris Flower Dataset EDA, (April 2021) https://www.kaggle.com/doreamon11122000/iris-flower-dataset-eda 
[9] Kaggle, Iris_Dataset_EDA_N, (April 2021) https://www.kaggle.com/necibecan/iris-dataset-eda-n 
[10] Medium, Exploratory Data Analysis of IRIS Data Set Using Python, (May 13, 2019), https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d 
[11] CMD Line Tips, How To Make Histogram in Python with Pandas and Seaborn?, (February 10th, 2019)
https://cmdlinetips.com/2019/02/how-to-make-histogram-in-python-with-pandas-and-seaborn/#:~:text=The%20Seaborn%20function%20to%20make,as%20argument%20to%20make%20histogram.&text=By%20default%2C%20the%20histogram%20from,axis%20label%20and%20its%20ranges. 
[12] Codecademy, Seaborn Styling, Part 2: Color, (no Date) https://www.codecademy.com/articles/seaborn-design-ii#:~:text=Seaborn%20has%20six%20variations%20of,bright%20%2C%20dark%20%2C%20and%20colorblind%20.  
[13] Matplotlib, matplotlib.pyplot.subplots (2012 – 2021) https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html 
[14] Stack Overflow, How to make several plots on a single page using matplotlib? (2010) https://stackoverflow.com/questions/1358977/how-to-make-several-plots-on-a-single-page-using-matplotlib 
[15] Javaer 101, seaborn violinplots: change violin color, axes names, legend (October 23rd, 2010) https://www.javaer101.com/en/article/14004962.html 
[16] Mathlab answers, How can I insert a title over a group of subplots? (April 26th, 2010) https://uk.mathworks.com/matlabcentral/answers/100459-how-can-i-insert-a-title-over-a-group-of-subplots 

Seaborn Links:
[1] Seaborn, Example Gallery, (2012 - 2021),  https://seaborn.pydata.org/examples/index.html 
[2] Seaborn Org, seaborn.swarmplot, (2012 – 2020), https://seaborn.pydata.org/generated/seaborn.swarmplot.html 
[3] Seaborn Org, Choosing Color Palettes, (2012 – 2020), https://seaborn.pydata.org/tutorial/color_palettes.html 
[4] Seaborn Org, seaborn.FacetGrid , (2012 – 2020), https://seaborn.pydata.org/generated/seaborn.FacetGrid.html 
[5] Seaborn Org, Choosing Color Palettes, (2012 – 2020), https://seaborn.pydata.org/tutorial/color_palettes.html 
[6] Seaborn Org, seaborn.scatterplot , (2012 – 2020), https://seaborn.pydata.org/generated/seaborn.scatterplot.html?highlight=scatterplot#seaborn.scatterplot 
[7] Seaborn Org, seaborn.implot , (2012 – 2020), https://seaborn.pydata.org/generated/seaborn.lmplot.html 
[8] Seaborn Org, Building structured multi-plots grids, (2012 – 2020), https://seaborn.pydata.org/tutorial/axis_grids.html
[9] Seaborn Org, Seaborn Histplot, (2012 – 2020), https://seaborn.pydata.org/generated/seaborn.histplot.html

YouTube:
Derek Banas, Matplotlib Tutorial, (August 22nd, 2020) https://www.youtube.com/watch?v=wB9C0Mz9gSo
Derek Banas, Seaborn Tutorial, ( September 1st, 2020) https://www.youtube.com/watch?v=6GUZXDef2U0 


