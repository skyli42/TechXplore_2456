from flask import Flask
import flask
from flask import request
from flask_socketio import SocketIO
from flask_socketio import emit
import random
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route("/")
def hello():
    return flask.render_template('index.html')


@socketio.on('new sequence')
def handle_sequence(data):
    seq = data
    print(seq)
    emit('sequence return string', "Sequence Received")


if __name__ == "__main__":
    socketio.run(app)
