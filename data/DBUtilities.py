import mysql.connector

user = 'jack'
password = 'jack'
host = 'localhost'
databasename = 'calculatorflask'

TABLE_DEFS = {}
TABLE_DEFS['Users'] =\
  '''
  create table products(
    id int not null auto_increment primary key,
    username varchar(100),
    password varchar(100)
  )
  '''
TABLE_DEFS['Calculations'] =\
  '''
  create table calculations(
    x float(53),
    op char(1),
    y float(53),
    val float(53),
    user_id int not null,
    date datetime
  )
  '''

'''
  Creates a connection to the DB
'''
def getDBCnx():
  return mysql.connector.connect(
      user=user,
      password=password,
      host=host,
      database=databasename )

def getDBCnxNoDBSpecified():
  return mysql.connector.connect(
      user=user,
      password=password,
      host=host )

'''
  Creates a database named databasename.
  Returns:
    (bool) whether the operation was successful
'''
def createDatabase():
  try:
    cnx = getDBCnxNoDBSpecified()
    cursor = cnx.cursor()
    print("Creating database", databasename)
    cursor.execute(
      "drop database if exists {}".format(databasename))
    cursor.execute(
      "CREATE DATABASE {}".format(databasename))
  except mysql.connector.Error as err:
    print("Exception creating database:", err)
    return False
  finally:
    try:
      cursor.close()
    except:
      pass
    try:
      cnx.close()
    except:
      pass
  return True

'''
  Executes the sql defined in TABLE_DEFS.
  Returns:
    (bool) whether the operation was successful
'''
def createTabes():
  try:
    cnx = getDBCnx()
    cursor = cnx.cursor()
    for key in TABLE_DEFS:
      print("Creating table {}: ".format(key), end='')
      cursor.execute(TABLE_DEFS[key])
      print('OK')
    return True
  except mysql.connector.Error as err:
    print("Exception creating tables:", err)
    return False
  finally:
    try:
      cursor.close()
    except:
      pass
    try:
      cnx.close()
    except:
      pass

'''
  Creates the database and tables specified above.
'''
def initializeDatabase():
  print("Starting initialization script")
  if(not createDatabase() ):
    print("aborting..")
    exit(1)
  if( not createTabes() ):
    print("aborting..")
    exit(1)
  print("Initialization complete")

if __name__ == "__main__":
  initializeDatabase()
