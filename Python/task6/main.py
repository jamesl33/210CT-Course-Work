#!/usr/bin/python3

import unittest, datetime
from address import address
from database import database
from student import student
from binary_tree import binary_tree
from node import node

student1 = student(1, "Ryan", datetime.date(1978, 1, 12), address(104, 'Main Street'), datetime.date(2017, 3, 9), "220CT", True)
student2 = student(2, "Devin", datetime.date(2000, 1, 12), address(10, '10, Station Road'), datetime.date(2017, 3, 9), "121COM", False)
student3 = student(3, "Rob", datetime.date(2002, 4, 2), address(1, '1, Lunch Lane'), datetime.date(2017, 3, 9), "290COM", True)
student4 = student(4, "Ellen", datetime.date(1997, 1, 12), address(1, 'Lunch Lane'), datetime.date(2017, 3, 9), "290COM", False)
student5 = student(5, "Taylor", datetime.date(1995, 5, 9), address(3, 'Judas Lane'), datetime.date(2017, 3, 9), "220CT", True)
students = [student5, student3, student4, student2, student1]
db = database(students)

print(db.find(1, 'uniqueId')) # uses binary search to find the student with the unique id which is equal to 1
print(db.find('220CT', 'classId')) # uses binary search to get a list of students which attend the class 220CT
