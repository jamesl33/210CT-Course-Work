#!/usr/bin/python3

import datetime
from database import Database
from student import Student
from address import Address

def main():
    student1 = Student(1, "Ryan", datetime.date(1978, 1, 12), Address(104, 'Main Street'), datetime.date(2017, 2, 9), '220CT', True)
    student2 = Student(2, "Devin", datetime.date(2000, 1, 12), Address(10, 'Station Road'), datetime.date(2013, 3, 9), '210CT', False)
    student3 = Student(3, "Rob", datetime.date(2002, 4, 2), Address(1, 'Lunch Lane'), datetime.date(2017, 3, 4), '210CT', True)
    student4 = Student(4, "Ellen", datetime.date(1997, 1, 12), Address(1, 'Lunch Lane'), datetime.date(2017, 3, 9), '290COM', False)
    student5 = Student(5, "Taylor", datetime.date(1995, 5, 9), Address(3, 'Judas Lane'), datetime.date(2017, 4, 9), '220CT', True)
    students = [student5, student4, student3, student2, student1]
    db = Database(students)

    #  Found student by id in this case it will be a list containing the reference to 'student3'
    print(db.find(3, 'unique_id'))


main()
