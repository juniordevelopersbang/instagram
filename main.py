from pymongo import MongoClient
import requests
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


client = MongoClient('localhost', 27017)
db = client.dbsparta


@app.route('/')
def home():
    return render_template('mainpage.html')



@app.route('/comments', methods=['GET'])
def listing():
    result = list(db.comments.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'comments': result})


@app.route('/comments', methods=['POST'])
def saving():
    comment_receive = request.form['comment_give']
    comments = {'comment': comment_receive}
    db.comments.insert_one(comments)
    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run('127.0.0.1', port=5000, debug=True)
