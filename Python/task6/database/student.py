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
        return 'ID: {0}\nName: {1}\nDate of Birth: {2}\nAddress: {3}\nEnrolment Date: {4}\nClass ID: {5}\nPostgraduate: {6}\
            '.format(self.data['uniqueId'], self.data['name'], self.data['dateOfBirth'], self.data['address'], \
            self.data['enrolmentDate'], self.data['classId'], self.data['postgraduate'])
