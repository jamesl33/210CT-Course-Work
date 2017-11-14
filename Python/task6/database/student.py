#!/usr/bin/python3

class student:
    def __init__(self, uniqueId, name, dateOfBirth, address, enrolmentDate, classId, postgraduate):
        self.data = {}
        self.data['uniqueId'] = uniqueId
        self.data['name'] = name
        self.data['dateOfBirth'] = dateOfBirth
        self.data['address'] = address
        self.data['enrolmentDate'] = enrolmentDate
        self.data['classId'] = classId
        self.data['postgraduate'] = postgraduate

    def __str__(self):
        return str(self.data['name'])
