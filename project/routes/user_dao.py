from . import database_connector as db

class UserDao:
    def __init__(self):
        pass

    def getAllUsers(self):
        cursor = db.mysql.connection.cursor()
        cursor.execute(''' SELECT * FROM user''')
        db.mysql.connection.commit()
        rv = cursor.fetchall()
        cursor.close()
        return rv

    def checkUser(self,userData):
        userId,userPass = userData
        sqlQuery = 'SELECT user_name  FROM user WHERE user_id = \'{0}\' AND user_password = \'{1}\''
        cursor = db.mysql.connection.cursor()
        cursor.execute(sqlQuery.format(userId,userPass))
        rv = cursor.fetchall()
        cursor.close()
        return rv
