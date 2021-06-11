import mysql.connector

class connection:

  def __init__(self) :
    host="localhost"
    user="root"
    password="admin"
    database="db_command_centre"

    self.myconnection = mysql.connector.connect(
      host=host,
      user=user,
      password=password,
      database=database
    )

    if not self.myconnection:
      raise Exception('Failed connect to db')
    else:
      print('success connect to db')

  def sql_select(self,sql):
    sql_cursor = self.myconnection.cursor()

    sql_cursor.execute(sql)
    
    sql_result = sql_cursor.fetchall()

    if sql_result:
      return sql_result
    else:
      False