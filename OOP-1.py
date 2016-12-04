# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 12:38:10 2016

@author: Thomas
"""

class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.__salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print( "Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print( "Name : ", self.name,  ", Salary: ", self.__salary)
      
   def changeEmployeeName(self, new_name):
       self.name = new_name
      
      

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)      


#name and salary of emp1 / Zara

to_return = emp1.displayEmployee()
print(to_return)
emp1.name

