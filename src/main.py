from flask import Flask, jsonify
from dbmod import read_demo;
from dbmod import insert_demo

app = Flask(__name__)


# http://localhost:5000/
@app.route('/')
def hello_world():
    return 'Hello, World!'


# http://localhost:5000/demo
@app.route('/demo', methods=["GET"])
def hello_world_demo():
    return 'Hello, World, DEMO'


# http://localhost:5000/add_one_user
@app.route("/add_one_user", methods=["GET"])
def add_one_user():
    insert_demo.mongo_insert_demo()
    return "User Added Successfully"
    


# http://localhost:5000/read_all_user
@app.route('/read_all_user', methods=['GET'])
def hello_list():
    list = read_demo.read_all_user()
    return jsonify(list)



if __name__ == '__main__':
    app.run(debug=True)
