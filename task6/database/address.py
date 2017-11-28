#!/usr/bin/python3

class address:
    def __init__(self, house_num, street_name):
        self.house_num = house_num
        self.street_name = street_name

    def __lt__(self, other):
        return self.house_num < other.house_num

    def __gt__(self, other):
        return self.house_num > other.house_num

    def __eq__(self, other):
        if str(other) == str(self):
            return True
        return False

    def __ne__(self, other):
        if str(other) == str(self):
            return False
        return True

    def __str__(self):
        return '{0} {1}'.format(self.house_num, self.street_name)
