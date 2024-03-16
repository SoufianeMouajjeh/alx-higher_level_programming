#!/usr/bin/python3
"""Filter cities by user input"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306, host="localhost")
    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities INNER JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id", (sys.argv[4],))
    rows = cursor.fetchall()
    print(", ".join([row[0] for row in rows]))
    cursor.close()
    db.close()
    
