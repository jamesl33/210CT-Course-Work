#!/usr/bin/python3

class student:
    def __init__(self, unique_id, name, date_of_birth, address, enrolment_date, class_id, postgraduate):
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
