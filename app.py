import flask
from flask import request
import os
import json
from flask_pymongo import PyMongo
from bson.json_util import dumps
import re
from flask_cors import CORS
from db_auth import connect_to_db

"""
"""
app = flask.Flask(__name__)
CORS(app)

db = connect_to_db()
#all_instances = collection.find()#

port = 4001
host = "0.0.0.0"

@app.route('/',methods = ['GET'])
def get_data():

    qs = request.args.get('name')
    if qs is None:
        todos = db.internships.find()
        return dumps(todos)
    else:
        rgx = re.compile(qs, re.IGNORECASE)  # compile the regex
        todos = db.internships.find({'company':rgx})
        return dumps(todos)

@app.route('/filter',methods = ['POST'])
def filter_data():
    print(request.json)
    industry_name = request.json['industry']
    is_paid = request.json['paid']
    is_remote = request.json['remote']
    position = request.json['position']

    industry_name_rgx = re.compile(industry_name, re.IGNORECASE)
    position_rgx = re.compile(position, re.IGNORECASE)

    if industry_name == '':
        todos = db.internships.find({'is_paid': {"$in":is_paid}, 'is_remote': {"$in":is_remote}, 'position': position_rgx})
        return dumps(todos)
    else:
        todos = db.internships.find({'industry':industry_name_rgx, 'is_paid': {"$in":is_paid}, 'is_remote': {"$in":is_remote}, 'position': position_rgx})
        return dumps(todos)
    
@app.route('/industry',methods = ['GET'])
def get_industry():

    # Get All industry type
    todos = db.internships.find({}, {'industry': 1, '_id': 0})

    # Filter duplicate industry values
    todos = [dict(t) for t in {tuple(d.items()) for d in todos}]

    # Make list of industries and send response
    return dumps(filter(None, [d['industry'] for d in todos]))
    
if __name__ == '__main__':
    app.run()    