# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 08:36:41 2016

@author: Thomas
"""
"""
This script defines three functions with the same purpose, create an acronym from a script.
- for loop
- list comprehension
- map function

The randomTester function takes a list of functions as argument, it generates random strings and makes sure that the 3 functions
return the same acronym.
"""

#### Import modules
import re
import random

######## 3 ways to create acronyms

#### Takes a string keep the first letter and turn it into upper case
def makeAcronym(expression):    
    return expression[0].upper()

#### map makeAcronym function to a list of strings
def acronymize(list_of_strings):
    return list(map(makeAcronym,list_of_strings))

#### apply makeAcronyme function to a list of strings using a list comprehension
def acronymize2(mylist):
    return [makeAcronym(elem) for elem in mylist]
    
####
def DaveAcronymization(splitted_string):
    
    mylist = []
    for each_word in splitted_string:
         mylist.append(makeAcronym(each_word))

    return mylist  
    
#### concatenates a list of strings into a string    
def concatenate(mylist):
    return ''.join(mylist)

    
#### Function that takes a string and a function as arguments
#### Returns an acronym
def createAcronym(long_string, FUN):  
    
    #### Remove 'duplicated' white spaces
    long_string = re.sub(' +', ' ',  long_string)
    
    #### Check if string is not only composed of white spaces
    if len(re.sub(' +', '',  long_string)) == 0:
        return
        
    return concatenate(FUN(long_string.strip().split(' ')))
    
#### Examples
createAcronym('i like python 2', acronymize)
#### returns 'ILP2'
createAcronym(' i prefer Python 3', acronymize2)    
#### returns 'IPP3'
createAcronym(' i prefer Python 3  too ', DaveAcronymization) 
#### returns 'IPP3T'

#### 
test_cases = ['first string 1',' second ','random words one two three']

func_to_test = [acronymize, acronymize2, DaveAcronymization]

expected = ['FS1', 'S','RWOTT']  

#### Test that for each funciton, actual output is equal to the expected output
def functionTest(func_to_test, expected):
    
    for i in range(len(func_to_test)):    
        a = [createAcronym(elem, func_to_test[i]) for elem in test_cases]
        assert expected ==  a
            
    return            

functionTest(func_to_test, expected)

####
def generateString():  
    
    letters = '               abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    tmp = int(random.randint(0, len(letters)))
    
    mylist = []

    for i in range(tmp):
        mylist += random.choice(letters)
  
    return mylist
    
####   
def randomTester(func_to_test):
     
     a = []
     random_string = concatenate(generateString())
     
     for i in range(len(func_to_test)):   
         a.append(createAcronym(random_string, func_to_test[i])) 
     
     assert len(set(a)) <= 1 
            
     return 

####
def iterateRandomTester(n_times):
    
    for n in range(n_times):
        randomTester(func_to_test)
    
    return    
    
iterateRandomTester(2000)    
