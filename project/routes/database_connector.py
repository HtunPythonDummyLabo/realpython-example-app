from __main__ import app
from flask_mysqldb import MySQL

app.config['MSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'rememberme95HMM$'
app.config['MYSQL_DB'] = 'demodb'

mysql = MySQL(app)
