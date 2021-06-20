from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'rememberme95HMM$SaySomeThingsDearDad'

from routes import login

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
