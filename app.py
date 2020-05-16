

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    return "Hello World!"

#assignment page
@app.route("/assignments")
def assignments():
    return "This is my assignment page"


@app.route("/classes")
def classes():
    return "This is my classes page"

#start the server
if __name__ == "__main__":
    app.run()