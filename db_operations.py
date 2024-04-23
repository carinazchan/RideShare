#All of db_operations.py is from the playlist assignment given by the professor, so it is not new code.

import mysql.connector
from helper import helper

class db_operations():
    #constructor with connection path to DB
    def __init__(self): #Connection WORKS, this is customized for Carina's computer
        self.connection = mysql.connector.connect(user='root', password='CPSC408!',
                                  host='macbook-2.local',
                                  database='RideShare')
        self.cursor = self.connection.cursor()
        print("connection made..")

    #function to simply execute a DDL or DML query.
    #commits query, returns no results. 
    #best used for insert/update/delete queries with no parameters
    def modify_query(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    #function to simply execute a DDL or DML query with parameters
    #commits query, returns no results. 
    #best used for insert/update/delete queries with named placeholders
    def modify_query_params(self, query, dictionary):
        self.cursor.execute(query, dictionary)
        self.connection.commit()

    #function to simply execute a DQL query
    #does not commit, returns results
    #best used for select queries with no parameters
    def select_query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()
        #return result.fetchall() #this is the original line from the playlist assignment, but it doesn't work for rideshare
    
    #function to simply execute a DQL query with parameters
    #does not commit, returns results
    #best used for select queries with named placeholders
    def select_query_params(self, query, dictionary):
        result = self.cursor.execute(query, dictionary)
        return result.fetchall()

    #function to return the value of the first row's 
    #first attribute of some select query.
    #best used for querying a single aggregate select 
    #query with no parameters
    def single_record(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchone()[0]
    
    #function to return the value of the first row's 
    #first attribute of some select query.
    #best used for querying a single aggregate select 
    #query with named placeholders
    def single_record_params(self, query, dictionary):
        self.cursor.execute(query, dictionary)
        return self.cursor.fetchone()[0]
    
    #function to return a single attribute for all records 
    #from some table.
    #best used for select statements with no parameters
    def single_attribute(self, query):
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        results = [i[0] for i in results]
        results.remove(None)
        return results
    
    #function to return a single attribute for all records 
    #from some table.
    #best used for select statements with named placeholders
    def single_attribute_params(self, query, dictionary):
        self.cursor.execute(query,dictionary)
        results = self.cursor.fetchall()
        results = [i[0] for i in results]
        return results
    
    #function for bulk inserting records
    #best used for inserting many records with parameters
    def bulk_insert(self, query, data):
        self.cursor.executemany(query, data)
        self.connection.commit()

#function that returns true/false depending on whether a certain driver ID already exists in Driver database
    def check_driverID(self, ID):
        #query to see if database has a Driver with given ID
            query = '''
            SELECT COUNT(*)
            FROM Driver
            WHERE driverID = {}
            '''.format(ID)

            #run query and returns true/false value given equivalency to a 0 count
            #returns true if no records, returns false if there is a record (kinda opposite logic, I know, but it works)
            result = self.single_record(query)
            return result == 0
    
#function that returns true/false depending on whether a certain rider ID already exists in Rider database
    def check_riderID(self, ID):
        #query to see if database has a rider with given ID
            query = '''
            SELECT COUNT(*)
            FROM Rider
            WHERE RiderID = {}
            '''.format(ID)

            #run query and returns true/false value given equivalency to a 0 count
            #returns true if no records, returns false if there is a record (kinda opposite logic, I know, but it works)
            result = self.single_record(query)
            return result == 0

    #destructor that closes connection with DB
    def destructor(self):
        self.cursor.close()
        self.connection.close()