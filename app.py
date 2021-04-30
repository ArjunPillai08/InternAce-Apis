from flask import Flask, redirect, jsonify

port = 3000
host = "0.0.0.0"

app = Flask(__name__)

def variable_maker():
    variable = {"day": 1, "month": 2, "year": 3}
    return variable

@app.route("/internships")
def home():
    internships = variable_maker()
    return jsonify(internships)

if __name__ == "__main__":
    app.run(host=host, port=port)