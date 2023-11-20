#!/usr/bin/python3
"""
This states all the states from the database `hbtn_0c_0_usa`
"""

import MySQdb
from sys import argv

if __name__ == '__main__':
    """
    Access database and retreve the states
    """
    db = MYSQLdb.connect(host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM STATES")
    rows = cur.fetchall()
    for row in rows:
        print(row)
