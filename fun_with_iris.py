# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 16:50:34 2016

@author: Thomas
"""

"""
The goal of this script is to do some data manipulation in Python using
the iris dataset.
"""

#### Import packages
from sklearn import datasets # To get the iris dataset
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn

#### Import the famous iris dataset
iris = datasets.load_iris()

#### From sklearn data structure to dataframe
iris = pd.DataFrame(data=np.c_[iris['data'],
                               iris['target']],
                     columns=iris['feature_names'] + ['target'])

#### Plot some data
plt.hist(iris['sepal length (cm)'])                     
plt.scatter(iris['sepal length (cm)'], iris["sepal width (cm)"])      

#### Fancier plot using seaborn
seaborn.plt.scatter(iris['sepal length (cm)'],
                 iris['sepal width (cm)'], 
                      c = iris['target']) 

#### Get some summary statistics
iris['target'].value_counts()               
iris.describe()                     

#### Create small table that maps the target to the name of an iris species
target = pd.Series([0, 1, 2],
                   name = 'target')
                   
species = pd.Series(['setosa', 'versicolor', 'virginica'], 
                    name = 'species')

#### Convert target value to int due to precision error of floats
iris['target'] = iris['target'].apply(int)

species_df = pd.concat([target, species], 
                       axis = 1)

del target, species

#### Join the species 
iris = pd.merge(left = iris, 
                right = species_df, 
                on = 'target')

del species_df

#### Get some statistics for setosa flowers   
iris[iris['species']== 'setosa'].mean(axis = 0)

#### Try the group by method and its mean method
grouped = iris.groupby('species', 
                       axis=0)
 
grouped_mean = grouped.mean()

#### Merge the statistics to the main dataframe
iris = pd.merge(left = iris,
                right = grouped_mean,
                left_on = 'species',
                right_index = True)
                
#### That is super convenient !
del grouped, grouped_mean
