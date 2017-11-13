#!/usr/bin/python3

import unittest, datetime, database

student1 = database.student(1, "Ryan", datetime.date(1978, 1, 12), database.address(104, 'Main Street'), datetime.date(2017, 3, 9), "220CT", True)
student2 = database.student(2, "Devin", datetime.date(2000, 1, 12), database.address(10, '10, Station Road'), datetime.date(2017, 3, 9), "121COM", False)
student3 = database.student(3, "Rob", datetime.date(2002, 4, 2), database.address(1, 'Lunch Lane'), datetime.date(2017, 3, 9), "290COM", True)
student4 = database.student(4, "Ellen", datetime.date(1997, 1, 12), database.address(1, 'Lunch Lane'), datetime.date(2017, 3, 9), "290COM", False)
student5 = database.student(5, "Taylor", datetime.date(1995, 5, 9), database.address(3, 'Judas Lane'), datetime.date(2017, 3, 9), "220CT", True)
students = [student5, student3, student4, student2, student1]
db = database.database(students)
