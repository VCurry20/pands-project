# pands-project

## Fisher's Iris Data Set

<br/>

![alt text](https://github.com/VCurry20/pands-project/blob/main/johnMuirlaw.1.jpg)
[0]
<br/>

### Overview
The purpose of this project is to research Fisher's Iris Dataset and to show how python can be used to investigate this dataset and output the results to graphs.
This is a dataset that examines three species of Iris Plant – Iris Setosa, Iris Virginica, and Iris Versicolor. It outlines their petal width and length and their sepal width and length. There are 50 samples of each of the three species, resulting in a 150 line data set.

<br/>

In this project I will include the following:

> A Full data set list

> An Overview of the Data and what it represents

> I will provide graphs that map this data

> Provide an over view of other research material 


### Fisher's Iris Dataset 
There are approximately 300 types of Iris, the name Iris comes from the Greek Goddess Iris, who was the Goddess of the Rainbow or a messenger of the Gods.  [4] [5] The names derives from the fact that they can be found in a wide variety of colours. These are a colourful showy plant which grow in the spring or summer and can be found in a variety of different climates and locations. [3] [7]

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
In this report Fisher "developed and evaluated a linear function to differentiate Iris species based on the morphology of their flowers". The data collected was used to form graphs which outlined the differences between the plants - when plotted the graphs differenciated between the species with little overlap except between the Iris Versicolor and the Iris Virginica. This overlap occurs when the data is used in cluster analysis.  [1][14][15]


![alt text](https://github.com/VCurry20/pands-project/blob/main/towardsdatascience2.jpg)
Figure from Fisher's Article [14]



### Data Review
We can use python to review this data set using the built in functions and modules. Firstly we will use Pandas to review the data set under various headings.

We can import Fisher Iris data set directly.

```python
from sklearn.datasets import load_iris

iris = load_iris()
print(iris)

```

We also need to add into out python script the various modules which we will be using both to review the data and then output it in graph form

```python 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

```
Module Explainer:
> Numpy:
> Pandas:
> Matplotlib.pyplot
> Seaborn:


Overview of the information
Using python we can break down the file and them analyis the various components of it

> File - [Analysis1.py](https://github.com/VCurry20/pands-project/blob/main/Analysis1.py)

In this file we open the Pandas and the Numpy modules and use them to review the data in various ways. 
Firstly we open the file containing the Fishers Dataset, from this we set this file as a variable. This allows for us to change the file name without having to alter the code. 

Once this is complete we can start to analyise the data

We can print the data out to another file - and another file type:

```python 
df.to_excel("Dataprintout.xlsx") 
```

Describe :

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

AJBVCODAJBV
ADJVBALJSBVC
#ABKCAB SLVCJ
BKASCHBA LCB 
ABKSB CALJSVB#


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
<th>Sepal Length</th>
<th>Sepal Width</th>
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