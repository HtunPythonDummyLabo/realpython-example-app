from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

from routes import login

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)