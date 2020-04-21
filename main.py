from pymongo import MongoClient
import requests
from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import sqlalchemy
from werkzeug.utils import secure_filename





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
    return render_template('post.html')


@app.route('/comments', methods=['GET'])
def listing():
    result = list(db.Instagram.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'instagram': result})


@app.route('/comments', methods=['POST'])
def saving():
    comment_receive = request.form['comment_give']
    comments = {'comment': comment_receive}

    db.Instagram.insert_one(comments)

    return jsonify({'result': 'success'})


@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save('./uploadimg/' + secure_filename(f.filename))
      return 'file uploaded successfully'
      





if __name__ == '__main__':
    app.run('127.0.0.1', port=5000, debug=True)
