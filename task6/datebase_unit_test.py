#!/usr/bin/python3

import unittest, datetime, database, tree

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.student1 = database.student(1, "Ryan", datetime.date(1978, 1, 12), "104, Main Street", datetime.date(2017, 3, 9), "220CT", True)
        self.student2 = database.student(2, "Devin", datetime.date(2000, 1, 12), "10, Station Road", datetime.date(2017, 3, 9), "121COM", False)
        self.student3 = database.student(3, "Rob", datetime.date(2002, 4, 2), "1, Lunch Lane", datetime.date(2017, 3, 9), "290COM", True)
        self.student4 = database.student(4, "Ellen", datetime.date(1997, 1, 12), "23, Lovelace Avenue", datetime.date(2017, 3, 9), "290COM", False)
        self.student5 = database.student(5, "Taylor", datetime.date(1995, 5, 9), "3, Judas Lane", datetime.date(2017, 3, 9), "220CT", True)
        self.students = [self.student3, self.student2, self.student4, self.student1, self.student5]
        self.db = database.database(self.students)

    def test_finding_student_by_id(self):
        correct = [self.student3]
        self.assertEqual(self.db.find(3, 'unique_id'), correct)

    def test_find_and_update_by_id(self):
        self.db.update('220CT', 'class_id', '210CT')
        self.assertEqual(self.student1.data['class_id'], '210CT')
        self.assertEqual(self.student5.data['class_id'], '210CT')

    def test_finding_student_by_class(self):
        correct = [self.student1, self.student5]
        self.assertEqual(self.db.find('220CT', 'class_id'), correct)

    def test_list_names_in_lex_order(self):
        correct = ['Devin', 'Ellen', 'Rob', 'Ryan', 'Taylor']
        self.assertEqual(self.db.list('name'), correct)

    def test_list_all_postgraduates(self):
        graduatedStudents = self.db.find(True, 'postgraduate')
        correct = [self.student1, self.student3, self.student5]
        for answer in correct:
            self.assertTrue(answer in graduatedStudents)

    def test_list_undergrads_by_class_in_lex_order(self):
        lex = []
        students = self.db.find('all', 'name')
        classes = self.db.find('all', 'class_id')
        for i in range(len(students)):
            for j in range(len(classes)):
                if students[i].owner == classes[j].owner:
                    lex.append('{0}: {1}'.format(classes[j], students[i]))
        self.assertEqual(lex, ['121COM: Devin', '290COM: Ellen', '290COM: Rob', '220CT: Ryan', '220CT: Taylor'])

    def test_remove_by_id(self):
        ''' self contained due to the fact that the other unit tests modify the students '''
        student1 = database.student(1, "Ryan", datetime.date(1978, 1, 12), database.address(104, 'Main Street'), datetime.date(2017, 2, 9), '220CT', True)
        student2 = database.student(2, "Devin", datetime.date(2000, 1, 12), database.address(10, 'Station Road'), datetime.date(2013, 3, 9), '210CT', False)
        student3 = database.student(3, "Rob", datetime.date(2002, 4, 2), database.address(1, 'Lunch Lane'), datetime.date(2017, 3, 4), '210CT', True)
        student4 = database.student(4, "Ellen", datetime.date(1997, 1, 12), database.address(1, 'Lunch Lane'), datetime.date(2017, 3, 9), '290COM', False)
        student5 = database.student(5, "Taylor", datetime.date(1995, 5, 9), database.address(3, 'Judas Lane'), datetime.date(2017, 4, 9), '220CT', True)
        students = [student5, student3, student4, student2, student1]
        db = database.database(students)
        db.remove_by_id(1)
        self.assertEqual(db.data['unique_id'].order(True), ['2', '3', '4', '5'])
        self.assertEqual(db.data['name'].order(True), ['Devin', 'Ellen', 'Rob', 'Taylor'])
        self.assertEqual(db.data['date_of_birth'].order(True), ['1995-05-09', '1997-01-12', '2000-01-12', '2002-04-02'])
        self.assertEqual(db.data['address'].order(True), ['1 Lunch Lane', '1 Lunch Lane', '3 Judas Lane', '10 Station Road'])
        self.assertEqual(db.data['enrolment_date'].order(True), ['2013-03-09', '2017-03-04', '2017-03-09', '2017-04-09'])
        self.assertEqual(db.data['class_id'].order(True), ['210CT', '210CT', '220CT', '290COM'])
        self.assertEqual(db.data['postgraduate'].order(True), ['False', 'False', 'True', 'True'])

    def test_remove_by_postgraduate(self):
        ''' self contained due to the fact that the other unit tests modify the students '''
        ''' There is a nasty logic error in the removing root node when the root has two children please FIX ME I cant for the life of me fix it '''
        student1 = database.student(1, "Ryan", datetime.date(1978, 1, 12), database.address(104, 'Main Street'), datetime.date(2017, 2, 9), '220CT', True)
        student2 = database.student(2, "Devin", datetime.date(2000, 1, 12), database.address(10, 'Station Road'), datetime.date(2013, 3, 9), '210CT', False)
        student3 = database.student(3, "Rob", datetime.date(2002, 4, 2), database.address(1, 'Lunch Lane'), datetime.date(2017, 3, 4), '210CT', True)
        student4 = database.student(4, "Ellen", datetime.date(1997, 1, 12), database.address(1, 'Lunch Lane'), datetime.date(2017, 3, 9), '290COM', False)
        student5 = database.student(5, "Taylor", datetime.date(1995, 5, 9), database.address(3, 'Judas Lane'), datetime.date(2017, 4, 9), '220CT', True)
        students = [student5, student4, student3, student2, student1]
        db = database.database(students)

        postGrads = db.find(True, 'postgraduate')
        db.remove_by_id(postGrads[0].data['unique_id'])

        self.assertEqual(db.data['unique_id'].order(True), ['1', '2', '3', '4'])
        self.assertEqual(db.data['name'].order(True), ['Devin', 'Ellen', 'Rob', 'Ryan'])
        self.assertEqual(db.data['date_of_birth'].order(True), ['1978-01-12', '1997-01-12', '2000-01-12', '2002-04-02'])
        self.assertEqual(db.data['address'].order(True), ['1 Lunch Lane', '1 Lunch Lane', '10 Station Road', '104 Main Street'])
        self.assertEqual(db.data['enrolment_date'].order(True), ['2013-03-09', '2017-02-09', '2017-03-04', '2017-03-09'])
        self.assertEqual(db.data['class_id'].order(True), ['210CT', '210CT', '220CT', '290COM'])
        self.assertEqual(db.data['postgraduate'].order(True), ['False', 'False', 'True', 'True'])

        db.remove_by_id(postGrads[1].data['unique_id'])

        self.assertEqual(db.data['unique_id'].order(True), ['1', '2', '4'])
        self.assertEqual(db.data['name'].order(True), ['Devin', 'Ellen', 'Ryan'])
        self.assertEqual(db.data['date_of_birth'].order(True), ['1978-01-12', '1997-01-12', '2000-01-12'])
        self.assertEqual(db.data['address'].order(True), ['1 Lunch Lane', '10 Station Road', '104 Main Street'])
        self.assertEqual(db.data['enrolment_date'].order(True), ['2013-03-09', '2017-02-09', '2017-03-09'])
        self.assertEqual(db.data['class_id'].order(True), ['210CT', '220CT', '290COM'])
        self.assertEqual(db.data['postgraduate'].order(True), ['False', 'False', 'True'])

        db.remove_by_id(postGrads[2].data['unique_id'])
        self.assertEqual(db.data['unique_id'].order(True), ['2', '4'])
        self.assertEqual(db.data['name'].order(True), ['Devin', 'Ellen'])
        self.assertEqual(db.data['date_of_birth'].order(True), ['1997-01-12', '2000-01-12'])
        self.assertEqual(db.data['address'].order(True), ['1 Lunch Lane', '10 Station Road'])
        self.assertEqual(db.data['enrolment_date'].order(True), ['2013-03-09', '2017-03-09'])
        self.assertEqual(db.data['class_id'].order(True), ['210CT', '290COM'])
        self.assertEqual(db.data['postgraduate'].order(True), ['False', 'False'])


if __name__ == '__main__':
    unittest.main()
