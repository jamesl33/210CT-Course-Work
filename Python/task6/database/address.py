#!/usr/bin/python3

class address:
    def __init__(self, houseNum, streetName):
        self.houseNum = houseNum
        self.streetName = streetName

    def __lt__(self, other):
        return self.houseNum < other.houseNum

    def __gt__(self, other):
        return self.houseNum > other.houseNum

    def __eq__(self, other):
        if str(other) == str(self):
            return True
        else:
            return False

    def __ne__(self, other):
        if str(other) == str(self):
            return False
        else:
            return True

    def __str__(self):
        return '{0} {1}'.format(self.houseNum, self.streetName)
