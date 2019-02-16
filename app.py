from flask import Flask
from flask import request
import flask
app = Flask(__name__)


@app.route("/")
def hello():
    response = "This is a message from the server"
    return flask.render_template('index.html', response=response)


if __name__ == "__main__":
    app.run()
