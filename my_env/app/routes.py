from datetime import MAXYEAR, datetime
from app import app
from flask import render_template
from flask import request
import os
@app.route('/')
@app.route('/room')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/api/chat/general',methods=['POST','GET'])
def chat():
    date=str(datetime.now())
    username=False
    if request.method=='POST':
        username=str(request.form.get('username'))
        msg=str(request.form.get('msg'))
        with open("data.txt","a") as data:
            data.write('[' + date + ']' + " " + username + " says: " + msg + "\n")
    my_data=""
    with open("data.txt","r")as data:
        my_data=data.read()
    return my_data

@app.route('/api/chat/<room>',methods=['GET','POST'])
def room_chat(room):
    date=str(datetime.now())
    filename=str(room) + '.txt'
    if request.method=='POST':
        username=str(request.form.get('username'))
        msg=str(request.form.get('msg'))
        with open(filename,"a") as data:
            data.write('[' + date + ']' + " " + username + " says: " + msg + "\n")
    my_data=""
    if os.path.exists(filename) :
        with open(filename,"r") as data:
            my_data=data.read()
        return my_data
    return render_template('index.html')
