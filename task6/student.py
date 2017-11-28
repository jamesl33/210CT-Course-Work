#!/usr/bin/python3


import datetime
from address import Address


class Student:
    """Student: Class representing a student
    """
    def __init__(self, unique_id, name, date_of_birth, address, enrolment_date, class_id, postgraduate):
        """__init__

        :param unique_id: ID of a student
        :param name: Name of the student
        :param date_of_birth: The sutdents DOB
        :param address: Where they live
        :param enrolment_date: When they enrolled
        :param class_id: What class they are in
        :param postgraduate: Whether they have graduated
        """
        assert isinstance(unique_id, int)
        assert isinstance(name, str)
        assert isinstance(date_of_birth, datetime.date)
        assert isinstance(address, Address)
        assert isinstance(enrolment_date, datetime.date)
        assert isinstance(class_id, str)
        assert isinstance(postgraduate, bool)

        self.data = {}
        self.data['unique_id'] = unique_id
        self.data['name'] = name
        self.data['date_of_birth'] = date_of_birth
        self.data['address'] = address
        self.data['enrolment_date'] = enrolment_date
        self.data['class_id'] = class_id
        self.data['postgraduate'] = postgraduate

    def __str__(self):
        return str(self.data['name'])
