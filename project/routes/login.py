from __main__ import app, render_template, request, redirect, url_for


@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        userName = request.form['username']
        return redirect(url_for('home',userName=userName))

    # sessions, cookies
    return render_template('login.html')

@app.route('/home/<userName>')
def home(userName):
    return render_template('home.html',userName=userName)
