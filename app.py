from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def hello():
    return "Welcome to Prion Prediction!"

if __name__ == "__main__":
    app.run()