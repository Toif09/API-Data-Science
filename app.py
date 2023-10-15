#membuat file python

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hai, ini percobaan untuk GET request"

@app.route("/submit", methods=["POST"])
def submit():
    return "Hai, ini percobaan untuk POST request"

app.run(host="localhost", port="5000") 
