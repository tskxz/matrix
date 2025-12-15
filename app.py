from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sum")
def sum():
    return("Sum Page")

@app.route("/scalar")
def scalar():
    return("Scalar Page")

@app.route("/multiply")
def multiply():
    return("Multiply Page")

@app.route("/determinant")
def determinant():
    return("Determinant Page")

@app.route("/inverse")
def inverse():
    return("Inverse Page")

@app.route("/encrypt")
def encrypt():
    return("Encrypt Page")

if __name__ == "__main__":
    app.run()