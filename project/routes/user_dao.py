from . import database_connector as db

def getAllUsers():
    cursor = db.mysql.connection.cursor()
    cursor.execute(''' SELECT * FROM user''')
    db.mysql.connection.commit()
    rv = cursor.fetchall()
    cursor.close()
    return rv

