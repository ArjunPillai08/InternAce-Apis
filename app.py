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

@app.route("/internships")
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

@app.route("/internships/remote")
def remote():
    my_query = {"is_remote": True}
    all_instances = list(collection.find(my_query, {"_id": 0}))
    return jsonify(all_instances)

@app.route("/internships/industry/<name>")
def in_person(name):
    name = name.capitalize()
    my_query = {"industry": str(name)}
    all_instances = list(collection.find(my_query, {"_id": 0}))
    print(all_instances)
    return jsonify(all_instances)

if __name__ == "__main__":
    app.run()