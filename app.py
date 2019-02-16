from flask import Flask
import flask
app = Flask(__name__)


@app.route("/")
def hello():
    return flask.render_template('index.html')


if __name__ == "__main__":
    app.run()
