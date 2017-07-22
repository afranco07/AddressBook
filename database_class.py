"""Class where all the database operations are done"""

import MySQLdb

class DataBaseClass(object):

    def __init__(self):
        self.db = MySQLdb.connect(
            host = 'localhost',
            user = 'testuser',
            passwd = 'testpassword',
            db = 'testdb'
        )

    def getNamesOfCustomers(self):
        """Returns a list with all the names"""
        people = []
        cursor = self.db.cursor()
        cursor.execute('SELECT first_name, last_name FROM foodtown ORDER BY last_name')
        results = cursor.fetchall()

        if results:
            for person in results:
                name = person[0] + ' ' + person[1]
                people.append(name)
        return people

    def returnAddressFromName(self, name_dict):
        cursor = self.db.cursor()
        cursor.execute('SELECT address1 ' \
                       'FROM foodtown ' \
                       'WHERE ' \
                       'first_name = ' + '\"' + name_dict['first_name'] + '\" AND ' \
                       'last_name = ' + '\"' + name_dict['last_name'] + '\"')
        address = cursor.fetchone()
        print(address[0])

    def returnAllCustomerInfo(self, name_dict):
        cursor = self.db.cursor()
        cursor.execute('SELECT * ' \
                       'FROM foodtown ' \
                       'WHERE ' \
                       'first_name = ' + '\"' + name_dict['first_name'] + '\" AND ' \
                       'last_name = ' + '\"' + name_dict['last_name'] + '\"')
        address = cursor.fetchone()
        return address