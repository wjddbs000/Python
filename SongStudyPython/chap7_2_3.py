from flask import Flask

app = Flask(__name__)

@app.route("/")

def hello():
    return "<h1>hello world!</h1>"

app.run(host='127.0.0.1',debug=True)