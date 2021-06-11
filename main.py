from connection import connection_db
from model import cmd_centre

import mysql.connector

try:
    myconnection = connection_db.connection()

    data = myconnection.sql_select('SELECT * FROM t_data_command ORDER BY timestamp desc')
    print(data)
except mysql.connector.Error as e:
    print('error : '+str(e))