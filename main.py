# import sys
# sys.path.append('routes')

from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

from routes import profile

@app.route('/')
def index():
    fruitList = ['apple','orange','banana']
    dictList = {'Orion':200,'Krin':150,'Asahi':100}
    return render_template('login.html',fruits = fruitList,dicts = dictList)

@app.route('/welcome',methods=['POST','GET'])
def welcome():
    if request.method == 'POST':
        user = request.form['name']
        return render_template('welcome.html',name = user)

    return render_template('error.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
