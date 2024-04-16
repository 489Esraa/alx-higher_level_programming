#!/usr/bin/python3
"""Takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument."""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]
    state_name_searched = argv[4]
    host = "localhost"
    port = 3306
    conn = MySQLdb.connect(
        host=host,
        port=port,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
    )
    cur = conn.cursor()
    sql_query = """SELECT * FROM states WHERE BINARY name = %s ORDER BY states.id ASC"""
    cur.execute(sql_query, (state_name_searched,))
    rows = cur.fetchall()
    for r in rows:
        print(r)
    cur.close()
    conn.close()
