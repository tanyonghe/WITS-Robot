from flask import Flask

print(__name__)
app = Flask(__name__)

@app.route("/")
def hello():
    return "hi i love you!"


