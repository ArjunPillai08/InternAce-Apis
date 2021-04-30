from flask import Flask, redirect, jsonify
from db_auth import connect_to_db
import pymongo, ssl, os
from dotenv import load_dotenv
import json

"""
"""

collection = connect_to_db()
#all_instances = collection.find()#
app = Flask(__name__)

port = 4001
host = "0.0.0.0"

@app.route("/opportunities")
def home():
    all_instances = list(collection.find({}))
    new_list = list()
    counter = 0
    for i in all_instances:
        dictionary = all_instances[counter]
        dictionary.pop("_id", None)
        new_list.append(dictionary)
        counter += 1
    print(len(new_list))
    internships = jsonify(new_list)
    return internships

if __name__ == "__main__":
    app.run(host=host, port=port, debug=False)