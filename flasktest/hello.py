#coding:utf-8

from flask import Flask, render_template
from flask import request
import sys
import re

reload(sys)

sys.setdefaultencoding('utf-8')

app = Flask(__name__)

def valid_input(input):
    pat = "[^\*]{1,64}\\n[^\*]{1,64}=[^\*]{1,255}"
    p=re.compile(pat)
    if (p.match(str(input))):
        return 1
    else:
        return 0

def add_to_record(input):
    return 'Succeed! '+str(input).replace('\n', '<br>')

def get_data(input):
    return 'data'+str(input)

@app.route('/')
def welcome_page():
    return 'Welcome'

@app.route('/user/<username>')
def welcome_user(username):
    return 'Welcome, %s!' % username

@app.route('/jiexin', methods=['GET', 'POST'])
def jiexins():
    error = None
    if request.method == 'POST':
        if valid_input(request.form['profile']):
            return add_to_record(request.form['profile'])
        else:
            error = 'Invalid input'
    return render_template('submit.html', action='Jiexin', data=get_data(0), error=error)


@app.route('/xuqiu', methods=['GET', 'POST'])
def xuqiu(): 
    error = None
    if request.method == 'POST':
        if valid_input(request.form['profile']):
            return add_to_record(request.form['profile'])
        else:
            error = 'Invalid input'
    return render_template('submit.html', action='Xuqiu', data=get_data(1), error=error)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

