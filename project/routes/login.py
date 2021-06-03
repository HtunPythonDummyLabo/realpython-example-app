from __main__ import app, render_template, request, redirect, url_for
import datetime


@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        userName = request.form['username']
        resp = redirect(url_for('home'))

        expire_date = datetime.datetime.now()
        expire_date = expire_date + datetime.timedelta(seconds=1)
        resp.set_cookie('userName',userName, expires=expire_date)
        return resp

    # sessions, cookies
    return render_template('login.html')

@app.route('/home')
def home():
    # username = request.args['userName']
    username = request.cookies.get('userName')
    print("UserName : " + username)
    return render_template('home.html',userName=username)
