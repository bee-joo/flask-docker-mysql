import os
import socket
import views
from __main__ import app, db
from flask import jsonify, request


@app.route('/')
def hello():
    name = os.getenv("NAME", 'world')
    hostname = socket.gethostname()

    return views.hello_view(name, hostname)


@app.route('/stat')
def stat():
    import datetime
    
    headers = str(request.headers['User-Agent'])
    date = datetime.datetime.now()
    db.add('logs', date, headers)
    
    return views.stat_view(date, headers)


@app.route('/logs')
def get_logs():
    res = db.find_all_as_dict('logs')
    return jsonify(res)


@app.route('/widgets')
def get_widgets():
    res = db.find_all_as_dict('widgets')
    return jsonify(res)
