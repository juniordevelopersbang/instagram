from pymongo import MongoClient
import requests
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


client = MongoClient('localhost', 27017)
db = client.dbsparta


@app.route('/')
def home():
    return render_template('mainpage.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/post', methods=["GET"])
def postpage():
    return render_template('index.html')


@app.route('/comments', methods=['GET'])
def listing():
    result = list(db.Instagram.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'instagram': result})


@app.route('/comments', methods=['POST'])
def saving():
    name_receive = request.form['name_give']
    names = {'name': name_receive}
    comment_receive = request.form['comment_give']
    comments = {'comment': comment_receive}

    db.Instagram.insert_one(names)
    db.Instagram.insert_one(comments)

    return jsonify({'result': 'success'})


@app.route('/')
def like():

    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run('127.0.0.1', port=5000, debug=True)
