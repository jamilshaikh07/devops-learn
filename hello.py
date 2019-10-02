from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Flask!"
@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/members")
def members():
    return "Members"

@app.route("/members/Jamil")
def getMember(name):
    return "Jamil"

if __name__ == "__main__":
    app.run()

