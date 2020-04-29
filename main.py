from pymongo import MongoClient
import requests
from flask import Flask, render_template, jsonify, request
from werkzeug.utils import secure_filename
from bson.json_util import loads, dumps
from bson import BSON
from bson.objectid import ObjectId

app = Flask(__name__)
client = MongoClient("localhost", 27017)
db = client.dbsparta

# mainpage
@app.route("/mainpage")
def home():
    return render_template("mainpage.html")


# login page
@app.route("/login")
def loginhtml():
    return render_template("login.html")


# signup page
@app.route("/signup")
def signup():
    return render_template("signup.html")


# post page
@app.route("/post")
def posting():
    return render_template("post.html")


# post 페이지 data 주는 부분
@app.route("/post", methods=["POST"])
def postpage():
    post_recieve = request.form["post_give"]
    posts = {"postcontent": post_recieve}
    db.instapost.insert_one(posts)
    return jsonify({"success": True})


# post page db 데이터 조회
@app.route("/post/api", methods=["GET"])
def postlisting():
    postresult = list(db.instapost.find({}, {"_id": 0}))
    return jsonify({"result": "success", "instapost": postresult})


# comments page db 조회
@app.route("/comments", methods=["GET"])
def listing():
    result = list(db.Instagram.find({}, {"_id": 0}))
    return jsonify({"success": True, "instagram": result})


# 작성받은 comments db에 집어넣기
@app.route("/comments/api", methods=["POST"])
def saving():
    comment_receive = request.form["comment_give"]    
    comments = {'comment':comment_receive}
    if comments["comment"] == "":
        return jsonify({"result": "fail"})
    else:
        db.Instagram.insert_one(comments)
    return jsonify({"result": "success"})
    


# 파일 업로드
@app.route("/uploader", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        f = request.files["file"]
        f.save("./uploadimg/" + secure_filename(f.filename))
        return "file uploaded successfully"




if __name__ == "__main__":
    app.run("127.0.0.1", port=5000, debug=True)
