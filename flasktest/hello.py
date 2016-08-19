
#coding:utf-8

from flask import Flask, render_template
from flask import request
import sys
import re
import os

reload(sys)

sys.setdefaultencoding('utf-8')

app = Flask(__name__)

def valid_input(input):
    pat = "[^\*\\n]{1,64}--[^\*\\n]{1,64}=[^\*\\n]{1,255}"
    p=re.compile(pat)
    if (p.match(str(input))):
        return 1
    else:
        return 0

def add_to_jrecord(input):
    f=open('jiexin.txt','a')
    for i in input:
        f.write(str(i))
    f.write("\n")
    f.close()
    return 'Succeed! '+str(input).replace('--', '<br>')

def add_to_xrecord(input):
    f=open('xuqiu.txt','a')
    for i in input:
        f.write(str(i))
    f.write("\n")
    f.close()
    return 'Succeed! '+str(input).replace('--', '<br>')

def get_data(input):
    a=open('jiexin.txt','a')
    a.close()
    a=open('xuqiu.txt','a')
    a.close()
    strd="data:\n"
    if (input==0):
        a=open('jiexin.txt','rt')
        while 1:
            s=a.readline()
            if(len(s)==0):
                break
            strd += "=="+str(s)
        a.close()
    elif (input==1):
        a=open('xuqiu.txt', 'rt')
        while 1:  
            s=a.readline()
            if(len(s)==0):
                break
            strd += "=="+str(s)
        a.close();
    return str(strd)

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
            return add_to_jrecord(request.form['profile'])
        else:
            error = 'Invalid input'
    return render_template('submit.html', action='Jiexin', data=get_data(0), error=error, flag=1)


@app.route('/xuqiu', methods=['GET', 'POST'])
def xuqiu(): 
    error = None
    if request.method == 'POST':
        if valid_input(request.form['profile']):
            return add_to_xrecord(request.form['profile'])
        else:
            error = 'Invalid input'
    return render_template('submit.html', action='Xuqiu', data=get_data(1), error=error)

@app.route('/resetallxuqiuandjiexin')
def reset():
    f=open("jiexin.txt","w")
    f.truncate()
    f.close()
    f=open("xuqiu.txt","w")
    f.truncate() 
    f.close()
    return "Reset succeed!"

@app.route('/delj/<name>')
def delj(name):
    if (re.compile("%E5%9C%88%E5%90%8D[^\\n\*]{1,64}").match(str(name)) == 1):
        return "Wrong Format "+ str(name)
    os.rename("jiexin.txt","jiexinold.txt")
    fin=open("jiexinold.txt", "r")
    fout=open("jiexin.txt", "a")
    chec=0
    while 1:
        st=fin.readline()
        if (len(st)==0):
            break
        if (st.find(name)==-1):
            fout.write(st)
        else:
            chec=1
    fin.close()
    fout.close()
    if(chec==1):
        return("Deleted")
    else:
        return("NotFound")

@app.route('/delx/<name>')
def delx(name):
    if (re.compile("%E5%9C%88%E5%90%8D[^\\n\*]{1,64}").match(str(name)) == 1):
        return "Wrong Format"+str(name)
    os.rename("xuqiu.txt","xuqiuold.txt")
    fin=open("xuqiuold.txt", "r")
    fout=open("xuqiu.txt", "a")
    chec=0
    while 1:
        st=fin.readline()
        if (len(st)==0):
            break
        if (st.find(name)==-1):
            fout.write(st) 
        else:
            chec=1
    fin.close()
    fout.close()
    if(chec==1):
        return("Deleted")
    else:
        return("NotFound")

if __name__ == '__main__':
    app.run(host='0.0.0.0')

