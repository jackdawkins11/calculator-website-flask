from data.DBUtilities import getDBCnx
import mysql
import datetime

#Executes the insert statement with the given parameters
#returns rowid of new entry or raises exception
def insert(sql, data):
    try:
        cnx = getDBCnx()
        cursor = cnx.cursor()
        cursor.execute(sql, data)
        cnx.commit()
        return cursor.lastrowid
    except mysql.connector.Error as err:
        print("Error executing sql:", err)
        raise err()
    finally:
        try:
            cursor.close()
        except:
            pass
        try:
            cnx.close()
        except:
            pass

#Executes the select statement with the given parameters,
#returns result or raises exception
def selectWithParams(sql, data):
    try:
        cnx = getDBCnx()
        cursor = cnx.cursor()
        cursor.execute(sql, data)
        return cursor.fetchall()
    except mysql.connector.Error as err:
        print("Error executing sql:", err)
        raise err()
    finally:
        try:
            cursor.close()
        except:
            pass
        try:
            cnx.close()
        except:
            pass

#Create a user with the given username and password
def insertUser(username, password):
    sql = '''insert into users (username, password)
            values (%s, %s)'''
    data = (username, password)
    return insert(sql, data)

#Check if the username is already used
def usernameTaken(username):
    sql = '''select count(*) > 0 from users u
            where u.username = %s'''
    data = (username,)
    return selectWithParams(sql, data)

#Checks if the username is taken, returns result as boolean
def usernameTakenAsBool(username):
    res = usernameTaken(username)
    return bool(res[0][0])

#Checks if there is an account with the given username and password
def authorizeUser(username, password):
    sql = '''select count(*) > 0 from users u
            where u.username = %s and u.password = %s'''
    data = (username, password)
    return selectWithParams(sql, data)

#Checks if there is an account with the given username and password,
#returns result as bool
def authorizeUserAsBool(username, password):
    res = authorizeUser(username, password)
    return bool(res[0][0])

#Gets the id of the user with the given username
def getUserId(username):
    sql = '''select u.id from users u
            where u.username = %s'''
    data = (username,)
    return selectWithParams(sql, data)

#Gets the id of the user with the given username,
#returns result as int
def getUserIdAsInt(username):
    res = getUserId(username)
    return int(res[0][0])

#gets the username of the user user with the given is
def getUsernameById(id):
    sql = '''select u.username from users u
            where u.id = %s'''
    data = (id,)
    return selectWithParams(sql, data)

#gets the username of the user with the given id
#returns result as string
def getUsernameByIdAsString(id):
    res = getUsernameById(id)
    return res[0][0]

#insert calculation into database
def insertCalculation(user_id, x, op, y, val, time):
    sql = '''insert into calculations
            (user_id, x, op, y, val, time)
            values (%s, %s, %s, %s, %s, %s)'''
    data = (user_id, x, op, y, val, time)
    return insert(sql, data)

#gets up to the last 10 calculations in the database
def getLast10Calculations():
    sql = '''select * from calculations c
            order by c.time desc
            limit 10'''
    data = ()
    return selectWithParams(sql, data)

#gets the last 10 calculations in the database
#populates the user_id with a username
#converts the types to correct type
def getLast10CalculationsFormatted():
    res = getLast10Calculations()
    formatted = []
    for row in res:
        user_id = int( row[4] )
        x = float(row[0])
        op = str(row[1])
        y = float(row[2])
        val = float(row[3])
        time = row[5]
        formatted.append( {
            "Username": getUsernameByIdAsString(user_id),
            "X": x,
            "Op": op,
            "Y": y,
            "Val": val,
            "Date": time
        } )
    return formatted

