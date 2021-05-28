from flask import Flask, redirect, url_for

app = Flask(__name__)

def helloGuest(guest):
    return "Hello %s. Nice to meet you." %guest

def helloAdmin():
    return "こんにちは、ご主人様！"

def helloUser(name):
    if name == 'admin':
        return redirect(url_for('helloAdmin'))

    return redirect(url_for('helloGuest',guest=name))

def home():
    return "Home Page"

app.add_url_rule("/hello/<name>","helloUser",helloUser)
app.add_url_rule("/guest/<guest>","helloGuest",helloGuest)
app.add_url_rule("/admin","helloAdmin",helloAdmin)
app.add_url_rule("/","",home)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port='8989')
