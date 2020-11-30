from data.DBUtilities import getDBCnx
import mysql
import datetime

#The following functions execute the input sql
#and return the result or raise an exception

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
