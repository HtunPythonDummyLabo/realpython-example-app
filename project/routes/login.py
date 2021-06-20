from __main__ import app, render_template, request, redirect, url_for, session
import datetime
# from . import user_dao as userDao
from .user_dao import UserDao

@app.route('/')
def index():
    return render_template('login.html',message='')

@app.route('/login',methods=['POST','GET'])
def login():
    msg = ''
    if request.method == 'POST':
        userId = request.form['userId']
        password = request.form['password']
        resp = redirect(url_for('home'))
        userDao = UserDao()
        res = userDao.checkUser((userId,password))
        if(len(res) > 0 ):
            # expire_date = datetime.datetime.now()
            # expire_date = expire_date + datetime.timedelta(seconds=1)
            # resp.set_cookie('userName',res[0][0], expires=expire_date)
            session['loginStatus'] = True
            session['userName'] = res[0][0]
            return resp
        msg = 'User data not found'

    return render_template('login.html',message=msg)

@app.route('/home')
def home():
    if 'loginStatus' in session and session['loginStatus']:
        return render_template('home.html',userName=session['userName'])
    
    return render_template('login.html',message='TimeOut')
