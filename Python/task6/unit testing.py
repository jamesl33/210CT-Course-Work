#!/usr/bin/python3

import unittest, datetime
from database import database
from student import student
from binary_tree import binary_tree
from node import node

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.student1 = student(1, "Ryan", datetime.date(1978, 1, 12), "104, Main Street", datetime.date(2017, 3, 9), "220CT", True)
        self.student2 = student(2, "Devin", datetime.date(2000, 1, 12), "10, Station Road", datetime.date(2017, 3, 9), "121COM", False)
        self.student3 = student(3, "Rob", datetime.date(2002, 4, 2), "1, Lunch Lane", datetime.date(2017, 3, 9), "290COM", True)
        self.student4 = student(4, "Ellen", datetime.date(1997, 1, 12), "23, Lovelace Avenue", datetime.date(2017, 3, 9), "290COM", False)
        self.student5 = student(5, "Taylor", datetime.date(1995, 5, 9), "3, Judas Lane", datetime.date(2017, 3, 9), "220CT", True)
        self.students = [self.student3, self.student2, self.student4, self.student1, self.student5]
        self.db = database(self.students)

    def test_finding_student_by_id(self):
        correct = [self.student3]
        self.assertEqual(self.db.find(3, 'uniqueId'), correct)

    def test_find_and_update_by_id(self):
        self.db.update('220CT', 'classId', '210CT')
        self.assertEqual(self.student1.data['classId'], '210CT')
        self.assertEqual(self.student5.data['classId'], '210CT')

    def test_finding_student_by_class(self):
        correct = [self.student1, self.student5]
        self.assertEqual(self.db.find('220CT', 'classId'), correct)

    def test_list_names_in_lex_order(self):
        correct = ['Devin', 'Ellen', 'Rob', 'Ryan', 'Taylor']
        self.assertEqual(self.db.list('name'), correct)

    def test_list_all_postgraduates(self):
        graduatedStudents = self.db.find(True, 'postgraduate')
        correct = [self.student1, self.student3, self.student5]
        for answer in correct:
            self.assertTrue(answer in graduatedStudents)

    def list_undergrads_by_class_in_lex_order(self):
        underGrads = self.db.find(False, 'postgraduate')
        class220CT = self.db.find('220CT', 'classId')
        class121COM = self.db.find('121COM', 'classId')
        class290COM = self.db.find('290COM', 'classId')

        for student in class220CT:
            if student not in underGrads:
                del(class220CT[student])

        for student in class121COM:
            if student not in underGrads:
                del(class121COM[student])

        for student in class290COM:
            if student not in underGrads:
                del(class290COM[student])

        correct220CT = []
        correct121COM = [self.student2]
        correct290COM = [self.student4]

        self.assertEqual(class220CT, correct220CT)
        self.assertEqual(class121COM, correct121COM)
        self.assertEqual(class290COM, correct290COM)

if __name__ == '__main__':
  unittest.main()
